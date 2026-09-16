from datetime import datetime
from collections import Counter


def find_peak_usage(logs: list[str]) -> int:
    """
    Finds the hour of the day (0-23) with the highest volume of logins.
    In case of a tie, the earliest hour is returned.
    """
    if not logs:
        return 0  # Return a default or handle empty input gracefully

    # Extract the hour from each ISO timestamp string
    hours = [datetime.fromisoformat(log).hour for log in logs]

    # Count occurrences of each hour
    counts = Counter(hours)

    # Find the peak hour based on max count, resolving ties by earliest hour
    # Python's min() with a key sorts primarily by the key (negative count for max)
    # and secondarily by the hour itself (ascending order for earliest tie)
    peak_hour = min(counts.keys(), key=lambda h: (-counts[h], h))

    return peak_hour


# --- Example Usage ---
if __name__ == "__main__":
    sample_logs = [
        "2026-08-04T13:21:18",
        "2026-08-04T13:45:00",
        "2026-08-04T14:02:11",
        "2026-08-04T14:59:59",
        "2026-08-04T08:15:30"
    ]

    # In this sample, hour 13 has 2 logins, and hour 14 has 2 logins.
    # Because of the tie, it should return the earliest hour: 13.
    result = find_peak_usage(sample_logs)
    print(f"The peak usage hour is: {result}")
