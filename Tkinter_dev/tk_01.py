#-*- coding: UTF-8 -*-
import tkinter as tk
root = tk.Tk()
root.title("nginx管理平台")    # 设置窗口标题
root.geometry("1000x500")    # 设置窗口大小 注意：是x 不是*
root.resizable(width=True, height=False) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
l = tk.Label(root, text="label", bg="pink", font=("Arial",12), width=8, height=3)
l.pack()   # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
root.mainloop() # 进入消息循环


