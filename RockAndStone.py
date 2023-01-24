#! bin/python

import discord
import random
import logging

handler = logging.FileHandler(filename='RockAndStone.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True

activity = discord.Activity(type=discord.ActivityType.listening, name='Rock and Stone! ⛏️')

client = discord.Client(intents=intents, activity=activity)

salutes = ["Rock on!", "Rock and Stone... Yeeaaahhh!", "Rock and Stone forever!", "ROCK... AND... STONE!", "Rock and Stone!", "For Rock and Stone!", "We are unbreakable!", "Rock and roll!", "Rock and roll and stone!", "That's it lads! Rock and Stone!", "Like that! Rock and Stone!", "Yeaahhh! Rock and Stone!", "None can stand before us!", "Rock solid!", "Stone and Rock! ...Oh, wait...", "Come on guys! Rock and Stone!", "If you don't Rock and Stone, you ain't comin' home!", "We fight for Rock and Stone!", "We rock!", "Rock and Stone everyone!", "Stone.", "Yeah, yeah, Rock and Stone.", "Rock and Stone in the Heart!", "For Teamwork!", "Did I hear a Rock and Stone?", "Rock and Stone!", "Rock and Stone, Brother!", "Rock and Stone to the Bone!", "For Karl!", "Leave No Dwarf Behind!", "By the Beard!"]

#zamień x na id jeszyka
jeszyk = x

@client.event
async def on_ready():
    print(f'Zalogowano jako {client.user}')
    print('''⠀⠀⠀⢀⣀⣠⣤⡤⠤⠄⣠⣤⣠⡀⠀⠀⠀⠀
⠀⠀⠰⣾⣬⣶⣶⣾⣶⣴⣄⣈⠉⡓⠢⣦⠀⠀
⠀⠀⠀⠀⠛⠛⠃⢀⣼⣛⣼⡿⣿⣿⡀⠻⣧⠀
⠀⠀⠀⠀⠀⢀⣖⠿⣬⣿⠿⠁⠈⢻⣷⣄⠹⣷
⠀⠀⠀⠀⢤⣼⣹⣾⣿⠋⠀⠀⠀⠈⠛⠛⠿⠏
⠀⢀⣀⡿⢦⣶⡿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡜⠋⣷⣿⡟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣻⢳⣶⣾⠟⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠲⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id == jeszyk:
        await message.reply("💀", mention_author=True)

    if message.content.lower() == len(message.content.lower()) * "v" and len(message.content) > 0:
        channel = message.channel
        await message.delete()
        random_salute = random.choice(salutes)
        await message.channel.send(f'{random_salute} ⛏️')

    if message.content == f'<@{jeszyk}>':
        await message.delete()

#zamień x na token
client.run("x", log_handler=handler, log_level=logging.DEBUG)
