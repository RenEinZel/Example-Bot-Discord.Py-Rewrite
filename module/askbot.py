import discord
import random
from discord.ext import commands

class AskBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_color(self):
        colors = ['0x7fffff', '0xff7fff', '0xffff7f']
        col = random.choice(colors)
        color = int(col, 16)
        return color

    @commands.command(name='ask')
    @commands.cooldown(1.0, 5.0, commands.BucketType.user)
    async def _ask(self, ctx, *, thing):
        reply_to = ctx.message.author
        output = thing
        response = ['Yes.', 'No.', 'Take A Wild Guess...', 'Very Doubtful...',
                        'Sure.', 'Without A Doubt!', 'Most Likely!', 'Might Be Possible...',
                        "You'll Be The Judge.", 'No... (╯°□°）╯︵ ┻━┻', 'No... Baka.',
                        'Senpai, Pls No ;-;']
        col = self.get_color()
        answer = random.choice(response)
        emb = discord.Embed(color=col, timestamp=ctx.message.created_at)
        emb.set_author(name='8Ball Result')
        emb.add_field(name='Question', value=f'{output}', inline=False)
        emb.add_field(name='Answer', value=f'{answer}', inline=False)
        emb.set_footer(text='Being Answer By Bot! :3 | Replying To {}'.format(reply_to))
        await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(AskBot(bot))