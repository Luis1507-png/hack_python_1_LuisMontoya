"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    result = result.replace(result,"f00z1m@n")
    return result  

print(fn_hack_5()) 