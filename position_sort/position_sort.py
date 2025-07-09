def position_sort(arr, bin_width=1e-2, sort_within_bucket=True):
    """
    Position Sort: Non-comparison-based sorting algorithm for real numbers.

    Parameters:
    - arr (List[float]): List of real numbers to be sorted.
    - bin_width (float): Resolution of binning. Smaller bin_width = higher precision.
    - sort_within_bucket (bool): Whether to sort values inside each bucket.

    Returns:
    - List[float]: Sorted array.
    """
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)
    bucket_count = int((max_val - min_val) / bin_width) + 1
    buckets = [[] for _ in range(bucket_count)]

    for val in arr:
        index = int((val - min_val) / bin_width)
        buckets[index].append(val)

    sorted_arr = []
    for bucket in buckets:
        if sort_within_bucket and len(bucket) > 1:
            sorted_arr.extend(sorted(bucket))
        else:
            sorted_arr.extend(bucket)

    return sorted_arr


# Example usage:
if __name__ == "__main__":
    test_data = [3.14, -2.71, 0.0, 1.41, -3.0, 2.71, 3.14, -2.72]
    result = position_sort(test_data, bin_width=0.01, sort_within_bucket=True)
    print("Original:", test_data)
    print("Sorted  :", result)
