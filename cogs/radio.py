import discord
from discord.ext import commands
from discord.commands import slash_command

class Radio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    radio_stations = {
        "iloveradio1": "https://streams.ilovemusic.de/iloveradio1.mp3",
        "DanceMusic": "https://streams.ilovemusic.de/iloveradio2.mp3",
        "2000sThrowBacks": "https://streams.ilovemusic.de/iloveradio37.mp3",
        "2010sThrowBacks": "https://streams.ilovemusic.de/iloveradio38.mp3",
        "hardstyle": "https://streams.ilovemusic.de/iloveradio21.mp3",
        "tmmrlands": "https://streams.ilovemusic.de/iloveradio15.mp3"
    }

    @slash_command(description="Start Radio")
    async def play(self, ctx, station: str = "iloveradio1"):
        if ctx.author.voice is None:
            return await ctx.respond("You're not in a voice channel!")

        if not ctx.author.voice.channel.permissions_for(ctx.guild.me).connect:
            return await ctx.respond("I don't have permission to connect to the voice channel.")

        if ctx.voice_client is None:
            await ctx.author.voice.channel.connect()  # Bot is not in any voice channel
        else:
            await ctx.voice_client.move_to(ctx.author.voice.channel)  # Bot is already in a different voice channel

        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()

        # Check if the requested station exists in the dictionary
        if station not in self.radio_stations:
            return await ctx.respond(f"Invalid station: {station}. Please choose from available stations: {', '.join(self.radio_stations.keys())}")

        station_url = self.radio_stations[station]
        ctx.voice_client.play(discord.FFmpegPCMAudio(station_url))
        await ctx.respond(f"Playing radio station: {station}")

    @slash_command(description="Stop Radio")
    async def leave(self, ctx):
        if ctx.voice_client is None:
            return await ctx.respond("I'm not in a voice channel!")

        await ctx.voice_client.disconnect()
        await ctx.respond("Disconnected!")

    @slash_command(description="List all Stations")
    async def stations(self, ctx):
        return await ctx.respond(f"**All Stations** \n{', '.join(self.radio_stations.keys())}")



def setup(bot):
    bot.add_cog(Radio(bot))
