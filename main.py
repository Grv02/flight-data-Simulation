from data_generation import generate_data
from data_analysis import analyze_data

def main():
    """
    Orchestrates the entire pipeline:
      1) Generate synthetic flight data
      2) Analyze & clean the data
    """
    print("===== PHASE 1: DATA GENERATION =====")
    generate_data()

    print("\n===== PHASE 2: DATA ANALYSIS & CLEANING =====")
    analyze_data()


if __name__ == "__main__":
    main()
