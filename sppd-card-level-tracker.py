# sppd-card-level-tracker.py
# this is a discord bot written to keep track of team members' card levels in SPPD
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    the_dude_abides = [
        'Nihilists! Fuck me. I mean, say what you want about the tenets of National Socialism, Dude, at least it\'s an ethos.',
        'Obviously you\'re not a golfer.',
        'Yeah, well, you know, that\'s just like, uh, your opinion, man.',
        'Hey, careful, man, there\'s a beverage here!',
        'Mr. Treehorn treats objects like women, man.',
        'I\'ll suck your cock for a thousand dollars.',
        'Will you come off it, Walter? You\'re not even fucking Jewish, man.',
        'Has the whole world gone crazy? Am I the only one around here who gives a shit about the rules? Mark it zero!',
        'Ah, fuck it, Dude. Let\'s go bowling.',
        'I told that kraut a fucking thousand times that I don\'t roll on Shabbos!',
    ]

    if message.content == 'the dude abides' or message.content == 'The dude abides':
        response = random.choice(the_dude_abides)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise
        
client.run(TOKEN)