import discord
from discord.ext import commands
from config import TOKEN
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            await attachment.save(f'./images/{file_name}')
            await ctx.send(f'Saved the image to ./images/{file_name}')
            result = get_class(model_path="keras_model.h5", label_path="labels.txt", image_path=f"./images/{file_name}")
            class_name = result[0]
            confidence_score = result[1]
            if class_name == 'Güvercin\n':
                await ctx.send('This is a pigeon! Confidence score: ' + str(confidence_score))
            elif class_name == 'Serçe\n':
                await ctx.send('This is a sparrow! Confidence score: ' + str(confidence_score))
            else:
                await ctx.send('I dont know what this is :(')
    else:
        await ctx.send('You forgot the upload the image')



bot.run(TOKEN)