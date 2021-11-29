from tkinter import *
from tkinter import messagebox
# 버튼을 사용하여 알림 창 띄우기
def clickButton() :
    messagebox.showinfo("버튼 클릭", '버튼을 클릭했습니다.')  # (메시지버튼 타이틀, 메세지 박스 내용)

window = Tk()
window.title("버튼 이벤트 연습")
window.geometry("200x200")  # 넓이 * 높이

button1 = Button(window, text='요기 눌러요1', fg='red', bg='yellow', command=clickButton)
button2 = Button(window, text='요기 눌러요2', fg='red', bg='yellow', command=clickButton)
button3 = Button(window, text='요기 눌러요3', fg='red', bg='yellow', command=clickButton)

# 배치 관련해서는 팩안에서 조정
button1.pack(side = TOP, padx=10, pady=10)
button2.pack(side = TOP, padx=10, pady=10)
button3.pack(side = BOTTOM, padx=10, pady=10)

window.mainloop()
