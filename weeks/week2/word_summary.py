def word_histogram(sentence):
    tally = {}
    wordsList = sentence.split()
    for word in wordsList:
        if tally.get(word):
            tally[word] += 1
        else:
            tally[word] = 1
    print tally

word_histogram('To be or not to be')


# Given a histogram tally (one returned from either letter_histogram or word_summary), print the top 3 words or letters.

def top_three(tally):
    top_three_items = {}
    while len(top_three_items) < 3:
        highKey = ''
        highestValue = 0
        for key, value in tally.items():
            if value > highestValue:
                highKey = key
                highestValue = value
        top_three_items[highKey] = tally[highKey]
        del tally[highKey]  # need to delete otherwise it won't stop
    print top_three_items
        

top_three(word_histogram('To be or not to be'))

# or

def top_three(tally):
    