from tkinter import*

root = Tk()
root.title("frog")
root.geometry("640x480+500+100")

txt = Text(root, width=30, height = 5)
txt.pack()

txt.insert(END, "글자를 입력하세요.")

e = Entry(root, width=30)
e.pack()
e.insert(0, "한줄만 입력해요.")

def btncmd():
    print(txt.get("1.0",END)) # 1: 첫 번째 라인, 0 : 0 번째 colum 위치
    print(e.get())

    #내용삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command = btncmd)
btn.pack()
root = mainloop()