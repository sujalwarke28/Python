#Tower of Hanoi

def tower_of_hanoi(n, a, b, c):
    if n == 1:
        print("Move disk 1 from", a, "to", b)
        return

    tower_of_hanoi(n - 1, a, c, b)

    print("Move disk", n, "from", a, "to", b)

    tower_of_hanoi(n - 1, c, b, a)


n = int(input("Enter the number of disks: "))
tower_of_hanoi(n, 'A', 'C', 'B')


