import discord
import random
import pytz
import datetime
import json
import os
from discord.ext import commands, tasks
from discord.commands import slash_command, Option


class QOTD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.questions = []
        self.load_questions()  # Load questions when the bot starts
        self.qotd_task.start()

    @tasks.loop(hours=24)
    async def qotd_task(self):
        await self.send_qotd()

    async def send_qotd(self):
        if not self.questions:
            return

        question = random.choice(self.questions)
        self.questions.remove(question)

        channel = await self.bot.fetch_channel(1234445319975211039)

        embed = discord.Embed(
            title="Question of the Day",
            description=f"Today's question is: {question}",
            color=discord.Color.orange()
        )
        embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/589118083500904448/eu-RVGFT_400x400.jpg")

        await channel.send(embed=embed)

    @slash_command(name="addquestion")
    @commands.has_permissions(administrator=True)
    async def add_question(self, ctx, question: str):
        self.questions.append(question)
        self.save_questions()  # Save questions after adding a new one
        await ctx.respond("Question added successfully!")

    @slash_command()
    @commands.has_permissions(administrator=True)
    async def qotd(self, ctx):
        await self.send_qotd()

    def load_questions(self):
        if os.path.exists("questions.json"):
            with open("questions.json", "r") as file:
                self.questions = json.load(file)

    def save_questions(self):
        with open("questions.json", "w") as file:
            json.dump(self.questions, file)




def setup(bot):
    bot.add_cog(QOTD(bot))
