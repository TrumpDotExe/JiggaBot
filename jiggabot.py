import discord
import asyncio
import random

client = discord.Client()

responses = ["WHAT DID YOU JUST SAY?!",
             "Waddya want?",
             "I'm busy. What do you need?",
             "SHUT UP",
             "...",
             "Come on, jigga! I'm Try'na sleep!",
             "Get lost, loofa!",
             "Ayyyy! Got a dollar?",
             "Wanna piece of pizza? I'm sure I got an extra piece SOMEWHERE!",
             "You ain't down with us no mo'!",
             "You ain't fat... You ain't FAT!",
             "Go away!"]


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print("---------")


@client.event
async def on_message(message):
    if message.content.startswith("*help"):
        print("message received!")
        await client.send_message(message.channel, """Commands:
*help: Request this message!
*jigga: Annoy me!

         Created by Trump.exe""")
    elif message.content.startswith("*jigga"):
        await client.send_message(message.channel, random.choice(responses))


client.run('MzYyMDQ3ODg1MzY3NTc0NTI5.DKtUaw.8qlZnkKeS0KjtxHyqx8b-c5BhO8')
