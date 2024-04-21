class Menu:
    @staticmethod
    def start_controller(notes_manager):
        while True:
            # Выводим меню
            print("\n1. Добавить заметку")
            print("2. Просмотреть все заметки")
            print("3. Поиск заметок")
            print("4. Удалить заметку")
            print("5. Выход")

            # Запрашиваем выбор пользователя
            choice = input("Выберите действие: ")

            # Обрабатываем выбор пользователя с помощью match case
            match choice:
                case '1':  # Добавить заметку
                    title = input("Введите заголовок: ")
                    content = input("Введите содержание: ")
                    notes_manager.add_note(title, content)
                    print("Заметка успешно добавлена!")
                case '2':  # Просмотреть все заметки
                    notes = notes_manager.get_all_notes()
                    if notes:
                        for note in notes:
                            print(f"№{note[0]}"
                                  f" Заголовок: {note[1]};"
                                  f" Содержание: {note[2]}")
                    else:
                        print("Заметок пока нет.")
                case '3':  # Поиск заметок
                    keyword = input("Введите ключевое слово для поиска: ")
                    found_notes = notes_manager.search_notes(keyword)
                    if found_notes:
                        for note in found_notes:
                            print(f"№{note[0]}"
                                  f" Заголовок: {note[1]};"
                                  f" Содержание: {note[2]}")
                    else:
                        print("Заметки не найдены.")
                case '4':  # Удалить заметку
                    note_id = input("Введите номер заметки, которую хотите удалить: ")
                    message = notes_manager.remove_note(note_id)
                    print(message)
                case '5':  # Выход
                    print("Работа программы завершена")
                    notes_manager.close_database_connection()
                    break
                case _:  # Неправильный выбор
                    print("Неверный выбор. Пожалуйста, выберите существующий пункт меню.")
