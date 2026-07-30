from typing import List

def get_words_length(words: List[str]) -> List[str]:
    return len(words)

def sort_words(words: List[str]) -> List[str]:
    words.sort(key=get_words_length, reverse=True)
    return words
    pass

def get_num_abs(number: int) -> int:
    return abs(number)

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=get_num_abs)
    return numbers
    pass


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
