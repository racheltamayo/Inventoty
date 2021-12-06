from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import *
from tkcalendar import Calendar, DateEntry


db=Database("SqliteDatabase.db")


window=Tk()
window.title("SQLite")
window.geometry("1280x720")
window.resizable(width=FALSE, height=FALSE)

name=StringVar()
price=StringVar()
status=StringVar()
serial=StringVar()
stock=StringVar()
exp=StringVar()
def form1():


    def form2():
        button4.destroy()

        def back():
            frame1.destroy()
            frame2.destroy()
            txtName.destroy()
            txtPrice.destroy()
            cb.destroy()
            txtSerial.destroy()
            lblStock.destroy()
            txtExp.destroy()
            btn_frame.destroy()
            btnSub.destroy()
            btnUp.destroy()
            btnDel.destroy()
            myFrame.destroy()
            table.destroy()
            btnClr.destroy()

            form1()

        frame1=Frame(window)
        frame1.configure(bg='#d1b2ff')
        frame1.place(x=780,y=200,width=500,height=720)
        frame2=Frame(window)
        frame2.place(x=1300,y=0,width=0,height=0)

        txtName=Entry(frame2,textvariable=name,font=("times",16),width=43)
        txtName.grid(row=1,column=1)


        txtPrice=Entry(frame2,font=("times",16),textvariable=price,width=43)
        txtPrice.grid(row=2,column=1)


        cb=ttk.Combobox(frame2,width=41,textvariable=status,state="readonly",font=("times",16))
        cb['values']=("AVAILABLE","NOT AVAILABLE")
        cb.grid(row=3,column=1)


        txtSerial=Entry(frame2,font=("times",16),width=43,textvariable=serial)
        txtSerial.grid(row=4,column=1)

        lblStock=Label(frame1,text="STOCK",bg="#d1b2ff",fg="#381919",font=("times",20),pady=20)
        lblStock.grid(row=5,column=0)

        txtStock=Entry(frame1,font=("times",20),textvariable=stock,width=15)
        txtStock.grid(row=5,column=1)

        txtExp = DateEntry(frame2, width= 41, background= "#9ef7fb", foreground= "black",pady=10,font=("times",16))
        txtExp.grid(row=6,column=1)

        btn_frame=Frame(frame1,bg="#2d3436")
        btn_frame.grid(row=8,column=1,columnspan=4)




        def fetchData():
            table.delete(*table.get_children())
            count=0
            for row in db.fetch_record():
                count+=1
                table.insert("",END,values=(count,row[0],row[1],row[2],row[3],row[4],row[5],row[6]))

        def addData():
            if txtName.get()=="" or txtPrice.get()=="" or txtSerial.get()=="" or txtStock.get()=="" or txtExp.get()=="":
                messagebox.showinfo("Message","Please Fill All Records")
            else:
                db.insert(txtName.get(),txtPrice.get(),cb.get(),txtSerial.get(),txtStock.get(),txtExp.get())
                fetchData()
                clearData()
                messagebox.showinfo("Message","Record Insert Successfully")

        def getrecord(event):
            srow = table.focus()
            data = table.item(srow)
            global row
            row = data['values']
            name.set(row[2])
            price.set(row[3])
            status.set(row[4])
            serial.set(row[5])
            stock.set(row[6])
            exp.set(row[7])


        def getrecord2():
            db.search()
            global row
            row = data['values']
            name.set(row[2])
            price.set(row[3])
            status.set(row[4])
            serial.set(row[5])
            stock.set(row[6])
            exp.set(row[7])

        def updateData():
            if txtName.get() == "" or txtPrice.get() == "" or txtSerial.get() == "" or cb.get() == "" or txtStock.get() == "" or txtExp.get() == "":
                messagebox.showinfo("Message", "Please Fill All Records")
            else:
                db.update_record(txtName.get(), txtPrice.get(), cb.get(), txtSerial.get(), txtStock.get(), txtExp.get(), (row[1]))
                fetchData()
                clearData()
                messagebox.showinfo("Message", "Record Update Successfully")

        def deleteData():
            db.remove_record(row[1])
            fetchData()
            clearData()
            messagebox.showinfo("Message", "Record Delete Successfully")

        def clearData():
            name.set("")
            price.set("")
            status.set("")
            stock.set("")
            exp.set("")
            serial.set("")
        def button_click(number):
            """Displays the numbers pressed"""
            # inputScreen.delete(0,END) # initially for testing purposes
            # inputScreen.insert(0,number) # inserts from the front(0)
            txtStock.insert(END, number)
            
        def button_subtract():
            """Specifies subtraction and automatically captures the previously typed in number"""

            fnum = txtStock.get()
            global firstNumber
            global math
            math = "subtraction"
            firstNumber = int(fnum)
            txtStock.delete(0, END)
        def button_equals():
            """Triggers display of results"""

            second_num = txtStock.get()
            txtStock.delete(0, END)
            txtStock.insert(0, int(firstNumber) - int(second_num))


        buttonOne = Button(btn_frame, text="1",bg="#01a3a4",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"), command=lambda: button_click(1))
        buttonTwo = Button(btn_frame, text="2",bg="#01a3a4",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"), command=lambda: button_click(2))
        buttonThree = Button(btn_frame, text="3",bg="#01a3a4",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"), command=lambda: button_click(3))

        buttonFour = Button(btn_frame, text="4",bg="#01a3a4",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"), command=lambda: button_click(4))
        buttonFive = Button(btn_frame, text="5",bg="#01a3a4",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"), command=lambda: button_click(5))
        buttonSix = Button(btn_frame, text="6",bg="#01a3a4",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"), command=lambda: button_click(6))

        buttonSeven = Button(btn_frame, text="7",bg="#01a3a4",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"), command=lambda: button_click(7))
        buttonEight = Button(btn_frame, text="8",bg="#01a3a4",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"), command=lambda: button_click(8))
        buttonNine = Button(btn_frame, text="9",bg="#01a3a4",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"), command=lambda: button_click(9))

        buttonZero = Button(btn_frame, text="0",bg="#01a3a4",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"), command=lambda: button_click(0))


        btnSub=Button(btn_frame,text=" - ",bg="#01a3a4",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"),command=button_subtract)
        btnSub.grid(row=4,column=1)
        
        btnUp=Button(btn_frame,text=" = ",bg="#F79F1F",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"),command=button_equals)
        btnUp.grid(row=4,column=2)

        buttonOne.grid(row=3, column=0)
        buttonTwo.grid(row=3, column=1)
        buttonThree.grid(row=3, column=2)

        buttonFour.grid(row=2, column=0)
        buttonFive.grid(row=2, column=1)
        buttonSix.grid(row=2, column=2)

        buttonSeven.grid(row=1, column=0)
        buttonEight.grid(row=1, column=1)
        buttonNine.grid(row=1, column=2)

        buttonZero.grid(row=4, column=0)
                    
        
        btnDel=Button(btn_frame,text="Update",bg="#ee5253",fg="white",width=16,padx=20,pady=5,font=("times",16,"bold"),command=updateData)
        btnDel.grid(row=6,column=0,columnspan=2)

        btnClr=Button(btn_frame,text="LogOut",bg="#1289A7",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"),command=back)
        btnClr.grid(row=6,column=2)



        myFrame=Frame(window)
        myFrame.configure(bg='#feee6b')
        myFrame.place(x=0,y=200,width=780,height=720)

        style=ttk.Style()
        style.configure("Treeview",font=("times",15),rowheight=35)
        style.configure("Treeview.Heading",font=("times",16,"bold"))

        table=ttk.Treeview(myFrame,columns=(0,1,2,3,4,5,6,7))

        table.column("0",stretch=NO,width=0,anchor=CENTER)
        table.column("1",stretch=NO,width=0,anchor=CENTER)
        table.column("2",stretch=NO,width=290,anchor=CENTER)
        table.column("3",stretch=NO,width=200)
        table.column("4",stretch=NO,width=200,anchor=CENTER)
        table.column("5",stretch=NO,width=0,anchor=CENTER)
        table.column("6",stretch=NO,width=0,anchor=CENTER)
        table.column("7",stretch=NO,width=0,anchor=CENTER)

        table.heading("0",text="S.NO")
        table.heading("1",text="NO.")
        table.heading("2",text="ITEM")
        table.heading("3",text="PRICE")
        table.heading("4",text="STATUS")
        table.heading("5",text="SERIAL NO.")
        table.heading("6",text="STOCK")
        table.heading("7",text="EXP. DATE")
        table["show"]='headings'
        table.bind("<ButtonRelease-1>",getrecord)
        table.pack(fill=X)

        fetchData()




    def form3():
        entry.destroy()
        entry2.destroy()
        label.destroy()
        button4.destroy()
        label3=Label(window, text='This is the first tab', font=('Times_New_Roman',25))
        label3.pack()
        def back2():
            label3.destroy()
            button3.destroy()
            myFrame.destroy()
            table.destroy()
            frame1.destroy()
            lblTitle.destroy()
            lblTitle2.destroy()
            lblName.destroy()
            txtName.destroy()
            txtPrice.destroy()
            lblStatus.destroy()
            cb.destroy()
            lblSerial.destroy()
            txtSerial.destroy()
            lblStock.destroy()
            txtStock.destroy()
            lblExp.destroy()
            txtExp.destroy()
            btn_frame.destroy()

            
            form1()


        frame1=Frame(window)
        frame1.configure(bg='#9ef7fb')
        frame1.place(x=0,y=0,width=1280,height=350)

        lblTitle=Label(frame1,bg="#9bf5f9",text="Dolce Treats Bread & Pastry",font=("Monotype Corsiva",40,"bold"),fg="black",pady=10)
        lblTitle.place(x=690, y=80)

        lblTitle2=Label(frame1,bg="#9bf5f9",text="INVENTORY SYSTEM",font=("Times New Roman",23,"bold"),fg="black",pady=10)
        lblTitle2.place(x=800, y=150)

        lblName=Label(frame1,text="ITEM",bg="#9ef7fb",fg="black",font=("times",16),pady=10)
        lblName.grid(row=1,column=0)

        txtName=Entry(frame1,textvariable=name,font=("times",16),width=43)
        txtName.grid(row=1,column=1)

        lblPrice=Label(frame1,text="PRICE",bg="#9ef7fb",fg="black",font=("times",16),pady=10)
        lblPrice.grid(row=2,column=0)

        txtPrice=Entry(frame1,font=("times",16),textvariable=price,width=43)
        txtPrice.grid(row=2,column=1)

        lblStatus=Label(frame1,text="STATUS",bg="#9ef7fb",fg="black",font=("times",16),pady=10)
        lblStatus.grid(row=3,column=0)

        cb=ttk.Combobox(frame1,width=41,textvariable=status,state="readonly",font=("times",16))
        cb['values']=("AVAILABLE","NOT AVAILABLE")
        cb.grid(row=3,column=1)

        lblSerial=Label(frame1,text="SERIAL NO.",bg="#9ef7fb",fg="black",font=("times",16),pady=10)
        lblSerial.grid(row=4,column=0)

        txtSerial=Entry(frame1,font=("times",16),width=43,textvariable=serial)
        txtSerial.grid(row=4,column=1)

        lblStock=Label(frame1,text="STOCK",bg="#9ef7fb",fg="black",font=("times",16),pady=10)
        lblStock.grid(row=5,column=0)

        txtStock=Entry(frame1,font=("times",16),textvariable=stock,width=43)
        txtStock.grid(row=5,column=1)

        lblExp=Label(frame1,text="EXPIRATION DATE",bg="#9ef7fb",fg="black",font=("times",16),pady=10)
        lblExp.grid(row=6,column=0)

        txtExp = DateEntry(frame1, width= 41, background= "#9ef7fb", foreground= "black",pady=10,font=("times",16))
        txtExp.grid(row=6,column=1)

        btn_frame=Frame(frame1,bg="#9ef7fb")
        btn_frame.grid(row=7,column=1,columnspan=4)




        def fetchData():
            table.delete(*table.get_children())
            count=0
            for row in db.fetch_record():
                count+=1
                table.insert("",END,values=(count,row[0],row[1],row[2],row[3],row[4],row[5],row[6]))

        def addData():
            if txtName.get()=="" or txtPrice.get()=="" or txtSerial.get()=="" or txtStock.get()=="" or txtExp.get()=="":
                messagebox.showinfo("Message","Please Fill All Records")
            else:
                db.insert(txtName.get(),txtPrice.get(),cb.get(),txtSerial.get(),txtStock.get(),txtExp.get())
                fetchData()
                clearData()
                messagebox.showinfo("Message","Record Insert Successfully")

        def getrecord(event):
            srow = table.focus()
            data = table.item(srow)
            global row
            row = data['values']
            name.set(row[2])
            price.set(row[3])
            status.set(row[4])
            serial.set(row[5])
            stock.set(row[6])
            exp.set(row[7])

            


        def getrecord2():
            db.search()
            global row
            row = data['values']
            name.set(row[2])
            price.set(row[3])
            status.set(row[4])
            serial.set(row[5])
            stock.set(row[6])
            exp.set(row[7])

        def updateData():
            if txtName.get() == "" or txtPrice.get() == "" or txtSerial.get() == "" or cb.get() == "" or txtStock.get() == "" or txtExp.get() == "":
                messagebox.showinfo("Message", "Please Fill All Records")
            else:
                db.update_record(txtName.get(), txtPrice.get(), cb.get(), txtSerial.get(), txtStock.get(), txtExp.get(), (row[1]))
                fetchData()
                clearData()
                messagebox.showinfo("Message", "Record Update Successfully")

        def deleteData():
            db.remove_record(row[1])
            fetchData()
            clearData()
            messagebox.showinfo("Message", "Record Delete Successfully")

        def clearData():
            name.set("")
            price.set("")
            status.set("")
            stock.set("")
            exp.set("")
            serial.set("")


        
        button3=Button(frame1,text='LogOut',bg="#01a3a4",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"),command=back2)
        button3.place(x=910, y=220)


        btnSub=Button(btn_frame,text="Insert",bg="#01a3a4",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"),command=addData)
        btnSub.grid(row=0,column=0)

        btnUp=Button(btn_frame,text="Update",bg="#F79F1F",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"),command=updateData)
        btnUp.grid(row=0,column=1)

        btnDel=Button(btn_frame,text="Delete",bg="#ee5253",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"),command=deleteData)
        btnDel.grid(row=0,column=2)

        btnClr=Button(btn_frame,text="Clear",bg="#1289A7",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"),command=clearData)
        btnClr.grid(row=0,column=3)

        myFrame=Frame(window)
        myFrame.configure(bg='#9ef7fb')
        myFrame.place(x=0,y=350,width=1280,height=500)

        style=ttk.Style()
        style.configure("Treeview",font=("times",15),rowheight=35)
        style.configure("Treeview.Heading",font=("times",16,"bold"))

        table=ttk.Treeview(myFrame,columns=(0,1,2,3,4,5,6,7))

        table.column("0",stretch=NO,width=0,anchor=CENTER)
        table.column("1",stretch=NO,width=0,anchor=CENTER)
        table.column("2",stretch=NO,width=290,anchor=CENTER)
        table.column("3",stretch=NO,width=200)
        table.column("4",stretch=NO,width=200,anchor=CENTER)
        table.column("5",stretch=NO,width=200,anchor=CENTER)
        table.column("6",stretch=NO,width=190,anchor=CENTER)
        table.column("7",stretch=NO,width=200,anchor=CENTER)

        table.heading("0",text="S.NO")
        table.heading("1",text="NO.")
        table.heading("2",text="ITEM")
        table.heading("3",text="PRICE")
        table.heading("4",text="STATUS")
        table.heading("5",text="SERIAL NO.")
        table.heading("6",text="STOCK")
        table.heading("7",text="EXP. DATE")
        table["show"]='headings'
        table.bind("<ButtonRelease-1>",getrecord)
        table.pack(fill=X)

        fetchData()
            
    
     
    label=Label(window, text='Dolce Treats', bg="#feee6b" ,font=('Monotype Corsiva',90), fg="#381919")
    label.place(x=610, y=10)
    label2=Label(window, text='BREAD AND PASTRY', bg="#feee6b", font=('Courier New',30), fg="#381919")
    label2.place(x=700, y=130)



    label3=Label(window, text='USERNAME', bg="#fdaff3" ,font=('Courier New',10), fg="black")
    label3.place(x=100, y=400)
    entry = Entry(window,font=('Courier New',15))
    entry.place(x=100, y=420,height=30, width=200)

    label4=Label(window, text='PASSWORD', bg="#fdaff3", font=('Courier New',10), fg="black")
    label4.place(x=100, y=460)
    entry2 = Entry(window,font=(15),show="*")
    entry2.place(x=100, y=480,height=30, width=200)
    

    def on_button():
        if entry.get() == "admin" and entry2.get() == "admin":
            form3()
        else:
            entry.delete(0, END)
            entry2.delete(0, END)


    button4=Button(window,bg="#F79F1F",fg="white",width=6,padx=10,pady=2,text='ADMIN', font=('Courier New',20),command=on_button)
    button4.place(x=150, y=550)


    label5=Label(window, text='USERNAME', bg="#9ff8fc" ,font=('Courier New',10), fg="black")
    label5.place(x=600, y=400)
    entry3 = Entry(window,font=('Courier New',15))
    entry3.place(x=600, y=420,height=30, width=200)

    label6=Label(window, text='PASSWORD', bg="#9ff8fc", font=('Courier New',10), fg="black")
    label6.place(x=600, y=460)
    entry4 = Entry(window,font=(15),show="*")
    entry4.place(x=600, y=480,height=30, width=200)
    

    def on_button2():
        if entry3.get() == "user" and entry4.get() == "user":
            form2()
        else:
            entry3.delete(0, END)
            entry4.delete(0, END)


    button5=Button(window,bg="#F79F1F",fg="white",width=6,padx=10,pady=2,text='USER', font=('Courier New',20),command=on_button2)
    button5.place(x=650, y=550)

    

    

bg = PhotoImage(file = "pic2.png")
  
# Create Canvas
canvas1 = Canvas(window, width = 1280,
                height = 720) 
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, 
                    anchor = "nw")
 
            
            

    

    
form1()
window.mainloop()
