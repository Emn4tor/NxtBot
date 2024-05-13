import os
from dotenv import load_dotenv
import discord
from discord.commands import Option

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

activity = discord.Activity(type=discord.ActivityType.playing, name="NxtGenGames")
status = discord.Status.online

bot = discord.Bot(
    intents=intents,
    debug_guilds=[1221490478940426340],
    status=status,
    activity=activity
)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


#DELETE SNITCH

@bot.event
async def on_message_delete(msg):
    if msg.author.bot:
        return
    await msg.channel.send(f"{msg.author} deleted a message:nerd::point_up_2: ")


#COMMANDS
@bot.slash_command(description="Say hello to someone")
async def greet(ctx, user: Option(discord.Member, "The user you wanna greet")):
    await ctx.respond(f"Hello {user.mention}")

@bot.slash_command(description="Say something in a specific channel")
@discord.default_permissions(manage_messages=True, administrator=True)
@discord.guild_only()
async def broadcast(
    ctx,
    text: Option(str, "Message u wanna send"),
    channel: Option(discord.TextChannel)
):
    await channel.send(text)
    await ctx.respond("Message sent!", ephemeral=True)

#EMBEDS

@bot.slash_command(description="Infos about a user")
async def info(ctx,user: Option(discord.Member, "USER", default=None)):
    if user is None:
        user = ctx.author

    embed = discord.Embed(
        title=f"infos about {user.name}",
        description=f"Details about {user.mention}",
        color=discord.Color.orange()
    )

    time = discord.utils.format_dt(user.created_at, "R")

    embed.add_field(name="Account creation", value=time,)
    embed.add_field(name="ID", value=user.id, inline=False)
    embed.set_thumbnail(url=user.display_avatar.url)
    embed.set_footer(text="NxtBot")
    await ctx.respond(embed=embed)





for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

load_dotenv()
bot.run(os.getenv("TOKEN"))
