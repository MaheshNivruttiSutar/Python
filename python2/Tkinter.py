#PYTHON GUI SOFTWARE USING TKINTER:
import tkinter as tk
import pyautogui

root= tk.Tk()

size1 = tk.Canvas(root, width = 300, height = 300, bg ='yellow')
size1.pack()

root.mainloop()

#PYTHON GUI SOFTWARE USING TKINTER:
'''import tkinter as tk
import pyautogui

root= tk.Tk()

size1 = tk.Canvas(root, width = 300, height = 300)
size1.pack()

def takesnap():

    screenshot = pyautogui.screenshot()
    screenshot.save(r'C:\\Users\\Mahesh\\Desktop\\dreamsnap.png')

Button1 = tk.Button(text='Take Snap', command=takesnap, bg='blue', fg='yellow', font=5)
size1.create_window(150, 150, window=Button1)

root.mainloop()'''