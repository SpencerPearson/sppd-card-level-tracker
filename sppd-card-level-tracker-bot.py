# sppd-card-level-tracker.py
# this is a discord bot written to keep track of team members' card levels in SPPD
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

## intents = discord.Intents.all()
## client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!')

# @bot.command(name='create-channel')
# @commands.has_role('admin')
# async def create_channel(ctx, channel_name='real-python'):
#     guild = ctx.guild
#     existing_channel = discord.utils.get(guild.channels, name=channel_name)
#     if not existing_channel:
#         print(f'Creating a new channel: {channel_name}')
#         await guild.create_text_channel(channel_name)

@bot.command(name='dude', help='Responds with a random quote from The Big Lebowski.')
async def the_dude_abides(ctx):
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

    response = random.choice(the_dude_abides)
    await ctx.send(response)

@bot.command(name='roll', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

bot.run(TOKEN)