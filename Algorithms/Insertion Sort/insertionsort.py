def main():
    a = [5, 8, 2, 6, 9, 1, 4, 3, 2]

    for i in range(1, len(a)):
        pos, temp = i, a[i]

        while temp < a[pos-1] and pos > 0:
            a[pos] = a[pos-1]
            pos -= 1
        a[pos] = temp
    print(a)


if __name__ == '__main__':
    main()
