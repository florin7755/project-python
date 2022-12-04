string=input("string= ")
result=string
vowels=('a','e','i','o','u','A','E','I','O','U')
for x in string:
    if x not in vowels:
        result=result.replace(x," ")
print("result=",result)