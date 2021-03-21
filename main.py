# third-party
import tkinter as tk

# modules
from open_quiz import open_quiz


def posthumously_call(window: tk.Tk,
                      callable: callable,
                      *args,
                      **kwargs) -> None:
    def inner():
        window.destroy()
        callable()
    return inner


main_window = tk.Tk(screenName="main")
main_window.geometry("900x600")

go_open_btn = tk.Button(
    text="МОИ ВИКТОРИНЫ",
    background="#006363",  # nice dark blue
    foreground="#ffffff",  # white
    width="256",
    command=posthumously_call(main_window, open_quiz)
)
go_make_btn = tk.Button(
    text="В РАЗРАБОТКЕ",
    background="#006363",  # nice dark blue
    foreground="#ffffff",  # white
    width="256",
    # command=make_quiz
)


go_open_btn.pack()
go_make_btn.pack()
main_window.mainloop()
