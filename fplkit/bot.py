import discord
import discord.ext
from typing import Optional
from innards.functions.associate import *

# GUILD 735830432641318922
# TOKEN MTE4Njg1NDczNDE1NDQ0NDkwMA.GW5dHh.xnbtkJhQrsetLeMOkeT2qKniPRRxhsYeevoZrU



import discord
from discord import app_commands


MY_GUILD = discord.Object(id=735830432641318922)  # replace with your guild id


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
client = MyClient(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')

@client.tree.command()
async def memberlist(interaction: discord.Interaction):
    asso = associate()
    playerList = asso.IDAssociate()
    print(playerList)
    await interaction.response.send_message(playerList)
    


@client.tree.command()
@app_commands.describe(
    first_value='The first value you want to add something to',
    second_value='The value you want to add to the first value',
)
async def add(interaction: discord.Interaction, first_value: int, second_value: int):
    """Adds two numbers together."""
    await interaction.response.send_message(f'{first_value} + {second_value} = {first_value + second_value}')

@client.tree.command()
@app_commands.rename(text_to_send='text')
@app_commands.describe(text_to_send='Text to send in the current channel')
async def send(interaction: discord.Interaction, text_to_send: str):
    """Sends the text into the current channel."""
    await interaction.response.send_message(text_to_send)


@client.tree.command()
@app_commands.describe(member='The member you want to get the joined date from; defaults to the user who uses the command')
async def joined(interaction: discord.Interaction, member: Optional[discord.Member] = None):
    member = member or interaction.user

    await interaction.response.send_message(f'{member} joined {discord.utils.format_dt(member.joined_at)}')



@client.tree.context_menu(name='FPL Members')
async def show_join_date(interaction: discord.Interaction, member: discord.Member):

    await interaction.response.send_message(f'{member} joined at {discord.utils.format_dt(member.joined_at)}')


@client.tree.context_menu(name='Report to Moderators')
async def report_message(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message(
        f'Thanks for reporting this message by {message.author.mention} to our moderators.', ephemeral=True
    )

    # Handle report by sending it into a log channel
    log_channel = interaction.guild.get_channel(0)  # replace with your channel id

    embed = discord.Embed(title='Reported Message')
    if message.content:
        embed.description = message.content

    embed.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)
    embed.timestamp = message.created_at

    url_view = discord.ui.View()
    url_view.add_item(discord.ui.Button(label='Go to Message', style=discord.ButtonStyle.url, url=message.jump_url))

    await log_channel.send(embed=embed, view=url_view)


client.run('MTE4Njg1NDczNDE1NDQ0NDkwMA.GW5dHh.xnbtkJhQrsetLeMOkeT2qKniPRRxhsYeevoZrU')