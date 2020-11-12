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




