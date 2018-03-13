#    Assess the passage for each of the following:
#    Approximate word count
#    Approximate sentence count
#    Approximate letter count (per word)
#    Average sentence length (in words)

import pandas as pd

fname = "textFile"

num_lines = 0
num_words = 0
num_chars = 0
wordcounts = []

with open(fname, 'r') as f:
    text = f.read()
    lines = text.split('.')
    for line in lines:
        words = line.split()
	num_lines += 1
        num_words += len(words)
        num_chars += len(line)
	wordcounts.append(len(words))

average_wordcount = sum(wordcounts)/len(wordcounts)

# word count
print(num_words)

# sentence count
print(num_lines)

# char count
print(num_chars)

# Approximate letter count (per word)
avgLetterCount = (num_chars)/num_words
print(avgLetterCount) 

# Average sentence length (in words)
print(average_wordcount)







