def get_num_words(doc):
    words = doc.split()
    word_count = len(words)
    return word_count

def get_letter_count(doc):
    doc = doc.lower()
    letter_count = {}

    for char in doc:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

    return letter_count

def sort_letters(letters):
    letter_list = [(key, value) for key, value in letters.items()]
    letter_list.sort(reverse=True, key=lambda L: L[1])
    for item in letter_list:
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")
