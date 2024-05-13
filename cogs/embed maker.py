import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.ui import Button, View

class embedmaker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    @commands.has_permissions(administrator=True)
    async def embed(self, ctx, title: str, description: str, color: discord.Color = discord.Color.random()):
        embed = discord.Embed(title=title, description=description, color=color)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(embedmaker(bot))