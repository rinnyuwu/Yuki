import disnake
import random
from disnake.ext import commands

class CoinFlip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="coinflip", description="Flip a coin")
    async def coinflip(self, inter: disnake.AppCmdInter):
        flip_result = random.choice(["Heads", "Tails"])
        edge_chance = random.randint(1, 100)
        if edge_chance <= 5:
            flip_result = "Edge... Wait, what?"

        embed_color = 0x2196F3
        embed = disnake.Embed(color=embed_color)
        embed.set_author(name="Coinflip result", icon_url=self.bot.user.avatar.url)
        embed.description = f"You flipped: **{flip_result}**"
        await inter.send(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(CoinFlip(bot))
