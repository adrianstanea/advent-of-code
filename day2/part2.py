def is_safe(data: list):
    diffs = []
    for left, right in zip(data[:-1], data[1:]):
        diff = right - left
        diffs.append(diff)

        if abs(diff) < 1 or abs(diff) > 3:
            return False

    is_increasing = all([val > 0 for val in diffs])
    is_decreasing = all([val < 0 for val in diffs])
    is_monotonic = is_increasing or is_decreasing
    return is_monotonic


n_safe_reports = 0

with open("input.txt") as f:
    for line in f:
        data = [int(c) for c in line.strip().split(" ")]

        subsets_safe = []
        for i in range(len(data)):
            subsets_safe.append(is_safe(data[:i] + data[i+1:]))
        if not any(subsets_safe):
            continue
        n_safe_reports += 1

print(f"Number of safe reports: {n_safe_reports}")
