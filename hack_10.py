"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result = "fooziman"
    transformaciones = {
        'o': '0',
        'i': '1',
        'a': '@'
    }
    lista = [] 
    for char in result:  
        if char in transformaciones:
            lista.append(transformaciones[char]) 
        else:
            lista.append(char.upper()) 
            
    result = lista
    return result  

print(fn_hack_10())
