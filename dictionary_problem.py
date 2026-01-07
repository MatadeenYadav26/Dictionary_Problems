#Problem-1 : Print Unique elements in array : Print unique elements in array, Display all the unique elements given in the present array. #Problem-2: Count frequency of array element.
# a = [1,1,1,2,2,2,2,3,3,4,4,4,4,4,5,5,5,5,5,6,6,7,8,8,8,9,10]
#method-1
# j = set(a)
# print(j)
#method-2
# d = {}
# for i in a :
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1

# print(d)
# #print unique elements in array :
# print(d.keys())

#Problem 3:Leet-Code : Jewels & Stones - #Hashing

# def numjewelsinstone (self,jewels: str, stones: str ) -> int:
#     d = {}
#     for i in stones:
#         if i in d.keys():
#             d[i] += 1
#         else:
#             d[i] = 1
#     count = 0
#     for i in d.keys():
#         if i in jewels:
#             count += d[i]

#     return(count)   

#Problem - 4 : check if sentence is pangram: pangram means a sentence of english where every word of english alphabet atleast occur once. #Leetcode

# d = {}
# for i in sentence:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1

# if len(d.keys()) == 26:
#     return True
# else:
#     return False

#Problem - 05 : First letter to appear twice. #Leetcode
# d  = {}

# for i in s:
#     if i in d.keys():
#         return i 
#     else:
#         d[i] = 1

#Problem - 6 : Leetcode : sum of unique elements 

# d = {}

# for i in nums : 
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1

#     sum = 0
#     for i in d:
#         if d[i] == 1:
#             sum = sum + i

#         return sum

# Problem - 07 : Leetcode : Sort the people : eg : descending height name & height list :
# names = ['aman','mata','deen']
# heights = [179,177,178]

# d = {}

# for i in range(len(names)):
#     d[names[i]] = heights[i]

# # sort by height (descending)
# sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)

# # extract names
# names = [name for name, height in sorted_items]

# print(names)

#Problem:08 : Check if 2 strings have same frequency

# s1 = "aabbccdd"
# s2 = "baccabdd"

# if len(s1) == len(s2):
#     d = {}
#     for i in s1:
#         if i in d.keys():
#             d[i] += 1
#         else:
#             d[i] = 1
    
#     for i in s2:
#         if i in d.keys():
#             d[i] -= 1
#         else:
#             print("An extra element was found.")
    
#     for i in d:
#         if d[i] != 0:
#             print("Sorry, your element are not same.")
#             break
#         else:
#             print("your strings are same.")

# else:
#     print("Not Same")

#Problem:09 : Find duplicates in array hash sets:

# a = [1,1,2,3,4,5,6,7,7,8,9,7,6,5,3,1]

# d ={}

# for i in a :
#     if i in d.keys():
#         d[i] += 1
#     else: 
#         d[i] = 1

# print(d)

# for i in d :
#     if d[i] > 1:
#         print(i)

#Problem:10 :Find the Most frequent Even Element.#LEETCODE

# d = {}

# for i in nums:
#     for i % 2 == 0:
#         if i in d.keys():
#         d[i] += 1
# else:
#     d[i] = 1

# if not d :
#     return -1

# max_f = max(d.values())

# cand = [num for num , freq in d.items() if freq == max_f]

# return min(cand)

#Problem:11 : 2283 : Leetcode : check if a number has equal digit count and digit value :

# d = {}
# for i in num    :
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1

# for i in range (len(num)):
#     if d.get(str(i),0) == int(num[i]):
#         continue
#     else:
#         return False
# return True

#Problem: 12 : Intersection of 2 arrays :

a = [1,2,2,1]
b = [2,2]
j = []
d = {}

for i in a :
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

for i in d.keys() :
    if i in b:
        j.append(i)

print(j)
