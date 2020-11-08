"""Write a program that estimates the number of unique words in
   the text /users/abrick/resources/urantia.txt"""
 
# Shoutout to Ed who pointed out I should use sets for faster processing!! 

# !! You need to run this program by typing python3 [program name]
# NOT 'python [program name]' --or it won't work!!

import sys
import string

urantia = "urantia.txt"

try: 
	with open(urantia) as f: 
		lines = f.readlines()
except FileNotFoundError:
	print("Errror: File {} not found.".format(urantia))
	exit()
 
urantia_list = [] 
unique = set() # counts unique words.  We want to use 'set' because it makes operations faster.

print("Processing... sit tight a couple seconds!")
# incredibly, turning the whole book into a list of lists takes almost no time at all!
for line in lines:
	line = line.rstrip()
	# removes punctuation. only works if you call program with "python3"!!!
	line = line.translate(line.maketrans('', '', string.punctuation))
	# removes digits, which appear a lot as section titles.
	line = line.translate(line.maketrans(string.ascii_letters, string.ascii_letters, string.digits))
	# turns every line into a list of words and saves those lists in the urantia list
	chop_it = line.split()
	urantia_list.append(chop_it)


# sets are faster than lists because they are hash tables
# meaning "in" takes the same amount of time no matter what. 
 
for splitline in urantia_list: 
	# if all words in the line are already in unique, skip that line.
	if all(elem in unique for elem in splitline): 
	  	continue
	# in lines we don't skip, add any word that isn't already in unique to unique.
	# we're making all words lowercase, so it doesn't count capital and noncapital as separate
	for word in splitline: 
		if word.lower() not in unique: 
			unique.add(word.lower())

uniq_count = (len(unique))
print("Ding! There are approximately {:,} unique words in the book 'Urantia.'".format(uniq_count))
