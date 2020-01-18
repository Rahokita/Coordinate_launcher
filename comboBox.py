from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import shutil
import os
import os.path

def button1_clicked():
    print('v1 = %s' % v1.get())
    rep_folder = v1.get()
    folder_exchange("coodinate","coodinate_bk",rep_folder)

def cb_selected(event):
    print('v1 = %s' % v1.get())

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        folder_reset("coodinate","coodinate_bk")
        root.destroy()

def folder_exchange(org_folder,bk_folder,rep_folder):
    #既存のフォルダをremaneして退避
    os.rename(org_folder, bk_folder)
    #コピー先のフォルダを作成（フォルダ名は固定）
    #os.mkdir(org_folder)
    #フォルダの中身ごとコピー
    shutil.copytree('Foo', org_folder)

def folder_reset(org_folder,bk_folder):
    #bk_dolderが存在するかをチェック
    if os.path.exists(bk_folder) == True:
        #フォルダを一旦削除
        shutil.rmtree(org_folder)
        #退避したフォルダを元に戻す
        os.rename(bk_folder, org_folder)

if __name__ == '__main__':
    root = Tk()
    root.title('Combobox 1')
    
    # Frame
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()
    
    # Combobox
    v1 = StringVar()
    cb = ttk.Combobox(frame1, textvariable=v1)
    cb.bind('<<ComboboxSelected>>', cb_selected)
    
    cb['values']=('Foo', 'Bar', 'Baz')
    cb.set("Foo")
    cb.grid(row=0, column=0)
    
    #Button
    button1 = ttk.Button(frame1, text='OK', command=button1_clicked)
    button1.grid(row=0, column=1)
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
