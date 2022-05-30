from tkinter import *

def button1():
    pass

window = Tk()
window.title("Paint") #标题
window.geometry("350x200") #窗口大小
lbl = Label(window, text="Hello", font=("Arial Bold", 50)) #字符大小
lbl.grid(column=0, row=0) #字符位置
btn = Button(window, text="角色信息",bg="orange", fg="red",command=button1) #按钮，前景色及背景色，获取函数
btn.grid(column=1, row=0) #按钮位置
txt = Entry(window, width=10) #获取用户输入
txt.grid(column=1, row=2)
window.mainloop()

def clicked(): #get获取用户输入
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)