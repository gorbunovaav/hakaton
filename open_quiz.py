# boult-in
import json
from functools import partial

# third-party
import tkinter as tk

# modules
from main import play_quiz


def open_quiz() -> None:
    root = tk.Tk()
    root.geometry("300x400")

    with open("quizes.json", "r") as file:
        quizes_str = file.read()
        for quiz_theme in json.loads(quizes_str):
            button = tk.Button(text=quiz_theme,
                               background="#006363",  # nice dark blue
                               foreground="#ffffff",  # white
                               width="256",
                               command=partial(open_chosen_quiz,
                                               root=root,
                                               quiz_theme=quiz_theme)
                               )
            button.pack()
    root.mainloop()


def open_chosen_quiz(root: tk.Tk,
                     quiz_theme: str):
    root.destroy()
    play_quiz(quiz_theme)


if __name__ == "__main__":
    open_quiz()
