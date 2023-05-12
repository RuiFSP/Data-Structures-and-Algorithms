def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)


if __name__ == '__main__':
    print_items(10)

# first double loop (i,j) we have O(n^2)
# second look (k) we have O(n)
# Time complexity is O(n^2 + n) = O(n^2), because if n -> infinity , the dominant term will always be n^2,
# we can simplify it by approximating it to O(n^2 + n) = O(n^2)
