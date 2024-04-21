from database.database import ManagingNotes
from control_of_notes import Menu


def main():
    db_name = 'database/notes.db'
    # Создаем экземпляр класса ManagingNotes
    notes_manager = ManagingNotes(db_name)
    # Запускаем главное меню приложения
    Menu.start_controller(notes_manager)


# вызываем функцию main для запуска программы
if __name__ == "__main__":
    main()
