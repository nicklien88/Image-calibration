# 此程式可刪模糊無法標的照片及txt檔
import os
from tkinter import *

file_path = os.path.abspath("file_deleter.py")
file_dir = file_path[:-15]

def run():
    for parent, dirnames, filenames in os.walk(file_dir):
             for filename in filenames:      # 輸出檔案資訊
                # print "filename is:" + filename
                if ".txt" in filename:
                    f = open(filename, "r", encoding="utf-8")
                    if f.read() == "":
                        f.close()
                        picture_name_of_the_same = filename[:-4] + file_extension_name.get()
                        try:
                            os.remove(filename)
                            print(filename, "is deleted")
                        except:
                            print("can't not find {}".format(filename))
                        try:
                            os.remove(picture_name_of_the_same)
                            print(picture_name_of_the_same)
                        except:
                            print("can't not find {}".format(picture_name_of_the_same))


window = Tk()
window.title("刪除空白檔案程式")
label_1 = Label(window, text="要刪除的副檔名, ex: .png").pack(side=LEFT)
file_extension_name = StringVar()
entry_1 = Entry(window, textvariable=file_extension_name).pack(side=LEFT)

button_1 = Button(window, text="確定", command=run).pack(side=BOTTOM)
window.mainloop()
