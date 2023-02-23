import discord
import datetime
from discord.ext import commands, tasks

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Estou pronto! Estou conectado como {bot.user}")
    current_time.start()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "palavrão" in message.content:
        await message.channel.send(
            f"Por favor, {message.author.name}, não ofenda os demais usuários!"
        )

        await message.delete()

    await bot.process_commands(message)

@bot.command(name='oi')
async def send_hello(ctx):
    name = ctx.author.name

 channel = bot.get_channel(1071791531507322911)

    response = "Olá, " + name



@bot.command(name="calcular")
async def calculate_expression(ctx, *exppression):
    exppression = "".join(exppression)

    print(exppression)

    response = eval(exppression)

    await ctx.send("A resposta é: " + str(response))

@tasks.loop(hours=1)
async def current_time():
    now = datetime.datetime.now()

    now = now.strftime("%d/%m/%Y às %H:%M:%S")

    channel = bot.get_channel(1071791531507322911)

    await channel.send("Data atual: " + now)

bot.run("MTA3MDUwODEyNDY4NDk2MzkxMQ.GcX6YW.9CiioSxyb6p8yMJBu8vQcxGuGnoiD4AJuRhrYE")