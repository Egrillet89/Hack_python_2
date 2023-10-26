"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(data):
    new_data = {}
    for key, value in data.items():
        if key == "foo":
            new_data[key.capitalize()] = value.capitalize().replace("k", "")

    return new_data