#   _  _    _____       _       _____ _             _ _       
# _| || |_ / ____|     | |     / ____| |           | (_)      
#|_  __  _| (___   ___ | | ___| (___ | |_ _   _  __| |_  ___  
# _| || |_ \___ \ / _ \| |/ _ \\___ \| __| | | |/ _` | |/ _ \ 
#|_  __  _|____) | (_) | | (_) |___) | |_| |_| | (_| | | (_) |
#  |_||_| |_____/ \___/|_|\___/_____/ \__|\__,_|\__,_|_|\___/  

import tkinter as tk

def click_button():
    global number
    number += 1
    show_info["text"] = f"You Clicked {number} times."

def setup_gui():
    root = tk.Tk()
    root.geometry("300x300")
    root.title("#SoloStudio")

    # Disable resizing
    root.resizable(width=False, height=False)

    global number
    number = 0

    clicking_button = tk.Button(root, text="Click Me!", padx=40, pady=40, bg="black", font="sans, 60", command=click_button)
    clicking_button.pack()

    global show_info
    show_info = tk.Label(root, text="Button clicker", font="Arial, 28", fg="red", pady=20)
    show_info.pack()

    root.mainloop()

if __name__ == "__main__":
    setup_gui()

#Developed in 2022 - SoloStudio
#SoloStudio
