"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""

def fn_hack_3(text):
    lenght = len(text)

    new_string = text.\
        replace('a', '@').\
        replace('e', '3').\
        replace('i', '¡').\
        replace('o', '0').\
        replace('u', 'v')

    word = new_string[:0] + new_string[0].upper() + new_string[1:]
    if word[lenght-1] != "v":
        word = word[:lenght-1] + word[lenght-1].upper() 

    return word
    
