import re
import build

def extract_playlist_id(playlist_link):
    # Extract playlist ID from the link
    match = re.search(r"(?<=list=)([a-zA-Z0-9_-]+)", playlist_link)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid playlist link format")


def get_playlist_video_count(playlist_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

    # Get playlist details
    playlist_info = youtube.playlists().list(
        part='contentDetails',
        id=playlist_id
    ).execute()

    # Extract video count from the response
    video_count = int(playlist_info['items'][0]['contentDetails']['itemCount'])

    return video_count


def count_videos_in_playlists(playlist_links):
    for link in playlist_links:
        try:
            playlist_id = extract_playlist_id(link)
            video_count = get_playlist_video_count(playlist_id)
            print(f'The playlist {link} has {video_count} videos.')
        except Exception as e:
            print(f'Error processing playlist {link}: {e}')


if __name__ == '__main__':
    # Replace 'YOUR_API_KEY' with your API key
    API_KEY = 'AIzaSyAICBg9zgsZFyjhEtCSsAPtaZ0l0ospYPo'

    # Replace playlist links with the links you want to process
    playlist_links = [
        'https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg',
        'https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg',
        # Add more playlist links as needed
    ]

    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'

    count_videos_in_playlists(playlist_links)