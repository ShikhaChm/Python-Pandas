# Assess the passage for each of the following:
#    Approximate word count
#    Approximate sentence count
#    Approximate letter count (per word)
#    Average sentence length (in words)

import pandas as pd

#fname = "textFile1.txt"
fname = "textFile2.txt"

num_lines = 0
num_words = 0
num_chars = 0
wordcounts = []

print "Paragraph Analysis", "\n"
print "===================","\n"

with open(fname, 'r') as f:
    text = f.read()
    lines = text.split('.')
    for line in lines:
        words = line.split()
	num_lines += 1
        num_words += len(words)
        num_chars += len(line)
	wordcounts.append(len(words))


# word count
print  "Approximate word count: ",num_words, "\n"
#    Approximate sentence count
#    Approximate letter count (per word)
#    Average sentence length (in words)

# sentence count
print  "Approximate sentence count: ",num_lines, "\n"

# char count
print  "Approximate letter count: ",num_chars, "\n"

# Approximate letter count (per word)
avgLetterCount = (num_chars)/num_words
print  "Average letter count: ",avgLetterCount, "\n"

# Average sentence length (in words)
avgSentenceLen = sum(wordcounts)/len(wordcounts)
print  "Average sentence length (in words): ",avgSentenceLen, "\n"









