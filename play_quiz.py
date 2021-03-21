# built-in
import json
import time

# third-party
import tkinter as tk
from tkinter import messagebox


class play_quiz():
    def __init__(self, quiz_theme: str):
        self.right_answer_count: int = 0
        self.root_destroyed: bool = False
        self.quiz: dict = self._get_quiz(quiz_theme)
        self._play_quiz()
    
    def _get_quiz(self, quiz_theme: str) -> dict:
        with open("quizes.json", "r") as file:
            text = file.read()
            quiz = json.loads(text)[quiz_theme]
        return quiz
    
    def _get_command(self, is_right_index: bool) -> callable:
        def inner() -> None:
            if is_right_index:
                self.right_answer_count += 1
            self.root_destroyed: bool = True
            self.play_qz_window.destroy()
        return inner

    def _tell_results(self,
                     quiz: dict
                    ) -> None:
        """
        def tell_results(self,
                         quiz: dict
                        ) -> None
        """
        all_options_count = len(quiz)
        messagebox.showinfo(
            "ваш результат",  # window name
            "{}%".format(  # window text
                round(100 * (self.right_answer_count / all_options_count), 1)
            )
        )

    def _play_question(self,
                      index: int,
                      question: int,
                      options: dict
                      ) -> None:
            self.play_qz_window = tk.Tk()  # !!! determining main window
            self.play_qz_window.geometry("900x600") # !!!

            question_label = tk.Label(self.play_qz_window,
                                      text=f"{question} (?{index+1})"
                                     )
            option_btns = [tk.Button(self.play_qz_window,
                           text=option,
                           background="#006363",  # nice dark blue
                           foreground="#ffffff",  # white
                           width="256",
                           command=self._get_command(is_right))

                           for option, is_right
                           in options.items()
                           ]
            # packing stuff
            question_label.pack()
            for button in option_btns:
                button.pack()
            self.play_qz_window.mainloop()
            # done with packing stuff

    def _play_quiz(self) -> tuple:
        # options: dict
        for index, (question, options)\
            in enumerate(self.quiz.items()):
            self._play_question(index, question, options)


            # to not start next question until button clicked
            while not self.root_destroyed:
                time.sleep(1)
        self._tell_results(self.quiz)

if __name__ == "__main__":
    with open("quizes.json", "r") as file:
        names = json.loads(file.read()).keys()
    print(*names, sep="\n")
    while True:
        choice = input()
        if choice in names:
            break
    play_quiz(choice)
