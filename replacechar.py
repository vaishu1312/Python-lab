string_1='hello'
string_2=' '
for i in range(len(string_1)):
    if 'e' not in string_1[i]:
        string_2 = string_2 + string_1[i]
    else:
        string_2= string_2+ '@'
    
print(string_2)
