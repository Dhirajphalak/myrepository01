from tkinter import *
import time
import datetime
import random
import tkinter.messagebox
import sqlite3

root =Tk()
root.geometry("1450x750+0+0")
root.title("CAFE O`")
root.configure(background='peru')       

Tops = Frame(root,bg='peru',bd=20,pady=5,relief=RIDGE)
Tops.pack(side=TOP)

lblTitle=Label(Tops,font=('arial',60,'bold'),text='CAFE O`',bd=21,bg='saddlebrown',
                fg='cornsilk',justify=CENTER)
lblTitle.grid(row=0)


ReceiptCal_F = Frame(root,bg='peru',bd=10,relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F,bg='peru',bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F=Frame(ReceiptCal_F,bg='peru',bd=6,relief=RIDGE)
Cal_F.pack(side=TOP)

Receipt_F=Frame(ReceiptCal_F,bg='peru',bd=4,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root,bg='peru',bd=10,relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame,bg='peru',bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame,bg='peru',bd=4)
Drinks_F.pack(side=TOP)


Drinks_F=Frame(MenuFrame,bg='peru',bd=4,relief=RIDGE)
Drinks_F.pack(side=LEFT)
Food_F=Frame(MenuFrame,bg='peru',bd=4,relief=RIDGE)
Food_F.pack(side=RIGHT)


var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofFood = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""

E_Mocha = StringVar()
E_Cappuccino = StringVar()
E_VanillaLatte = StringVar()
E_Espresso = StringVar()
E_Americano = StringVar()
E_IcedCofeeLatte = StringVar()
E_LemonJuice = StringVar()
E_OrangeJuice = StringVar()

E_Cookies = StringVar()
E_Cheesecake = StringVar()
E_Tart = StringVar()
E_RedVelvetCake = StringVar()
E_Waffle = StringVar()
E_Pie = StringVar()
E_VanillaCake = StringVar()
E_Pancake = StringVar()

E_Mocha.set("0")
E_Cappuccino.set("0")
E_VanillaLatte.set("0")
E_Espresso.set("0")
E_Americano.set("0")
E_IcedCofeeLatte.set("0")
E_LemonJuice.set("0")
E_OrangeJuice.set("0")

E_Cookies.set("0")
E_Cheesecake.set("0")
E_Tart.set("0")
E_RedVelvetCake.set("0")
E_Waffle.set("0")
E_Pie.set("0")
E_VanillaCake.set("0")
E_Pancake.set("0")

DateofOrder.set(time.strftime("%d/%m/%y"))

##########################################Function Declaration####################################################

def iExit():
    iExit=tkinter.messagebox.askyesno("Exit Restaurant System","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Reset():

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofFood.set("")
    CostofDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)


    E_Mocha.set("0")
    E_Cappuccino.set("0")
    E_VanillaLatte.set("0")
    E_Espresso.set("0")
    E_Americano.set("0")
    E_IcedCofeeLatte.set("0")
    E_LemonJuice.set("0")
    E_OrangeJuice.set("0")

    E_Cookies.set("0")
    E_Cheesecake.set("0")
    E_Tart.set("0")
    E_RedVelvetCake.set("0")
    E_Waffle.set("0")
    E_Pie.set("0")
    E_VanillaCake.set("0")
    E_Pancake.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)


    txtMocha.configure(state=DISABLED)
    txtCappuccino.configure(state=DISABLED)
    txtVanillaLatte.configure(state=DISABLED)
    txtEspresso.configure(state=DISABLED)
    txtAmericano.configure(state=DISABLED)
    txtIcedCofeeLatte.configure(state=DISABLED)
    txtLemonJuice.configure(state=DISABLED)
    txtOrangeJuice.configure(state=DISABLED)
    txtCookies.configure(state=DISABLED)
    txtCheesecake.configure(state=DISABLED)
    txtTart.configure(state=DISABLED)
    txtRedVelvetCake.configure(state=DISABLED)
    txtWaffle.configure(state=DISABLED)
    txtPie.configure(state=DISABLED)
    txtVanillaCake.configure(state=DISABLED)
    txtPancake.configure(state=DISABLED)

def CostofItem():
    Item1=float(E_Mocha.get())
    Item2=float(E_Cappuccino.get())
    Item3=float(E_VanillaLatte.get())
    Item4=float(E_Espresso.get())
    Item5=float(E_Americano.get())
    Item6=float(E_IcedCofeeLatte.get())
    Item7=float(E_LemonJuice.get())
    Item8=float(E_OrangeJuice.get())

    Item9=float(E_Cookies.get())
    Item10=float(E_Cheesecake.get())
    Item11=float(E_Tart.get())
    Item12=float(E_RedVelvetCake.get())
    Item13=float(E_Waffle.get())
    Item14=float(E_Pie.get())
    Item15=float(E_VanillaCake.get())
    Item16=float(E_Pancake.get())

    PriceofDrinks =(Item1 * 100) + (Item2 * 120) + (Item3 * 150) + (Item4 * 100) + (Item5 * 110) + (Item6 * 140) + (Item7 * 120) + (Item8 * 130)

    PriceofFood =(Item9 * 150) + (Item10 * 200) + (Item11 * 120) + (Item12 * 150) + (Item13 * 100) + (Item14 * 110) + (Item15 * 100) + (Item16 * 120)



    DrinksPrice = "???",str('%.2f'%(PriceofDrinks))
    FoodPrice =  "???",str('%.2f'%(PriceofFood))
    CostofFood.set(FoodPrice)
    CostofDrinks.set(DrinksPrice)
    SC = "???",str('%.2f'%(1.59))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "???",str('%.2f'%(PriceofDrinks + PriceofFood + 1.59))
    SubTotal.set(SubTotalofITEMS)

    Tax = "???",str('%.2f'%((PriceofDrinks + PriceofFood + 1.59) * 0.15))
    PaidTax.set(Tax)

    TT=((PriceofDrinks + PriceofFood + 1.59) * 0.15)
    TC="???",str('%.2f'%(PriceofDrinks + PriceofFood + 1.59 + TT))
    TotalCost.set(TC)


def chkMocha():
    if(var1.get() == 1):
        txtMocha.configure(state = NORMAL)
        txtMocha.focus()
        txtMocha.delete('0',END)
        E_Mocha.set("")
    elif(var1.get() == 0):
        txtMocha.configure(state = DISABLED)
        E_Mocha.set("0")

def chkCappuccino():
    if(var2.get() == 1):
        txtCappuccino.configure(state = NORMAL)
        txtCappuccino.focus()
        txtCappuccino.delete('0',END)
        E_Cappuccino.set("")
    elif(var2.get() == 0):
        txtCappuccino.configure(state = DISABLED)
        E_Cappuccino.set("0")

def chk_VanillaLatte():
    if(var3.get() == 1):
        txtVanillaLatte.configure(state = NORMAL)
        txtVanillaLatte.delete('0',END)
        txtVanillaLatte.focus()
    elif(var3.get() == 0):
        txtVanillaLatte.configure(state = DISABLED)
        E_VanillaLatte.set("0")

def chk_Espresso():
    if(var4.get() == 1):
        txtEspresso.configure(state = NORMAL)
        txtEspresso.delete('0',END)
        txtEspresso.focus()
    elif(var4.get() == 0):
        txtEspresso.configure(state = DISABLED)
        E_Espresso.set("0")

def chk_Americano():
    if(var5.get() == 1):
        txtAmericano.configure(state = NORMAL)
        txtAmericano.delete('0',END)
        txtAmericano.focus()
    elif(var5.get() == 0):
        txtAmericano.configure(state = DISABLED)
        E_Americano.set("0")

def chk_IcedCofeeLatte():
    if(var6.get() == 1):
        txtIcedCofeeLatte.configure(state = NORMAL)
        txtIcedCofeeLatte.delete('0',END)
        txtIcedCofeeLatte.focus()
    elif(var6.get() == 0):
        txtIcedCofeeLatte.configure(state = DISABLED)
        E_IcedCofeeLatte.set("0")

def chk_LemonJuice():
    if(var7.get() == 1):
        txtLemonJuice.configure(state = NORMAL)
        txtLemonJuice.delete('0',END)
        txtLemonJuice.focus()
    elif(var7.get() == 0):
        txtLemonJuice.configure(state = DISABLED)
        E_LemonJuice.set("0")

def chk_OrangeJuice():
    if(var8.get() == 1):
        txtOrangeJuice.configure(state = NORMAL)
        txtOrangeJuice.delete('0',END)
        txtOrangeJuice.focus()
    elif(var8.get() == 0):
        txtOrangeJuice.configure(state = DISABLED)
        E_OrangeJuice.set("0")

def chk_Cookies():
    if(var9.get() == 1):
        txtCookies.configure(state = NORMAL)
        txtCookies.delete('0',END)
        txtCookies.focus()
    elif(var9.get() == 0):
        txtCookies.configure(state = DISABLED)
        E_Cookies.set("0")

def chk_Cheesecake():
    if(var10.get() == 1):
        txtCheesecake.configure(state = NORMAL)
        txtCheesecake.delete('0',END)
        txtCheesecake.focus()
    elif(var10.get() == 0):
        txtCheesecake.configure(state = DISABLED)
        E_Cheesecake.set("0")

def chk_Tart():
    if(var11.get() == 1):
        txtTart.configure(state = NORMAL)
        txtTart.delete('0',END)
        txtTart.focus()
    elif(var11.get() == 0):
        txtTart.configure(state = DISABLED)
        E_Tart.set("0")

def chk_RedVelvetCake():
    if(var12.get() == 1):
        txtRedVelvetCake.configure(state = NORMAL)
        txtRedVelvetCake.delete('0',END)
        txtRedVelvetCake.focus()
    elif(var12.get() == 0):
        txtRedVelvetCake.configure(state = DISABLED)
        E_RedVelvetCake.set("0")

def chk_Waffle():
    if(var13.get() == 1):
        txtWaffle.configure(state = NORMAL)
        txtWaffle.delete('0',END)
        txtWaffle.focus()
    elif(var13.get() == 0):
        txtWaffle.configure(state = DISABLED)
        E_Waffle.set("0")

def chk_Pie():
    if(var14.get() == 1):
        txtPie.configure(state = NORMAL)
        txtPie.delete('0',END)
        txtPie.focus()
    elif(var14.get() == 0):
        txtPie.configure(state = DISABLED)
        E_Pie.set("0")

def chk_VanillaCake():
    if(var15.get() == 1):
        txtVanillaCake.configure(state = NORMAL)
        txtVanillaCake.delete('0',END)
        txtVanillaCake.focus()
    elif(var15.get() == 0):
        txtVanillaCake.configure(state = DISABLED)
        E_VanillaCake.set("0")

def chk_Pancake():
    if(var16.get() == 1):
        txtPancake.configure(state = NORMAL)
        txtPancake.delete('0',END)
        txtPancake.focus()
    elif(var16.get() == 0):
        txtPancake.configure(state = DISABLED)
        E_Pancake.set("0")


def create():
    conn=sqlite3.connect('retail.db')
    c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS sale(ReceiptRef StringVar, Date StringVar, Mocha float, Cappuccino float, VanillaLatte float, Espresso float, Americano float, IcedCofeeLatte float, LemonJuice float, OrangeJuice float, Cookies float, Cheesecake float, Tart float, RedVelvetCake float, Waffle float, Pie float, VanillaCake float, Pancake float, CostofDrinks float, CostofFood float, PaidTax float, SubTotal float, ServiceCharge float, TotalCost float)")
    conn.commit()
    conn.close()


def savedata():
    conn=sqlite3.connect('retail.db')
    c=conn.cursor()
    c.execute('INSERT INTO sale(ReceiptRef ,Date , Mocha, Cappuccino , VanillaLatte , Espresso , Americano, IcedCofeeLatte , LemonJuice , OrangeJuice , Cookies , Cheesecake , Tart , RedVelvetCake , Waffle , Pie, VanillaCake , Pancake , CostofDrinks , CostofFood , PaidTax , SubTotal , ServiceCharge, TotalCost) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(Receipt_Ref.get(),DateofOrder.get(),E_Mocha.get(),E_Cappuccino.get(),E_VanillaLatte.get(),E_Espresso.get(),E_Americano.get(),E_IcedCofeeLatte.get(),E_LemonJuice.get(),E_OrangeJuice.get(),E_Cookies.get(),E_Cheesecake.get(),E_Tart.get(),E_RedVelvetCake.get(),E_Waffle.get(),E_Pie.get(),E_VanillaCake.get(),E_Pancake.get(),CostofDrinks.get(),CostofFood.get(),PaidTax.get(),SubTotal.get(),ServiceCharge.get(),TotalCost.get()))
    conn.commit()
    conn.close()

def Receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(10908,500876)
    randomRef= str(x)
    Receipt_Ref.set("Bill"+ randomRef)

    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get() +'\t'+ DateofOrder.get() +'\n')
    txtReceipt.insert(END,'Items(Price Per Item)\t\t\t\t'+"Quantity of Item \n")
    if(E_Mocha.get()=='0'):
        pass
    else:
       txtReceipt.insert(END,'Mocha:\t???100\t\t\t\t' + E_Mocha.get() +'\n')
    if(E_Cappuccino.get()=='0'):
        pass
    else:
       txtReceipt.insert(END,'Cappuccino:\t???120\t\t\t\t'+ E_Cappuccino.get()+'\n')
    if(E_VanillaLatte.get()=='0'):
        pass
    else:
       txtReceipt.insert(END,'VanillaLatte:\t???150\t\t\t\t'+ E_VanillaLatte.get()+'\n')
    if(E_Espresso.get()=='0'):
        pass
    else:
       txtReceipt.insert(END,'Espresso:\t???100\t\t\t\t'+ E_Espresso.get()+'\n')
    if(E_Americano.get()=='0'):
        pass
    else:
       txtReceipt.insert(END,'Americano:\t???110\t\t\t\t'+ E_Americano.get()+'\n')
    if(E_IcedCofeeLatte.get()=='0'):
        pass
    else:
       txtReceipt.insert(END,'IcedCofeeLatte:\t???140\t\t\t\t'+ E_IcedCofeeLatte.get()+'\n')
    if(E_LemonJuice.get()=='0'):
        pass
    else:
       txtReceipt.insert(END,'LemonJuice:\t???120\t\t\t\t'+ E_LemonJuice.get()+'\n')
    if(E_OrangeJuice.get()=='0'):
        pass
    else:
       txtReceipt.insert(END,'OrangeJuice:\t???130\t\t\t\t'+ E_OrangeJuice.get()+'\n')
    if(E_Cookies.get()=='0'):
        pass
    else:
       txtReceipt.insert(END,'Cookies:\t???150\t\t\t\t'+ E_Cookies.get()+'\n')
    if(E_Cheesecake.get()=='0'):
        pass
    else:
       txtReceipt.insert(END,'Cheesecake:\t???200\t\t\t\t'+ E_Cheesecake.get()+'\n')
    if(E_Tart.get()=='0'):
        pass
    else:
       txtReceipt.insert(END,'Tart:\t???120\t\t\t\t'+ E_Tart.get()+'\n')
    if(E_RedVelvetCake.get()=='0'):
        pass
    else: 
       txtReceipt.insert(END,'RedVelvetCake:\t???150\t\t\t\t'+ E_RedVelvetCake.get()+'\n')
    if(E_Waffle.get()=='0'):
        pass
    else:
       txtReceipt.insert(END,'Waffle:\t???100\t\t\t\t'+ E_Waffle.get()+'\n')
    if(E_Pie.get()=='0'):
        pass
    else:
       txtReceipt.insert(END,'Pie:\t???110\t\t\t\t'+ E_Pie.get()+'\n')
    if(E_VanillaCake.get()=='0'):
        pass
    else:
       txtReceipt.insert(END,'VanillaCake:\t???100\t\t\t\t'+ E_VanillaCake.get()+'\n')
    if(E_Pancake.get()=='0'):
        pass
    else:
       txtReceipt.insert(END,'Pancake:\t???120\t\t\t\t'+ E_Pancake.get()+'\n')

    txtReceipt.insert(END,'Cost of Drinks:\t\t'+ CostofDrinks.get()+'\nTax Paid:\t\t'+PaidTax.get()+"\n")
    txtReceipt.insert(END,'Cost of Foods:\t\t'+ CostofFood.get()+'\nSubTotal:\t\t'+str(SubTotal.get())+"\n")
    txtReceipt.insert(END,'Service Charge:\t\t'+ ServiceCharge.get()+'\nTotal Cost:\t\t'+str(TotalCost.get())+"\n")
    create()
    savedata()

Mocha=Checkbutton(Drinks_F,text='Mocha',variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='peru',command=chkMocha).grid(row=0,sticky=W)
Cappuccino=Checkbutton(Drinks_F,text='Cappuccino',variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='peru',command=chkCappuccino).grid(row=1,sticky=W)
VanillaLatte=Checkbutton(Drinks_F,text='VanillaLatte',variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='peru',command=chk_VanillaLatte).grid(row=2,sticky=W)
Espresso=Checkbutton(Drinks_F,text='Espresso',variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='peru',command=chk_Espresso).grid(row=3,sticky=W)
Cappuccino=Checkbutton(Drinks_F,text='Americano',variable=var5,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='peru',command=chk_Americano).grid(row=4,sticky=W)
IcedCofeeLatte=Checkbutton(Drinks_F,text='IcedCofeeLatte',variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='peru',command=chk_IcedCofeeLatte).grid(row=5,sticky=W)
LemonJuice=Checkbutton(Drinks_F,text='LemonJuice',variable=var7,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='peru',command=chk_LemonJuice).grid(row=6,sticky=W)
OrangeJuice=Checkbutton(Drinks_F,text='OrangeJuice',variable=var8,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='peru',command=chk_OrangeJuice).grid(row=7,sticky=W)

txtMocha = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Mocha)
txtMocha.grid(row=0,column=1)

txtCappuccino = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Cappuccino)
txtCappuccino.grid(row=1,column=1)

txtVanillaLatte = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_VanillaLatte)
txtVanillaLatte.grid(row=2,column=1)

txtEspresso= Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Espresso)
txtEspresso.grid(row=3,column=1)

txtAmericano = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Americano)
txtAmericano.grid(row=4,column=1)

txtIcedCofeeLatte = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_IcedCofeeLatte)
txtIcedCofeeLatte.grid(row=5,column=1)

txtLemonJuice = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_LemonJuice)
txtLemonJuice.grid(row=6,column=1)

txtOrangeJuice = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_OrangeJuice)
txtOrangeJuice.grid(row=7,column=1)

Cookies = Checkbutton(Food_F,text="Cookies\t\t\t ",variable=var9,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='peru',command=chk_Cookies).grid(row=0,sticky=W)
Cheesecake = Checkbutton(Food_F,text="Cheesecake",variable=var10,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='peru',command=chk_Cheesecake).grid(row=1,sticky=W)
Tart = Checkbutton(Food_F,text="Tart ",variable=var11,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='peru',command=chk_Tart).grid(row=2,sticky=W)
RedVelvetCake = Checkbutton(Food_F,text="RedVelvetCake ",variable=var12,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='peru',command=chk_RedVelvetCake).grid(row=3,sticky=W)
Waffle = Checkbutton(Food_F,text="Waffle ",variable=var13,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='peru',command=chk_Waffle).grid(row=4,sticky=W)
Pie = Checkbutton(Food_F,text="Pie ",variable=var14,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='peru',command=chk_Pie).grid(row=5,sticky=W)
VanillaCake = Checkbutton(Food_F,text="VanillaCake ",variable=var15,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='peru',command=chk_VanillaCake).grid(row=6,sticky=W)
Pancake = Checkbutton(Food_F,text="Pancake ",variable=var16,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='peru',command=chk_Pancake).grid(row=7,sticky=W)

txtCookies=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Cookies)
txtCookies.grid(row=0,column=1)

txtCheesecake=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Cheesecake)
txtCheesecake.grid(row=1,column=1)

txtTart=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Tart)
txtTart.grid(row=2,column=1)

txtRedVelvetCake=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_RedVelvetCake)
txtRedVelvetCake.grid(row=3,column=1)

txtWaffle=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Waffle)
txtWaffle.grid(row=4,column=1)

txtPie=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Pie)
txtPie.grid(row=5,column=1)

txtVanillaCake=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_VanillaCake)
txtVanillaCake.grid(row=6,column=1)

txtPancake=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Pancake)
txtPancake.grid(row=7,column=1)

lblCostofDrinks=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Drinks\t',bg='peru',
                fg='black',justify=CENTER)
lblCostofDrinks.grid(row=0,column=0,sticky=W)
txtCostofDrinks=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofDrinks)
txtCostofDrinks.grid(row=0,column=1)

lblCostofFood=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Foods  ',bg='peru',
                fg='black',justify=CENTER)
lblCostofFood.grid(row=1,column=0,sticky=W)
txtCostofFood=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofFood)
txtCostofFood.grid(row=1,column=1)

lblServiceCharge=Label(Cost_F,font=('arial',14,'bold'),text='Service Charge',bg='peru',
                fg='black',justify=CENTER)
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1)

lblPaidTax=Label(Cost_F,font=('arial',14,'bold'),text='\tPaid Tax',bg='peru',bd=7,
                fg='black',justify=CENTER)
lblPaidTax.grid(row=0,column=2,sticky=W)
txtPaidTax=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=PaidTax)
txtPaidTax.grid(row=0,column=3)

lblSubTotal=Label(Cost_F,font=('arial',14,'bold'),text='\tSub Total',bg='peru',bd=7,
                fg='black',justify=CENTER)
lblSubTotal.grid(row=1,column=2,sticky=W)
txtSubTotal=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=SubTotal)
txtSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Cost_F,font=('arial',14,'bold'),text='\tTotal',bg='peru',bd=7,
                fg='black',justify=CENTER)
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=TotalCost)
txtTotalCost.grid(row=2,column=3)

txtReceipt=Text(Receipt_F,width=46,height=12,bg='white',bd=4,font=('arial',12,'bold'))
txtReceipt.grid(row=0,column=0)


btnTotal=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Total',
                        bg='peru',command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Receipt',
                        bg='peru',command=Receipt).grid(row=0,column=1)
btnReset=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Reset',
                        bg='peru',command=Reset).grid(row=0,column=2)
btnExit=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Exit',
                        bg='peru',command=iExit).grid(row=0,column=3)


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""




txtDisplay=Entry(Cal_F,width=45,bg='white',bd=4,font=('arial',12,'bold'),justify=RIGHT,textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

btn7=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='7',
                        bg='light yellow',command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='8',
                        bg='light yellow',command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='9',
                        bg='light yellow',command=lambda:btnClick(9)).grid(row=2,column=2)
btnAdd=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='+',
                        bg='light yellow',command=lambda:btnClick('+')).grid(row=2,column=3)
btn4=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='4',
                        bg='light yellow',command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='5',
                        bg='light yellow',command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='6',
                        bg='light yellow',command=lambda:btnClick(6)).grid(row=3,column=2)
btnSub=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='-',
                        bg='light yellow',command=lambda:btnClick('-')).grid(row=3,column=3)
btn1=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='1',
                        bg='light yellow',command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='2',
                        bg='light yellow',command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='3',
                        bg='light yellow',command=lambda:btnClick(3)).grid(row=4,column=2)
btnMulti=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='*',
                        bg='light yellow',command=lambda:btnClick('*')).grid(row=4,column=3)
btn0=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='0',
                        bg='light yellow',command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='C',
                        bg='light yellow',command=btnClear).grid(row=5,column=1)
btnEqual=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='=',
                        bg='light yellow',command=btnEquals).grid(row=5,column=2)
btnDiv=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='/',
                        bg='light yellow',command=lambda:btnClick('/')).grid(row=5,column=3)



root.mainloop()