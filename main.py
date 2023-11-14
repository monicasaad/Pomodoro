# import required modules
from tkinter import *

# constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_countdown, text="00:00")
    check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        countdown(work_secs)
        title_label.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        countdown(long_break_secs)
        title_label.config(text="30-Break", fg=RED)
    else:
        countdown(short_break_secs)
        title_label.config(text="5-Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes = count // 60
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_countdown, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(reps//2):
            mark += "✔"
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
# create screen window
window = Tk()
window.title("Pomodoro") # fun fact "pomodoro" means tomato in Italian!
window.config(padx=100, pady=50, bg=YELLOW) # adjust window size/ padding and colour

# title label
title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW) #fg changes colour
title_label.grid(row=0, column=1)

# buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# canvas to add background image
canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0) # size, background colour, remove canvas outline
# read in tomato image to create photo Image object to input into create_image method
tomato = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=tomato) # place in center of canvas
timer_countdown = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")) # x pos, y pos, text
canvas.grid(row=0, column=1)

# checkmarks label
check_marks = Label(text="", fg=GREEN, font=(FONT_NAME, 15), bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()
