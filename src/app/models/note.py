from dataclasses import dataclass
from datetime import datetime
import uuid

@dataclass
class Note:
    id: str
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
    
    @classmethod
    def create_new(cls, title: str = "New Note", content: str = "") -> 'Note':
        now = datetime.now()
        return cls(
            id=str(uuid.uuid4()),
            title=title,
            content=content,
            created_at=now,
            updated_at=now
        ) 