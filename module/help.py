import discord
from discord.ext import commands

class HELPStuff(commands.Cog):
    # init
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help', pass_context=True)
    async def _help(self, ctx, cata=""):
        reply_to = ctx.message.author
        if cata =="":
            embed_config = discord.Embed(
                colour=discord.Colour.blue()
            )
            embed_config.set_author(name='❓ Help Page ☕')
            embed_config.add_field(name='Bot Prefixes:', value='" e: "')
            embed_config.add_field(name='Help Usage:', value='Use `{prefix}help {module}`', inline=False)
            embed_config.add_field(name='Commands:', value='- echo\n- ping\n- serverinfo', inline=False)
            embed_config.set_footer(text='❗ Replying To {}'.format(reply_to))
            await ctx.send(embed=embed_config)
            return


def setup(bot):
    bot.add_cog(HELPStuff(bot))