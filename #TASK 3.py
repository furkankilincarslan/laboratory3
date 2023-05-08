#TASK 3
 
def get_unique_numbers():
    user_input = input("Enter a comma-separated list of items: ")
    items = user_input.split(",")
    unique_numbers = set()

    for item in items:
        if item.isdigit():
            unique_numbers.add(int(item))
        else:
            return "bad data"
    return unique_numbers

unique_numbers = get_unique_numbers()
if unique_numbers == "bad data":
    print("bad data")
else:
    unique_numbers = sorted(unique_numbers)
    print("Unique numbers:", end=" ")
    print(*unique_numbers, sep=",")
