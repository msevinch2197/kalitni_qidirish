def check_key(d, key):
    return key in d

def get_value(d, key):
    return d.get(key, "Topilmadi")

# test
info = {'name': 'Ali', 'age': 25, 'city': 'Toshkent'}
print(check_key(info, 'age'))
print(get_value(info, 'age'))
