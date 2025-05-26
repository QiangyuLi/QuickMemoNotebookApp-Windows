import json
import os
from datetime import datetime
from ..models.note import Note

NOTES_DIR = os.path.join(os.path.expanduser("~"), ".quickmemo", "notes")
os.makedirs(NOTES_DIR, exist_ok=True)

def save_note(note: Note) -> None:
    """Save a note to disk."""
    note.updated_at = datetime.now()
    note_path = os.path.join(NOTES_DIR, f"{note.id}.json")
    
    with open(note_path, "w", encoding="utf-8") as f:
        json.dump({
            "id": note.id,
            "title": note.title,
            "content": note.content,
            "created_at": note.created_at.isoformat(),
            "updated_at": note.updated_at.isoformat()
        }, f, ensure_ascii=False, indent=2)

def get_all_notes() -> list[Note]:
    """Load all notes from disk."""
    notes = []
    for filename in os.listdir(NOTES_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(NOTES_DIR, filename), "r", encoding="utf-8") as f:
                data = json.load(f)
                notes.append(Note(
                    id=data["id"],
                    title=data["title"],
                    content=data["content"],
                    created_at=datetime.fromisoformat(data["created_at"]),
                    updated_at=datetime.fromisoformat(data["updated_at"])
                ))
    return sorted(notes, key=lambda x: x.updated_at, reverse=True) 