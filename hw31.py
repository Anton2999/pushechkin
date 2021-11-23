def spisok():
    b = list()
    z = input()
    while z != "":
        b.append(z)
        z = input()
    return b


if __name__ == "__main__":
    print(spisok())
