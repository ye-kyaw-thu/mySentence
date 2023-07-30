# Check word-tag pairs
# How to run : python eq_count.py <word-file> <tag-file> 
# Example : python eq_count.py test.my test.tg > err.test
# Author : Thura Aung

import sys

wordFile = open(sys.argv[1], 'r')
tagFile = open(sys.argv[2], 'r')
	
count = 0
	
for word, tag in zip(wordFile, tagFile):
	count = count + 1
	word_lst = word.split()
	tag_lst = tag.split()
	if len(word_lst) != len(tag_lst):
		print("Line {} : {} <||> {}".format(count,word_lst,tag_lst))
		print("Number of word tokens : {} and Number of tags : {}".format(len(word_lst),len(tag_lst)))
		print("===================================")
	else:
		continue

wordFile.close()
tagFile.close()	
