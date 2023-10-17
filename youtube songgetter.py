import os

def read_songs_from_file(file_path):
    songs = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(' - ')
            if len(parts) == 2:
                songs.append((parts[0], parts[1]))
    return songs

def get_user_input(song_name, artist):
    print(f"Search for '{song_name} - {artist}' on YouTube.")
    youtube_link = input("Enter the YouTube link for the song (or press Enter to skip): ")
    return youtube_link

def process_songs(songs):
    with open('youtube_links.txt', 'w', encoding='utf-8') as output:
        for song in songs:
            song_name, artist = song
            youtube_link = get_user_input(song_name, artist)
            if youtube_link:
                output.write(f"{song_name} - {artist}: {youtube_link}\n")

# Replace 'path_to_your_file.txt' with the actual path to your text file
file_path = 'songs_list.txt'
songs_to_search = read_songs_from_file(file_path)

process_songs(songs_to_search)
