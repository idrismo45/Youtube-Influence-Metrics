# %%
import os
import pandas as pd
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from the environment variable
API_KEY = os.getenv("YOUTUBE_API_KEY")
API_VERSION = 'v3'

# Build the YouTube API client
youtube = build('youtube', API_VERSION, developerKey=API_KEY)

# Function to find channel ID using the search endpoint
def get_channel_id_from_search(youtube, query):
    try:
        request = youtube.search().list(
            part='snippet',
            q=query,
            type='channel',
            maxResults=1
        )
        response = request.execute()

        if 'items' in response and response['items']:
            return response['items'][0]['snippet']['channelId']
        else:
            print(f"No channel ID found for query: {query}")
            return None

    except Exception as e:
        print(f"An error occurred while searching for query: {query} - {e}")
        return None

# Function to get channel statistics using a channel ID
def get_channel_stats(youtube, channel_id):
    try:
        # Make the API request for channel stats
        request = youtube.channels().list(
            part='snippet,statistics',
            id=channel_id
        )
        response = request.execute()

        if 'items' in response and response['items']:
            data = {
                'channel_name': response['items'][0]['snippet']['title'],
                'total_subscribers': response['items'][0]['statistics']['subscriberCount'],
                'total_views': response['items'][0]['statistics']['viewCount'],
                'total_videos': response['items'][0]['statistics']['videoCount'],
            }
            return data
        else:
            print(f"No data found for channel ID: {channel_id}")
            return None

    except Exception as e:
        print(f"An error occurred for channel ID: {channel_id} - {e}")
        return None

# Example usernames (could be loaded from a CSV or input manually)
channel_usernames = ['sidemen', 'juliusdein', 'liverpoolfc', 'sirhcchris2010', 'thedadlab']

# Initialize a list to store channel stats
channel_stats = []

# Loop through each username to get stats using the search method
for username in channel_usernames:
    # Convert username to channel ID using the search method
    channel_id = get_channel_id_from_search(youtube, username)
    if channel_id:
        # Get stats using the channel ID
        stats = get_channel_stats(youtube, channel_id)
        if stats:
            channel_stats.append(stats)

# Convert the list of stats to a DataFrame
stats_df = pd.DataFrame(channel_stats)

# Save the resulting stats to a CSV file
stats_df.to_csv('youtube_channel_stats.csv2', index=False)

# Print the first 10 rows of the DataFrame
print(stats_df.head(10))


