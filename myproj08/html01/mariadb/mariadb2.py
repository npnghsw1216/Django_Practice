from tkinter import *
#  문자를 포현할 수 있는 라벨 사용

window = Tk()
window.title("라벨 연습")
window.geometry("400x100")  # 넓이 * 높이(가로*세로) # 사이즈를 지정하지않으면 크게이 따라 맞게 실행됨

# 라벨선언
label1 = Label(window, text='This is MariaDB를 ')
label2 = Label(window, text='열심히 ', font=("궁서체",30), fg="blue")
label3 = Label(window, text='공부 중입니다.', bg='magenta', width=20, height=5, anchor=SE)
# 레이블이 올라갈 윈도우, 출력된 글, 설정: font, fg=폰트색, bg=배경색, anchor는 글자의 위치

# 위젯 적용
label1.pack()
label2.pack()
label3.pack()

window.mainloop()
