# Daily Fillout Bot written by Tarek Joumaa (@frdayboy)

import discord, json, random, sys
from discord.ext import commands
from datetime import date

cached_date = str(date.today().isoformat()) + ":\n"
__VERS__ = "v0.0.3 (ALPHA)"
confirmation = ["Gotchu", "Np", "Got it", "Heard", "Mhm", "Ok", "Yup", "That's what's up", "Nice"]
bot = commands.Bot(command_prefix='!')

def initialize_secret():
	with open("creds.json", "r") as f:
		content = f.read()
	f.close()
	KILLUSER = str(json.loads(content)['KILLUSER'])
	global KILLUSER
	return json.loads(content)['TOKEN']

def rw_log(who):
	try:
		f = open("logs/log-{}.txt".format(who), "r+")
	except IOError or FileNotFoundError:
		f = open("logs/log-{}.txt".format(who), "w+")
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
		await ctx.send("Not enough args")
		return
	try:
		int(args[0])
		int(args[1])
	except ValueError:
		await ctx.send("Wrong format in args")
		return
	if cached_date not in log.read():
		log.write(cached_date)
	log.write("\t" + "\n\nMATCH:\n")
	for i in range(0, len(args)):
		#TODO: Make a class or enum obj and add type of arg to elim nested conditionals
		#TODO: Make \t standard in a wrapper
		if i == 0:
			log.write("\t" + "KILLS : {}\n".format(args[i]))
		elif i == 1:
			log.write("\t" + "DEATHS : {}\n".format(args[i]))
		elif i == 2:
			log.write("\t" + "W/L : {}\n".format(args[i]))
		elif i == 3:
			log.write("\t"  + "OPERATOR : {}\n".format(args[i]))
		elif i == 4:
			log.write("\t"  + "OTHER NOTES : {}\n".format(args[i]))
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

@bot.command(name='kill', help='Shuts bot down')
async def kill(ctx):
	if str(ctx.author) == KILLUSER:
		sys.exit(0)
	else:
		await ctx.send("You are not authorized to use this command.")

if __name__ == '__main__':
	#Bad naming, ik
	TOKEN = initialize_secret()
	
	#Boot bot
	bot.run(TOKEN)

