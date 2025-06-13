from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QShortcut

def setup_shortcuts(window):
    # New note shortcut (Ctrl+N)
    new_note_shortcut = QShortcut(QKeySequence("Ctrl+N"), window)
    new_note_shortcut.activated.connect(window.note_list.create_new_note)
    
    # Save note shortcut (Ctrl+S)
    save_note_shortcut = QShortcut(QKeySequence("Ctrl+S"), window)
    save_note_shortcut.activated.connect(window.note_editor.save_note)
    
    # Search notes shortcut (Ctrl+F)
    search_shortcut = QShortcut(QKeySequence("Ctrl+F"), window)
    search_shortcut.activated.connect(window.show_search)
    
    # Toggle dark mode shortcut (Ctrl+D)
    dark_mode_shortcut = QShortcut(QKeySequence("Ctrl+D"), window)
    dark_mode_shortcut.activated.connect(window.toggle_dark_mode)
    
    # Quick access menu shortcut (Ctrl+Q)
    quick_access_shortcut = QShortcut(QKeySequence("Ctrl+Q"), window)
    quick_access_shortcut.activated.connect(window.show_quick_access) 