def get_even_numbers():
    user_input = input("Enter numbers separated by spaces: ")
    lst = []
    for x in user_input.split():
        lst.append(int(x))
    even_numbers = []
    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
    print(f"Even numbers: {even_numbers}")
get_even_numbers()
