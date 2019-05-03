import discord
import asyncio
import random

from module.util.config import read_config
from discord.ext import commands

# setting some stuff
bot = discord.client
bot = commands.Bot(command_prefix=read_config('prefix'))
bot.remove_command('help')
status = discord.Status



# load_modules
startup_extensions = ['module.help',
                      'module.info',
                      'module.main']



if __name__ == "__main__":
    for extension in startup_extensions:
        try:

            bot.load_extension(extension)
            print(f'{extension} Has Been Loaded!  All {extension} Command Is Up!')
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))


# creating Random Presence
@bot.event
async def presence():
    await bot.wait_until_ready()
    while not bot.is_closed():
        get_info = random.randint(1, 3)
        if get_info == 1:
            thing = ('In {} Servers'.format(len(bot.guilds)))
        if get_info == 2:
            thing = ('With {} Users'.format(len(list(bot.get_all_members()))))
        if get_info == 3:
            thing = "Prefixes: 'e:'"
        await bot.change_presence(status=status.dnd, activity=discord.Game(name=thing))
        await asyncio.sleep(15)



# startup bot
@bot.event
async def on_ready():
    bot.loop.create_task(bot.presence()) #add this line for random presence
    print("The Bot Is Now Online And Ready To Work! :)")
    print(f'Extensions Loaded: {len(bot.extensions)}/{len(startup_extensions)}')
    print('all module are up!')
    
bot.run(read_config('token')
