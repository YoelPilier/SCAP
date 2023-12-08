def To_Minutes(Seconds):
    try:
        Seconds=int(Seconds)
        seconds=int(Seconds)
        minutes = int(Seconds // 60)
        seconds = round(Seconds % 60)
    
        return f"{minutes}:{seconds:02d}"
    except Exception as e:
        return "0:00"