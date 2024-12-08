import discord
from discord.ext import commands
from config import token

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'Giriş yaptı:  {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        await message.channel.send(message.content)

@client.command()
async def about(ctx):
    await ctx.send('Ben bir botum.')

@client.command()
async def info(ctx):
    await ctx.send('https://images.theconversation.com/files/378097/original/file-20210111-23-bqsfwl.jpg?ixlib=rb-4.1.0&rect=36%2C84%2C7980%2C5072&q=20&auto=format&w=320&fit=clip&dpr=2&usm=12&cs=strip')

client.run(token)
