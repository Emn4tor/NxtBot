import discord
from discord.ext import commands
from discord.commands import slash_command, Option


class cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




    @slash_command(description="Explore YellowMC's diverse gamemodes")
    async def yellowmc(self, ctx, gamemode: Option(str, description="Choose a gamemode", choices=["Realmforge", "Factions", "More (coming soon!)"])):
        """Provides descriptions for various YellowMC gamemodes"""

        gamemode_descriptions = {
            "Realmforge": "**Realmforge:** Where Minecraft Goes Epic \n Ever felt vanilla Minecraft lacked a certain...spark?  Do endless cobblestone castles and predictable creeper chases leave you yearning for more?  Then shatter those diamond swords and prepare to embark on a legendary quest with YellowMC!",
            "Factions": "**Factions:** Conquer, dominate, and forge alliances in this thrilling PvP experience. Strategize, raid, and build your faction to the top of the YellowMC food chain!",
            "More (coming soon!)": "YellowMC is constantly expanding! Stay tuned for even more exciting gamemodes to be announced soon."
        }

        description = gamemode_descriptions.get(gamemode, "Invalid gamemode. Please choose from the available options.")
        return await ctx.respond(description)

    @slash_command(description="Explore YellowMC's diverse gamemodes")
    async def turmonline(self, ctx, gamemode: Option(str, description="Choose a gamemode", choices=["CityBuild" "More (coming soon!)"])):
        """Provides descriptions for various YellowMC gamemodes"""

        gamemode_descriptions = {
            "CityBuild": "**CityBuild:** soon https://discord.gg/wV4BdYAPmy",
            "More (coming soon!)": "YellowMC is constantly expanding! Stay tuned for even more exciting gamemodes to be announced soon."
        }

        description = gamemode_descriptions.get(gamemode, "Invalid gamemode. Please choose from the available options.")
        return await ctx.respond(description)

#FUN
    @slash_command(description="Give someone a virtual hug!")
    async def hug(self, ctx, user: Option(discord.Member, "The user you want to hug")):
        if user == ctx.author:
            return await ctx.respond("Aww, you seem to need a hug! Here's one for you: ")  # Self-hug scenario

        if user is None:
            return await ctx.respond("Hey, you gotta tell me who to hug! Try mentioning a user.")  # Missing user

        hug_gifs = [
            "https://media1.tenor.com/m/J7eGDvGeP9IAAAAC/enage-kiss-anime-hug.gif",
            "https://i.pinimg.com/originals/4d/89/d7/4d89d7f963b41a416ec8a55230dab31b.gif",
            "https://i.imgur.com/b8i6SNI.gif",
            "https://gifdb.com/images/high/anime-hug-constanze-akko-ckpz3d1ia0qua40k.gif",
        ]
        random_gif = random.choice(hug_gifs)  # Choose a random hug GIF from the list

        embed = discord.Embed(
            title=f"{ctx.author.name} hugs {user.name}!",
            description=f"Here's a warm hug for you, {user.mention}!",
            color=discord.Color.gold(),
        )
        embed.set_image(url=random_gif)
        await ctx.respond(embed=embed)
    #8ball
    import random

    @slash_command(description="Ask the magic 8-ball a question! ")
    async def eightball(self, ctx, question: Option(str, "Your question for the magic 8-ball")):
        """Provides a random 8-ball response to a question."""
        if question is None:
            return await ctx.respond("You gotta ask a question for the 8-ball to answer!")

        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Cannot predict now.",
            "Don't count on it.",
            "My sources say no.",
            "Outlook not so good.",
            "Most likely.",
            "Yes.",
            "Signs point to yes.",
        ]
        answer = random.choice(responses)
        await ctx.respond(f"**{question}**\nThe magic 8-ball says: {answer}")

    @slash_command(description="Flip a coin! Heads or tails?")
    async def coinflip(self, ctx):
      """Flips a coin and displays the result."""
      coin_flips = ["heads", "tails"]
      result = random.choice(coin_flips)
      await ctx.respond(f"Flipping a coin... It lands on {result.upper()}!")

    @slash_command(description="Roll a dice! Choose the number of sides.")
    async def roll(self, ctx, sides: Option(int, "The number of sides on the dice", choices=[4, 6, 8, 10, 12, 20, 100])):
        """Rolls a dice with the specified number of sides."""
        result = random.randint(1, sides)
        await ctx.respond(f"The dice rolls... It lands on **{result}**!")


    @slash_command(description="Test your IQ!")
    async def iq(self, ctx):
        iq_score = random.randint(1, 200)

        if iq_score == 69:
            response = "Well, aren't you cheeky! Your IQ score is **69**. �"
        elif iq_score < 50:
            response = "Your Iq matches the IQ of a toast 🍞 Go to school!📚"
        elif iq_score < 70:
            response = "You might want to work on those brain teasers! less beer more books!🍺📚"
        elif iq_score < 90:
            response = "You're doing okay! Keep exercising that brain.🧠"
        elif iq_score < 110:
            response = "solid! You're above average. Keep it up!👍"
        elif iq_score < 130:
            response = "Nice! here is a cookie 🍪"
        elif iq_score < 150:
            response = "Congratulations! You're a certified genius!🎉🎉🎉"
        elif iq_score < 170:
            response = "Go make a application as Developer!👨‍💻👩‍💻 rn!"
        elif iq_score < 190:
            response = "New Albert Einstein is born! 🧠🧠"
        else:
            response = "Astounding! Your IQ is beyond measure. You're a once-in-a-lifetime genius!"

        await ctx.respond(f"Your IQ score is **{iq_score}**. {response}")


    @slash_command(description="Inspire yourself with a motivational quote!")
    async def qoute(self, ctx):
        """Provides a random motivational quote."""
        quotes = [
            "The only way to achieve the impossible is to believe it is possible.",
            "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.",
            "Don't watch the clock; do what it does. Keep going.",
            "The only limit to our realization of tomorrow will be our doubts of today.",
            "The best way to predict the future is to create it.",
            "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it.",
            "Success is not in what you have, but who you are.",
            "The secret of getting ahead is getting started.",
            "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart.",
            "The harder you work for something, the greater you'll feel when you achieve it.",
        ]
        quote = random.choice(quotes)
        await ctx.respond(f"**Motivational Quote:**\n{quote}")



    @slash_command(description="Get a random dad joke!")
    async def dadjoke(self, ctx):
        """Provides a random dad joke."""
        dad_jokes = [
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "I'm reading a book on anti-gravity. It's impossible to put down!",
            "Why don't skeletons fight each other? They don't have the guts.",
            "I used to play piano by ear, but now I use my hands.",
            "I'm on a seafood diet. I see food and I eat it.",
            "I'm reading a book about mazes. I got lost in it.",
            "I told my wife she should embrace her mistakes. She gave me a hug.",
            "I'm friends with 25 letters of the alphabet. I don't know y.",
            "I used to be a baker, but I couldn't make enough dough.",
            "I'm reading a book on the history of glue. I just can't seem to put it down.",
            "I'm friends with a lot of vegetarians. I meat them at the salad bar.",

        ]
        joke = random.choice(dad_jokes)
        await ctx.respond(f"**Dad Joke:**\n{joke}")


    @slash_command(description="Get a random joke!")
    async def joke(self, ctx):
        """Provides a random joke."""
        jokes = [
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "I'm reading a book on anti-gravity. It's impossible to put down!",
            "Why don't skeletons fight each other? They don't have the guts.",
            "I used to play piano by ear, but now I use my hands.",
            "I'm on a seafood diet. I see food and I eat it.",
            "I'm reading a book about mazes. I got lost in it.",
            "I told my wife she should embrace her mistakes. She gave me a hug.",
            "I'm friends with 25 letters of the alphabet. I don't know y.",
            "I used to be a baker, but I couldn't make enough dough.",
            "I'm reading a book on the history of glue. I just can't seem to put it down.",
            "I'm friends with a lot of vegetarians. I meat them at the salad bar.",
            "Why don't scientists trust atoms? Because they make up everything!",
            "Did you hear about the claustrophobic astronaut? He needed space.",
            "How does a penguin build its house? Igloos it together.",
            "Why don't skeletons go to scary movies? They don't have the guts.",
            "I'm trying to organize a hide and seek competition, but it's tough to find good players. They're always hiding.",
            "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
            "I told my computer I needed a break, and now it won't stop sending me vacation ads.",
            "What do you call fake spaghetti? An impasta.",
            "I'm reading a book about anti-gravity. It's impossible to put down!",
            "Why did the tomato turn red? Because it saw the salad dressing!",
            "I told my wife she was drawing her eyebrows too high. She looked surprised.",
            "How do you organize a space party? You planet.",
            "What do you call fake noodle? An impasta.",
            "Why did the scarecrow become a successful neurosurgeon? Because he was outstanding in his field.",
            "Why don't skeletons fight each other? They don't have the guts.",
            "Why did the bicycle fall over? It was two-tired.",
            "I'm reading a book about mazes. I got lost in it.",
            "I told my wife she should embrace her mistakes. She gave me a hug.",
            "I'm friends with 25 letters of the alphabet. I don't know y.",
            "Why don't scientists trust atoms? Because they make up everything!",
            "What did the janitor say when he jumped out of the closet? \"Supplies!\"",
            "I used to be a baker, but I couldn't make enough dough.",
            "I'm reading a book on the history of glue. I just can't seem to put it down.",
            "I'm friends with a lot of vegetarians. I meat them at the salad bar."
        ]

        joke = random.choice(jokes)
        await ctx.respond(f"**Joke:**\n{joke}")


    @slash_command(description="uwuify your text!")
    async def uwu(self, ctx, text: Option(str, "The text you want to uwuify")):
        """Converts text into uwu language."""
        uwu_text = text.replace("l", "w").replace("r", "w")
        await ctx.respond(uwu_text)

    @slash_command(description="Throwing stuff is fun!")
    async def throw(self, ctx):
        #throw an random item at a random user
        items = ["banana", "apple", "shoe", "brick", "book", "pillow", "water bottle", "rubber duck", "potato", "sock", "cheese", "homeless man", "rock", "car", "cat", "dog", "fish", "bird", "laptop", "phone", "keyboard", "mouse", "monitor", "chair", "table", "lamp", "couch", "bed", "pillow", "blanket", "towel", "toothbrush", "toothpaste", "soap", "shampoo", "conditioner", "towel", "toilet paper", "toilet", "sink", "bathtub", "shower", "mirror", "window", "door", "wall", "floor", "ceiling", "roof", "tree", "bush", "flower", "grass", "dirt", "sand", "water", "fire", "air", "earth", "metal", "wood", "plastic", "glass", "paper", "cloth", "leather", "stone", "brick", "cement", "sand", "dirt", "mud", "clay", "snow", "ice", "fog", "smoke", "steam", "cloud", "rain", "snow", "hail", "sleet", "wind", "breeze", "gust", "storm", "hurricane", "tornado", "thunderstorm", "lightning", "rainbow", "sun", "moon", "star", "planet", "galaxy", "universe", "black hole", "wormhole", "supernova", "nebula", "quasar", "pulsar", "comet", "asteroid", "meteor", "meteorite", "moon rock", "star dust", "alien", "ufo", "spaceship", "astronaut", "rocket", "satellite", "space station", "space suit", "space helmet", "space boots", "space gloves", "space food", "space drink", "space toilet", "space shower", "space bed", "space couch", "space chair", "space table", "space lamp", "space window", "space door", "space wall", "space floor", "space ceiling", "space roof", "space tree", "space bush", "space flower", "space grass", "space dirt", "space sand", "space water", "space fire", "space air", "space earth", "space metal", "space wood"]
        users = ctx.guild.members
        item = random.choice(items)
        user = random.choice(users)
        await ctx.respond(f"**{ctx.author}** threw a **{item}** at **{user}**!")


def setup(bot):
    bot.add_cog(cmds(bot))

import random