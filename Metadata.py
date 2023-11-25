import mutagen
 

# Metadata keys
    
TITLE = "title"
ARTIST = "artist"
ALBUM = "album"
YEAR = "year"
DURATION = "duration"


def get_song_info(file,ext ):
    mutagen_file = mutagen.File(file )
    metadata = {'title': 'Unknown', 'artist': 'Unknown', 'album': 'Unknown', 'year': 'Unknown', 'duration': 'Unknown'}
    
    if ext == '.m4a':
        metadata['title'] = mutagen_file.tags['\xa9nam'][0]
        metadata['artist'] = mutagen_file.tags['\xa9ART'][0]
        metadata['album'] = mutagen_file.tags['\xa9alb'][0] 
        metadata['year'] = mutagen_file.tags['\xa9day'][0] 
        metadata['duration'] = mutagen_file.info.length
    elif ext == '.mp3':
        metadata['title'] = mutagen_file.tags['TIT2'][0]
        metadata['artist'] = mutagen_file.tags['TPE2'][0]
        metadata['album'] = mutagen_file.tags['TALB'][0] 
        metadata['year'] = mutagen_file.tags['TDRC'][0] 
        metadata['duration'] = mutagen_file.info.length
    elif ext == '.flac':
        metadata['title'] = mutagen_file.tags['title'][0]
        metadata['artist'] = mutagen_file.tags['artist'][0]
        metadata['album'] = mutagen_file.tags['album'][0] 
        metadata['year'] = mutagen_file.tags['date'][0] 
        metadata['duration'] = mutagen_file.info.length
    return metadata