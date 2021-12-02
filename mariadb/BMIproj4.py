import pymysql
from tkinter import *
from tkinter import messagebox

# 데이터베이스 연동 함수
def insertData():
    conn = None
    cur = None

    # 데이터베이스 접속
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='projdb', charset='utf8')

    # 커서
    cur = conn.cursor()

    # 회원 정보 insert 기능 구현
    # 사용자에게 입력받은 회원 정보 초기화
    name, age, height, weight, bmi, decision = "", "", "", "", "", ""

    # GUI에서 입력한 데이터 담기
    name = edt1.get()
    age = edt2.get()
    gender = edt3.get()
    height = edt4.get()
    weight = edt5.get()
    bmi = edt6.get()
    decision = edt7.get()

    # SQL 쿼리 만들기

    sql = "INSERT  INTO userTBL(name, age, gender, height, weight, bmi, decision, mDate)VALUES "\
          "('"+name+"','"+age+"','"+height+"','"+weight+"', '"+bmi+"', '"+decision+"', CURDATE())"
    try:
        cur.execute(sql)
    except:
        messagebox.showerror("입력오류", "데이터 입력 오류가 발생 했습니다.")
    else:
        # 쿼리 실행이 완료(오류 없이)
        # 1) 메시지 박스로 성공 알림
        messagebox.showinfo("성공", "정보가 저장 되었습니다.")
        # 2) 데이터 커밋 (진짜 저장)
        conn.commit()
        # 3) 테이블 조회(새로고침)
        selectData()

    # GUI에 입력한 데이터 삭제
    edt1.delete(0, "end")
    edt2.delete(0, "end")
    edt3.delete(0, "end")
    edt4.delete(0, "end")
    edt5.delete(0, "end")
    edt6.delete(0, "end")
    edt7.delete(0, "end")

    # DB접속 종료
    conn.close()
# 프레임 이동(메인화면으로 돌아가기)
def backFrame():
    editFrame.pack()
    listFrame.pack_forget()

    # select 기능 구현
    # sql = "SELECT userID, name, birthYear, addr from userTBL WHERE userID= '"+userID+"' ORDER BY mDate DESC"


def selectData():
    conn = None
    cur = None

    lName, lAge, lGender, lHeight, lWeight, lBmi, lDecision = [], [], [], [], [], [], []

    # 데이터베이스 접속
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='projdb', charset='utf8')
    conn.commit()

    # 커서
    cur = conn.cursor()
    # 데이터 초기화
    lName.append("이름(Name)")
    lName.append("--------")

    lAge.append("나이(Age)")
    lAge.append("--------")

    lGender.append("성별(Gender)")
    lGender.append("--------")

    lHeight.append("키(Height)")
    lHeight.append("--------")

    lWeight.append("몸무게(Weight)")
    lWeight.append("--------")

    lBmi.append("BMI")
    lBmi.append("--------")

    lDecision.append("Decision")
    lDecision.append("--------")

    # select 기능 구현
    sql = "SELECT name, age, gender, height, weight, bmi, decision from userTBL ORDER BY mDate DESC "
    cur.execute(sql)

    while (True):
        row = cur.fetchone()

        if row == None:
            break

        #  lUserID, lName, lBirthYear, lAddr
        lName.append(row[0])
        lAge.append(row[1])
        lGender.append(row[2])
        lHeight.append(row[3])
        lWeight.append(row[4])
        lBmi.append(row[5])
        lDecision.append(row[6])

    # GUI ListBox에 insert
    # listUserID, listName, listBirthYearm listAddr
    # 1) 리스트 박스 초기화
    listName.delete(0, listName.size() - 1)
    listAge.delete(0, listAge.size() - 1)
    listGender.delete(0, listGender.size() - 1)
    listHeight.delete(0, listHeight.size() - 1)
    listWeight.delete(0, listWeight.size() - 1)
    listBmi.delete(0, listBmi.size() - 1)
    listDecision.delete(0, listDecision.size() - 1)

    # 2) select 해온 데이터 insert
    for item1, item2, item3, item4, item5, item6, item7 in zip(lName, lAge, lGender, lHeight, lWeight, lBmi, lDecision):
        listName.insert(END, item1)
        listAge.insert(END, item2)
        listGender.insert(END, item3)
        listHeight.insert(END, item4)
        listWeight.insert(END, item5)
        listBmi.insert(END, item6)
        listDecision.insert(END, item7)

    conn.close()

def new():
    global new
    new = Toplevel()

    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='projdb', charset='utf8')
    conn.commit()

    new.title('BMI 계산기')
    new.geometry('400x300')
    new.config(bg='#686e70')

    def reset_entry():
        age_entry.delete(0, 'end')
        height_entry.delete(0, 'end')
        weight_entry.delete(0, 'end')

    def calculate_bmi():
        kg = int(weight_entry.get())
        m = int(height_entry.get()) / 100
        bmi = kg / (m * m)
        bmi = round(bmi, 1)
        bmi_index(bmi)

    def bmi_index(bmi):
        if bmi < 18.5:
            messagebox.showinfo('bmi-calculate', f'당신의 BMI 수치는 저체중 입니다. BMI : {bmi}')
        elif (bmi > 18.5) and (bmi < 23):
            messagebox.showinfo('bmi-calculate', f'당신의 BMI 수치는 정상 입니다. BMI : {bmi}')
        elif (bmi > 23) and (bmi < 25):
            messagebox.showinfo('bmi-calculate', f'당신의 BMI 수치는 과체중 입니다. BMI : {bmi}')
        elif (bmi > 25) and (bmi < 30):
            messagebox.showinfo('bmi-calculate', f'당신의 BMI 수치는 비만 입니다. BMI :  {bmi}')
        elif bmi > 30:
            messagebox.showinfo('bmi-calculate', f'당신의 BMI 수치는 고도비만 입니다. BMI :  {bmi}')
        else:
            messagebox.showerror('bmi-calculate', '잘못됬습니다!')

    var = IntVar()

    frame = Frame(new, padx=10, pady=10)
    frame.pack(expand=True)

    age_lable = Label(frame, text="나이(Age)")
    age_lable.grid(row=1, column=1)

    age_entry = Entry(frame, )
    age_entry.grid(row=1, column=2, pady=5)

    gen_label = Label(frame, text='성별(Gender)')
    gen_label.grid(row=2, column=1)

    frame2 = Frame(frame)
    frame2.grid(row=2, column=2, pady=5)

    male_radiobutton = Radiobutton(frame2, text='남성', variable=var, value=1)
    male_radiobutton.pack(side=LEFT)

    female_radiobutton = Radiobutton(frame2, text='여성', variable=var, value=2)
    female_radiobutton.pack(side=RIGHT)

    height_label = Label(frame, text="키(cm)")
    height_label.grid(row=3, column=1)

    weight_label = Label(frame, text="몸무게(kg)")
    weight_label.grid(row=4, column=1)

    height_entry = Entry(frame, )
    height_entry.grid(row=3, column=2, pady=5)

    weight_entry = Entry(frame, )
    weight_entry.grid(row=4, column=2, pady=5)

    bmi_bmi = Listbox(listFrame)
    bmi_bmi.pack(side=LEFT, fill=BOTH, expand=1)

    decision_bmi = Listbox(listFrame)
    decision_bmi.pack(side=LEFT, fill=BOTH, expand=1)

    frame3 = Frame(frame)
    frame3.grid(row=5, columnspan=3, pady=10)

    cal_button = Button(frame3, text='계산', command=calculate_bmi)
    cal_button.pack(side=LEFT)

    reset_button = Button(frame3, text='초기화', command=reset_entry)
    reset_button.pack(side=LEFT)

    exit_button = Button(frame3, text='종료', command=lambda: new.destroy())
    exit_button.pack(side=RIGHT)

# GUI 화면 구성
window = Tk()
window.geometry("1000x300")
window.title("건강 체크")

editFrame = Frame(window)
editFrame.pack()

listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

label1 = Label(editFrame, text="회원명(Name)")
label1.pack(side=LEFT, padx=10, pady=10)
edt1 = Entry(editFrame, width=10)
edt1.pack(side=LEFT, padx=10, pady=10)

label2 = Label(editFrame, text="나이(Age)")
label2.pack(side=LEFT, padx=10, pady=10)
edt2 = Entry(editFrame, width=10)
edt2.pack(side=LEFT, padx=10, pady=10)

label3 = Label(editFrame, text="성별(Gender)")
label3.pack(side=LEFT, padx=10, pady=10)
edt3 = Entry(editFrame, width=10)
edt3.pack(side=LEFT, padx=10, pady=10)


label4 = Label(editFrame, text="키(Height)")
label4.pack(side=LEFT, padx=10, pady=10)
edt4 = Entry(editFrame, width=10)
edt4.pack(side=LEFT, padx=10, pady=10)


label5 = Label(editFrame, text="몸무게(weight)")
label5.pack(side=LEFT, padx=10, pady=10)
edt5 = Entry(editFrame, width=10)
edt5.pack(side=LEFT, padx=10, pady=10)

label6 = Label(editFrame, text="BMI")
label6.pack(side=LEFT, padx=10, pady=10)
edt6 = Entry(editFrame, width=10)
edt6.pack(side=LEFT, padx=10, pady=10)

label7 = Label(editFrame, text="Decision")
label7.pack(side=LEFT, padx=10, pady=10)
edt7 = Entry(editFrame, width=10)
edt7.pack(side=LEFT, padx=10, pady=10)


# 계산 버튼
btnCalculate = Button(editFrame, text="계산하기", command=new)
btnCalculate.pack(side=LEFT, padx=10, pady=10)

# 버튼
btnInsert = Button(editFrame, text="저장", command=insertData)
btnInsert.pack(side=LEFT, padx=10, pady=10)

btnSelect = Button(editFrame, text="조회", command=selectData)
btnSelect.pack(side=LEFT, padx=10, pady=10)

listName = Listbox(listFrame)
listName.pack(side=LEFT, fill=BOTH, expand=1)

listGender = Listbox(listFrame)
listGender.pack(side=LEFT, fill=BOTH, expand=1)

listAge = Listbox(listFrame)
listAge.pack(side=LEFT, fill=BOTH, expand=1)

listHeight = Listbox(listFrame)
listHeight.pack(side=LEFT, fill=BOTH, expand=1)

listWeight = Listbox(listFrame)
listWeight.pack(side=LEFT, fill=BOTH, expand=1)

listBmi = Listbox(listFrame)
listBmi.pack(side=LEFT, fill=BOTH, expand=1)

listDecision = Listbox(listFrame)
listDecision.pack(side=LEFT, fill=BOTH, expand=1)



window.mainloop()