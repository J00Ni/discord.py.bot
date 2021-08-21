from discord.ext import commands
import discord
import asyncio
import random
import datetime
import json
import os
bot = commands.Bot(command_prefix=commands.when_mentioned_or("b!", "B!"), case_insensitive=True)





class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot \


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, rr, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(title=f'Der {member} wurde gebannt.\nGrund: `{rr}`')
        await ctx.reply(embed=embed)
        await ctx.message.delete()
#der grund wird nur bei der message angezeigt aber nicht bei den server gebannten leuten...

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, rr, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(title=f'Der {member} wurde gekickt.\nGrund: `{rr}`')
        await ctx.reply(embed=embed)
        await ctx.message.delete()
#der grund wird nur bei der message angezeigt aber nicht bei den server gebannten leuten...


  

def setup(bot):
    bot.add_cog(moderation(bot))
