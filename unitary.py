import os
from discord.ext import commands
from pint import UnitRegistry

bot = commands.Bot(command_prefix='?', description='Unit conversion bot')
unitRegistry = UnitRegistry()
quantity = unitRegistry.Quantity


@bot.command()
async def about():
    await bot.say("""I can convert units.

Try these queries:
`?find 60mph in kph`
`?find 180cm in inches`
`?find 5 feet + 11 inches in cm`""")


@bot.command()
async def find(*, message: str):
    try:
        src, dst = message.split(' in ')
        await bot.say(quantity(src).to(dst))
    except:
        await bot.say('I did not understand your query. Try rephrasing it.')

bot.run(os.environ.get('BOT_TOKEN'))
