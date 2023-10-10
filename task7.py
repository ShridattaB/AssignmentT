# → WAP to print the number of counts form the given string
def count_characters(string):
    char_counts = {}

    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


input_string = "hello world"
counts = count_characters(input_string)

for char, count in counts.items():
    print(f"'{char}' occurs {count} time(s)")



# s= “ This is a bit similar to the earlier project. The only difference is that in this case,
# you will also be using React hooks “
def count_characters(string):
    char_counts = {}

    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


input_string = " This is a bit similar to the earlier project. The only difference is that in this case, you will also be using React hooks "


input_string = input_string.replace(" ", "").lower()

counts = count_characters(input_string)

for char, count in counts.items():
    print(f"'{char}' occurs {count} time(s)")


# → WAP to reverse the first and last numbers of list without changing the middle
# numbers of the list.
# [ 12,3,6,3,63,8,46,33,90]
def reverse_first_last(lst):
    if not lst:
        return lst

    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

numbers = [12, 3, 6, 3, 63, 8, 46, 33, 90]
reversed_numbers = reverse_first_last(numbers)

print(reversed_numbers)

# → WAP to reverse the words in the string only not reverse the String only the words.
def reverse_words_in_string(input_string):
    words = input_string.split()
    reversed_words = [word[::-1] for word in words]
    reversed_string = ' '.join(reversed_words)
    return reversed_string


input_string = "This is a sample string"
reversed_words_string = reverse_words_in_string(input_string)

print("Original string:", input_string)
print("Reversed words string:", reversed_words_string)
