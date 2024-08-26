from english_words import get_english_words_set
lower_word = get_english_words_set(['web2'], lower=True)
lower_word=list(lower_word)
result = []
for word in lower_word:
    if len(word)==5:
        result.append(word)
print(result[:10])