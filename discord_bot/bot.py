import discord
from discord.ext import commands
from llm_integration import get_response_from_llm

TOKEN = "YOUR_DISCORD_BOT_TOKEN_HERE"  # Placeholder for the bot token

# Initialize the bot with command prefix "!"
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.command()
async def ask(ctx, *, question):
    """Command to ask the bot a physics question"""
    response = get_response_from_llm(question)
    await ctx.send(response)

if __name__ == "__main__":
    bot.run(TOKEN)
 
