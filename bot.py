import discord
from discord.ext import commands
import random

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client  = commands.Bot(command_prefix='!', intents=intents) 
# intents = intents inside the above parameters
@client.event
async def on_ready():
    print('bot is ready. ')
    
    

    
@client.event
async def on_member_join(member):
    message = f'{member} joined the server'
    
    
@client.event
async def on_member_remove(member):
    message = f'{member} has been removed from the server.'
    
    
@client.command()
async def ping(ctx):
    await ctx.send(f'pong {round(client.latency * 1000)} ms')
    

@client.command(aliases = ['8ball','question'])
async def _8ball(ctx,*,questions):
    responses = ['It is certain', 
                 'Without a doubt',
                 'You may rely on it',
                 'Yes definitely',
                 'Ask again later',
                 'Cannot predict now',
                 'Concentrate and ask again',
                 'Don’t count on it',
                 'My sources say no',
                 'Very doubtful'
                 
    ]
    await ctx.send(f'question: {questions}\nAnswer: {random.choice(responses)}')
    
@client.command()
async def clear(ctx, ammount = 5):
     await ctx.channel.purge(limit = ammount)
     
     
#  how to kick the user 
@client.command()
async def kick(ctx, member: discord.Member, *, reason = None):
    await member.kick(reason = reason)
    
@client.command()
async def ban(ctx, member: discord.Member, *, reason = None):
    await member.ban(reason = reason)
    
@client.command()
async def unban(ctx,*, member):
    banned_users = await ctx.guild.bans()
    # member_name, member_discriminator = member.split('#')
    
    for ban_entry in banned_users:
        user = ban_entry.user
        
        
        await ctx.guild.unban(user)
        await ctx.send(f"unbanned the {user.mention}")
        return
    
    
     
     
    
client.run('ODg1MDMwMzkxODYwMzEwMDI2.YThGyA.TIOF8W3Wh72NFu1-sBBSTZoXFW0')

