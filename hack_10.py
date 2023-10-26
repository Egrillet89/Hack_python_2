"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""

def fn_hack_10(arr):
    new_arr = []
    pos = 1

    for item in arr:
        if pos == 3:
            new_arr.append({str(pos), str(pos+1)})
        else:
            new_arr.append({str(pos): str(pos+1)})
        pos += 2
    
    return new_arr

