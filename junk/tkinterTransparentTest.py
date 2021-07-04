from tkinter import *
from PIL import ImageTk, Image

main = Tk()
photo = ImageTk.PhotoImage(Image.open("../images/gold.jpg"))

# photo=PhotoImage(file='../images/gold.jpg')

Label(main,image=photo,bg='grey').pack()

#your other label or button or ...
Label(main,text="hello",bg='white', compound='center').place(x=100, y=100)
Label(main,text="there",bg='grey', compound='center').place(x=80, y=80)

# makes that part of the window transparent
# main.wm_attributes("-transparentcolor", 'grey')

main.mainloop()