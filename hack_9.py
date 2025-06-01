"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    result = [1,2,3]
    length = len(result)
    n=1 
    while n<=length+2:
        result.insert(n,"@")
        n+=2
    return result  

print(fn_hack_9())