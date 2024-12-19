import disnake
from disnake.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="info", description="Get information about the bot")
    async def info(self, inter: disnake.AppCmdInter):
        embed = disnake.Embed(
            description="I'm your friendly bot, always here to help with tasks on the server 🤍",
            color=0x0099FF
        )
        embed.set_author(name="Bot info", icon_url=self.bot.user.avatar.url)
        embed.add_field(name="Features", value="Sadly, I don't do much yet...", inline=False)
        embed.set_footer(text=f"Developer: rinny.uwu\nVersion: 2.0.0\nBot ID: {self.bot.user.id}")
        await inter.send(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(Info(bot))
