word = 'cheese'

long_vowels = ['oo', 'ee']

result = ''
for i in range(len(word)):
    twoletters = word[i:i+2]
    if twoletters in long_vowels:
        result += word[i] * 4
    else:
        result += word[i]

print result
