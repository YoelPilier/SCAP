def To_Minutes(Seconds):
    minutes = int(Seconds // 60)
    seconds = round(Seconds % 60)
    
    return f"{minutes}:{seconds}"
