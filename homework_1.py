# task_1

print("----------Que.-1--------")
x,y,z=10,20.20,'Hello'
print(x)
print(y)
print(z)

print("--------Que.-2----------")
a=2+4j
b=2
a,b=b,a
print("a=",a,"and","b=",b)

print("---------Que.-3----------")
a=1
b=2
q=a
a=b
b=q
print("a=",a,"and","b=",b)
a,b=b,a
print("a=",a,"and","b=",b)

print("----------Que.-4----------")
type_here=input()
print(type_here)

print("----------Que.-5----------")
print("Enter the two value in the range of 1 and 10")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if a and b in range (0,10):
    result=a+b+30
    print(result)

print("----------Que.-6-----------")
print("Enter any data to see it's data type")
h=input()
p=type(h)
print("The input value Data type is:",p)

############################################################################################
print("----------Que.-7-----------")

s =str(input())
def convert(s):
    if(len(s) == 0):
        return
    s1 = ''
    s1 += s[0].upper()
    for i in range(1, len(s)):
        if (s[i] == ' '):
            s1 += s[i + 1].upper()
            i += 1
        elif(s[i - 1] != ' '):
            s1 += s[i]
    print("CamelCase:",s1)
print("Uppercase:",s.upper())
print("Lowercase:",s.lower())


# Driver Code

convert(s)
############################################################################################
print("----------Que.-8-----------")
g=3
print(g)
print(type(g))
g="three"
print(g)
print(type(g))

