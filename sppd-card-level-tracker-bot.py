# sppd-card-level-tracker.py
# this is a discord bot written to keep track of team members' card levels in SPPD
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

## intents = discord.Intents.all()
## client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!')
@bot.command(name='thedudeabides', help='Responds with a random quote from The Big Lebowski.')
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


bot.run(TOKEN)