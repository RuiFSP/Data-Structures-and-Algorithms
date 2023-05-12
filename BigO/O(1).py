def add_items(n):
    return n + n


def add_items2(n):
    return n + n + n


if __name__ == "__main__":
    print(add_items(10))
    print(add_items2(10))

# the output will be one operation
# Time complexity will be O(1) , also called constant
# Even if the n increases, we simplify O(2) -> O(1)
