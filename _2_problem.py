# Write a Python program to reverse a string.

def reverse(s):
    str =" "
    for i in s:
        str = i + str
    return str

s = input("Enter the string : ")
print("The orignal : ",end=" ")
print(s)

print("The reversed string :",end =" ")
print(reverse(s))
