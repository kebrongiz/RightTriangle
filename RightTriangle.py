#A

def right_triangle():
    for i in range(1, 7):
        row = []
        for j in range(1, i + 1):
            row.append(str(j))

        row.reverse()
        padding = " " * (12 - (2 * i))
        print(padding, end='')
        print(" ".join(row))


print("A. \n")
right_triangle()
print()
#B


def upside_down_right_triangle():
    for i in range(6, 0, -1):
        row = []
        for j in range(1, i + 1):
            row.append(str(j))
        padding = " " * (12 - (2 * i))
        print(padding, end='')
        print(" ".join(row))


print("B.\n")
upside_down_right_triangle()
