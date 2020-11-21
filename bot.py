import random
import discord
from discord.ext import commands


client = commands.Bot(command_prefix='.')
client.remove_command('help')


@client.event
async def on_ready():
    print("Logged in.")


@client.event  # Info
async def on_message(message):
    if message.content.startswith('.help'):
        embedVar = discord.Embed(color=0x541d81)
        embedVar.add_field(name="my cock", value="Just do .d6-d20", inline=False)
        await message.channel.send(embed=embedVar)
    await client.process_commands(message)


@client.command()
async def d4(ctx):
    num1 = random.randint(1, 4)
    await ctx.message.channel.send(num1)


@client.command()
async def d6(ctx):
    num1 = random.randint(1, 6)
    await ctx.message.channel.send(num1)


@client.command()
async def d8(ctx):
    num1 = random.randint(1, 8)
    await ctx.message.channel.send(num1)


@client.command()
async def d12(ctx):
    num1 = random.randint(1, 12)
    await ctx.message.channel.send(num1)


@client.command()
async def d20(ctx):
    num1 = random.randint(1, 20)
    await ctx.message.channel.send(num1)


@client.command()
async def d10(ctx):
    num1 = random.randint(1, 10)
    await ctx.message.channel.send(num1)



client.run('')
