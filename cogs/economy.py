from random import random
import discord
from discord.ext import commands
import random
import sqlite3
from datetime import date, datetime

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def db(self, ctx):
        db = sqlite3.connect('Arsen.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM wallet")
        data = cursor.fetchall()
        formatted_data = [f"UserID: {user_id} | Wallet: {amount}$\n" for amount, user_id in data]
        await ctx.send("```" + "".join(formatted_data) + "```")
        db.commit()
        db.close()

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def crime(self, ctx):
        rdmnum = random.randint(300, 1500)
        db = sqlite3.connect('Arsen.db')
        cursor = db.cursor()
        cursor.execute("SELECT money FROM wallet WHERE user_id = ?", (ctx.author.id,))
        data = cursor.fetchone()
        if not data:
            cursor.execute("INSERT INTO wallet(money, user_id) VALUES(?, ?)", (rdmnum, ctx.author.id,))
            e1 = discord.Embed(
                description=f'{ctx.author.mention}  was a bad person and earned **{rdmnum}$**',
                timestamp=discord.utils.utcnow(),
                color=discord.Colour.random()
            )
            e1.set_footer(text="😆")
            e2 = discord.Embed(
                description=f'{ctx.author.mention}  committed a devious crime and earned **{rdmnum}$**',
                timestamp=discord.utils.utcnow(),
                color=discord.Colour.random()
            )
            e2.set_footer(text="😃")
            await ctx.send(embed=random.choice([e1,e2]))
        if data:
            newvalue = data[0] + rdmnum
            cursor.execute('UPDATE wallet SET money = ? WHERE user_id = ?', (newvalue, ctx.author.id))
            e1 = discord.Embed(
                description=f'{ctx.author.mention}  was a bad person and earned **{rdmnum}$**',
                timestamp=discord.utils.utcnow(),
                color=discord.Colour.random()
            )
            e1.set_footer(text="😆")
            e2 = discord.Embed(
                description=f'{ctx.author.mention}  committed a devious crime and earned **{rdmnum}$**',
                timestamp=discord.utils.utcnow(),
                color=discord.Colour.random()
            )
            e2.set_footer(text="😃")
            await ctx.send(embed=random.choice([e1,e2]))
        db.commit()
        cursor.close()
        db.close()

    @commands.command(aliases=["bal", "wallet"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def balance(self, ctx, member: discord.Member = None):
        member = ctx.author if member is None else member
        db = sqlite3.connect('Arsen.db')
        cursor = db.cursor()
        cursor.execute("SELECT money FROM wallet WHERE user_id = ?", (member.id,))
        data = cursor.fetchone()
        if data is None:
            e1 = discord.Embed(
                description=f'{member.mention} has a balance of **0$**',
                color=discord.Colour.random(),
                timestamp=discord.utils.utcnow(),
            )
            e1.set_footer(text="😟")
            e2 = discord.Embed(
                description=f'{member.mention} has a balance of **0$**',
                color=discord.Colour.random(),
                timestamp=discord.utils.utcnow(),
            )
            e2.set_footer(text="😭")
            await ctx.send(embed=random.choice([e1,e2]))
        if data:
            e1 = discord.Embed(
                description=f'{member.mention} has a balance of **{data[0]}$**',
                color=discord.Colour.random(),
                timestamp=discord.utils.utcnow(),
            )
            e1.set_footer(text="😟")
            e2 = discord.Embed(
                description=f'{member.mention} has a balance of **{data[0]}$**',
                color=discord.Colour.random(),
                timestamp=discord.utils.utcnow(),
            )
            e2.set_footer(text="😭")
            await ctx.send(embed=random.choice([e1,e2]))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def work(self, ctx):
        rdmnum = random.randint(100, 300)
        db = sqlite3.connect('Arsen.db')
        cursor = db.cursor()
        cursor.execute("SELECT money FROM wallet WHERE user_id = ?", (ctx.author.id,))
        data = cursor.fetchone()
        if not data:
            cursor.execute("INSERT INTO wallet(money, user_id) VALUES(?, ?)", (rdmnum, ctx.author.id,))
            e1 = discord.Embed(
                description=f'{ctx.author.mention}  worked hard for a day and earned **{rdmnum}$**',
                timestamp=discord.utils.utcnow(),
                color=discord.Colour.random()
            )
            e1.set_footer(text="🤪")
            e2 = discord.Embed(
                description=f'{ctx.author.mention}  got a promotion at work and earned **{rdmnum}$**',
                timestamp=discord.utils.utcnow(),
                color=discord.Colour.random()
            )
            e2.set_footer(text=f"😇")
            await ctx.send(embed=random.choice([e1,e2]))
        if data:
            newvalue = data[0] + rdmnum
            cursor.execute('UPDATE wallet SET money = ? WHERE user_id = ?', (newvalue, ctx.author.id))
            e1 = discord.Embed(
                description=f'{ctx.author.mention}  worked hard for a day and earned **{rdmnum}$**',
                timestamp=discord.utils.utcnow(),
                color=discord.Colour.random()
            )
            e1.set_footer(text="🤪")
            e2 = discord.Embed(
                description=f'{ctx.author.mention}  got a promotion at work and earned **{rdmnum}$**',
                timestamp=discord.utils.utcnow(),
                color=discord.Colour.random()
            )
            e2.set_footer(text=f"😇")
            await ctx.send(embed=random.choice([e1,e2]))
        db.commit()
        cursor.close()
        db.close()

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def rob(self, ctx):
        rdmnum = random.randint(1000, 5000)
        db = sqlite3.connect('Arsen.db')
        cursor = db.cursor()
        cursor.execute("SELECT money FROM wallet WHERE user_id = ?", (ctx.author.id,))
        data = cursor.fetchone()
        if not data:
            cursor.execute("INSERT INTO wallet(money, user_id) VALUES(?, ?)", (rdmnum, ctx.author.id,))
            e1 = discord.Embed(
                description=f'{ctx.author.mention}  swiftly robbed the bank without getting caught and earned **{rdmnum}$**',
                timestamp=discord.utils.utcnow(),
                color=discord.Colour.random()
            )
            e1.set_footer(text="😉")
            e2 = discord.Embed(
                description=f'{ctx.author.mention}  robbed the bank and escaped with **{rdmnum}$**',
                timestamp=discord.utils.utcnow(),
                color=discord.Colour.random()
            )
            e2.set_footer(text="😁")
            await ctx.send(embed=random.choice([e1,e2]))
        if data:
            newvalue = data[0] + rdmnum
            cursor.execute('UPDATE wallet SET money = ? WHERE user_id = ?', (newvalue, ctx.author.id))
            e1 = discord.Embed(
                description=f'{ctx.author.mention}  swiftly robbed the bank and earned **{rdmnum}$**',
                timestamp=discord.utils.utcnow(),
                color=discord.Colour.random()
            )
            e1.set_footer(text="😉")
            e2 = discord.Embed(
                description=f'{ctx.author.mention}  robbed the bank and barely escaped with **{rdmnum}$**',
                timestamp=discord.utils.utcnow(),
                color=discord.Colour.random()
            )
            e2.set_footer(text="😁")
            await ctx.send(embed=random.choice([e1,e2]))
        db.commit()
        cursor.close()
        db.close()

async def setup(bot):
    await bot.add_cog(Economy(bot))