# flight-data-Simulation

A two-phase Python pipeline for simulating and analyzing flight data. The pipeline is organized as a package named flight_pipeline with a modular structure.

Overview
Phase 1: Data Generation

Creates thousands of JSON files under /tmp/flights/ (by default).
Each file contains flight records with various fields (date, origin, destination, duration, passengers).
A small percentage of records are “dirty,” meaning they have None values in one or more fields.
Phase 2: Data Analysis

Reads all generated JSON files and processes flight records.
Skips dirty records, then calculates metrics such as:
Total records processed & total dirty records.
Top 25 destination cities by total arriving passengers, plus the average and 95th percentile flight duration.
Net passenger balance per city (arrivals minus departures), identifying which city has the highest and lowest net passenger count.
