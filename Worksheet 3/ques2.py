def is_within_100_1000_or_2000():
    n = int(input("Enter a number: "))
    return 100 <= n <= 1000 or n == 2000


if is_within_100_1000_or_2000():
    print("The number is within the range.")
else:
    print("The number is not within the range.")