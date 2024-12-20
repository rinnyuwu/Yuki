import disnake
from disnake.ext import commands
import sqlite3
from database.database import get_permissions

class SlowMode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="slowmode", description="Set slowmode for the current channel (seconds)")
    async def slowmode(self, inter: disnake.AppCmdInter, time: int):
        if time < 1:
            await inter.send("The slowmode time must be at least 1 second", ephemeral=True)
            return

        has_permission = False
        if inter.user == inter.guild.owner or inter.author.guild_permissions.administrator:
            has_permission = True
        else:
            roles = inter.author.roles
            for role in roles:
                permissions = get_permissions(inter.guild.id, role.id)
                if "Slowmode" in permissions:
                    has_permission = True
                    break

        if not has_permission:
            await inter.send("You do not have permission to change the slowmode settings", ephemeral=True)
            return

        await inter.channel.edit(slowmode_delay=time)

        embed = disnake.Embed(
            description=f"Slowmode has been set to **{time}** seconds in this channel",
            color=0x2196F3
        )
        embed.set_author(name="Slowmode updated", icon_url=self.bot.user.avatar.url)
        await inter.send(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(SlowMode(bot))