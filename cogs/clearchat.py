import discord
from discord.ext import commands, tasks
from discord.commands import slash_command, Option


class clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='clear', aliases=['clr'])
    @commands.has_permissions(manage_messages=True)
    async def clear_chat(self, ctx, amount: int = 1):
        await ctx.channel.purge(limit=amount)
        await ctx.respond(f'Cleared {amount} messages', ephemeral=True)

def setup(bot):
    bot.add_cog(clear(bot))
