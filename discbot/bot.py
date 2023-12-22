import discord

# Define the intents
intents = discord.Intents.default()
intents.message_content = True  # Allow the bot to listen for message events

# Create an instance of the Discord client with intents
client = discord.Client(intents=intents)

# Event: Triggered when the bot is ready and connected to Discord
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Event: Triggered when a message is received
@client.event
async def on_message(message):
    # Check to ensure the bot doesn't respond to its own messages
    if message.author == client.user:
        return

    # Check for a specific command (e.g., "!fplinfo")
    if message.content.startswith('!fplinfo'):
        # Your FPL information handling code here
        response = "bar"
        await message.channel.send(response)

    if message.content.startswith('!goals-solanke'):
        response = "6"
        await message.channel.send(response)

# Run the bot with your Discord bot token
client.run('MTE4Njg1NDczNDE1NDQ0NDkwMA.GW5dHh.xnbtkJhQrsetLeMOkeT2qKniPRRxhsYeevoZrU')
