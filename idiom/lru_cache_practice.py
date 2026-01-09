from functools import lru_cache

@lru_cache(maxsize=100)
def fibonacci(n: int) -> int:
    print(f"computing fibonacci({n})")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    # it will be extremely slow without @lru_cache
    fibonacci(40)