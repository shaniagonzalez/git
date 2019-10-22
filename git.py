import random
import tkinter as tk
window = tk.Tk()

window.title("Is That Really Your Friend???!!!")

window.geometry("400x400")


def phrase_generator():
   phrases = ["are best friends!", "  will make it", " should get together..*wink wink*... ", " will kill each "
                                                                                                    "other",
              "better off apart" ]

   name = str(entry_field1.get())
   name2 = str(entry_field2.get())
   return name + " and " + name2 +  phrases[random.randint(0, 3)]


def phrase_display():

   response = phrase_generator()

   response_calculator = tk.Text(master=window, height=5, width=30)
   response_calculator.grid(column=0, row=5)
   response_calculator.insert(tk.END, response)


title = tk.Label(text="Hey girl, what's your name? :")
title.grid(column=0, row=0)

entry_field1 = tk.Entry()
entry_field1.grid(column=0, row=1)

title2 = tk.Label(text="Do You ACTUALLY have friends? Whats their name? :")
title2.grid(column=0, row=2)

entry_field2 = tk.Entry()
entry_field2.grid(column=0, row=3)


button1 = tk.Button(text="Click me!", command=phrase_display)
button1.grid(column=0, row=4)

window.mainloop()
