# built-in
import json
from functools import partial

# third-party
import tkinter as tk

class add_quiz:
    def __init__(self):
        self.quiz_theme: str
        self.quiz: dict = {}
        self.make_window()

    def make_window(self):
        self.add_qz_window = tk.Tk() # !!! window
        self.add_qz_window.geometry("900x600") # !!!

        self.question = tk.Entry(
            self.add_qz_window,
            width=256
            )
        self.entry_options_list = [
            tk.Entry(
                self.add_qz_window,
                width="256"
                )
            for i in
            range(1, 4+1)
            ]
        self.right_option_entry = tk.Entry(
            self.add_qz_window,
            width="256"
            )
        self.add_question_btn = tk.Button(
            self.add_qz_window,
            text="ДОБАВИТЬ ВОПРОС",
            background="#36d88a", # nice light green
            foreground="#000000", # black
            width="256",
            command=partial(
                self.add_question,
                self.add_qz_window,
                self.question,
                self.entry_options_list,
                self.right_option_entry
                )
            )
        self.done_quiz_btn = tk.Button(
            self.add_qz_window,
            text="ЗАКОНЧИТЬ ВИКТОРИНУ",
            background="#3aaacf", # nice light blue
            foreground="#000000", # black
            width="256",
            command=partial(
                self.done_quiz,
                self.add_qz_window
                )
            )
        # packing stuff
        self.question.pack()
        self.question.insert(0, "вопрос")
        for i, entry_option in enumerate(self.entry_options_list):
            entry_option.pack()
            entry_option.insert(0, "{} вариант ответа".format(i+1))

        self.right_option_entry.pack()
        self.right_option_entry.insert(0, "номер правильного ответа")
        self.add_question_btn.pack()
        self.done_quiz_btn.pack()
        self.add_qz_window.mainloop()

    def add_question(self,
                     window: tk.Tk,
                     question: tk.Entry,
                     entry_options_list: list,
                     right_option_entry: tk.Entry
                     ) -> None:
        question_txt = question.get()
        txt_options_list = [
            option.get()
            for option in entry_options_list
            ]
        right_option_index = int(right_option_entry.get()) - 1
        window.destroy()
        self.quiz[question_txt] = {
            option: txt_options_list.index(option) == right_option_index
            for option in txt_options_list
        }
        self.make_window()
    
    def done_quiz(self,
                  window: tk.Tk
                  ) -> None:
        window.destroy()

        self.final_window = tk.Tk()
        self.final_window.geometry("300x300")
        self.quiz_theme_entry = tk.Entry(
            self.final_window,
            width="256"
            )
        self.done_btn = tk.Button(
            self.final_window,
            text="ГОТОВО",
            background="#00b945", # nice green
            foreground="#ffffff", # white
            width="256",
            command=partial(
                self.done_adding,
                self.final_window,
                self.quiz_theme_entry
                )
            )
        # packing
        self.quiz_theme_entry.pack()
        self.done_btn.pack()
        self.quiz_theme_entry.insert(0, "название викторины")
        self.final_window.mainloop()

    def done_adding(self,
                    window: tk.Tk,
                    quiz_theme_entry: tk.Entry
                    ) -> None:
        self.quiz_theme = quiz_theme_entry.get()
        window.destroy()
        self.update_json(
            self.quiz_theme,
            self.quiz
            )

    def update_json(self,
                    quiz_theme: str,
                    quiz: dict
                    ) -> None:
        with open("quizes.json", "r") as  file:
            json_object = json.load(file)
            json_object[quiz_theme] = quiz

        with open("quizes.json", "w") as file:
            json.dump(json_object, file)

if __name__ == "__main__":
    add_quiz()
