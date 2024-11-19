def count_vowels(string):
    vowels = 'ёёуеыаоэяиюЁУЕЫАОЭЯИЮ'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


input_string = 'Какая-то строка с гласными'
print(f"Количество гласных в строке = {count_vowels(input_string)}")

