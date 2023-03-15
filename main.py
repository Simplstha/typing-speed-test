from tkinter import *
import mechanism

word_list = []
L_PINK = "#FFCAC8"
D_PINK = "#FB2576"
L_YELLOW = "#FEFAE0"
TIME = None
FONT_STYLE = "Courier"

word = mechanism.GenerateWord()
text = word.generate_text()
instruction = " Welcome to the Typing Speed Calculator. After pressing the start button random words will show up in " \
              "this box. You will have 60 seconds to type as much words as you can below. After 60 seconds the result" \
              " will show up in this box. The result will be given in CPM or counts per minute and WPM or words per " \
              "minute. Average speed is 40 WPM. See if you can score higher with practice. Good luck!"


# ----------------------------------------- COUNT DOWN & CALCULATE ----------------------------------------------------
def count_down(count):
    global TIME
    global text
    timer_label.config(text=f"Time: {count}")
    if count > 0:
        TIME = window.after(1000, count_down, count - 1)
    if count == 0:
        canvas.itemconfig(text_display, text="")
        in_text = text_box.get(1.0, "end")
        score = word.calculate(text, in_text)
        result = f"Your score is {score} CPM that is {round(score / 5)} WPM!"
        canvas.itemconfig(text_display, text=result, font=(FONT_STYLE, 35, "bold"), fill="green")
        text_box.delete(1.0, "end")


# ------------------------------------------------START TIME----------------------------------------------------------
def start_timer():
    canvas.itemconfig(text_display, text=text, fill="black")
    text_box.focus()
    count_down(60)


# -------------------------------------------- Restart and Quit-------------------------------------------------------
def restart():
    canvas.itemconfig(text_display, text=instruction, font=(FONT_STYLE, 20, "bold"), fill=D_PINK)
    timer_label.config(text="Time: 60 ")


def quit_game():
    window.destroy()


# ------------------------------------------------ UI SETUP -----------------------------------------------------------
window = Tk()
window.config(padx=40, pady=40, bg=L_PINK)
window.title("Typing Speed Calculator")

timer_label = Label(bg=D_PINK, fg="white", text="Time: 60 ", font=(FONT_STYLE, 25, "bold"))
timer_label.grid(column=2, row=0, columnspan=2)

canvas = Canvas(width=1200, height=350, bg=L_YELLOW)
text_display = canvas.create_text(600, 200, text=instruction, width=1100, font=(FONT_STYLE, 20, "bold"), fill=D_PINK)
canvas.grid(column=0, row=1, columnspan=6)

text_box = Text(height=10, width=150)
text_box.grid(column=0, row=2, columnspan=6)

start_button = Button(fg="white", bg=D_PINK, text="Start Typing", font=(FONT_STYLE, 15, "normal"), command=start_timer)
start_button.grid(row=3, column=2, columnspan=2)

restart_button = Button(fg="white", bg=D_PINK, text="Restart", font=(FONT_STYLE, 15, "normal"), command=restart)
restart_button.grid(row=3, column=0)

quit_button = Button(fg="white", bg=D_PINK, text="Quit", font=(FONT_STYLE, 15, "normal"), command=quit_game)
quit_button.grid(row=3, column=5)

window.mainloop()
