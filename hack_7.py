"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(arr):
    lenght = len(arr)
    number = 1
    word = []

    if arr == []:
        return [0]
    elif arr == [0]:
        return [0]

    while(number <= lenght):
        if (number) % 2 == 0:
            word.append(number)
        else:
            word.append(str(number))

        number += 1

    return word
print(fn_hack_7(["a","b","c","d","e"]))