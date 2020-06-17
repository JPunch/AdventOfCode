a = list(range(0,91,1))[::-1]
b = list(range(-1,-91,-1))
c = list(range(-91,-181,-1))
d = list(range(91,181,1))
e = [a,b,c,d]


def dumbsort(x):
    for i in x:
        if i <= 90 and i > 0:
            x[x.index(i)] = 90 + (1 / i)
        elif i == 0:
            x[x.index(i)] = 92
        elif i < 0 and i >= -180:
            x[x.index(i)] = -i + 180
        else:
            x[x.index(i)] = i + 270
    return x

if __name__ == "__main__":
    print(dumbsort(a))
    print(dumbsort(b))
    print(dumbsort(c))
    print(dumbsort(d))