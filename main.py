from NoteManager import NoteManager

def main():
    manager = NoteManager()

    while True:
        print("\nКоманды: add, list, edit, delete, find, exit")
        command = input("Введите команду: ")

        if command == "add":
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            manager.add_note(title, body)
            print("Заметка добавлена.")
        
        elif command == "list":
            notes = manager.list_notes()
            if notes:
                for note in notes:
                    print(f"[{note.note_id}] {note.title} - {note.timestamp}")
            else:
                print("Заметок пока нет.")

        elif command == "edit":
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок (или оставьте пустым для сохранения прежнего): ")
            body = input("Введите новый текст заметки (или оставьте пустым для сохранения прежнего): ")
            manager.edit_note_by_id(note_id, title, body)
            print("Заметка обновлена.")

        elif command == "delete":
            note_id = int(input("Введите ID заметки для удаления: "))
            manager.delete_note_by_id(note_id)
            print("Заметка удалена.")
        
        elif command == "find":
            date = input("Введите дату в формате YYYY-MM-DD: ")
            notes = manager.get_notes_by_date(date)
            if notes:
                for note in notes:
                    print(f"[{note.note_id}] {note.title} - {note.timestamp}")
            else:
                print("Заметок на эту дату нет.")
        
        elif command == "exit":
            print("Программа завершена.")
            break
        
        else:
            print("Неизвестная команда, попробуйте снова.")

if __name__ == "__main__":
    main()
