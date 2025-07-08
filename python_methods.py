Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name="gopal is a good person"
name.upper()
'GOPAL IS A GOOD PERSON'
name.lower()
'gopal is a good person'
name.capitalize()
'Gopal is a good person'
name.swapcase()
'GOPAL IS A GOOD PERSON'
name.center(30,"*")
'****gopal is a good person****'
name.ljust(30,"~")
'gopal is a good person~~~~~~~~'
name.ljust(30," ")+":"
'gopal is a good person        :'
age.rjust(30,"*")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    age.rjust(30,"*")
NameError: name 'age' is not defined
name.rjust(30,"*")
'********gopal is a good person'
'56'.zfill(5)
'00056'
''.zfill(12)
'000000000000'
name
'gopal is a good person'
name.find ('gopal')
0
name.rfind('gopal)
           
SyntaxError: unterminated string literal (detected at line 1)
name
           
'gopal is a good person'
name.find('a')
           
3
name.rfind('a')
           
9
name
           
'gopal is a good person'
name.count('o')
           
4
'PFS30' startswith('PFS')
           
SyntaxError: invalid syntax
'PFS30'.startswith('PFS')
           
True
'abc'.isalpha()
...            
True
>>> 'abc122'.isalpha()
...            
False
>>> '2468'.isdigit()
...            
True
>>> 'gopal24'.isalnum()
...            
True
>>> 'HEMANTH'.isupper()
...            
True
>>> 'HEMANTH'.islower()
...            
False
>>> 'myvar'.isidentifier()
...            
True
>>> '8'.isidentifier()
...            
False
>>> name
...            
'gopal is a good person'
>>> name.replace('gopal','hemanth')
...            
'hemanth is a good person'
>>> name
...            
'gopal is a good person'
>>> name=name.replace('gopal','hemanth')
...            
>>> name
...            
'hemanth is a good person'
>>> name.split('')
...            
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    name.split('')
ValueError: empty separator
>>> name.split(' ')
...            
['hemanth', 'is', 'a', 'good', 'person']
