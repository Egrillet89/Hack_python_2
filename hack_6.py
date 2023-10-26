"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
      ["1","2","3","4","5"]
      ["0","1","2","3","4"]
text: [] output => ["0"] 
"""

def fn_hack_6(arr):
    lenght = len(arr)
    new_array = []
    word = []

    for number in range(lenght):
        word.append(str(number+1))

    if arr == []:
        return ["0"]

    for pos in range(lenght):

        if (pos+1) % 2 == 0:
            new_array.append("-")
        else:
            new_array.append(word[pos])

    return new_array
