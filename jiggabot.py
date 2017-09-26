#! /usr/bin/env python3

# JIGGA BOT

import discord
import asyncio
import random

client = discord.Client()

responses = ["WHAT DID YOU JUST SAY?!",
            "Waddya want?",
            "I'm busy. What do you need?",
            "SHUT UP!",
            "...",
            "Come on, jigga. I'm try'na sleep!",
            "Ayy! Got a dollar?",
            "Wanna piece of pizza? I'm sure I got an extra piece around here SOMEWHERE!",
            "You ain't down wit' us no mo'!",
            "You ain't fat... YOU AIN'T FAT!",
            "Go away!"]


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print("------------")
    


@client.event
async def on_message(message):
    if message.content.startswith("*help"):
        print("help message sent!")
        await client.send_message(message.channel,
                            """Commands:
*help: Request this message!
*jigga: Annoy me!

        More commands coming soon! (hopefully)
                Created by Trump.exe#3431""")

    elif message.content.startswith("*jigga"):
        print("Jigga message sent!")
        await client.send_message(message.channel, random.choice(responses))


client.run("MzYyMDQ3ODg1MzY3NTc0NTI5.DKwRoQ.QvDH37828R4lp9x5w-uk2bCyhR0")
