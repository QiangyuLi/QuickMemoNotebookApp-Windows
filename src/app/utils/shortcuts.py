from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QShortcut
from ..windows.main_window import MainWindow

def setup_shortcuts(window: MainWindow) -> None:
    """Setup keyboard shortcuts for the main window."""
    # New note shortcut
    new_note_shortcut = QShortcut(QKeySequence("Ctrl+N"), window)
    new_note_shortcut.activated.connect(window.note_list.create_new_note)
    
    # Save note shortcut
    save_note_shortcut = QShortcut(QKeySequence("Ctrl+S"), window)
    save_note_shortcut.activated.connect(window.note_editor.save_note)
    
    # Search notes shortcut
    search_shortcut = QShortcut(QKeySequence("Ctrl+F"), window)
    search_shortcut.activated.connect(window.note_list.show_search)
    
    # Toggle dark mode shortcut
    dark_mode_shortcut = QShortcut(QKeySequence("Ctrl+D"), window)
    dark_mode_shortcut.activated.connect(window.toggle_dark_mode)
    
    # Quick access menu shortcut
    quick_access_shortcut = QShortcut(QKeySequence("Ctrl+Q"), window)
    quick_access_shortcut.activated.connect(window.show_quick_access_menu) 