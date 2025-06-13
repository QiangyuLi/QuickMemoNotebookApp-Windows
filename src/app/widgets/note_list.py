from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton
from PySide6.QtCore import Signal
from ..models.note import Note
from ..utils.storage import get_all_notes

class NoteList(QWidget):
    note_selected = Signal(Note)
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.refresh_notes()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # Create list widget
        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self.on_note_selected)
        layout.addWidget(self.list_widget)
        
        # Create new note button
        self.new_button = QPushButton("New Note")
        self.new_button.clicked.connect(self.create_new_note)
        layout.addWidget(self.new_button)
        
    def refresh_notes(self):
        self.list_widget.clear()
        notes = get_all_notes()
        for note in notes:
            self.list_widget.addItem(note.title)
            
    def on_note_selected(self, item):
        # Implement note selection logic
        pass
        
    def create_new_note(self):
        # Implement new note creation logic
        pass 