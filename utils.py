import random
import datetime
from typing import List, Optional

def random_date_within_current_month() -> str:
    """
    Return a random date (YYYY-MM-DD) within the current month.
    """
    today = datetime.date.today()
    start_of_month = today.replace(day=1)

    # Start of next month (to find how many days in this month)
    if start_of_month.month == 12:
        next_month = start_of_month.replace(year=start_of_month.year + 1, month=1, day=1)
    else:
        next_month = start_of_month.replace(month=start_of_month.month + 1, day=1)

    days_in_month = (next_month - start_of_month).days
    random_day = random.randint(1, days_in_month)
    random_date = start_of_month + datetime.timedelta(days=random_day - 1)
    return random_date.isoformat()

def percentile(sorted_list: List[float], percentile_val: float) -> Optional[float]:
    """
    Compute the `percentile_val` (e.g., 95 for 95th percentile)
    from a pre-sorted list of numbers. Returns None if the list is empty.
    """
    if not sorted_list:
        return None
    if percentile_val <= 0:
        return sorted_list[0]
    if percentile_val >= 100:
        return sorted_list[-1]

    index = (len(sorted_list) - 1) * (percentile_val / 100.0)
    lower = int(index)
    upper = lower + 1
    if upper >= len(sorted_list):
        return sorted_list[-1]
    weight = index - lower
    return sorted_list[lower] * (1 - weight) + sorted_list[upper] * weight
