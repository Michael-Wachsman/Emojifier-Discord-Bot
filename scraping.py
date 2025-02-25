import praw
import re
import emoji 
import os
from os import system
from collections import defaultdict
import json
from multiprocessing import Manager, Pool

config = []

with open('config.json', 'r') as file:
	keys = json.load(file)	
	#insert your praw credentials here
	config.append(keys["PRAW_CLI_ID"])
	config.append(keys["PRAW_CLI_SECRET"])
	config.append(keys["PRAW_USER_AGENT"])


reddit = praw.Reddit(client_id = config[0], client_secret = config[1],  user_agent = config[2])



def is_emoji(s):
    return emoji.is_emoji(s)

def this_folder(): # returns the folder this file is located in 
	return os.getcwd()


words = re.compile(r"\w+\W{1,3}")
realWords = re.compile(r"\w+\W{0}")

def analyze_comment(post_set, emoji_base, ctr):
	for submission in post_set:
		for top_level_comment in submission.comments:
			comments = words.findall(top_level_comment.body)
			for emoji_content in comments:
				for i in range(2,0,-1):
					if is_emoji(emoji_content[-i]):
						actual_word = realWords.findall(emoji_content)[0].lower()
						if actual_word not in emoji_base:
							emoji_base[actual_word] = [emoji_content[-i]]
						else:
							emoji_base[actual_word].append(emoji_content[-i])
		ctr[0] += 1
		print(ctr[0])

	return(emoji_base)

fh = ("db.json", 'w')



def main():
	threads = 4
	# total post count to scrape
	post_ct = 800

	# Bypass Reddit Api query rate limit with multithreading >:)
	with Manager() as manager:
		emoji_bases = [{} for i in range(threads)]
		ctr = manager.list([0])
		with Pool(threads) as pool:
			
			post_sets = [[] for i in range(threads)]
			ct = 0 
			for post in reddit.subreddit("emojipasta").top(limit=post_ct):

				post_sets[ct//(post_ct//threads)].append(post)
				ct += 1
			
			emoji_bases = pool.starmap(analyze_comment, [(post_sets[i], emoji_bases[i],ctr) for i in range(threads)])

		emoji_base = defaultdict(list)

		for base in emoji_bases:
			for key, value in base.items():
				emoji_base[key] += value


		print(emoji_base)
		json.dump(emoji_base, fh)

	fh.close()



if __name__=="__main__":
    main()