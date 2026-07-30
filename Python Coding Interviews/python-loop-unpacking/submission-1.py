from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    name,s=scores[0]
    for i in range(len(scores)-1):
        if s<scores[i+1][1]:
            name,s=scores[i+1]
    return name
    pass


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))