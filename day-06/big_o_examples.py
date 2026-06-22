# ## (O)

# arr=[12,2,3,4,23,44,10]
# print(arr[2])

# ## (O(n)

# for i in arr:
#     print(i)

    
# ## O(n^2)

# for i in arr:
#     for j in arr:
#         print(i,j)


##Optional task whether string is palindrome or not

str=input("Enter the string: ")
stk=[]

for char in str:
    stk.append(char)

rev_str=""
while stk:
    rev_str+=stk.pop()

if str==rev_str:
    print("Palindrome")
else:
    print("Not a Palindrome")