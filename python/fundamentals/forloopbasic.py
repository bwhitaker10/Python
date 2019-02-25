# 1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
def biggie(list):
    newlist = []
    for i in list:
        if i < 1:
            newlist.append("Big")
        else:
            newlist.append(i)
    return newlist
print(biggie([-1,3,5,-5]))

# 2. Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values.
def countPositives(list):
    newlist = []
    for i in list:
        if i < 1:
            newlist.append(i)
        else:
            newlist.append(i) in range(0,i)
    return newlist
print(countPositives([-1,1,1,1]))

# 3. Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
def sumTotal(list):
    return sum(list)
print(sumTotal([1,2,3,4]))

# 4. Average - Create a function that takes a list and returns the average of all the values.
def avgValues(list):
    return sum(list) / len(list)
print(avgValues([1,2,3,4]))

# 5. Create a function that takes a list and returns the length of the list.
def length(list):
    count = 0
    for i in list:
        count += 1
    return count
print(length([37,2,1,-9]))

# 6. Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
def minimum(list):
    return min(list)
print(minimum([37,2,1,-9]))

# 7. Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
def maximum(list):
    return max(list)
print(maximum([37,2,1,-9]))

# 8. Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def ultimate(list):
    print("sumTotal:", sum(list))
    print("average:", sum(list) / len(list))
    print("minimum:", min(list))
    print("maximum:", max(list))
    print("length:", len(list))
print(ultimate([37,2,1,-9]))

# 9. Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
def reverse(list):
    return list[::-1]
print(reverse([37,2,1,-9]))