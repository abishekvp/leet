def isSubsetSum(arr, target):
    if len(arr) == 0:
        return False
    if sum(arr) == target:
        return True
    for i in range(len(arr)):
        if sum(arr[:i]+arr[i:][1:]) == target:
            return True
    return False

test_cases = [
    # Basic cases
    {"target": 0, "values": [], "expected": False},
    {"target": 5, "values": [5], "expected": True},
    {"target": 3, "values": [5], "expected": False},

    # Two elements
    {"target": 3, "values": [1, 2], "expected": True},
    {"target": 4, "values": [1, 2], "expected": False},

    # Simple multi-element
    {"target": 6, "values": [1, 2, 3], "expected": True},   # 1+2+3
    {"target": 5, "values": [1, 2, 3], "expected": True},   # 2+3
    {"target": 4, "values": [1, 2, 3], "expected": True},   # 1+3
    {"target": 7, "values": [1, 2, 3], "expected": False},

    # Reveals bug in current logic
    {"target": 10, "values": [2, 3, 5, 7], "expected": True},  # 3+7 ❌
    {"target": 8, "values": [2, 3, 5], "expected": True},     # 3+5 ❌
    {"target": 9, "values": [2, 4, 6], "expected": False},

    # Larger arrays
    {"target": 15, "values": [5, 5, 5, 5], "expected": True},
    {"target": 20, "values": [5, 5, 5, 5], "expected": True},
    {"target": 6, "values": [1, 1, 1, 1, 1], "expected": False},

    # Duplicate values
    {"target": 4, "values": [2, 2, 2], "expected": True},
    {"target": 6, "values": [2, 2, 2], "expected": True},
    {"target": 5, "values": [2, 2, 2], "expected": False},

    # Zero handling
    {"target": 0, "values": [0, 0, 0], "expected": True},
    {"target": 1, "values": [0, 0, 1], "expected": True},
    {"target": 2, "values": [0, 0, 1], "expected": False},

    # Negative numbers
    {"target": 0, "values": [-1, 1], "expected": True},
    {"target": 3, "values": [-1, 2, 4], "expected": True},
    {"target": 1, "values": [-2, -1, 4], "expected": False},
]
print("Failed Cases :-")
for case in test_cases:
    if not isSubsetSum(case["values"], case["target"]) == case["expected"]:
        print(case)