import os

def extract_info(file_name):
    # Assuming the file name is formatted as <songname> - <contributingartist>
    parts = os.path.splitext(file_name)[0].split(' - ')
    song_name = parts[0]
    artist = parts[1] if len(parts) == 2 else None
    return song_name, artist

def process_folder(folder_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as output:
        for file_name in os.listdir(folder_path):
            if file_name.lower().endswith(('.mp3', '.m4a', '.wav')):
                song_name, artist = extract_info(file_name)
                output.write(f"{song_name} - {artist}\n")

# Replace 'path_to_your_folder' with the actual path to your folder
folder_path = 'put songs folder path here'
output_file = 'songs_list.txt'

process_folder(folder_path, output_file)


