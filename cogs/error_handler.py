import discord
from discord.ext import commands
import random

class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        ignored = (commands.CommandNotFound, commands.UserInputError)
        if isinstance(error, ignored):
            print(error)

        if isinstance(error, commands.CommandOnCooldown):
            m, s = divmod(error.retry_after, 60)
            h, m = divmod(m, 60)
            if int(h) == 0 and int(m) == 0:
                await ctx.send(
                    f' {ctx.author.mention}, you must wait `{int(s)}` seconds to use the `{ctx.invoked_with}` command!')
            elif int(h) == 0 and int(m) != 0:
                await ctx.send(
                    f' {ctx.author.mention}, you must wait `{int(m)} minutes` and `{int(s)} seconds` to use the `{ctx.invoked_with}` command!')
            else:
                await ctx.send(
                    f' {ctx.author.mention}, you must wait {int(h)} hours, {int(m)} minutes and {int(s)} seconds to use the `{ctx.invoked_with}` command!')
        elif isinstance(error, commands.MissingPermissions):
            missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_permissions]
            if len(missing) > 2:
                fmt = '{}, {}'.format(", ".join(missing[:-1]), missing[-1].lower())
            else:
                fmt = ' and '.join(missing)
            _message = '{}: `{}` requires the `{}` permissions'.format(ctx.author.mention, ctx.invoked_with,
                                                                         fmt.lower())
            e = discord.Embed(
                description=f'{_message}',
                color=discord.Colour.random()
            )
            await ctx.send(embed=e)
        raise error

async def setup(bot):
    await bot.add_cog(Error(bot))