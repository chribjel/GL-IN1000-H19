def prosedyre1():
    p1a = 1
    p1b = 2
    print("prosedyre1:", p1a + p1b)


def prosedyre2(p2a, p2b):
    print("prosedyre2:", p2a + p2b)


def funksjon1():
    f1a = 1
    f1b = 2
    return f1a + f1b


def funksjon2(f2a, f2b):
    return f2a, f2b, f2a + f2b



prosedyre1()
prosedyre2(1, 2)
funksjon1()
sum = funksjon2(1, 2)

print(sum[0], "+", sum[1], "=", sum[2])