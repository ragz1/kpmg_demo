object = {"x": {"y": {"z": "a"}}}

def get_value(obj, key):
    if key in obj:
        return obj[key]
    for k, v in obj.items():
        if isinstance(v, dict):
            result = get_value(v, key)
            if result is not None:
                return result

key_to_find = "x"
value = get_value(object, key_to_find)
print(value)




