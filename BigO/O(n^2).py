def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


if __name__ == '__main__':
    print_items(10)

# we need "generate" n*n items goes form 0,0 to 9,9
# Time complexity O(n * n) = O(n^2)
# O(n^2) "needs" more operations, so time complexity is higher
