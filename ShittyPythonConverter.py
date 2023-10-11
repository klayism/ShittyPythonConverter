#importation
from tkinter import *
#initialisation de la fenetre
root=Tk()
root.title("multi converter")
root.minsize(width=270, height=150)
#initialisation de les variable
mm,cm,m,km,long,time,temp,ms,s,mn,h,j,f,c,k = 'mm','cm','m','km',"Longeur","Temps","Temperature",'ms','s','min','h','j','f','c','k'
optionsconversion=[long,time,temp]
optionlonguer=[mm,cm,m,km]
optiontemperature=[f,c,k]
optiontime=[ms,s,mn,h,j]
state = long
lselectedfrom=StringVar()
lselectedfrom.set(mm)
lselectedto=StringVar()
lselectedto.set(cm)
tselectedfrom=StringVar()
tselectedfrom.set(s)
tselectedto=StringVar()
tselectedto.set(mn)
tempselectedfrom=StringVar()
tempselectedfrom.set(c)
tempselectedto=StringVar()
tempselectedto.set(f)
selectedmode=StringVar()
selectedmode.set(long)
def forget(widget):
    widget.grid_forget()
def enterlength():
    lconvertfrom.grid(column=1,row=0)
    lconvertto.grid(column=1,row=1)
    lbutton.grid(column=1,row=3)
def entertime():
    tconvertfrom.grid(column=1,row=0)
    tconvertto.grid(column=1,row=1)
    tbutton.grid(column=1,row=3)
def entertemp():
    tempsconvertfrom.grid(column=1,row=0)
    tempsconvertto.grid(column=1,row=1)
    tempsbutton.grid(column=1,row=3)
def exitlength():
    forget(lconvertfrom)
    forget(lconvertto)
    forget(lbutton)
    result.config(text="")
def exittime():
    forget(tconvertfrom)
    forget(tconvertto)
    forget(tbutton)
    result.config(text="")
def exittemps():
    forget(tempsconvertfrom)
    forget(tempsconvertto)
    forget(tempsbutton)
    result.config(text="")
def retrieve_input():
    t1=int(text1.get("1.0","end-1c"))
    if state == long:
        fromchoice=str(lselectedfrom.get())
        tochoice=str(lselectedto.get())
        if fromchoice == tochoice:
            result.config(text=t1)
        elif fromchoice == mm and tochoice == cm:
            result.config(text=t1/10)
        elif fromchoice == mm and tochoice == m:
            result.config(text=t1/100)
        elif fromchoice == mm and tochoice == km:
            result.config(text=t1/1000000)
        elif fromchoice == cm and tochoice == mm:
            result.config(text=t1*10)
        elif fromchoice == cm and tochoice == m:
            result.config(text=t1/100)
        elif fromchoice == cm and tochoice == km:
            result.config(text=t1/100000)
        elif fromchoice == m and tochoice == mm:
            result.config(text=t1*1000)
        elif fromchoice == m and tochoice == cm:
            result.config(text=t1*100)
        elif fromchoice == m and tochoice == km:
            result.config(text=t1/1000)
        elif fromchoice == km and tochoice == mm:
            result.config(text=t1*1000000)
        elif fromchoice == km and tochoice == cm:
            result.config(text=t1*100000)
        elif fromchoice == km and tochoice == m:
            result.config(text=t1*1000)
    elif state == time:
        fromchoice=str(tselectedfrom.get())
        tochoice=str(tselectedto.get())
        if fromchoice == tochoice:
            result.config(text=t1)
        elif fromchoice == ms and tochoice == s:
            result.config(text=t1/1000)
        elif fromchoice == ms and tochoice == mn:
            result.config(text=t1/60000)
        elif fromchoice == ms and tochoice == h:
            result.config(text=round(t1/3600000,10))
        elif fromchoice == ms and tochoice == j:
            result.config(text=round(t1/86400000, 10))
        elif fromchoice == s and tochoice == mn:
            result.config(text=t1/60)
        elif fromchoice == s and tochoice == ms:
            result.config(text=t1*1000)
        elif fromchoice == s and tochoice == h:
            result.config(text=t1/3600)
        elif fromchoice == s and tochoice == j:
            result.config(text=t1/86400)
        elif fromchoice == mn and tochoice == ms:
            result.config(text=t1*60000)
        elif fromchoice == mn and tochoice == s:
            result.config(text=t1*60)
        elif fromchoice == mn and tochoice == h:
            result.config(text=t1/60)
        elif fromchoice == mn and tochoice == ms:
            result.config(text=t1/1440)
        elif fromchoice == h and tochoice == ms:
            result.config(text=t1*3600000)
        elif fromchoice == h and tochoice == s:
            result.config(text=t1*3600)
        elif fromchoice == h and tochoice == mn:
            result.config(text=t1*60)
        elif fromchoice == h and tochoice == j:
            result.config(text=t1/24)
        elif fromchoice == j and tochoice == ms:
            result.config(text=t1*86400000)
        elif fromchoice == j and tochoice == s:
            result.config(text=t1*86400)
        elif fromchoice == j and tochoice == mn:
            result.config(text=t1*1440)
        elif fromchoice == j and tochoice == h:
            result.config(text=t1*24)
    elif state == temp:        
        fromchoice=str(tempselectedfrom.get())
        tochoice=str(tempselectedto.get())
        if fromchoice == tochoice:
            result.config(text=t1)
        elif fromchoice == c and tochoice == f:
            result.config(text=round(t1*(9/5)+32))
        elif fromchoice == c and tochoice == k:
            result.config(text=round(t1+273.15))
        elif fromchoice == f and tochoice == c:
            result.config(text=round((t1-32)*5/9))
        elif fromchoice == f and tochoice == k:
            result.config(text=round((t1-32)*9/5+273.15))
        elif fromchoice == k and tochoice == c:
            result.config(text=round(t1-273.15))
        elif fromchoice == k and tochoice == f:
            result.config(text=round((t1-273.15)*9/5+32))
#sert a 
def switch():
    global state
    modechoice=str(selectedmode.get())
    if modechoice == state:
        pass
    elif modechoice == long:
        if state == time:
            exittime()
        elif state == temp:
            exittemps()
        enterlength()
        state = long
    elif modechoice == time:
        if state == long:
            exitlength()
        elif state == temp:
            exittemps()
        entertime()
        state = time
    elif modechoice == temp:
        if state == long:
            exitlength()
        elif state == time:
            exittime()
        entertemp()
        state = temp
#chose qui serat toujours la
text1=Text(root, height = 1, width = 10)
result=Label(root, height=1, width=10)
dropconver=OptionMenu(root, selectedmode, *optionsconversion)
switchmodebutton=Button(root,height=1,width=10,text="switch mode", command=lambda: switch())
text1.grid(column=0,row=0)
result.grid(column=0,row=1)
dropconver.grid(column=1,row=2)
switchmodebutton.grid(column=0,row=2)
#chose qui serat placer par la fonction enterlength()
lconvertfrom=OptionMenu(root, lselectedfrom, *optionlonguer,)
lconvertto=OptionMenu(root, lselectedto, *optionlonguer)
lbutton=Button(root, height=1, width=5, text="resulta", command=lambda: retrieve_input())
#chose qui serat placer par la fonction entertime() 
tconvertfrom=OptionMenu(root,tselectedfrom, *optiontime)
tconvertto=OptionMenu(root,tselectedto,*optiontime)
tbutton=Button(root, height=1, width=5, text="resulta", command=lambda: retrieve_input())
#chose qui serat placer par la fonction entertemo()
tempsconvertfrom=OptionMenu(root, tempselectedfrom, *optiontemperature)
tempsconvertto=OptionMenu(root, tempselectedto, *optiontemperature)
tempsbutton=Button(root, height=1, width=5, text="resulta", command=lambda: retrieve_input())
enterlength()
root.mainloop()