import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.ui import Button, View
import random
import asyncio

class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.flags = {
    "bosnia": "🇧🇦 ",
"uk": "🇬🇧",
"usa": "🇺🇸",
"france": "🇫🇷",
"germany": "🇩🇪",
"italy": "🇮🇹",
"canada": "🇨🇦",
"australia": "🇦🇺",
"japan": "🇯🇵",
"china": "🇨🇳",
"india": "🇮🇳",
"russia": "🇷🇺",
"brazil": "🇧🇷",
"south_korea": "🇰🇷",
"spain": "🇪🇸",
"mexico": "🇲🇽",
"south_africa": "🇿🇦",
"argentina": "🇦🇷",
"turkey": "🇹🇷",
"egypt": "🇪🇬",
"ireland": "🇮🇪",
"switzerland": "🇨🇭",
"netherlands": "🇳🇱",
"belgium": "🇧🇪",
"sweden": "🇸🇪",
"norway": "🇳🇴",
"denmark": "🇩🇰",
"finland": "🇫🇮",
"poland": "🇵🇱",
"austria": "🇦🇹",
"singapore": "🇸🇬",
"thailand": "🇹🇭",
"indonesia": "🇮🇩",
"kenya": "🇰🇪",
"nigeria": "🇳🇬",
}
        self.scores = {}

    @slash_command()
    async def flags(self, ctx):
        await ctx.respond("Starting the game in 3 seconds...")
        await asyncio.sleep(3)

        start_time = discord.utils.utcnow()
        while (discord.utils.utcnow() - start_time).total_seconds() < 30:
            country, flag_url = random.choice(list(self.flags.items()))
            await ctx.send(f"Guess the country for this flag: {flag_url}")

            def check(m):
                return m.channel == ctx.channel and m.content.lower() == country.lower()

            try:
                guess = await self.bot.wait_for('message', check=check, timeout=5)
            except asyncio.TimeoutError:
                await ctx.send(f"Time's up! The correct answer was {country}.")
            else:
                self.scores[guess.author] = self.scores.get(guess.author, 0) + 1
                await ctx.send(f"Correct, {guess.author}! Your current score is {self.scores[guess.author]}.")

        await ctx.send("Game over!")

    @slash_command()
    async def topflags(self, ctx):
        leaderboard = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        embed = discord.Embed(title="Flag Guessing Leaderboard", description="\n".join(f"{i+1}. {user}: {score}" for i, (user, score) in enumerate(leaderboard)))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(games(bot))