from discord.ext import commands
import discord
import pickle


bot = commands.Bot(command_prefix='$')

@bot.command('cat')
async def cat(ctx):
    '''По команде $cat возвращает категории списком'''
    pass


@bot.command('rand')
async def rand(ctx):
    '''По команде $rand возвращает случайный анекдот'''
    pass

@bot.command('anek')
async def anek(ctx, cat):
    '''По команде $anek {категория} возвращает случайный анекдот из выбранной категории'''
    pass


bot.run('MTAyMDkwNjIwMTk2NzQ5NzMyNg.GS1MLs.0dzDS2PASuV3v7qy0jLarNH7cLXZsupe7pgNPc')
