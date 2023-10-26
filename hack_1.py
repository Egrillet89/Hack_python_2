"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""

def fn_hack_1(text):

    if len(text) >= 3:
        word = text[:1] + text[1].upper() + text[2:]
        if len(text) > 4:
            word = word[:4] + word[4].upper() + word[5:]
    else:
        return text
    
    return word

