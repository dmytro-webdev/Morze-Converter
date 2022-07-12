english_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                ',', '.', '?']

morze = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
         ".---", "-.-", ".-..", "--", "-.", "---", ".---.", "--.-", ".-.",
         "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----",
         "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----",
         "--..--", ".-.-.-", "..--.."]

user_string = input("Please, type your message: ").lower()
morze_symbols_array = []
for string_char in user_string:
    for char in english_chars:
        if string_char == char:
            morze_symbols_array.append(morze[english_chars.index(char)])
morze_string = ' '.join(morze_symbols_array)
print(f"Your typed message: {user_string}")
print(f"Converted to Morze: {morze_string}")

