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

insultsList = ["is the bloody son of a motherless kobold!", "likes to eat cheese without crackers",
               "sleeps on their stomach", "is a big baby", "enjoys eating soggy doritos", "collects orc toenails",
               "doesn't know how to tap dance", "couldn't beat a level 1 slime"]

commandsList = [f"Here is a list of the following commands:\n",
                f"``about``               get information about me!\n",
                f"``roll <dice> <nun>``   roll some dice!\n",
                f"``name <race>``         generate a player name!\n",
                f"``insult <user>``       insults yourself or another!\n",
                f"``apologize <user>``    says sorry to someone else\n",
                f"``back me up``          provides moral support\n",
                f"``goodbye``             say bye to Beholder :("]


@client.event
async def on_ready():
    """
    Description: This tells the bot what to do when it turns on
    """
    print(f"We have logged in as {client.user}")
    await client.change_presence(
        activity=discord.Activity(name='Jeepers Creepers', type=discord.ActivityType.listening))


@client.event
async def on_message(message):
    """
    Description: On a message with the prefix of $ (a command), Beholder will parse
    the message and do something accordingly
    :param message: String. Any message a user sends in the discord server Beholder is a part of
    """
    if message.author == client.user:
        return

    if message.content.startswith("$help"):
        await message.channel.send("My prefix is ``$``\n")
        time.sleep(1)

        for command in commandsList:
            await message.channel.send(command)
            time.sleep(0.5)

    elif message.content.startswith("$about"):
        await message.channel.send("I am a D&D bot created by schnibs ;)")

    elif message.content.startswith("$roll"):
        msgList = message.content.split()
        await message.channel.send("Rolling...")
        time.sleep(0.5)
        await message.channel.send(multiroll(msgList[1], int(msgList[2])))

    elif message.content.startswith("$name"):
        msgstr = message.content.split()
        await message.channel.send(
            f"Choosing a good name for you based on {random.randint(15, 1000)} data points...")
        time.sleep(0.5)
        await message.channel.send(f"Your new name is...\n{generator(msgstr[1])}")

    elif message.content.startswith("$insult"):
        msgstr = message.content.split()
        try:
            await message.channel.send(f"{msgstr[1]} {random.choice(insultsList)}")
        except IndexError:
            await message.channel.send(f"<@{message.author.id}> {random.choice(insultsList)}")

    elif message.content.startswith("$apologize"):
        msgstr = message.content.split()

        if len(msgstr) == 3:
            i = 2
        elif len(msgstr) == 2:
            i = 1
        else:
            return

        await message.channel.send(f"Sorry {msgstr[i]} :frowning:")

    elif message.content.startswith("$back"):
        await message.add_reaction("👍")
        await message.add_reaction("💯")
        await message.add_reaction("😤")

    elif message.content.startswith("$goodbye"):
        await message.add_reaction("😴")
        await message.add_reaction("👋")
        await client.close()

    elif message.content.startswith("$"):
        await message.channel.send("Command not recognized..."
                                   "Type ``$help`` for commands!")


if __name__ == '__main__':
    load_dotenv()
    client.run(os.getenv('TOKEN'))
