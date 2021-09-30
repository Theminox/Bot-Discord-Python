import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re

bot = commands.Bot(command_prefix='!', description="This is a helper bot")

@bot.command()
async def ping (ctx):
    await ctx.send(' :ping_pong: Pong!')

@bot.command()
async def suma (ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def stats (ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem ipsum", timestamp=datetime.datetime.utcnow(), color=discord.Color .blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://i.gifer.com/XNY.gif")
    await ctx.send(embed=embed)


@bot.command()
async def youtube(ctx, *, search):
    query_strings = parse.urlencode({'search_query': search})
    html_content = request.urlopen('https://www.youtube.com/results?' + query_strings)
    search_results=re.findall('watch\?v=(.{11})',html_content.read().decode('utf-8'))
    print(search_results)
    await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])

         
#Evento
@bot.event
async def on_ready():
     await bot.change_presence(activity=discord.Streaming(name="Stream",url="https://www.twitch.tv/"))
     print('Bot is ready')



    
bot.run('')

