from pathlib import Path

# Directory to store/read the JSON flight files
DATA_DIR = Path("/tmp/flights")

# Approx. number of JSON files to generate
NUM_FILES = 5000

# Each generated file has this many records
RECORDS_PER_FILE_MIN = 50
RECORDS_PER_FILE_MAX = 100

# Flight duration range (in seconds) -> e.g., 30 mins to 10 hrs
FLIGHT_DURATION_RANGE = (1800, 36000)

# Number of passengers range
PASSENGER_RANGE = (10, 300)

# Dirty record probability range [0.5%, 1%]
DIRTY_RECORD_PROB_MIN = 0.5
DIRTY_RECORD_PROB_MAX = 0.1

# If you want to pick a random subset of the static city list each run:
MIN_CITIES = 100   
MAX_CITIES = 200 


CITY_LIST = [
    # United States
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
    "Austin", "Jacksonville", "Fort Worth", "Columbus", "San Francisco",
    "Charlotte", "Indianapolis", "Seattle", "Denver", "Washington",
    "Boston", "El Paso", "Nashville", "Detroit", "Oklahoma City",
    "Portland", "Las Vegas", "Memphis", "Louisville", "Baltimore",
    
    # Canada
    "Toronto", "Montreal", "Vancouver", "Calgary", "Edmonton",
    "Ottawa", "Winnipeg", "Quebec City", "Hamilton", "Kitchener",
    
    # Europe
    "London", "Berlin", "Madrid", "Rome", "Paris",
    "Vienna", "Budapest", "Warsaw", "Prague", "Dublin",
    "Barcelona", "Munich", "Milan", "Brussels", "Amsterdam",
    "Copenhagen", "Stockholm", "Oslo", "Helsinki", "Lisbon",
    
    # Latin America
    "Mexico City", "São Paulo", "Rio de Janeiro", "Buenos Aires",
    "Santiago", "Bogotá", "Lima", "Quito", "Caracas", "Guadalajara",
    
    # Asia
    "Tokyo", "Seoul", "Beijing", "Shanghai", "Hong Kong",
    "Singapore", "Bangkok", "Mumbai", "Delhi", "Jakarta",
    "Kuala Lumpur", "Taipei", "Manila", "Osaka", "Shenzhen",
    
    # Middle East
    "Dubai", "Abu Dhabi", "Riyadh", "Jeddah", "Istanbul",
    "Ankara", "Tehran", "Jerusalem", "Doha", "Kuwait City",
    
    # Africa
    "Cairo", "Lagos", "Kinshasa", "Johannesburg", "Nairobi",
    "Casablanca", "Cape Town", "Addis Ababa", "Algiers", "Accra",
    
    # Australia / Oceania
    "Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide",
    "Auckland", "Wellington", "Christchurch", "Suva", "Port Moresby"
]

