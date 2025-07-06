import csv
import os
import re
from mutagen import File as MutagenFile
from mutagen.easyid3 import EasyID3

LASTFM_CSV = "last.fm.csv"
INPUT_M3U = "all_music.m3u"
OUTPUT_M3U = "scrobbled_only.m3u"

scrobbled_tracks = set()

with open(LASTFM_CSV, "r", encoding="latin1") as f:
    reader = csv.DictReader(f)
    for row in reader:
        artist = row["artist"].strip().lower()
        title = row["track"].strip().lower()
        scrobbled_tracks.add((artist, title))

matched_files = []

def extract_from_filename(path):
    filename = os.path.basename(path)
    filename = os.path.splitext(filename)[0]

    filename = re.sub(r'^\d{2}(-\d{2})?\s+', '', filename)

    parts = filename.split(" - ", 1)
    if len(parts) == 2:
        artist = parts[0].strip().split(",")[0].lower()
        title = parts[1].strip().lower()
        return artist, title
    return "", ""

with open(INPUT_M3U, "r", encoding="latin1") as f:
    for line in f:
        path = line.strip()
        if not os.path.isfile(path):
            continue

        artist_first = ""
        title = ""

        try:
            tags = EasyID3(path)
            artist_raw = tags.get("artist", [""])[0].strip().lower()
            title = tags.get("title", [""])[0].strip().lower()
            artist_first = artist_raw.split(";")[0].split(",")[0].strip()
        except Exception:
            try:
                audio = MutagenFile(path, easy=True)
                if audio:
                    artist_raw = audio.get("artist", [""])[0].strip().lower()
                    title = audio.get("title", [""])[0].strip().lower()
                    artist_first = artist_raw.split(";")[0].split(",")[0].strip()
            except Exception:
                pass

        if not artist_first or not title:
            artist_first, title = extract_from_filename(path)

        if artist_first and title:
            if (artist_first, title) in scrobbled_tracks:
                print(f"Match: {artist_first} - {title}")
                matched_files.append(path)
            else:
                print(f"No match: {artist_first} - {title}")
        else:
            print(f"Missing data: {path}")

with open(OUTPUT_M3U, "w", encoding="latin1") as f:
    for filepath in matched_files:
        f.write(filepath + "\n")

print(f"\nNumber of scrobbled tracks: {len(scrobbled_tracks)}")
print(f"Done: {len(matched_files)} file saved here: {OUTPUT_M3U}")