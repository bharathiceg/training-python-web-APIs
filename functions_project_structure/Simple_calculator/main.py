from calculator import operations
from calculator import history
def get_numbers():
    try:
        number1 = float(input("enter number 1:"))
        number2 = float(input("enter number 1:"))
        return number1,number2
    except ValueError:
        print("Invalid entry enter the numbers alone:")
        return None,None
def main():
    print("Enter the operation u needed add \n sub \n mul \n div\n")
    print("If u want to exit type exit or wanted to view previous history type history")
    while True:
            op= input("enter the choice of operation    : ")
            x,y= get_numbers()
            if op=="exit":
                 break
            elif op=="history":
                 history.History.show()
                 continue
            elif op not in {"add","sub","mul","div"}:
                print("invalid operation")
                continue
            elif op=="add":
                 re=operations.add(x,y)
            elif op=="sub":
                 re=operations.sub(x,y)
            elif op=="mul":
                 re=operations.mul(x,y)
            elif op=="div":
                 re=operations.add()
            
            print(re)
                 
            
     
if __name__ == "__main__":
    main()





            
