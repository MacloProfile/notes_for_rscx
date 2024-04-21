import sqlite3
from crypto import CryptoManager


class ManagingNotes:
    def __init__(self, db_name):
        """Соединяется с базой данных SQLite, создает курсор и таблицу с именем db_name"""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.key_path = "encryption_key.key"
        self.crypto_manager = CryptoManager(self.key_path)
        self._create_table()

    def _create_table(self):
        """Создает таблицу notes, если она не существует"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                text TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_note(self, title, content):
        """Добавляет новую заметку в базу данных."""
        # Шифруем контент перед добавлением
        encrypted_content = self.crypto_manager.encrypt_text(content)
        self.cursor.execute('''
            INSERT INTO notes (title, text) VALUES (?, ?)
        ''', (title, encrypted_content))
        self.conn.commit()

    def get_all_notes(self):
        """Возвращает список всех заметок из базы данных (id, title, content)."""
        self.cursor.execute('''
            SELECT * FROM notes
        ''')
        notes = self.cursor.fetchall()
        # Дешифруем контент перед возвратом
        decrypted_notes = [(note[0],
                            note[1],
                            self.crypto_manager.decrypt_text(note[2])) for note in notes]
        return decrypted_notes

    def search_notes(self, keyword):
        """Возвращает заметки по ключевому слову в заголовке"""
        self.cursor.execute('''
            SELECT * FROM notes WHERE title LIKE ?
        ''', ('%' + keyword + '%',))
        notes = self.cursor.fetchall()
        # Дешифруем контент перед возвратом
        decrypted_notes = [(note[0],
                            note[1],
                            self.crypto_manager.decrypt_text(note[2])) for note in notes]
        return decrypted_notes

    def remove_note(self, note_id):
        """Удаляет заметку с указанным номером
         из базы данных и возвращает результат"""
        self.cursor.execute('''
            DELETE FROM notes WHERE id=?
        ''', (note_id,))
        self.conn.commit()

        if self.cursor.rowcount == 0:
            return "Нет такой записи."
        else:
            return "Заметка успешно удалена!"

    def close_database_connection(self):
        """Закрывает соединение с базой данных."""
        self.conn.close()
