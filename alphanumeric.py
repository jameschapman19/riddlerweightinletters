import numpy as np
import matplotlib.pyplot as plt

# https://www.quora.com/How-do-I-convert-numbers-to-words-in-Python
def num2words(num):
    under_20 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
                'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    above_100 = {100: 'Hundred', 1000: 'Thousand', 1000000: 'Million', 1000000000: 'Billion'}

    if num < 20:
        return under_20[num]

    if num < 100:
        return tens[int(num / 10) - 2] + ('' if num % 10 == 0 else ' ' + under_20[num % 10])

    # find the appropriate pivot - 'Million' in 3,603,550, or 'Thousand' in 603,550
    pivot = max([key for key in above_100.keys() if key <= num])

    return num2words((int)(num / pivot)) + ' ' + above_100[pivot] + (
        '' if num % pivot == 0 else ' ' + num2words(num % pivot))


def wordstoscore(word):
    return sum([ord(x) % 32 for x in word])


def num2score(num):
    return wordstoscore(num2words(num))


largest = 500

numbers = list(range(largest))
scores = [num2score(n) for n in numbers]

# for i in range(0, 999999):
#    if i < wordstoscore(num2words(i)):
#        print(i)
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(numbers, scores,marker='o',linestyle='none',label='alphanumeric score')
ax.plot(numbers, numbers,'-',label='number')
ax.set_title("Numbers vs. their alphanumeric scores")
ax.legend()
plt.show()

import num2words

def num2score(num):
    return wordstoscore(num2words(num))


