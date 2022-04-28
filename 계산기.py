import tkinter as tk  #윈도우를 만들기 위해 tkinter 사용

disValue = 0
operator = {'+':1,'-':2, '/':3,'*':4, 'C':5, '=':6} #각 명령에 딕셔너리형태로 번호를 붙여줌.
stoValue = 0
opPre = 0

def number_click(value):
    #print('숫자',value)
    global disValue    #disValue변수를 이 함수에서 사용하겠다는 의미
    disValue = (disValue*10) +value  #숫자를 클릭할 때마다 10의 자리씩 이동한다
    str_value.set(disValue)  #화면에 숫자를 나타낸다

def clear():
    global disValue, operator, stoValue, opPre
    stoValue = 0
    opPre = 0
    disValue = 0
    str_value.set(disValue)

def operator_click(value):
    global disValue, operator, stoValue, opPre
    op = operator[value]
    if op == 5:  #C를 눌렀을때 클리어 함수
        clear()
    elif disValue ==0: #값이 눌린게 없을때
        opPre = 0 #이전의 명령을 초기화
    elif opPre == 0:  #이전 명령이 없고 새로 명령이 눌렸을때
        opPre = op
        stoValue = disValue  #현재값 저장
        disValue = 0 #화면의 값을 0으로 초기화
        str_value.set(disValue)  #값 출력
    elif op ==6:
        if opPre == 1:
            disValue = stoValue +disValue
        str_value.set(disValue)
        if opPre == 2:
            disValue = stoValue - disValue
        str_value.set(disValue)
        if opPre == 3:
            disValue = stoValue /disValue
        str_value.set(disValue)
        if opPre == 4:
            disValue = stoValue *disValue
        str_value.set(disValue)
        disValue=0
        stoValue=0  #계산 완료되면 값 초기화

def button_click(value):

    try:
        value=int(value)
        number_click(value)
    except:
        operator_click(value)


win = tk.Tk()         #Tk()라는 함수를 통해 윈도우를 만드는 것 가능
win.title('계산기')    #윈도우.title 통해 윈도우 캡션 정할수 있음

            #기본값
str_value = tk.StringVar()  #tkinter GUI에서 화면에 띄운 내용을 필요에 따라 바꾸어야 할 때 사용하는 방법
str_value.set(str(disValue)) #그 값을 문자로 변환환tk.Entry(win, textvariable= str_value)  #맨 위에 두는 edit 창: Entry 사용 여기 값이 늘 변화할 거임....그 변수를 위에 두는 것
dis = tk.Entry(win, textvariable=str_value, justify='right',bg='white',fg='blue')
dis.grid(column=0, row=0, columnspan= 4, ipadx=80, ipady=30)

calItem = [['+','0','-','*'],
           ['7','8','9','/'],
           ['4','5','6','C'],
           ['1','2','3','=']
           ]
for i ,items in enumerate(calItem):
    for k,item in enumerate(items):
        try:
            color = int(item)
            color = 'black'
            fontcolor= int(item)
            fontcolor= 'skyblue'
        except:
            color = 'skyblue'
            fontcolor = 'black'
        bt = tk.Button(win,
            text=item,
            width=10,
            height=5,
            bg= color,
            fg= fontcolor,
            command = lambda cmd=item: button_click(cmd),
            )

        bt.grid(column=k, row=(i+1))

win.mainloop()  #mainloop는 윈도우 내부에서 수행되는 마우스 클릭 같은 이벤트가 발생하게끔 유지해주는 함수