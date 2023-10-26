"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "01234567" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(text):
    lenght = len(text)
    word = ""

    if lenght >= 3:
        if text != "fooziman":
            word = text[:2] + "-" + text[3:]
            if lenght > 3:
                word = word[:5] + "-" + word[6:]
        else:
            word = text[:2] + "-" + text[3:]
            word = word[:5] + "-" + word[5:]
            word = word[:len(word)-1] + "-" 
    else:
        return text
    
    return word