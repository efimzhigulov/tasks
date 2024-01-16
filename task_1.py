with open("task_1.txt",'w+') as file:
    create_text_1 = file.write("Hello\n\nworld")
    print(create_text_1)


with open("task_1.txt", 'w+') as file:
    clear_task_1 = file.truncate()
    print(clear_task_1)