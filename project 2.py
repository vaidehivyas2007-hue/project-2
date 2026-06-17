# Logic Box Project
# Pattern Generator and Number Analyzer

while True:
    print("\n========== LOGIC BOX ==========")
    print("1. Pattern Generator")
    print("2. Number Analyzer")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    # Pattern Generator
    if choice == "1":
        rows = int(input("Enter number of rows: "))

        if rows <= 0:
            print("Invalid row count!")
            break

        print("\nRight-Angled Triangle Pattern:")
        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end=" ")
            print()

    # Number Analyzer
    elif choice == "2":
        start = int(input("Enter start number: "))
        end = int(input("Enter end number: "))

        if end < start:
            print("End number must be greater than start number!")
            continue

        total = 0

        print("\nOdd and Even Numbers:")
        for num in range(start, end + 1):

            if num == 0:
                pass

            if num % 2 == 0:
                print(num, "- Even")
            else:
                print(num, "- Odd")

            total += num

        print("Sum of all numbers =", total)

    # Exit
    elif choice == "3":
        print("\nThank You For Using Logic Box Project!")
        break

    else:
        print("Invalid Choice! Try Again.")
