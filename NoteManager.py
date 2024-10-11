import json
from Note import Note

class NoteManager:
    def __init__(self, file_name='notes.json'):
        self.file_name = file_name
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.file_name, 'r') as file:
                notes_data = json.load(file)
                return [Note.from_dict(note) for note in notes_data]
        except FileNotFoundError:
            return []

    def save_notes(self):
        with open(self.file_name, 'w') as file:
            json.dump([note.to_dict() for note in self.notes], file, indent=4)

    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        note = Note(note_id, title, body)
        self.notes.append(note)
        self.save_notes()

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        return None

    def delete_note_by_id(self, note_id):
        self.notes = [note for note in self.notes if note.note_id != note_id]
        self.save_notes()

    def edit_note_by_id(self, note_id, title=None, body=None):
        note = self.get_note_by_id(note_id)
        if note:
            note.update(title, body)
            self.save_notes()

    def get_notes_by_date(self, date):
        return [note for note in self.notes if note.timestamp.startswith(date)]

    def list_notes(self):
        return self.notes
