import discord
from discord.ext import commands

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='echo')
    @commands.cooldown(1.0, 10.0, commands.BucketType.user)
    async def _echo(self, ctx, *, thing):
        reply_to = ctx.message.author
        output = str(thing).replace('@everyone', '⛔ Dont Do That')
        print('{} Has Requested An Echo Message. (Content: {})'.format(reply_to, output))
        echo = await ctx.send('{}'.format(output))
        await ctx.message.delete()

    @commands.command(name='ping')
    @commands.cooldown(1.0, 5.0, commands.BucketType.user)
    async def _ping(self, ctx):
        msg = ctx.message
        reply_to_ping = msg.author
        start = time.perf_counter()
        checkping = await msg.channel.send('Checking Ping...')
        end = time.perf_counter()
        duration = (end - start) * 1000
        pingcheck_embed = discord.Embed(
            colour=discord.Colour.blue()
        )
        pingcheck_embed.set_author(name='PingCheck')
        pingcheck_embed.add_field(name='Ping', value='{:.2f}ms'.format(duration), inline=False)
        pingcheck_embed.set_footer(text='Replying To {}'.format(reply_to_ping))
        await msg.channel.send(embed=pingcheck_embed)
        await checkping.delete()
        pass

def setup(bot):
    bot.add_cog(Main(bot))