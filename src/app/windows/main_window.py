from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from ..widgets.note_editor import NoteEditor
from ..widgets.note_list import NoteList
from ..utils.shortcuts import setup_shortcuts

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuickMemo Notebook")
        self.setMinimumSize(800, 600)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Initialize components
        self.note_list = NoteList()
        self.note_editor = NoteEditor()
        
        # Add widgets to layout
        layout.addWidget(self.note_list)
        layout.addWidget(self.note_editor)
        
        # Setup keyboard shortcuts
        setup_shortcuts(self)
        
        # Connect signals
        self.note_list.note_selected.connect(self.note_editor.load_note)
        self.note_editor.note_saved.connect(self.note_list.refresh_notes) 