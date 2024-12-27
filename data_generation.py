import json
import random
import datetime

from config import (
    DATA_DIR, NUM_FILES, 
    RECORDS_PER_FILE_MIN, RECORDS_PER_FILE_MAX,
    FLIGHT_DURATION_RANGE, PASSENGER_RANGE,
    DIRTY_RECORD_PROB_MIN, DIRTY_RECORD_PROB_MAX,
    MIN_CITIES, MAX_CITIES,
    CITY_LIST
)
from utils import random_date_within_current_month

def _create_record(origin_city: str, city_list: list, dirty_prob: float) -> dict:
    """
    Create a single flight record. With probability `dirty_prob`,
    randomly assign one or more fields to None (dirty).
    """
    record = {
        "date": random_date_within_current_month(),
        "origin_city": origin_city,
        "destination_city": random.choice(city_list),
        "flight_duration_secs": random.randint(*FLIGHT_DURATION_RANGE),
        "No_of_passengers_on_board": random.randint(*PASSENGER_RANGE)
    }

    # Decide if this record should be 'dirty'
    if random.random() < dirty_prob:
        # Randomly choose how many fields to turn into None (1 to all)
        num_dirty_fields = random.randint(1, len(record))
        dirty_fields = random.sample(list(record.keys()), num_dirty_fields)
        for field in dirty_fields:
            record[field] = None

    return record

def generate_data():
    """
    Phase 1: Data Generation
    Uses a static list of real-world city names from config.py (CITY_LIST).
    """
    # 1) Possibly pick a random subset of the static city list
    #    If you want to use ALL cities every time, do:
    #        cities = CITY_LIST
    #    Otherwise, to have variety each run:
    num_cities = random.randint(MIN_CITIES, MAX_CITIES)
    cities = random.sample(CITY_LIST, k=min(num_cities, len(CITY_LIST)))

    # 2) Ensure output directory exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # 3) Generate ~NUM_FILES JSON flight files
    today = datetime.date.today()
    mm_yy = today.strftime("%m-%y")  # e.g. "12-24"

    for i in range(NUM_FILES):
        # Pick a random origin city from the (sub)list
        origin_city = random.choice(cities)

        # Decide how many records to create in this file
        num_records = random.randint(RECORDS_PER_FILE_MIN, RECORDS_PER_FILE_MAX)

        # Probability of dirty data in [DIRTY_RECORD_PROB_MIN..DIRTY_RECORD_PROB_MAX]
        dirty_prob = random.uniform(DIRTY_RECORD_PROB_MIN, DIRTY_RECORD_PROB_MAX)

        # Generate flight records
        records = []
        for _ in range(num_records):
            record = _create_record(origin_city, cities, dirty_prob)
            records.append(record)

        # Build filename => e.g. "12-24-New York-flights.json"
        # Note: If city has spaces, it will appear in the filename with spaces 
        # or you can replace them with underscores if you prefer.
        filename = f"{mm_yy}-{origin_city}-flights.json"
        filepath = DATA_DIR / filename

        # Avoid overwriting if same filename exists
        suffix = 1
        new_filepath = filepath
        while new_filepath.exists():
            new_filepath = DATA_DIR / f"{mm_yy}-{origin_city}-flights_{suffix}.json"
            suffix += 1

        # Write JSON
        with new_filepath.open("w", encoding="utf-8") as f:
            json.dump(records, f, indent=2)

    print(f"[Data Generation Complete] Generated {NUM_FILES} files in '{DATA_DIR}'.")
