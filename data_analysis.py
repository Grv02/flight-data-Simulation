import json
import time
import statistics

from config import DATA_DIR
from utils import percentile

def analyze_data():
    """
    Phase 2: Data Analysis & Cleaning
    - Load all JSON files in DATA_DIR
    - Process records, skip "dirty" ones (where any field is None)
    - Compute and print:
       1) total_records_processed
       2) total_dirty_records
       3) total runtime (ms)
       4) top 25 destination cities by total # of arriving passengers, 
          with average and 95th percentile flight duration
       5) passenger balance: city with max and city with min remaining passengers
    """
    start_time = time.time()

    total_records_processed = 0
    total_dirty_records = 0

    # For top 25 analysis
    city_arrivals_passengers = {}
    city_arrivals_durations = {}

    # Net passengers for each city = arrivals - departures
    city_net_passengers = {}

    # Read all JSON files
    for file_path in DATA_DIR.glob("*.json"):
        with file_path.open("r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                # If file is invalid JSON, skip
                continue

            for record in data:
                total_records_processed += 1

                # Check if "dirty" => any field is None
                if any(value is None for value in record.values()):
                    total_dirty_records += 1
                    continue

                origin_city = record["origin_city"]
                destination_city = record["destination_city"]
                flight_duration = record["flight_duration_secs"]
                passengers = record["No_of_passengers_on_board"]

                # Track arrivals for city-level stats
                if destination_city not in city_arrivals_passengers:
                    city_arrivals_passengers[destination_city] = 0
                    city_arrivals_durations[destination_city] = []
                city_arrivals_passengers[destination_city] += passengers
                city_arrivals_durations[destination_city].append(flight_duration)

                # Update net passenger balance
                if origin_city not in city_net_passengers:
                    city_net_passengers[origin_city] = 0
                if destination_city not in city_net_passengers:
                    city_net_passengers[destination_city] = 0

                city_net_passengers[origin_city] -= passengers
                city_net_passengers[destination_city] += passengers

    total_runtime_ms = int((time.time() - start_time) * 1000)

    # Find top 25 destination cities (by arriving passengers)
    sorted_by_arrivals = sorted(
        city_arrivals_passengers.items(),
        key=lambda x: x[1],
        reverse=True
    )
    top_25 = sorted_by_arrivals[:25]

    top_25_metrics = []
    for city, total_pax in top_25:
        durations = city_arrivals_durations[city]
        avg_duration = statistics.mean(durations) if durations else 0
        sorted_durations = sorted(durations)
        p95_duration = percentile(sorted_durations, 95) or 0

        top_25_metrics.append({
            "city": city,
            "total_arriving_passengers": total_pax,
            "avg_flight_duration_secs": round(avg_duration, 2),
            "p95_flight_duration_secs": round(p95_duration, 2)
        })

    # City with max and min net passengers
    if city_net_passengers:
        city_with_max = max(city_net_passengers, key=city_net_passengers.get)
        city_with_min = min(city_net_passengers, key=city_net_passengers.get)
    else:
        city_with_max = None
        city_with_min = None

    results = {
        "total_records_processed": total_records_processed,
        "total_dirty_records": total_dirty_records,
        "analysis_runtime_ms": total_runtime_ms,
        "top_25_cities_by_passenger_arrivals": top_25_metrics,
        "passenger_balance": {
            "city_with_max_passengers": {
                "city": city_with_max,
                "balance": city_net_passengers.get(city_with_max, 0) if city_with_max else None
            } if city_with_max else None,
            "city_with_min_passengers": {
                "city": city_with_min,
                "balance": city_net_passengers.get(city_with_min, 0) if city_with_min else None
            } if city_with_min else None
        }
    }

    # Print the analysis results as JSON
    print(json.dumps(results, indent=2))
