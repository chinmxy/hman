from tkinter import *
import wSelect


#initialise
window=Tk()
frame=Frame(window,width=500,height=500,bg='white')
frame.grid()
window.title("Hangman.exe")
window.configure(bg='cyan')

#importing a word
new_ip=get_word()
lenip=len(new_ip)
list1='_'
list2=[]
print(new_ip)

#set of characters in new_ip
list3=[]

#no repetition of letters
list4=[]

#functions
def mkunder(new_ip):
    #printing underscores
    list2.clear()
    for i in range(0,len(new_ip)):
        list2.append(list1)
mkunder(new_ip)
 
def mkset(new_ip):
    list3.clear()
    for char in new_ip:
        list3.append(char)

mkset(new_ip)
    
def convert(l): 
    new = ""   
    for x in l: 
        new += x 
        new += ' '
    return new 

def click():
    ip=tBox.get()
    tBox.delete(0,1)
    check(ip)
    v.set(convert(list2))
    print(list2)
    check_finish()
    
def check(ip):
    if ip in list3 and ip not in list4:
        list4.append(ip)
        for j in range(len(list3)):
            if ip==list3[j]:
                list2[j]=ip
    else:
        if ip in list3:
            print('LETTER REPEATED')
        else:
            print('LETTER NOT IN WORD')
            #flag increment
def check_finish():
    us='_'
    if us not in list2:
        print("YOU HAVE WON !")
        
def change():
    tBox.delete(0,1)
    new_ip=get_word()
    print(new_ip)
    mkunder(new_ip)
    print(list2)
    v.set(convert(list2))
    mkset(new_ip)
    print(list3)
        
      
#functions_end

#hangman title
l1=Label(window,text='HANGMAN',fg='black',bg='cyan',font='none 20 bold italic')
l1.grid(row=0,column=0,sticky=N)

#image
photo=PhotoImage(file="1.gif")
l3=Label(window,image=photo,bg='cyan',height=126,width=90)
l3.grid(row=1,column=0,sticky=N)

#input character box
tBox=Entry(window, width=2, bg='white')
tBox.grid(row=2,column=0,sticky=N)

#submit button
b1=Button(window, text='SUBMIT',width=6,command=click)
b1.grid(row=3,column=0,sticky=E)

#change word button
b2=Button(window, text='CHANGE',width=6,command=change)
b2.grid(row=3,column=0,sticky=W)

#output box
v=StringVar(value=list2)
l2=Label(window,textvariable=v,fg='black',bg='cyan',font='none 12')
l2.grid(row=4,column=0)



window.mainloop()

