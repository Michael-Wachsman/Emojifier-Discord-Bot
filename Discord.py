import discord
from discord.ext import commands
import re
import json
import random

stop_words = set(["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"])

with open('db.json', 'r') as file:
	data = json.load(file)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.command()
async def pasta(ctx, *, args):
	tokens = re.findall(r'\w+|\W+', args)  # Splits into words and non-words in sequence
	finalPasta = ""
	for token in tokens: 
		parsed_token = token.lower()
		finalPasta += token
		if parsed_token in data:
			if (parsed_token not in stop_words) or (random.randint(1,20) == 9):
				ind = random.randint(0,len(data[token.lower()])-1)
				finalPasta += " " + data[token.lower()][ind]
				if random.randint(1,10) == 2:
					ind = random.randint(0,len(data[token.lower()])-1)
					finalPasta += " " + data[token.lower()][ind]
				
		#finalPasta += nonWordHolder[i]
	if finalPasta != "":
		await ctx.channel.send(finalPasta)




with open('config.json', 'r') as file:
	config = json.load(file)	#insert your discord bot key here
	bot.run(config["DISCORD_API_KEY"])



