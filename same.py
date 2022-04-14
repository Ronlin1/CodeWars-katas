a = [121, 144, 19, 161, 19, 144, 19, 11, 22]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
import math

def comp(a, b):
    sqs = None
    if a is None or b is None:
        return False
    elif None in a or None in b:
            return False
    else:
        sqs = [n**2 for n in a]
    
    
    
    # c =set(sqs).intersection(b)
    # return bool(set(sqs) & set(b))
        
        
    
    
    # print(sqs)
    # for n in b:
    #     n = math.sqrt(n)
    #     if n not in sqs and n not in a:
    #         return False
    # for n in a:
    #     new = n**2
    #     if new not in b:
    #         return False
    #     print(new)
    # return True

print(comp(a, b))



