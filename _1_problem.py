# Write a Python function to sum all the numbers in a list.


size = int(input("Enter the size of eliment : "))
lst = []
result = 0
add=()
for i in range(size):
    element = int(input("enter the value : "))
    lst.append(element)
print(lst)

def sum(lst,size):
    if(size == 0):
        return 0
    else:
        return lst[size - 1] + sum(lst,size - 1)

total = sum(lst, len(lst))
print("Sum of element : ",total)