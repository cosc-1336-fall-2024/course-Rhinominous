import devprocess

def main():
    value1 = input("Enter value 1 ")
    value2 = input("Enter value 2 ")

    result = devprocess.add_numbers(int(value1), int(value2))
    print(result)

main()