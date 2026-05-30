import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

PREFIX = "!"
BOT_NAME = "VeerEngineBot"
PROJECT_NAME = "Neev Game Engine"
CORE_VALUES = ["Gratitude", "Freedom", "Family", "Unbreakable"]
MISSION = "Un creators ko power dena jinke paas skills hain, paisa nahi."
SECRET_CODE_PHRASE = "Theek Hai Bhai"
SECRET_RESPONSE = "Aur Sab Theek"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"✅ {BOT_NAME} is online!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=PROJECT_NAME))

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if SECRET_CODE_PHRASE.lower() in message.content.lower():
        await message.channel.send(f"{SECRET_RESPONSE} 🤝")
    await bot.process_commands(message)

@bot.tree.command(name="ping", description="Bot status check")
async def slash_ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"🏓 {BOT_NAME} alive! Latency: {round(bot.latency * 1000)}ms")

@bot.tree.command(name="project", description="Game engine status")
async def slash_project(interaction: discord.Interaction):
    embed = discord.Embed(title=PROJECT_NAME, description=MISSION, color=discord.Color.green())
    embed.add_field(name="Core Values", value="\n".join(CORE_VALUES), inline=False)
    await interaction.response.send_message(embed=embed)

@bot.command()
async def info(ctx):
    await ctx.send(f"🤖 {BOT_NAME}\nPrefix: `{PREFIX}`\nCommands: `!info`, `!project`\nSlash: `/ping`, `/project`")

@bot.command()
async def project(ctx):
    embed = discord.Embed(title=PROJECT_NAME, color=discord.Color.purple())
    embed.add_field(name="Mission", value=MISSION, inline=False)
    embed.add_field(name="Core Values", value=", ".join(CORE_VALUES), inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def restart(ctx):
    if ctx.author.guild_permissions.administrator:
        await ctx.send("♻️ Restarting...")
        os._exit(0)
    else:
        await ctx.send("❌ Admin only.")

if __name__ == "__main__":
    print(f"🚀 Starting {BOT_NAME}...")
    bot.run(TOKEN)
