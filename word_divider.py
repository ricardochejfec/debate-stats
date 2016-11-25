import string
import sys
from nltk.corpus import stopwords
from collections import Counter
import random
#method that gets rid of all punctuation 
def punctuation(word):
	exclude = set(string.punctuation)
	word = ''.join(ch for ch in word if ch not in exclude)
	for l in word.split():
		if l == "'":
			word.replace("'", "")
	word = word.lower()
	return word

def print_results(candidate, candidate_list, candidate_dict):
    print "{} used {} different words out of {} words". format(candidate, len(candidate_dict), len(candidate_list))
    #print Trump ratio
    print float(len(candidate_list))/len(candidate_dict)

def print_comparison(candidate_one, candidate_two):
    set_one = candidate_one.most_common(50)
    set_two = candidate_two.most_common(50)
    for x, j in zip(set_one, set_two):
        size = len(x[0]) + len(str(x[1])) 
        word = x[0] + " - " + str(x[1]) 
        word += " " * (13 - size)
    	print " DT: {} |     HC: {} - {}".format(word, j[0], j[1])


#get the debate transcript
debate_transcript = raw_input("Enter the transcript's file name: ")
try:
    f = open(debate_transcript, "r")
    transcript = f.read()
    f.close()
except IOError:
    print "File doesnt exist." 
    sys.exit()


trump = ""
hillary = ""
key = ""

#separate the transcript into what each candidate said 
for word in transcript.split():
	if word == "HOLT:" or word == "AC:" or word == "Moderator:" or word == "MR:" or word == "Voter:" or word == "Wallace:":
		key = "0"
	elif word == "TRUMP:" or word == "DT:" or word == "Trump:":
		key = "1"
	elif word == "CLINTON:" or word == "HC:" or word == "Clinton:":
		key = "2"
	else:
		if key == "0":
			continue 
		elif key == "1": 
			tmp = punctuation(word)
			trump = trump + tmp + " "
		elif key == "2":
			tmp = punctuation(word)
			hillary = hillary + tmp + " "

#set of common words
s=set(stopwords.words('english'))
#set of irrelevant words
si = set(["thats", "us", "lot", "weve", "hes", "ive", "theyre", "im", "youre", "shes"])

#eliminate common words and irrelevant words from Hillary
hillary_list = filter(lambda w: not w in s,hillary.split())
hillary_list = filter(lambda w: not w in si,hillary_list)

#eliminate common words and irrelevant words from Trump
trump_list = filter(lambda w: not w in s,trump.split())
trump_list = filter(lambda w: not w in si,trump_list)

#create counter 'dicitionaries' 
hillary_dict = (Counter(hillary_list))
trump_dict = (Counter(trump_list))

#RESULTS
#print Trump results 

print
print_results("Trump", trump_list, trump_dict)
print
#print Hillary's results
print_results("Hillary", hillary_list, hillary_dict) 
print
#print comparison of results
print_comparison(trump_dict, hillary_dict)
"""
rand_a = random.randint(0,1)
if rand_a == 0:
	rand_b, rand_c = random.randint(0, len(hillary_list)), random.randint(0, len(hillary_list))
	print hillary_list[rand_b], hillary_list[rand_c]
else:
	rand_b, rand_c = random.randint(0, len(trump_list)), random.randint(0, len(hillary_list))
	print trump_list[rand_b], trump_list[rand_c]
"""