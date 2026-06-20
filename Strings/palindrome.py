'''Palindrome String'''

def is_palindrome(s):
     left=0
     right= len(s)-1

     while left < right:
          if s[left] != s[right]:
               return False
          left +=1
          right -=1
     return True

string = "radar"
result= is_palindrome(string)
print(f'Is "{string}" a palindrome? {result}')

        

   
          
      