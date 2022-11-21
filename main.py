import discord
from discord import app_commands
import random

id_do_servidor = 1044059682752450581  #Coloque aqui o ID do seu servidor

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False #Nós usamos isso para o bot não sincronizar os comandos mais de uma vez

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #Checar se os comandos slash foram sincronizados 
            await tree.sync(guild = discord.Object(id=id_do_servidor)) # Você também pode deixar o id do servidor em branco para aplicar em todos servidores, mas isso fará com que demore de 1~24 horas para funcionar.
            self.synced = True
        print(f"Logado como {self.user}.")

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'teste', description='Testando') #Comando específico para seu servidor
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Estou funcionando!", ephemeral = True) 

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'dado', description='Dado Lançado e o numero é...') #Comando específico para seu servidor
async def slash2(interaction: discord.Interaction):
    categorias = random.randint(1,10)
    await interaction.response.send_message(f"O número da categoria sorteada foi {categorias}", ephemeral = False) 


aclient.run('MTA0NDA1OTMxOTc5NDE0NzQ1OQ.GjbHCw.BDdRfQ9gbIcGiWGYT69gnW9D9fjcpW62zszRGM')