#     ____       __       ____ 
#    / __ \___  / /______/ __ \
#   / /_/ / _ \/ __/ ___/ / / /
#  / _, _/  __/ /_/ /  / /_/ / 
# /_/ |_|\___/\__/_/   \____/  

# Libraries
import discord
from discord.ext import commands
#import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True
client = discord.Client()
client = commands.Bot(command_prefix='.', intents=intents)

# WHen the program starts
@client.event
async def on_ready():
    print("     ____       __       ____  ")
    print("    / __ \___  / /______/ __ \ ")
    print("   / /_/ / _ \/ __/ ___/ / / / ")
    print("  / _, _/  __/ /_/ /  / /_/ /  ")
    print(" /_/ |_|\___/\__/_/   \____/   ")

    print('Bot is Online!'.format(client))

    # Discord presence
    await client.change_presence(status=discord.Status.online, activity=discord.Game('DM for help!'))

@client.event
async def on_message(message):
    empty_array = []
    modmail_channel = discord.utils.get(client.get_all_channels(), name="mod-mail")

    if message.author == client.user:
        return
    if str(message.channel.type) == "private":
        if message.attachments != empty_array:
            files = message.attachments
            await modmail_channel.send("[" + message.author.display_name + "]")

            for file in files:
                await modmail_channel.send(file.url)
        else:
            await modmail_channel.send("[" + message.author.display_name + "] " + message.content)

    elif str(message.channel) == "mod-mail" and message.content.startswith("<"):
        member_object = message.mentions[0]
        if message.attachments != empty_array:
            files = message.attachments
            await member_object.send("[" + message.author.display_name + "]")

            for file in files:
                await member_object.send(file.url)
        else:
            index = message.content.index(" ")
            string = message.content
            mod_message = string[index:]
            await member_object.send("[" + message.author.display_name + "]" + mod_message)

keep_alive()
# add your bot token in the client.run area
client.run('Toekn')