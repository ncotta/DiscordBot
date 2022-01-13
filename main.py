"""
Discord Bot
Author(s): Niklaas Cotta
Created: 01/13/22
"""

import discord
import os
from dotenv import load_dotenv

client = discord.Client()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")


if __name__ == '__main__':
    load_dotenv()
    client.run(os.getenv('TOKEN'))
