import discord
from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='serverinfo')
    @commands.cooldown(1.0, 5.0, commands.BucketType.user)
    async def _serverinfo(self, ctx):
        reply_to = ctx.message.author
        message = ctx.message
        channel = message.channel
        server = message.guild
        server_name = server.name
        server_region = server.region
        server_id = server.id
        server_roles_amount = len(server.roles)
        server_emotes_amount = len(server.emojis)
        server_members_amount = server.member_count
        server_online = str(sum(1 for member in server.members if member.status!=status.offline))
        server_owner = server.owner
        server_verif_level = server.verification_level
        server_created_at = server.created_at
        image = server.icon_url_as(format='png')
        server_info_embed = discord.Embed(color=0x7fffff)
        server_info_embed.set_thumbnail(url=image)
        server_info_embed.set_author(name='Server Info')
        server_info_embed.add_field(name='Name', value='{}'.format(server_name), inline=False)
        server_info_embed.add_field(name='Region', value='{}'.format(server_region), inline=False)
        server_info_embed.add_field(name='ID', value='{}'.format(server_id), inline=False)
        server_info_embed.add_field(name='Owner', value='{}'.format(server_owner), inline=False)
        server_info_embed.add_field(name='VerificationLevel', value='{}'.format(server_verif_level), inline=False)
        server_info_embed.add_field(name='MembersAmount', value='All:`{}`\nOnline:`{}`'.format(server_members_amount, server_online), inline=False)
        server_info_embed.add_field(name='EmojiAmount', value='{}'.format(server_emotes_amount), inline=False)
        server_info_embed.add_field(name='RolesAmount', value='{}'.format(server_roles_amount), inline=False)
        server_info_embed.add_field(name='CreatedAt', value='{}'.format(server_created_at), inline=False)
        server_info_embed.add_field(name='Image', value=f'[Link]({image})', inline=False)
        server_info_embed.set_footer(text='Replying To {}'.format(reply_to))
        await channel.send(embed=server_info_embed)

def setup(bot):
    bot.add_cog(Info(bot))