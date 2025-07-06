
# Last.FM m3u Filter

This project is a simple Python script that filters out scrobbled music tracks from your Last.fm history and matches them with tracks listed in an M3U playlist file. It generates a new M3U file that only contains the tracks that have been scrobbled according to your Last.fm data.

## Files in the Project:

- `filter_scrobbled_tracks.py` - The Python script that performs the filtering.
- `last.fm.csv` - Your exported Last.fm listening history. You can download it from [here](https://lastfm.ghan.nl/export/) or [here](https://mainstream.ghan.nl/export.html), or other sources.
- `all_music.m3u` - The M3U playlist file that contains all the music tracks.
- `requirements.txt` - The file listing the required Python packages for this project.
- `scrobbled_only.m3u` - The output M3U playlist file, which contains only scrobbled tracks.
- `README.md` - This file.

## How to Use:

1. Download your Last.fm listening history as a CSV file from [here](https://lastfm.ghan.nl/export/) or from the provided links.

2. Ensure you have Python installed and the required libraries. You can install them by running:

   ```
   pip install -r requirements.txt
   ```

3. Place the downloaded `last.fm.csv` file and the `all_music.m3u` file in the same directory as the script.

4. Run the Python script:

   ```
   python filter_scrobbled_tracks.py
   ```

5. After the script completes, it will generate a new M3U file called `scrobbled_only.m3u` containing only the tracks that are present in your Last.fm scrobbled history.

## Requirements:

- Python 3.x
- Mutagen library (for handling MP3 tags)
- CSV library (for reading Last.fm CSV export)

You can install the required libraries using the `requirements.txt` file.

## Notes:

- Ensure that the `last.fm.csv` and `all_music.m3u` are in the correct format and properly encoded. The script currently supports Latin-1 encoding.
- The script matches tracks by comparing the artist and title, so ensure that these are correct in both the CSV and M3U files.
- If a track is missing metadata or can't be read, it will be skipped.

## License:

This project is open source and free to use. Feel free to fork and contribute!