def n_queens(k, n):
    for i in range(1, n + 1):
        if place(k, i):
            x[k] = i
            if k == n:
                print("The Positions are :-", end=" ")
                for j in range(1, n + 1):
                    print(x[j], end=" ")
                print()
            else:
                n_queens(k + 1, n)

def place(k, i):
    for j in range(1, k):
        if x[j] == i or abs(x[j] - i) == abs(j - k):
            return False
    return True

if __name__ == "__main__":
    print("Enter the number of Queens:")
    n = int(input())
    x = [0] * (n + 1)

    if n == 2 or n == 3:
        print("Not Possible!")
    else:
        n_queens(1, n)
