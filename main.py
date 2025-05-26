from utils.videos_fetcher import fetch_video_metadata

def main():
    keywords = input("Enter keyword (or a list of words separated by commas(,): ").strip()

    videos_list = fetch_video_metadata(keywords)
    print(f"✅ Results: {videos_list}")

if __name__ == '__main__':
    main()