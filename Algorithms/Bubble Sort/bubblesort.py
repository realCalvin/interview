def main():
    a = [5, 8, 2, 6, 9, 1, 4, 3, 2]

    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    print(a)


if __name__ == '__main__':
    main()
