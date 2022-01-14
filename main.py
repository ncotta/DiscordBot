"""
Discord Bot
Author(s): Niklaas Cotta
Created: 01/13/22
"""

import discord
import os
import time
from dice import *
from nameGenerator import *
from dotenv import load_dotenv

client = discord.Client()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    await client.change_presence(activity=discord.Activity(name='Jeepers Creepers', type=discord.ActivityType.listening))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$help"):
        await message.channel.send("My prefix is ``$``\n")
        time.sleep(0.5)
        await message.channel.send("Here is a list of the following commands:\n"
                                   "``about``\t\t\t get information about me!\n"
                                   "``roll <dice> <nun>``\t\t\t roll some dice!\n"
                                   "``name <race>``\t\t\t generate a player name! ")
    elif message.content.startswith("$about"):
        await message.channel.send("I am a D&D bot created by schnibs ;)")

    elif message.content.startswith("$roll"):
        msgList = message.content.split()
        await message.channel.send("Rolling...")
        time.sleep(0.5)
        await message.channel.send(multiroll(msgList[1], int(msgList[2])))

    elif message.content.startswith("$name"):
        await message.channel.send(f"Choosing a good name for you based on {random.randint(5000, 200000)} data points...")
        time.sleep(0.5)
        await message.channel.send(generator("human"))

    elif message.content.startswith("$"):
        await message.channel.send("Command not recognized...")


if __name__ == '__main__':
    load_dotenv()
    client.run(os.getenv('TOKEN'))
