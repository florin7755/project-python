string=input("string=  ")
print('string=',string)
x=" "
y=" "
for i in string:
    if i.isnumeric:
        x=x+i
else:
        y=y+i
print("number=",x)
print("character=",y)


print()
string=input("string=  ")
print('string=',string)
res=[int(i) for i in string.split() if i.isdigit()]
#res1=[chr(i) for i in string.split() if i.isdigit()]
print("list2=",str(res))
#print("list1=",str(res1))
