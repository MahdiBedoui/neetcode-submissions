from typing import List


def create_list_of_odds(n: int) -> List[int]:
    odds_list = [i for i in range(1,n+1,+2)]
    return odds_list
    pass


# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))
