from num2words import num2words
import matplotlib.pyplot as plt
import unicodedata


def wordstoscore(word):
    score=sum([ord(x) % 32 for x in word])
    return score


def num2score(num, language):
    u = num2words(num, lang=language).replace(' and', '').replace(' ', '').replace('-', '')
    return wordstoscore(
        unicodedata.normalize('NFKD', u).encode('ASCII', 'ignore').decode())


largest = 2000
available_languages = ['en','cz', 'de', 'dk', 'es', 'fi','fr', 'id', 'it', 'pl','pt', 'nl']

numbers = list(range(largest))

import pandas as pd

scores = pd.DataFrame(columns=available_languages)

language_max = {}
for language in available_languages:
    scores[language] = [num2score(n, language) for n in numbers]
    for n in numbers:
        if n < num2score(n, language):
            language_max[language] = n

# for i in range(0, 999999):
#    if i < wordstoscore(num2words(i)):
#        print(i)
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(scores, marker='o', linestyle='none')
ax.set_title("Numbers vs. their alphanumeric scores")
ax.legend(available_languages)
plt.show()

fig2, ax2 = plt.subplots()
ax2.bar(*zip(*language_max.items()))
ax2.set_title("Maximum by language")
plt.show()
