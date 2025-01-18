#Count the number of ocurrances in list


def count_occurrences(lst, x):
    count = 0

    for i in lst:
        if i == x:
            count += 1

    return count


lst = [1, 2, 3, 4, 2, 2, 5]
x = int(input("Enter the number: "))
print("The number", x, "appears", count_occurrences(lst, x), "times in the list")