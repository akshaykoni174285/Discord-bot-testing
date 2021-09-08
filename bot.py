import discord
from discord.ext import commands

# intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client  = commands.Bot(command_prefix='/') 
# intents = intents inside the above parameters

@client.event
async def on_ready():
    print('bot is ready. ')

    
# @client.event
# async def on_member_join(member):
#     print(f'{member} has joined the server.')
    
# @client.event
# async def on_member_remove(member,ctx):
#     print(f'{member} has been removed from the server.')
   
@client.command()
async def ping(ctx):
    await ctx.send(f'pong {round(client.latency * 1000)} ms')
    

    
client.run('ODg1MDMwMzkxODYwMzEwMDI2.YThGyA.Sx2OsQX1ijTJoD85yeykH13XBYs')

