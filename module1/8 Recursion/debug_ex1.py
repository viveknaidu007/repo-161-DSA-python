# 0, 1, 1, 2, 3, 5, 8
# 0, 1, 2, 3, 4, 5, 6
def get_fibonacci(n):
    if n == 0 or n == 1:
        return n
    return get_fibonacci(n-1) + get_fibonacci(n-2)

if __name__ == "__main__":
    print(get_fibonacci(6))