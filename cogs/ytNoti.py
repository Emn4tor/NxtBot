from discord.ext import commands, tasks

import scrapetube


class Youtube(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channels = {
            "YellowMC Network": f"https://www.youtube.com/@YellowMCNetwork",
            "Emn4tor": f"https://youtube.com/@emn4tor"
        }
        self.videos = {}

    @commands.Cog.listener()
    async def on_ready(self):
        self.check.start()

    @tasks.loop(seconds=60)
    async def check(self):
        discord_channel = self.bot.get_channel(1221490479468904508)

        for channel_name in self.channels:
            videos = scrapetube.get_channel(channel_url=self.channels[channel_name], limit=5)
            video_ids = [video["videoId"] for video in videos]

            if self.check.current_loop == 0:
                self.videos[channel_name] = video_ids
                continue

            for video_id in video_ids:
                if video_id not in self.videos[channel_name]:
                    url = f"https://youtu.be/{video_id}"
                    await discord_channel.send(f"**{channel_name}** uploaded a new video! \n\n{url}")

            self.videos[channel_name] = video_ids


def setup(bot):
    bot.add_cog(Youtube(bot))