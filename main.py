import tkinter as tk

# История ответов
chronology = [None]

# Определить контент истории
content = {
    "Начало": "1937 год. Молодой человек по имени Иван сидел на остановке, ожидая автобус номер 410. Когда автобус наконец прибыл, Иван сел в него и вскоре заснул.\n\n"
              "Проснувшись, Иван обнаружил, что находится в незнакомом месте. Вокруг него возвышались высокие заборы с колючей проволокой, а вдалеке виднелись деревянные бараки. Иван понял, что попал в трудовой лагерь.\n\n"
              "Иван бродил по лагерю, пытаясь понять, как он здесь оказался и как ему вернуться домой. Внезапно его окликнула женщина в форме.\n\n"
              "— Гражданин, почему вы не в рабочей одежде? — спросила она.\n\n",
    "Вариант1": "\tОтвет 1 - Я... я не знаю, — пробормотал Иван.\n",
    "Вариант2": "\tОтвет 2 - Я переоделся, — солгал Иван.\n\n",
    "Ответ1": "Иван не стал слушать голос из шкафа и вместо этого переоделся в рабочую одежду. Однако когда он вышел из барака, его заметила женщина в форме.\n\n"
              "— Гражданин, почему вы не переоделись? — спросила она.\n\n",
    "Вариант1_Ответ1": "\tОтвет 1 - Я переоделся, — солгал Иван.\n",
    "Вариант2_Ответ1": "\tОтвет 2 - Я не обязан вам отвечать, — сказал Иван.\n\n",
    "Ответ2": "Иван переоделся в рабочую одежду, но оставил свои вещи в шкафу. Когда он вышел из барака, женщина в форме не заметила его. Иван бродил по лагерю, пытаясь найти выход.\n\n"
}

# Сохранять историю
story = {"Начала": content["Начало"]}

# Создать главное окно
window = tk.Tk()
window.title("Текстовая новелла")

# Создать текстовое поле для отображения истории
story_text = tk.Text(window, height=20, width=60, wrap="word")
story_text.pack()
story_text.insert(tk.END, content["Начало"])
story_text.insert(tk.END, content["Вариант1"])
story_text.insert(tk.END, content["Вариант2"])

# Создать кнопки для выбора вариантов
option1_button = tk.Button(window, text="Ответ 1")
option1_button.pack()
option2_button = tk.Button(window, text="Ответ 2")
option2_button.pack()
# Создать кнопку для начала заново
restart_button = tk.Button(window, text="Начать заново")
restart_button.pack()

# Определить функцию для обработки выбора варианта
def handle_option_click(option, chronology, story):
    # Обновить текст истории в зависимости от выбранного варианта
    if option == 1:
        if chronology[0] is None:
            chronology[0] = "Ответ1"
            story["Вариант1"] = content["Вариант1"]
        else:
            chronology[0] += "_Ответ1"
            story["Вариант1" + chronology[0]] = content["Вариант1" + chronology[0]]
    elif option == 2:
        if chronology[0] is None:
            chronology[0] = "Ответ2"
            story["Вариант2"] = content["Вариант2"]
        else:
            chronology[0] += "_Ответ2"
            story["Вариант2" + chronology[0]] = content["Вариант2" + chronology[0]]

    story_text.insert(tk.END, content[chronology[0]])
    story[chronology[0]] = content[chronology[0]]

    option1_button.configure(state=tk.NORMAL)
    option2_button.configure(state=tk.NORMAL)

    if not ("Вариант1_" + chronology[0]) in content and not ("Вариант2_" + chronology[0]) in content:
        option1_button.configure(state=tk.DISABLED)
        option2_button.configure(state=tk.DISABLED)
        story_text.insert(tk.END, "Конец!\n")
        # Открытия файла запись и закрытие
        file = open(chronology[0]+".txt", "w")
        for val, key in enumerate(story):
            file.write(story[key])
        file.write("Конец")
        file.close()
    elif not ("Вариант1_" + chronology[0]) in content:
        option1_button.configure(state=tk.DISABLED)
        story_text.insert(tk.END, content["Вариант2_" + chronology[0]])
    elif not ("Вариант2_" + chronology[0]) in content:
        option2_button.configure(state=tk.DISABLED)
        story_text.insert(tk.END, content["Вариант1_" + chronology[0]])
    else:
        story_text.insert(tk.END, content["Вариант1_" + chronology[0]])
        story_text.insert(tk.END, content["Вариант2_" + chronology[0]])

def handle_restart_click():
    # Очистить текстовое поле истории
    story_text.delete("1.0", tk.END)

    # Сбросить историю и хронологию
    chronology[0] = None
    story = {"Начала": content["Начало"]}

    # Вставить начальный текст истории
    story_text.insert(tk.END, content["Начало"])
    story_text.insert(tk.END, content["Вариант1"])
    story_text.insert(tk.END, content["Вариант2"])

    # Активировать кнопки выбора вариантов
    option1_button.configure(state=tk.NORMAL)
    option2_button.configure(state=tk.NORMAL)


# Привязать функцию обработки к кнопкам
option1_button.configure(command=lambda: handle_option_click(1, chronology, story))
option2_button.configure(command=lambda: handle_option_click(2, chronology, story))
restart_button.configure(command=handle_restart_click)

# Запустить главное окно
window.mainloop()
