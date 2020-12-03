input = "abacabade"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!
    for i in string:
        if i.isalpha():
            location = ord(i) - ord('a')
            alphabet_occurrence_array[location] += 1
    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord('a')))
    for char in string:
        if char in not_repeating_character_array:
            return char

result = find_not_repeating_character(input)
print(result)