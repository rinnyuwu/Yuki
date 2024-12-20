import disnake
from disnake.ext import commands
from database.database import init_db, update_permissions

class Permissions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        init_db()

    @commands.default_member_permissions(administrator=True)
    @commands.slash_command(name="permissions", description="Edit role permissions")
    async def permissions(
        self, 
        inter: disnake.AppCmdInter, 
        role: disnake.Role, 
        permission: str = commands.Param(
            choices=["Slowmode"],
            description="Choose permissions to modify"
        )
    ):
        server_id = inter.guild.id
        role_id = role.id
        permissions_list = []
        
        if permission == "Slowmode":
            permissions_list.append("Slowmode")
        update_permissions(server_id, role_id, permissions_list)

        embed = disnake.Embed(
            description=(
                f"Permissions for role **{role.name}** have been updated:\n"
                f" - **{', '.join(permissions_list)}**"
            ),
            color=0x2196F3
        )
        embed.set_author(name="Permissions updated", icon_url=self.bot.user.avatar.url)
        await inter.send(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(Permissions(bot))