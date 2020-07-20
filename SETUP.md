# How to setup FilloutBot!

Some notes:
  I'm not currently able to have a permanent server up with all your logs, so you'll have to host your own server.
  You can probably find some free hosting service for Discord (or any other online service) that you can keep this script running.
  You can keep this script running on your desktop at all times, or even when your team is playing.
  If you have an old computer that is idle at home, you can even keep that running with this script (which obviously needs internet)

Requirements to run script:
  1. A folder in the same directory as the script named 'logs'
  2. Python version >= 3.0 (https://www.python.org/downloads/)
  3. Discord Python module (can be installed by running command 'pip3 install discord.py')

Follow this guide to setup a Discord bot on your server and get credentials:
  https://realpython.com/how-to-make-a-discord-bot-python/

Once you have your token, open 'creds.json' and copy and paste the token into the 'TOKEN' field in the file, so that it looks like this:
 {
   "TOKEN" : "abcdefghijklmnop
 }

 Now, you're ready to run the script!
 If you're having trouble with running it, Google's your best friend!
