str = "[()](" 

def is_balanced(str):
    pairs = { ")": "(", "}":"{", "]":"["}
    stack =[]
    for item in str:
        if item in pairs.values():
            stack.append(item)   
        else:
            curr = stack.pop() 
            if curr != pairs[item]:   
                return False
    
    if len(stack) == 0:
        return True
    else:
        return False

print(is_balanced(str))