from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_icon.config(text="")
    global reps
    reps = 0

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    reps += 1
    # print(reps)
    if reps in (1, 3, 5, 7):
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    elif reps in (2, 4, 6):
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    elif reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
# ---------------------------- UI SETUP ------------------------------- #
def count_down(count):
    global timer
    count_min = count // 60
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec:02d}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 != 0:
            check_str = int(reps/2) * "✔"
            print(check_str)
            check_icon.config(text=check_str)

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_btn = Button(text="Start", padx=10, highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", padx=10, highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

check_icon = Label(fg=GREEN, font=(FONT_NAME, 12, "normal"), bg=YELLOW)
check_icon.grid(column=1, row=3)


window.mainloop()