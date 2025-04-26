def add (n, k):
    for i in range(2, n):
        if n % i == 0:
            print("عدد اول نیست")
            return
    c = 0
    while c < k:
        n += 1
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            c = c+1
    print(n)

add (10, 5)
