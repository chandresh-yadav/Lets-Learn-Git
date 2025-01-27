def rev_inp(value):
    if isinstance(value,str):
        return value[::-1]
    elif isinstance(value,int):
        return (str(value))[::-1]
    else:
        return "Invalid Input"
        
print(rev_inp(563.56))