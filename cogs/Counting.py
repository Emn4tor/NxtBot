import discord
from discord.ext import commands

class Count(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.current_count = 1
        self.last_sender = None

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or message.channel.id != 1234254837982564433:
            return

        content = message.content.strip()
        expected_count = str(self.current_count)

        if content == expected_count:
            if self.last_sender == message.author:
                await message.add_reaction('❌')
                await message.channel.send("**Oops!** You can't count twice in a row!")
                self.current_count = 1
                self.last_sender = None
                await message.channel.send("0")
            else:
                await message.add_reaction('✅')
                self.current_count += 1
                self.last_sender = message.author
        else:
            await message.add_reaction('❌')
            await message.channel.send(f"**Oops!** Expected number was {expected_count}.")
            self.current_count = 1  # Reset count
            self.last_sender = None  # Reset last sender

            await message.channel.send("0")

def setup(bot):
    bot.add_cog(Count(bot))
