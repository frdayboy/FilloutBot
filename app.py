# Daily Fillout Bot written by Tarek Joumaa (@frdayboy)

import discord, json, random
from discord.ext import commands
from datetime import date

cached_date = str(date.today().isoformat()) + ":\n"
__VERS__ = "v0.0.2 (ALPHA)"
confirmation = ["Gotchu", "Np", "Got it", "Heard", "Mhm", "Ok", "Yup", "That's what's up", "Nice"]
bot = commands.Bot(command_prefix='!')

def initialize_secret():
	with open("creds.json", "r") as f:
		content = f.read()
	f.close()
	return json.loads(content)['TOKEN']

def rw_log(who):
	try:
		f = open("logs/log-{}.txt".format(who), "w+")
	except IOError:
		return 1
	return f 

@bot.event
async def on_ready():
	print("[FilloutBot] Booted {}".format(__VERS__))

@bot.command(name='fill', help="(kills) (deaths) (w/l) (optional: operator) (optional: assists) (optional: other notes)")
async def fillout(ctx, *args):
	log = rw_log(str(ctx.author))
	if log == 1:
		await ctx.send("Error occured while opening file")
		return
	#Arg parse
	if len(args) < 3:
		await ctx.send("Not enough args" + help)
		return
	try:
		assert type(args[0]) == int and type(args[1] == int) and type(args[2]) == str
	except AssertionError:
		ctx.send("Wrong format of args" + help)
		return
	if cached_date not in log.read():
		log.write(cached_date)
	for i in range(0, len(args)-1):
		#TODO: Make a class or enum obj and add type of arg to elim nested conditionals
		#TODO: Make \t * 5 standard in a wrapper
		if i == 0:
			log.write(("\t" * 5) + "KILLS : {}\n".format(args[i]))
		elif i == 1:
			log.write(("\t" * 5) + "DEATHS : {}\n".format(args[i]))
		elif i == 2:
			log.write(("\t" * 5) + "W/L : {}\n".format(args[i]))
		elif i == 3:
			log.write(("\t" * 5) + "OPERATOR : {}\n".format(args[i]))
		elif i == 4:
			log.write(("\t" * 5) + "OTHER NOTES : {}\n\n".format(args[i]))
		await ctx.send(random.choice(confirmation))

@bot.command(name="retrieve", help="Prints your log")
async def retrieve(ctx):
	try:
		with open("logs/log-{}.txt".format(str(ctx.author)), "r") as f:
			content = f.read()
		f.close()
	except IOError or FileNotFoundError:
		await ctx.send("No log is available for you")
		return
	await ctx.send(content)

if __name__ == '__main__':
	TOKEN = initialize_secret()
	#Boot bot
	bot.run(TOKEN)

