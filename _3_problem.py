# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

str = input("Enter the string : ")
def char(str):
    upper_case = 0
    lower_case = 0
    for i in str:
        
       if i>='A' and i<='Z':
        upper_case += 1

       if i >='a' and i<='z':
        lower_case += 1
    
    print("No of Upper case characters are :  ",upper_case)

    print("NO of lower case characters are : ",lower_case)
    return(str)
char(str)