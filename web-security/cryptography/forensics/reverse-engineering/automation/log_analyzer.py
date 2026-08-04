from collections import Counter
from pathlib import Path

LOG_FILE = Path("sample.log")


def extract_ip(line):
    parts = line.split()

    if not parts:
        return None

    return parts[0]


def analyze_log(path):
    counts = Counter()

    with path.open("r", encoding="utf-8") as log:
        for line in log:
            ip = extract_ip(line)

            if ip:
                counts[ip] += 1

    return counts


if __name__ == "__main__":
    results = analyze_log(LOG_FILE)

    print("Most frequent source addresses:")

    for ip, count in results.most_common(10):
        print(f"{ip}: {count}")
