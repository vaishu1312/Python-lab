def strpal(word):
   str2=word[::-1]
   if word==str2:
     return ('it is a palindrome')
   else:
       return('it is not a palindrome')
  
str1=input('enter a word ')
print(strpal(str1))


def strpal1(word):
   i=0
   j=len(word)-1
   while i<j:
      if word[i]!=word[j]:
         return ('it is not a palindrome')
      else:
         i+=1
         j-=1
   return ('it is a palindrome')

str1=input('enter a word ')
print(strpal1(str1))

#using recursion
def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
a=str(input("Enter string:"))
if(is_palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")

