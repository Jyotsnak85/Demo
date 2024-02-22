# def binary (n,L1 , left ,right):
#     # left = 0
#     # right = len(L1)-1
#     if right >= left  :
#         mid = (left + right) // 2
#         if n == L1[mid]:
#             return mid
#         elif n < L1[mid]:
        
#             # left = 0 
#             # right =mid-1
#             return  binary(n,L1 , left ,mid-1)
#         else:
#             return binary(n,L1 , mid+1 ,right)
        
#     else:
#         return -1


# arr = [2,8,3,6,5]  
# n =  8  
# s= len(arr) 
# # print (s)
# result =(binary(n,arr,0,s-1))

# print (result)

# if result != -1:
# 	print("Element is present at index", str(result))

    
# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.

# Returns index of x in arr if present, else -1
# def binary_search(arr, low, high, x):

# 	# Check base case
# 	if high >= low:

# 		mid = (high + low) // 2

# 		# If element is present at the middle itself
# 		if arr[mid] == x:
# 			return mid

# 		# If element is smaller than mid, then it can only
# 		# be present in left subarray
# 		elif arr[mid] > x:
# 			return binary_search(arr, low, mid - 1, x)

# 		# Else the element can only be present in right subarray
# 		else:
# 			return binary_search(arr, mid + 1, high, x)

# 	else:
# 		# Element is not present in the array
# 		return -1

# # Test array
# arr = [ 2, 3, 4, 10, 40 ]
# x = 3

# # Function call
# result = binary_search(arr, 0, len(arr)-1, x)

# if result != -1:
# 	print("Element is present at index", str(result))
# else:
# 	print("Element is not present in array")


def binary_search(n, L1, left, right):
    if right >= left:
        mid = (left + right) // 2
        if n == L1[mid]:
            return mid
        elif n < L1[mid]:
            # left = 0 
            # right = mid - 1
            return binary_search(n, L1, left, mid - 1)
        else:
            return binary_search(n, L1, mid + 1, right)
    else:
        return -1

arr = [2, 8, 3, 6, 5]  
n = 8  
s = len(arr) 
result = binary_search(n, arr, 0, s - 1)

print("Result:", result)



