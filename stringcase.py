#converts lower to upper and vice versa
string_1='CAPItAL'
string_2=' '
for i in range(len(string_1)):
    code=ord(string_1[i])
    if 65<=code<=90 :
        code=code+32
        string_2 = string_2 + chr(code)
    elif 97<=code<=122 :
            code=code-32
            string_2 = string_2 + chr(code)
            
            
print(string_2)        
    
