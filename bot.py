import discord
from discord.ext import commands

# Setup the Discord bot
intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def help_gacha(ctx):
    await ctx.send('Here are the commands for the gacha bot!')

# Load cogs
# You can load cogs here (uncomment the line below)
# bot.load_extension('cog_name')

# Run the bot
TOKEN = 'YOUR_BOT_TOKEN'
bot.run(TOKEN)