from PySide5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton
from PySide5.QtCore import Signal
from ..models.note import Note
from ..utils.storage import save_note

class NoteEditor(QWidget):
    note_saved = Signal()
    
    def __init__(self):
        super().__init__()
        self.current_note = None
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # Create text editor
        self.editor = QTextEdit()
        self.editor.textChanged.connect(self.auto_save)
        layout.addWidget(self.editor)
        
        # Create save button
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_note)
        layout.addWidget(self.save_button)
        
    def load_note(self, note: Note):
        self.current_note = note
        self.editor.setText(note.content)
        
    def save_note(self):
        if self.current_note:
            self.current_note.content = self.editor.toPlainText()
            save_note(self.current_note)
            self.note_saved.emit()
            
    def auto_save(self):
        # Implement auto-save logic here
        pass 