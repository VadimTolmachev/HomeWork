# Решение через цикл FOR
def single_root_words(root_word, *other_words):
    same_words = []
    for x in other_words:
        if x.lower() in root_word.lower():
            same_words.append(x)
        if root_word.lower() in x.lower():
            same_words.append(x)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
