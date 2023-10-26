"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""

def fn_hack_2(text):
    new_string = text.\
        replace('a', '').\
        replace('e', '').\
        replace('i', '').\
        replace('o', '').\
        replace('u', '')
    
    return new_string  