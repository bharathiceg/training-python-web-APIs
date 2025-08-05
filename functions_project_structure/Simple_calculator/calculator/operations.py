def add(n1,n2):
    result=n1+n2
    return(result)
def sub(n1,n2):
    result=n1-n2
    return(result)
def mul(n1,n2):
    result=n1*n2
    return(result)
def div(n1,n2):
    if n2 == 0:
        raise ValueError("Cannot divide by zero.")
    result=n1/n2
    return(result)