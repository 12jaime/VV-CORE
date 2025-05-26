from yt_dlp import YoutubeDL

def fetch_video_metadata(keywords, max_videos=10):
    """
    Fetches video metadata for a list of keywords.

    Args:
        keywords (str): Comma-separated string of keywords.
        max_videos (int): Maximum number of videos to fetch per keyword.

    Returns:
        list: A list of video URLs.
    """
    url_list = []
    # Split the input string by commas and strip whitespace
    keyword_list = [kw.strip() for kw in keywords.split(',') if kw.strip()]

    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'extract_flat': True  # Extract metadata without downloading
    }

    with YoutubeDL(ydl_opts) as ydl:
        for keyword in keyword_list:
            search_query = f"ytsearch{max_videos}:{keyword}"
            try:
                search_results = ydl.extract_info(search_query, download=False)
                for entry in search_results.get('entries', []):
                    video_url = f"https://www.youtube.com/watch?v={entry.get('id')}"
                    url_list.append(video_url)
                    title = entry.get('title')
                    channel = entry.get('uploader')
                    published_at = entry.get('upload_date')
                    views = entry.get('view_count')
                    # Attempt to extract like_count from nested structures
                    like_count = None
                    if 'like_count' in entry:
                        like_count = entry.get('like_count')
                    elif 'topLevelButtons' in entry:
                        for button in entry['topLevelButtons']:
                            if 'likeButtonRenderer' in button:
                                like_count = button['likeButtonRenderer'].get('likeCount', None)

                    print(f"🎬 Title       : {title}")
                    print(f"📺 Channel     : {channel}")
                    print(f"📅 Published   : {published_at}")
                    print(f"👁️ Views      : {views}")
                    print(f"👍 Likes       : {like_count}")
                    print(f"🔗 URL         : {video_url}")
                    print("-" * 60)
            except Exception as e:
                print(f"❌ Error fetching data for keyword '{keyword}': {e}")
    return url_list

# Example usage
if __name__ == "__main__":
    keywords = input("Enter keywords (comma-separated): ").strip()
    video_urls = fetch_video_metadata(keywords)
    print("✅ Video URLs:")
    for url in video_urls:
        print(url)
