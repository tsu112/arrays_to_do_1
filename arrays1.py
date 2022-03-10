# Push Front
# Given an array and an additional value, insert this value at the beginning of the array. Do this without using any built-in array methods.

def pushInFront(arr, val):
    arr.append(0)
    for x in range(len(arr)-1, 0, -1):
        arr[x] = arr[x-1]
    arr[0] = val
    print(arr)


arr = [1, 2, 3, 4, 5, 6, 7, 8]

pushInFront(arr, 0)
# # *****************************************************

# Pop Front
# Given an array, remove and return the value at the beginning of the array. Do this without using any built-in array methods except pop().

my_arr = [1, 2, 3]
x = my_arr[-1]
my_arr.pop()
my_arr.insert(0, x)
print(my_arr)
# *****************************************************

# Insert At
# Given an array, index, and additional value, insert the value into array at given index. Do this without using built-in array methods. You can think of pushFront(arr,val) as equivalent


def pushIn(arr, index, val):
    arr.append(index)
    for x in range(len(arr)-1, 0, -1):
        arr[x] = arr[x-1]
    arr[index] = val
    print(arr)


arr = [1, 2, 3, 4, 5, 6, 7, 8]

pushIn(arr, 1, 0)
# *****************************************************
# Remove At (Bonus Challenge)
# Given an array and an index into array, remove and return the array value at that index. Do this without using built-in array methods except pop(). Think of popFront(arr) as equivalent to removeAt(arr,0).


def removeIn(arr, index):
    temp = arr[index]
    arr.pop(index)
    return temp


arr = [1, 2, 3, 4, 5, 6, 7, 8]

removeIn(arr, 2)
# *****************************************************

# Swap Pairs (Bonus Challenge)
# Swap positions of successive pairs of values of given array. If length is odd, do not change the final element. For [1,2,3,4], return [2,1,4,3]. For example, change input ["Brendan",true,42] to [true,"Brendan",42]. As with all array challenges, do this without using any built-in array methods.

arr = [1, 2, 3, 4, 5]

for x in range(0, len(arr), 2):
    arr[x], arr[x+1] = arr[x+1], arr[x]
    if x > len(arr) / 2 - 1:
        break
print(arr)
# *****************************************************

# Remove Duplicates (Bonus Challenge)
# Sara is looking to hire an awesome web developer and has received applications from various sources. Her assistant alphabetized them but noticed some duplicates. Given a sorted array, remove duplicate values. Because array elements are already in order, all duplicate values will be grouped together. As with all these array challenges, do this without using any built-in array methods.

arr = ["Ada", "Kash", "Sue", "Ada"]

arr.sort()


def rem_dup(list):
    non_dup = []
    for x in list:
        if x not in non_dup:
            non_dup.append(x)
    return non_dup


print(rem_dup(arr))


# Second: Solve this without using any nested loops.
