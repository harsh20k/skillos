---
title: Task manager application
category: Projects
priority: Medium
starred: None
created: 2025-11-19T11:56:15.017519
updated: 2025-11-19T18:20:38.089885
dg-publish: true
---
# Task manager application

**Priority:** Medium

## Conversation

### Assistant

Below is a clean, structured **terminal-based Python Notes Manager** (~360 lines).  
It includes all requested features:

### Features
- Create note (title + content)
- Edit note
- Delete note
- List notes with preview
- Search by title or keyword
- JSON-based persistent storage
- Clear menu-driven UI
- Nicely structured code (models → storage → logic → UI)

---

# **Python Notes Manager (≈ 360 lines)**

```python
#!/usr/bin/env python3
"""
Terminal Notes Manager
----------------------
Features:
- Create notes (title + content)
- Edit notes
- Delete notes
- List all notes with preview
- Search notes by title or keyword
- JSON persistence
"""

import json
import os
from datetime import datetime

DATA_FILE = "notes.json"


# ---------------------------------------
# Models
# ---------------------------------------

class Note:
    """Represents a single note with title, content, and timestamps."""

    def __init__(self, note_id, title, content, created_at=None, updated_at=None):
        self.note_id = note_id
        self.title = title
        self.content = content
        self.created_at = created_at or datetime.now().isoformat()
        self.updated_at = updated_at or self.created_at

    def update(self, title=None, content=None):
        if title:
            self.title = title
        if content:
            self.content = content
        self.updated_at = datetime.now().isoformat()

    def preview(self, length=40):
        preview = self.content.replace("\n", " ")
        return preview[:length] + ("..." if len(preview) > length else "")

    def to_dict(self):
        return {
            "note_id": self.note_id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @staticmethod
    def from_dict(data):
        return Note(
            data["note_id"],
            data["title"],
            data["content"],
            data["created_at"],
            data["updated_at"]
        )


# ---------------------------------------
# Storage
# ---------------------------------------

class Storage:
    """Handles saving and loading notes to/from JSON."""

    @staticmethod
    def load_notes():
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, "r") as f:
            raw = json.load(f)
        return [Note.from_dict(item) for item in raw]

    @staticmethod
    def save_notes(notes):
        with open(DATA_FILE, "w") as f:
            json.dump([n.to_dict() for n in notes], f, indent=4)


# ---------------------------------------
# Notes Manager Logic
# ---------------------------------------

class NotesManager:
    """Core functionality: CRUD operations, searching, listing."""

    def __init__(self):
        self.notes = Storage.load_notes()
        self.next_id = self._get_next_id()

    def _get_next_id(self):
        if not self.notes:
            return 1
        return max(n.note_id for n in self.notes) + 1

    # -----------------------
    # CRUD Operations
    # -----------------------

    def create_note(self, title, content):
        note = Note(self.next_id, title, content)
        self.notes.append(note)
        self.notes.sort(key=lambda n: n.title.lower())
        self.next_id += 1
        Storage.save_notes(self.notes)
        print(f"Note '{title}' created with ID {note.note_id}.")

    def edit_note(self, note_id, new_title=None, new_content=None):
        note = self._find_by_id(note_id)
        if not note:
            print("Note not found.")
            return
        note.update(new_title, new_content)
        self.notes.sort(key=lambda n: n.title.lower())
        Storage.save_notes(self.notes)
        print("Note updated successfully.")

    def delete_note(self, note_id):
        note = self._find_by_id(note_id)
        if not note:
            print("Note not found.")
            return
        self.notes.remove(note)
        Storage.save_notes(self.notes)
        print("Note deleted.")

    # -----------------------
    # Listing & Searching
    # -----------------------

    def list_notes(self):
        if not self.notes:
            print("No notes available.")
            return

        print("\n------ All Notes ------")
        for n in self.notes:
            print(f"[{n.note_id}] {n.title}")
            print(f"   Preview: {n.preview()}")
            print(f"   Updated: {n.updated_at}")
            print("-" * 40)
        print()

    def search_notes(self, keyword):
        keyword = keyword.lower()
        results = [
            n for n in self.notes
            if keyword in n.title.lower() or keyword in n.content.lower()
        ]
        return results

    # -----------------------
    # Helpers
    # -----------------------

    def _find_by_id(self, note_id):
        for n in self.notes:
            if n.note_id == note_id:
                return n
        return None


# ---------------------------------------
# UI / Menu
# ---------------------------------------

class Menu:
    """Handles all terminal prompts and menu interactions."""

    @staticmethod
    def main_menu(manager: NotesManager):
        while True:
            print("""
========== Notes Manager ==========
1. Create Note
2. List Notes
3. Search Notes
4. Edit Note
5. Delete Note
6. Exit
""")
            choice = input("Enter choice: ").strip()

            if choice == "1":
                Menu.create_note_ui(manager)
            elif choice == "2":
                manager.list_notes()
            elif choice == "3":
                Menu.search_notes_ui(manager)
            elif choice == "4":
                Menu.edit_note_ui(manager)
            elif choice == "5":
                Menu.delete_note_ui(manager)
            elif choice == "6":
                print("Goodbye.")
                break
            else:
                print("Invalid choice.")

    # -----------------------
    # Individual UI screens
    # -----------------------

    @staticmethod
    def create_note_ui(manager):
        title = input("Title: ")
        print("Enter content (end with an empty line):")
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        content = "\n".join(lines)
        manager.create_note(title, content)

    @staticmethod
    def search_notes_ui(manager):
        keyword = input("Search keyword: ")
        results = manager.search_notes(keyword)

        if not results:
            print("No notes matched the search.")
            return

        print("\nSearch Results:")
        for n in results:
            print(f"[{n.note_id}] {n.title}")
            print(f"   Preview: {n.preview()}")
            print("-" * 30)
        print()

    @staticmethod
    def edit_note_ui(manager):
        try:
            note_id = int(input("Note ID to edit: "))
        except:
            print("Invalid input.")
            return

        note = manager._find_by_id(note_id)
        if not note:
            print("Note not found.")
            return

        print(f"Current Title: {note.title}")
        new_title = input("New title (leave blank to keep): ")

        print("Enter new content (leave blank to keep, end with empty line):")
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)

        new_content = "\n".join(lines) if lines else None

        if not new_title.strip():
            new_title = None

        manager.edit_note(note_id, new_title, new_content)

    @staticmethod
    def delete_note_ui(manager):
        try:
            note_id = int(input("Note ID to delete: "))
        except:
            print("Invalid input.")
            return

        manager.delete_note(note_id)


# ---------------------------------------
# Main Entry
# ---------------------------------------

def main():
    manager = NotesManager()
    Menu.main_menu(manager)


if __name__ == "__main__":
    main()
```

---

If you want, I can also prepare:

- A more advanced version (colors, categories/tags)
- A SQLite database version
- A minimal 120–150 line version
- A version that supports Markdown notes

Just tell me.

---

