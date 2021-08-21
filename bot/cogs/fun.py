from discord.ext import commands
import discord
import asyncio
import random
import datetime
import json
import os






class lustig(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=["8ball"])
    async def ball(self, ctx, *, frage):
            antworten = ["Ja", "Nein","Vielleicht", "Negativ", "Positiv"]
            embed = discord.Embed(title="Gebe mir eine Sekunde Ich werde das Orakel fragen!", color=0xffd700)
            msg = await ctx.reply(embed = embed)
            await asyncio.sleep(3)
            embed = discord.Embed(title=f"Die Antwort vom dem Orakel auf deine Frage:",
                                  description=f'**{frage}**:\n`{random.choice(antworten)}`', color=discord.Color.gold())
            embed.set_footer(text=f'frage von {ctx.author}', icon_url=f"{ctx.message.author.avatar_url}")
            await msg.edit(embed=embed)
            await ctx.message.delete()

    @commands.command(aliases=["av"])
    async def avatar(self, ctx, *, member: discord.Member = None):
        if member is None:
            member = ctx.author
        embed = discord.Embed(description=f"Hier ist das gewünschte [Icon]({member.avatar_url}) von {member.mention}",
                              color=0x2f3136, timestamp=datetime.datetime.utcnow())
        embed.set_image(url=f"{member.avatar_url}")
        embed.set_footer(text=f'von {ctx.author} \u200b', icon_url=f'{ctx.author.avatar_url}')
        await ctx.reply(embed=embed)
        await ctx.message.delete(delay=1)

    @commands.command()
    async def echo(self, ctx, *, text=None):
        if text is None:
            await ctx.send('Du musst einen Text angeben!')
            return
        if len(text) >= 4069:
            await ctx.send('Du kannst maximal Zeichen im Text verwenden!')
            return
        embed = discord.Embed(description=f"{text}", color=0xffd700)
        embed.set_thumbnail(url='https://tenor.com/view/cat-music-vibing-headphones-kitty-gif-20294084')
        await ctx.send(embed=embed)
        await ctx.message.delete(delay=1)

    @commands.command()
    async def userinfo(self, ctx, *, member: discord.Member = None):


        if member is None:
            member = ctx.author
        create = member.created_at
        joincreate = member.joined_at
        createtimestamp = create.timestamp()
        joincreatetimestamp = joincreate.timestamp()
        embed = discord.Embed(title=f'User Info - {member}, colour=member.color, timestap=ctx.message.created_at)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Angefragt von {ctx.author}", icon_url=ctx.author.avatar_url)

        embed.add_field(name="User ID:", value=member.id, inline=False)
        embed.add_field(name="Nickname:", value=member.display_name, inline=False)

        embed.add_field(name="Erstellt am:", value=member.created_at.strftime(f"<t:{int(createtimestamp)}:D>"), inline=False)
        embed.add_field(name="Gejoint:", value=member.joined_at.strftime(f"<t:{int(joincreatetimestamp)}:D>"), inline=False)
        await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(lustig(bot))