###Question1
# Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o',
#and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5
s='azcbobobegghakl'
count=0
for item in s:
    if item in 'aeiou':
        count+=1
print('Number of vowels:', count)
###Question2
#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
#Number of times bob occurs is: 2
a = 'azcbobobegghaklbob'
timer=0
for x in range (len(a)-2):
    if a[x:x+3]=='bob':
        timer+=1
print('Number of times bob occurs is:', timer)
###Question3:print an inverted star pattern
rows=int(input('Enter the number of rows : '))
for i in range(rows,0,-2):
               print('*' *i)
###Question4:print a traingle star pattern
row=int(input('Enter the number of rows : '))
for j in range(row,0,-1):
      space=' '*(row-j)
      star='*'*(2*j-1)
      print(space+star)
###Question5:Assume s is a string of lower case characters.
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#Longest substring in alphabetical order is: abc
t='azcbobobegghakl'
longest = t[0]
current = t[0]
for c in t[1:]:
    if c >= current[-1]:
        current += c
        if len(current) > len(longest):
            longest = current
    else:
        current = c
print ("Longest substring in alphabetical order is:", longest)

      
      
      

    
    

       
      

