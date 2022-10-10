def kek():
    return 1
    
def calc(n1, op, n2):
    operations = ['+', '-', '*', '/']
      
    if op in operations:
        
        if op == '+':
           return(n1 + n2)
        elif op == '-':
            return(n1 - n2)
        elif op == '*':
            return(n1 * n2)
        elif op == '/':
            if n2 != 0:
                return(n1 / n2)
            else:
                return("Zero division")
    else:
        return("Unsupported operation")
    