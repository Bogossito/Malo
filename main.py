import discord
import time
print("lancement du Bot...")


from discord.ext import commands


bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
    print("Bot prêt")
    await bot.change_presence(status=discord.Status.idle,
            activity=discord.Game("Baiser ta mère"))

@bot.command()
async def regles(ctx):
    await ctx.send("*Ne pas être pd \n* Pas de SIMP \n* Que des alphas")

@bot.command()
async def spam(ctx, pd: discord.Member):
    pseudo = pd.mention
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")
    time.sleep(0.75)
    await ctx.send(f"T'es pd {pseudo}")

@spam.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Essaye sous cette forme : \n !spam @pseudo")

@bot.command()
async def commands(ctx):
    await ctx.send("Les commandes sont \n !spam @pseudo \n !regles")


@bot.command()
async def sang(ctx):
    await ctx.send("Célina est une pute")




jeton = "NzM2NTYzMTI1MTEyOTMwMzA1.Xxwn3Q.ZWqq9Qk9EB1_doIEmEgqfoEb-kY"

bot.run(jeton)



