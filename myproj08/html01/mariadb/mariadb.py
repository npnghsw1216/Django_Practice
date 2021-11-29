from tkinter import *

window = Tk()
window.title("윈도우창 연습")
window.geometry("400x100")  # 넓이 * 높이(가로*세로)
# window.resizable(width=FALSE, height=FALSE)  # window  고정시키기
window.resizable(width=FALSE, height=True)  # 높이 조정가능

# GUI 화면 코딩

window.mainloop()
