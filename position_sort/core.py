from collections import defaultdict
from typing import List, Union

Number = Union[int, float]

def position_sort(arr: List[Number]) -> List[Number]:
    if not arr:
        return []

    position_map = defaultdict(list)
    for val in arr:
        position_map[val].append(val)

    sorted_keys = sorted(position_map.keys())
    result = []
    for key in sorted_keys:
        result.extend(position_map[key])
    return result
