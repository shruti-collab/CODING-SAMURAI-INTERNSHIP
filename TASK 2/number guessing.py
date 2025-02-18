from tkinter import*
import random
from turtle import textinput

ranvalue = random.randint(0,100)

count =0


def display():
    global textipt,checkbtn,labelinfo
    r=Tk()
    r.title("Number Guessiing")
    r.geometry("500x500")
    
    f=Frame(r)
    textipt=Entry(f,width=20)
    checkbtn=Button(f,text="guess?",font=('Arial',10,'bold') ,fg='white',bg='red',command=guess)
    labelinfo=Label(f,font=('Arial',10),height=3,state='disabled')

    textipt.grid(row=0, column=0,pady=10,ipady=3)
    checkbtn.grid(row=0,column=1,padx=10,pady=10)
    labelinfo.grid(row=1,column=0,columnspan=2)


    f.place(relx=0.5 ,rely=0.5,anchor=CENTER)
    r.mainloop()
def guess():
    global textipt,labelinfo,ranvalue,count
    print(ranvalue)

    strvalue = textipt.get().strip()
    if(strvalue != "" ):
         
        value = int(strvalue)
        if(ranvalue == value):
             
             labelinfo.config(text=f"ya! you guess the correct number in {count} attempt")
             textipt.delete(0,END)
             ranvalue = random.randint(0,100)
             count = 0 
        elif(ranvalue < value):

            labelinfo.config(text ="oops!you guess too high")
            textipt.delete(0,END)
            count += 1 
        else:
             labelinfo.config(text="oops! you guess too low")
             textipt.delete(0,END)
             count +=1


        


    else:
        labelinfo.config(text='You need to enter some value')




if __name__ == '__main__':
    display()
