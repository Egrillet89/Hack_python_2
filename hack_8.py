"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b"] output => ["2","1"]
"""

def fn_hack_8(arr):
    length = len(arr)
    new_arr = []

    if (length % 2) == 0:
        for number in range(length):
            new_arr.insert(0, str(number+1))
    else:
        for number in range(length):
            new_arr.insert(0, arr[number] + "-" + str(number+1))

    return new_arr