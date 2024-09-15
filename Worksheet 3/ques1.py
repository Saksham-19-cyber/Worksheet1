def difference_with_17():
    n = int(input("Enter a number: "))
    if n > 17:
        return 2 * (n - 17)
    else:
        return 17 - n


result = difference_with_17()
print(f"Difference: {result}")