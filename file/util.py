import os

def input_validation_list(_text,_type,_list):
    v = input(_text)
    try:
        if v in _list:
            return _type(v)
    except:
        return input_validation_list(_text,_type,_list)
    

def input_split_validation_type(_text,_split,_type):
    value = input(_text).strip().split(_split)
    try:
        return _type(value)
    except:
        return input_split_validation_type(_text,_split,_type)

def clear():
    os.system('cls' if os.name=='nt' else 'clear')