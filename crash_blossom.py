
user_input = input("Enter a sentence: ")

# functionality to capitalise each word


def titlecase(text):
    change_case = []
    for word in text.split():
        cap_word = word.capitalize()
        change_case.append(cap_word)
    return " ".join(change_case)


crash_blossom = titlecase(user_input)
print(crash_blossom)
