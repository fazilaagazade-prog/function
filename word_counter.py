def count_words(text):
    result = {}
    words = text.lower().split()
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


text = input("Metn daxil edin: ")
counts = count_words(text)
print(counts)

if counts:
    most_word = ""
    most_count = 0
    for word, count in counts.items():
        if count > most_count:
            most_word = word
            most_count = count
    print("Ən çox təkrarlanan söz:", most_word, "-", most_count, "dəfə")
else:
    print("Metn boşdur")