from datetime import datetime

def isoparse(date_string: str) -> datetime:
    return datetime.fromisoformat(date_string)
