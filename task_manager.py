tasks = []
while True:
    command = input("> ")
    if command == "exit":
        break
    elif command == "list":
        if len(tasks) == 0:
            print("Задач нет")
        else:
            for i in range(len(tasks)):
                print(i,":", tasks[i])
    elif command.startswith("add "):
        text = command[4:]
        tasks.append(text)
    elif command.startswith("delete "):
        index_str = command[7:]

        if index_str.isdigit():
            index = int(index_str)

            if index < len(tasks):
                tasks.pop(index)
                print("Задача удалена")
            else:
                print("Ошибка: неверный индекс")
        else:
            print("Ошибка: нужно число")
    else:
        print("Неверная команда")
