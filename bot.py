# Import the necessary modules
import discord
import requests

# Define the Discord bot token and the Google API key
TOKEN = "YOUR_BOT_TOKEN"
API_KEY = "YOUR_API_KEY"

# Define the search engine ID for the Google Custom Search API
SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID"

# Create a client object for the Discord bot
client = discord.Client()

# Define the event that is triggered when the bot is ready
@client.event
async def on_ready():
    # Print a message to the console
    print("Bot ready!")

# Define the event that is triggered when a user sends a message
@client.event
async def on_message(message):
    # Check if the message is a command to search for an image
    if message.content.startswith("!image"):
        # Get the search query from the message
        query = message.content.split(" ")[1]

        # Build the URL for the Google Custom Search API
        url = "https://www.googleapis.com/customsearch/v1"
        url += "?key=" + API_KEY
        url += "&cx=" + SEARCH_ENGINE_ID
        url += "&q=" + query
        url += "&searchType=image"
        url += "&num=1"
        url += "&safe=high"
        url += "&fields=items(link)"

        # Send a request to the Google Custom Search API
        response = requests.get(url)

        # Get the first result from the response
        result = response.json()["items"][0]

        # Get the URL of the image
        image_url = result["link"]

        # Send the image to the Discord channel
        await message.channel.send(image_url)

# Start the bot
client.run(TOKEN)
