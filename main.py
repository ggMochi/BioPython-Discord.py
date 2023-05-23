import os
import discord
from config import TOKEN, PREFIX
from discord.ext import commands
boss = commands.Bot(command_prefix=PREFIX, 
        intents = discord.Intents().all())

@boss.event
async def on_ready():
    print(f'{boss.user} foi corretamente iniciado')
    await load_cog(boss)
    

@boss.event  
async def on_message(message):
    if message.author == boss.user:
        return
    
    await boss.process_commands(message)

async def load_cog(boss):
    file = os.listdir("commands")
    for subfile in file:
        archive = os.path.join("commands", subfile)
        final_archive = os.listdir(archive)
        for final in final_archive:
            if os.path.isdir(final):
                pass
            else: 
                if(final.endswith(".py")):
                    cog = final[:-3]                        
                    await boss.load_extension(f"commands.{subfile}.{cog}")
    
    print("Cogs carregadas com sucesso")

boss.run(TOKEN)
