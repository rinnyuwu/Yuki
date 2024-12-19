import disnake
import random
from disnake.ext import commands

class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="roll", description="Number roll")
    async def roll(self, inter: disnake.AppCmdInter, number: int):
        result = random.randint(1, number)

        embed_color = 0x4CAF50 if result > number / 2 else 0xF44336
        embed = disnake.Embed(
            color=embed_color
        )
        embed.set_author(name="Roll result", icon_url=self.bot.user.avatar.url)
        embed.description = f"You rolled a **{result}** out of **{number}**"
        await inter.send(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(Roll(bot))
