def count_calls():
    global calls
    calls +=1

def string_info (string_1):
    tuple_1 = (len(string_1), string_1.upper(), string_1.lower(),)
    count_calls()
    return tuple_1

def is_contains (name, list_):
    for i in list_:
        if i.lower() == name.lower():
            count_calls()
            return True
        else:
            continue
    count_calls()
    return False

calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print('Result calls = ', calls)