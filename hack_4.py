"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""

def fn_hack_4(text):
    lenght = len(text)
    word = ""
    
    if lenght > 3:
        word = text[1:]
        word = word[:lenght-2]
    else:
        return text

    return word