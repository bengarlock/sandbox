import math


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


# print(find_missing_number([1, 2, 3, 5, 6, 7, 8, 10, 11, 12]))

def find_single_dupe(array):
    return list(set([i for i in array if array.count(i) > 1]))


# print(find_single_dupe([1,2,3,4,4,5,6,7,8,8,9,10]))
# [8, 4]


# Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which number is not present in the second array.

def find_common_numbers(array1, array2):
    common = []
    for i in range(len(array1)):
        if array1[i] in array2:
            common.append(array1[i])
    return list(set(common))


# print(find_common_numbers(array1=[1,2,3,4,5], array2=[2,3,1,0,5]))
# 2,3,4


# How do you find the second highest number in an integer array?
def find_second_higest_number(array):
    array.sort()
    return array[-2]


# print(find_second_higest_number([14,200,33,4,12,6,70,44,23,10]))


# How to find all pairs in an array of integers whose sum is equal to the given number?
def find_pair_sets(array, number):
    pairs = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == number:
                pairs.append([array[i], array[j]])
    return pairs


# print(find_pair_sets(array=[2,4,6,8,10], number=10))


def format_date(date):
    date_split = date.split("/")
    return date_split[2] + date_split[1] + date_split[0]


# print(format_date("11/12/2019"))

def atbash(txt):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    encrypted_word = []

    for i in txt:
        if i.isupper():
            lower_case_letter = i.lower()
            index = alphabet.index(lower_case_letter) * -1 - 1
            encrypted_word.append(alphabet[index].upper())
        elif i.islower():
            index = alphabet.index(i) * -1 - 1
            encrypted_word.append(alphabet[index])
        else:
            encrypted_word.append(i)

    return ''.join(encrypted_word)


# print(atbash("Christmas is the 25th of December"))


def is_ascending(string):
    string_array = list(string)

    for i in range(len(string_array)):
        array = string_array[i: i + 3]
        for j in range(len(array)):
            for k in range(j + 1, len(array)):
                for l in range(k + 1, len(array)):
                    if array[j + 1] == array[k] and array[k + 1] == array[l]:
                        print(array[j + 1], array[k + 1], array[l])
    return False


# print(is_ascending("32332432536"))


def fizz_buzz(n):
    if n % 2 == 0 and n >= 2 and n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and n >= 6 and n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")
    else:
        print("Weird")


# print(fizz_buzz(15))

def is_square(n):
    if n < 0:
        return False
    elif math.sqrt(n).is_integer():
        return True


# is_square(26)

def song_decoder(song):
    split_slot = song.split("WUB")
    if split_slot[0] == "":
        split_slot.pop(0)
    if split_slot[-1] == "":
        split_slot.pop(-1)
    final_string = ''
    for word in split_slot:
        if word != "":
            final_string += word + " "
    return final_string[0:len(final_string) - 1]
    # return " ".join(song.replace("WUB", " ").split())


# print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
# print(song_decoder("AWUBBWUBC"))


def find_short(s):
    return min(len(x) for x in s.split())


# print(find_short("bitcoin take over the world maybe who knows perhaps"))


def likes(names):
    if len(names) == 1:
        return names[0] + " likes this"
    elif len(names) == 2:
        return names[0] + ' and ' + names[1] + " like this"
    elif len(names) == 3:
        return names[0] + ', ' + names[1] + ', ' + ' and ' + names[2] + " like this"
    elif len(names) > 3:
        return names[0] + ', ' + names[1] + ' and ' + str(len(names) - 2) + " others like this"
    else:
        return "no one likes this"


# print(likes(['Alex', 'Jacob']))


def alphabet_position(text):
    results = []
    for letter in text:
        try:
            results.append([letter for letter in "abcdefghijklmnopqrstuvwxyz"].index(letter.lower()) + 1)
        except:
            pass
    return ' '.join([str(i) for i in results])


# print(alphabet_position("The sunset sets at twelve o' clock."))


import operator


def high(x):
    word_array = x.split(' ')
    obj = {}
    for word in word_array:
        value = 0
        for letter in word:
            value += ord(letter) - 96
            obj[word] = value
    return max(obj, key=obj.get)


# print(high('man i need a taxi up to ubud'))

x = 'man i need a taxi up to ubud'


# print(ord("b")-96)


def to_camel_case(text):
    if len(text) > 0:
        cleaned_text = ''
        for letter in text:
            if not letter.isalpha():
                letter = " "
                cleaned_text += letter
            else:
                cleaned_text += letter
        lower_text = cleaned_text.split(" ")
        for word in lower_text:
            word.capitalize()
        first_word = lower_text[0]
        remaining_words = lower_text[1:]
        remaining_words_capitalized = ''
        for word in remaining_words:
            remaining_words_capitalized += word.capitalize()
        return "{}{}".format(first_word, remaining_words_capitalized)
    else:
        return text


# print(to_camel_case('the-Stealth-Warrior'))
# print(to_camel_case("A-B-C"))


import string


def is_pangram(s):
    alphabet = [i for i in "abcdefghijklmnopqrstuvwxyz"]
    d = dict()
    for letter in alphabet:
        d[letter] = False
        if letter in s.lower():
            d[letter] = True
    final_results = list(d.values())
    if False in final_results:
        return False
    else:
        return True


# pangram = "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"
# print(is_pangram(pangram))


def unique_in_order(iterable):
    results = []
    prev = None

    for char in iterable:
        if char != prev:
            results.append(char)
            prev = char

    return results


# print(unique_in_order('AAAABBBCCDAABBB'))

from collections import Counter

def duplicate_encode(word):
    word = word.lower()
    counter = Counter(word)
    return ''.join(('(' if counter[c] == 1 else ')') for c in word)

#print(duplicate_encode("recede"))
#print(duplicate_encode("Success"))

def duplicate_count(text):
    d = dict(Counter(text.lower()))
    count = 0
    for key, value in d.items():
        if value > 1:
            count += 1
    return count

#print(duplicate_count("indivisibility"))
#print(duplicate_count("abcdea"))


def iq_test(numbers):
    array = [int(i) for i in numbers.split(" ") if i.isnumeric()]
    gid = [i % 2 for i in array]

    if gid.count(0) > 1:
        return gid.index(1) + 1
    else:
        return gid.index(0) + 1

#print(iq_test("2 4 7 8 10"))

def tower_builder(n_floors):
    result = []
    count = 0
    while count < n_floors:
        star = "*" * count
        space = ''
        space_index = n_floors
        while space_index > 0:
            space += " " * (n_floors - (space_index - 1))
            space_index -= 1

        print(space + star + space)
        count += 1

#print(tower_builder(5))


def reverse(x):
    y = x[::-1]
    int(y)
    return y


#print(reverse(-123))


def solution(n):
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    roman_string = ''
    for key in sorted(roman_numerals.keys(), reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string

#print(solution(89))


import re
def pig_it(text):
    array = text.split(" ")
    results = []
    for word in array:
        if word.isalpha():
            results.append("{}{}ay".format(word[1:], word[0]))
        else:
            results.append(word)
    return " ".join(results)

pig_it('Pig latin is cool!')


def to_weird_case(string):
    array = string.split(" ")
    results = []
    for word in array:
        for index, value in enumerate(word):
            if index % 2 == 0:
                results.append(value.upper())
            else:
                results.append(value)
        results.append(" ")
    final = "".join(results)
    return final[0: len(final)-1]

#print(to_weird_case('This is a test'))
