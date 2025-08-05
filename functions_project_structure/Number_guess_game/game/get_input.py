def get_input():
    
    while True:
        try:
             guess = int(input("Enter the number(1-100):"))
             return guess
        except ValueError:
            print("Invalid entry")
