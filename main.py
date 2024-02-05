import timeit
from  typing import Callable

from bm import boyer_moore_search
from kmp import kmp_search
from rabina import rabin_karp_search

#Завдання 1
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for i in range(len(self.table[key_hash])):
                if self.table[key_hash][i][0] == key:
                    self.table[key_hash].pop(i)
                    return True
        return False

#Завдання 2    
def binary_search(arr, value):
    low, high = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] < value:
            low = mid + 1
        else:
            upper_bound = arr[mid]
            high = mid - 1
    
    return iterations, upper_bound    


# iterations, upper_bound = binary_search([0.1, 3.2, 6.3, 7.5], 8.0)
# print(f"Кількість ітерацій: {iterations}")
# print(f"Верхня межа: {upper_bound}")

#Task 3
def read_file(filename):
    with open(filename, 'r', encoding='cp1251') as f:
        return f.read()


def benchmark(func: Callable, text_: str, pattern_: str):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}(text, pattern)"
    return timeit.timeit(stmt=stmt, setup=setup_code, globals={'text': text_, 'pattern': pattern_}, number=10)


if __name__ == '__main__':
    text = read_file('article.txt')
    real_pattern = "пошуку вимагає"
    fake_pattern = "fake pattern"

    text_2 = read_file('article_2.txt')
    real_pattern_2 = "Рекомендаційні системи"


    results = []
    for pattern in (real_pattern, fake_pattern):
        time = benchmark(boyer_moore_search, text, pattern)
        results.append((boyer_moore_search.__name__, pattern, time))
        time = benchmark(kmp_search, text, pattern)
        results.append((kmp_search.__name__, pattern, time))
        time = benchmark(rabin_karp_search, text, pattern)
        results.append((rabin_karp_search.__name__, pattern, time))    
    title = f"{'Алгоритм':<30} | {'Підрядок 1 в статті 1':<30} | {'Час виконання, сек'}"
    print(title)
    print("-" * len(title))
    for result in results:
        print(f"{result[0]:<30} | {result[1]:<30} | {result[2]}")

    results_2 = []
    for pattern in (real_pattern_2, fake_pattern):
        time = benchmark(boyer_moore_search, text_2, pattern)
        results_2.append((boyer_moore_search.__name__, pattern, time))
        time = benchmark(kmp_search, text_2, pattern)
        results_2.append((kmp_search.__name__, pattern, time))
        time = benchmark(rabin_karp_search, text_2, pattern)
        results_2.append((rabin_karp_search.__name__, pattern, time))    
    
    print("-" * len(title))
    title = f"{'Алгоритм':<30} | {'Підрядок 2 в статті 2':<30} | {'Час виконання, сек'}"
    print(title)
    print("-" * len(title))

    for result in results_2:
        print(f"{result[0]:<30} | {result[1]:<30} | {result[2]}")    