# does input contain a 3.4.5 triangle?
def is_triangle(input):
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            for k in range(j + 1, len(input)):
                if input[i] ** 2 + input[j] ** 2 == input[k] ** 2:
                    return True
    return False


# print(is_triangle([1, 3, 4, 5, 6, 7, 8]))


def find_missing_number(array):
    missing_numbers = []

    for i in range(len(array)):
        j = i + 1
        try:
            if array[j] != array[i] + 1:
                missing_numbers.append(array[i] + 1)
        except:
            pass

    return missing_numbers


#print(find_missing_number([1, 2, 3, 5, 6, 7, 8, 10, 11, 12]))

def find_single_dupe(array):
    return list(set([i for i in array if array.count(i) > 1]))

#print(find_single_dupe([1,2,3,4,4,5,6,7,8,8,9,10]))
# [8, 4]


#Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which number is not present in the second array.

def find_common_numbers(array1, array2):
    common = []
    for i in range(len(array1)):
        if array1[i] in array2:
            common.append(array1[i])
    return list(set(common))

#print(find_common_numbers(array1=[1,2,3,4,5], array2=[2,3,1,0,5]))
#2,3,4


#How do you find the second highest number in an integer array?
def find_second_higest_number(array):
    array.sort()
    return array[-2]

#print(find_second_higest_number([14,200,33,4,12,6,70,44,23,10]))


#How to find all pairs in an array of integers whose sum is equal to the given number?
def find_pair_sets(array, number):
    pairs = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == number:
                pairs.append([array[i], array[j]])
    return pairs

print(find_pair_sets(array=[2,4,6,8,10], number=10))
