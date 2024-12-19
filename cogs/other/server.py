import disnake
from disnake.ext import commands

class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="server", description="Get information about the server")
    async def server_info(self, inter: disnake.AppCmdInter):
        guild = inter.guild
        owner = guild.owner.mention if guild.owner else "Unknown"
        created_at = int(guild.created_at.timestamp())
        bot_count = len([m for m in guild.members if m.bot])
        user_count = guild.member_count - bot_count

        if bot_count == 1:
            member_text = f"Members: **{guild.member_count}** (**{user_count} user** and **{bot_count} bot**)"
        elif bot_count > 1:
            member_text = f"Members: **{guild.member_count}** (**{user_count} users** and **{bot_count} bots**)"
        else:
            member_text = f"Members: **{guild.member_count}** (**{user_count} users**)"

        text_channels = len([c for c in guild.channels if isinstance(c, disnake.TextChannel)])
        voice_channels = len([c for c in guild.channels if isinstance(c, disnake.VoiceChannel)])
        stage_channels = len([c for c in guild.channels if isinstance(c, disnake.StageChannel)])
        forum_channels = len([c for c in guild.channels if isinstance(c, disnake.ForumChannel)])
        media_channels = len([c for c in guild.channels if isinstance(c, disnake.TextChannel) and c.is_news()])
        active_threads = len([t for t in guild.threads if isinstance(t, disnake.Thread) and not t.archived])

        embed = disnake.Embed(color=0x2196F3)
        embed.set_author(name="Server information", icon_url=guild.icon.url if guild.icon else None)
        embed.description = (
            f" - Name: **{guild.name}**\n"
            f" - Server ID: **{guild.id}**\n"
            f" - Owner: **{owner}**\n"
            f" - Created on: <t:{created_at}:f>\n"
            f" - {member_text}\n"
            f" - Boosts: **{guild.premium_subscription_count}**\n"
            f" - Roles: **{len(guild.roles)}**\n"
            f" - Channels: **{len(guild.channels)}**\n"
            f"  - Text channels: **{text_channels}**\n"
            f"  - Voice channels: **{voice_channels}**\n"
            f"  - Stage channels: **{stage_channels}**\n"
            f"  - Active threads: **{active_threads}**\n"
            f"  - Forum channels: **{forum_channels}**\n"
            f"  - Media channels: **{media_channels}**"
        )
        await inter.send(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(ServerInfo(bot))
