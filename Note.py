from datetime import datetime

class Note:
    def __init__(self, note_id, title, body):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def update(self, title=None, body=None):
        if title:
            self.title = title
        if body:
            self.body = body
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def to_dict(self):
        return {
            'id': self.note_id,
            'title': self.title,
            'body': self.body,
            'timestamp': self.timestamp
        }

    @staticmethod
    def from_dict(note_dict):
        note = Note(
            note_id=note_dict['id'],
            title=note_dict['title'],
            body=note_dict['body']
        )
        note.timestamp = note_dict['timestamp']
        return note
