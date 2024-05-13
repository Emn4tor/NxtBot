import discord
from discord import Intents
from discord.ext import commands
from discord.commands import slash_command

class Greet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def greett(self, ctx):
        await ctx.respond(f"Hi {ctx.author.mention}")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(
            title="Welcome",
            description=f"{member.mention} joined",
            color=discord.Color.orange()
        )
        embed.set_thumbnail(url=member.display_avatar.url)

        channel = await self.bot.fetch_channel(1221490479019987213)
        await channel.send(embed=embed)




def setup(bot):
    bot.add_cog(Greet(bot))