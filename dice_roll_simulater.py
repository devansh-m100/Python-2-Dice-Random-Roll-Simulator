import tkinter as tk # Here alias is used 'tk' for tkinter
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("900x500")
window.title("Dice Roll")

# def roll_dice():
#     a = random.randint(1, 6)
#     label = tk.Label(window, text = a).pack()


# button = tk.Button(window, text = "click", command = roll_dice)
# button.pack()
dice = ["dice1.png", "dice2.png", "dice3.png", "dice4.png", "dice5.png", "dice6.png"]
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((400, 400), Image.ANTIALIAS))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((400, 400), Image.ANTIALIAS))

label1 = tk.Label(window, image = image1)
label2 = tk.Label(window, image = image2)

# Now here we create function (functionality) for the labe11 and label2

label1.img = label1
label2.img = label2

label1.place(x = 100, y = 150)
label2.place(x = 450, y = 150)

# Button to roll the dice in the Python GUI

def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((400, 400), Image.ANTIALIAS))
    label1.configure(image = image1)
    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((400, 400), Image.ANTIALIAS))
    label2.configure(image = image2)
    label2.image = image2
                                

button = tk.Button(window, text = "ROLL", bg = "#7B3F00", fg = "#FFD700", font = "Times 50 bold", command = dice_roll)
button.place(x= 350, y = 30)
window.mainloop()