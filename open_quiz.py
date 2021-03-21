# boult-in
import json
from functools import partial

# third-party
import tkinter as tk

# modules
from play_quiz import play_quiz


def open_quiz() -> None:
    open_qz_window = tk.Tk()
    open_qz_window.geometry("300x400")

    with open("quizes.json", "r") as file:
        quizes_str = file.read()
        for quiz_theme in json.loads(quizes_str):
            button = tk.Button(
                text=quiz_theme,
                background="#006363",  # nice dark blue
                foreground="#ffffff",  # white
                width="256",
                command=partial(
                    open_chosen_quiz,
                    window=open_qz_window,
                    quiz_theme=quiz_theme
                    )
                )
            button.pack()
    open_qz_window.mainloop()


def open_chosen_quiz(window: tk.Tk,
                     quiz_theme: str):
    window.destroy()
    play_quiz(quiz_theme)


if __name__ == "__main__":
    open_quiz()
