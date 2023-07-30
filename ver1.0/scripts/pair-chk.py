# Check word-tag pairs
# How to run : python pair-chk.py <word-file> <tag-file> 
# Example : python pair-chk.py test.my test.tg > err.test
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
		for w,t in zip(word_lst,tag_lst):
			print("{}\{}".format(w,t),end=" ")
		print()
		print("Line {} => Number of word tokens : {} and Number of tags : {}".format(count,len(word_lst),len(tag_lst)))
		print("===================================")
	else:
		continue

wordFile.close()
tagFile.close()	
