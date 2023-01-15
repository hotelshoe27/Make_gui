from tkinter import*

root = Tk()
root.title("button")
root.geometry("640x480+500+100")

photo = PhotoImage(file="gui_basic/btn1.png")
btn1 = Button(root, image=photo)
btn1.pack()

def btncmd():
    print("버튼이 클릭되었어요.")
btn7 = Button(root, text = "동작하는 버튼", command = btncmd)
btn7.pack()





root = mainloop()