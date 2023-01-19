from tkinter import *
import time
from datetime import date

master = Tk()
master.geometry('500x500')
master.title('Mój zegarek w Pythonie by Celina')

timenow = ' '
cframe = Frame(master, width = 5000, height=10000, bg='black', relief=RAISED)
cframe.pack()

clock = Label(cframe, padx=25, pady=40, bd=3, fg='pink',
              font=('arial', 48, 'bold'), text=timenow, bg='light yellow', relief=RAISED)
clock.pack()

def tick():
    global timenow
    newtime = time.strftime('%H: %M: %S %p')
    if newtime != timenow:
        timenow = newtime
        clock.config(text=timenow)

    return clock.after(100,tick)

date_today = date.today()
yearOfBirth = int(input('Podaj swój rok urodzenia: '))
monthOfBirth = int(input("Podaj swój miesiąc urodzenia: "))
dayOfBirth = int(input('Podaj swój dzień urodzenia: '))

dateOfBirth = date(yearOfBirth, monthOfBirth, dayOfBirth)
delta = date_today - dateOfBirth
deltaString = str(delta)
rightDate = deltaString.split(' ')

data =f"Dzisiaj jest: {date_today}"
lived = f'Przeżyłeś już {rightDate[0]} dni'

var = StringVar()
var.set(data)
date2 = Label(master, textvariable=var, padx=10, pady=10, fg='red', bg='light yellow', relief=RAISED )
date2.pack()

var2 = StringVar()
var2.set(lived)
licznik = Label(master, textvariable=var2, padx=10, pady=10, fg='red', bg='light yellow', relief=RAISED )
licznik.pack()

b = Button(master, text="Zamknij",padx=10, pady=10, command=master.destroy, fg='red', bg='light yellow')
b.pack()

tick()
master.mainloop()
