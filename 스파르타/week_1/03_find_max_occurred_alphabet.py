input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!
    for i in string:
        if i.isalpha():
            location = ord(i) - ord('a')
            alphabet_occurrence_array[location] += 1
    max_num = max(alphabet_occurrence_array)
    max_index = alphabet_occurrence_array.index(max_num)
    return chr(max_index+97)


result = find_max_occurred_alphabet(input)
print(result)