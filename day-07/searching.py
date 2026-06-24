## Searching algo

num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
s=int(input("Enter the number to search: "))
def linear_search():
    for i in range(len(num)):
        if num[i] == s:
            print(s,"is present in the list")
            break
    else:
        print(s,"is not present in the list")
def binary_search():
    n=len(num)
    l=0
    h=n-1
    while l<=h:
        mid=l+(h-l)//2
        if mid==s:
            return mid
            break
        elif s<mid:
            h=mid-1
        else:
            l=mid+1
    return -1
    
linear_search()
# number=binary_search()
# if number!=-1:
#     print(f"{s} is present in the list")
# else:
#     print(f"{s} is not present in the list")
    
