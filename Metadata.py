import mutagen
 

# Metadata keys
    
TITLE = "title"
ARTIST = "artist"
ALBUM = "album"
YEAR = "year"
DURATION = "duration"
INDEX = "index"


def get_song_info(file,ext ):
    mutagen_file = mutagen.File(file )
    metadata = {'title': 'Unknown', 'artist': 'Unknown', 'album': 'Unknown', 'year': 'Unknown', 'duration': 'Unknown'}
    if mutagen_file is None or not mutagen_file.tags:
        return metadata
    if ext == '.m4a' or ext == '.mp4':
        if '\xa9nam' in mutagen_file.tags:
            metadata['title'] = mutagen_file.tags['\xa9nam'][0]
        if '\xa9ART' in mutagen_file.tags:
            metadata['artist'] = mutagen_file.tags['\xa9ART'][0]
        if '\xa9alb' in mutagen_file.tags:
            metadata['album'] = mutagen_file.tags['\xa9alb'][0]
        if '\xa9day' in mutagen_file.tags:
            metadata['year'] = mutagen_file.tags['\xa9day'][0]
        metadata['duration'] = mutagen_file.info.length
    elif ext == '.mp3':
        if 'TIT2' in mutagen_file.tags:
            metadata['title'] = mutagen_file.tags['TIT2'][0]
        if 'TPE1' in mutagen_file.tags:
            metadata['artist'] = mutagen_file.tags['TPE1'][0]
        elif 'TPE2' in mutagen_file.tags:
            metadata['artist'] = mutagen_file.tags['TPE2'][0]
        if 'TALB' in mutagen_file.tags:
            metadata['album'] = mutagen_file.tags['TALB'][0]
        if 'TDRC' in mutagen_file.tags:
            metadata['year'] = mutagen_file.tags['TDRC'][0]
        metadata['duration'] = mutagen_file.info.length
    elif ext == '.flac':
        if 'title' in mutagen_file.tags:
            metadata['title'] = mutagen_file.tags['title'][0]
        if 'artist' in mutagen_file.tags:
            metadata['artist'] = mutagen_file.tags['artist'][0]
        if 'album' in mutagen_file.tags:
            metadata['album'] = mutagen_file.tags['album'][0]
        if 'date' in mutagen_file.tags:
            metadata['year'] = mutagen_file.tags['date'][0]
        metadata['duration'] = mutagen_file.info.length
    return metadata