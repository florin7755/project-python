string=input("string= ")
print("string=",string)
z=0
y=0
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in string:
   if i in vowels:
      y+=1
   else:
      z+=1
print("vowels=",y)
print("consonants=",z)