from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizzlerGui:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.quiz_text = self.canvas.create_text(150, 125, width=280, text="This where qs will show up", font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score = Label(text="Score = ", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        cross_img = PhotoImage(file="images/false.png")
        tick_img = PhotoImage(file="images/true.png")
        self.cross = Button(image=cross_img, bg=THEME_COLOR, highlightthickness=0, command=self.check_wrong)
        self.cross.config(padx=20, pady=20)
        self.cross.grid(row=2, column=0)
        self.tick = Button(image=tick_img, bg=THEME_COLOR, highlightthickness=0, command=self.check_right)
        self.tick.config(padx=20, pady=20)
        self.tick.grid(row=2, column=1)

        self.get_next()

        self.window.mainloop()

    def get_next(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_qs():
            self.score.config(text=f"Score = {self.quiz.score}")
            nq = self.quiz.next_qs()
            self.canvas.itemconfig(self.quiz_text, text=nq)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end. Thank you for playing!")
            self.cross.config(state="disabled")
            self.tick.config(state="disabled")

    def check(self, boolean):
        if boolean:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next)

    def check_right(self):
        self.check(self.quiz.check_ans("true"))

    def check_wrong(self):
        self.check(self.quiz.check_ans("false"))

