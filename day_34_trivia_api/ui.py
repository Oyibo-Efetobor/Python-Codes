from tkinter import * 
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface: 
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(
            padx=20,
            pady=20,
            bg=THEME_COLOR
            )
        
        self.score_label = Label(
            text="Score : 0", 
            fg="white", 
            bg=THEME_COLOR
            )
        self.score_label.grid(row=0, column=3)
        
        self.canvas = Canvas(
            width=300, 
            height=250, 
            bg="white"
            )
        self.canvas.grid(row=1, column=1, pady=50, columnspan=2)
        
        self.question_text = self.canvas.create_text(
            150,
            125,
            width= 280,
            text="Some Question Text", 
            fill =THEME_COLOR,
            font = ("Arial", 15, "italic")
            )
        
        true_image = PhotoImage(file="images/true.png")
        self.true_button =Button(
            image=true_image,
            highlightthickness=0
        )
        self.true_button.grid(row=2, column=1)
        
        false_image = PhotoImage(file="images/false.png")
        self.true_button =Button(
            image=false_image,
            highlightthickness=0
        )
        self.true_button.grid(row=2, column=2)
        
        self.get_next_question()
        
        self.window.mainloop()
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)