from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import sqlite3
import tkinter as tk
import tkinter

conn = sqlite3.connect('company.db')

cr= conn.cursor()



#emp_ID,emp_name,emp_mobile = tk.StringVar(),tk.StringVar(),tk.StringVar()
#emp_person,emp_date,emp_place = tk.StringVar(),tkinter.StringVar(),tk.StringVar()


#emp_flat,emp_floor,emp_price = tk.StringVar(),tk.StringVar(),tk.StringVar()
#emp_pp,emp_deposite,emp_way = tk.StringVar(),tk.StringVar(),tk.StringVar()

#emp_total,emp_still,emp_age = tk.StringVar(),tk.StringVar()

cr.execute(""" create table if not exists company (ID TEXT NOT NULL PRIMARY KEY,


name text not null , mobile text not null , person text not null,
date text not null , place text not null , floor text not null , 
flat text not null , price text not null , pp text not null , 
deposite text not null , way text not null , total text not null ,
still text not null)

      """)



    
    



        







class student:
    
    def __init__(self,root) :
        self.root =root
        self.root.geometry('1350x690+1+1')
        self.root.title("شركة الرحاب للسياحة")
        self.root.configure(background="silver")
        self.root.resizable(False,False)
        title= Label(self.root,
        text = "[نظام تسجيل بيانات العملاء]",
        bg = "#1AAECB",
        font =("monospace",14),
        fg = "white"
        )
        title.pack(fill=X)
        


 
        self.ID1 = StringVar()
        self.name1 =StringVar()
        self.mobile1 = StringVar()
        self.person1 = StringVar()
        self.date1 =StringVar()
        self.place1 = StringVar()
        self.floor1 = StringVar()
        self.flat1 = StringVar()
        self.price1 = StringVar()
        self.pp1 =StringVar()
        self.deposite1 = StringVar()
        self.way1 = StringVar()
        self.total1= StringVar()
        self.still1= StringVar()











            
        

        def add_data():
            
            

            cr= conn.cursor()

          

            
            cr.execute("insert into company values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(self.ID1.get(),self.name1.get(),self.mobile1.get(),self.person1.get(),self.date1.get(),self.place1.get(),self.floor1.get(),self.flat1.get(),self.price1.get(),self.pp1.get(),self.deposite1.get(),self.way1.get(),self.total1.get(),self.still1.get())
                      )

            

            conn.commit()

            ID_Entry.delete(0, tk.END)
            
            name_Entry.delete(0, tk.END)
            
            mobile_Entry.delete(0, tk.END)
           
            person_Entry.delete(0, tk.END)
            

            date_Entry.delete(0, tk.END)
            
            place_Entry.delete(0, tk.END)
            
            floor_Entry.delete(0, tk.END)
            
            flat_Entry.delete(0, tk.END)
            

            price_Entry.delete(0, tk.END)
           
            pp_Entry.delete(0, tk.END)
            
            deposite_Entry.delete(0, tk.END)
            
            combo_way.delete(0, tk.END)
            

            total_Entry.delete(0, tk.END)
            
            still_Entry.delete(0, tk.END)

            

            def on_close(self):
          # Close the database connection when the window is closed
               conn.close()
               self.master.destroy()



            

            
        def fetchall():
                
              cr=conn.cursor()
              cr.execute("select * from company")
              rows =cr.fetchall()
              for row in rows:
                  return row
                  print(row)
                   
                   
        
        def delete(self):
             self.cr.execute("delete from compan where id=?",(id,))
             self.conn.commit()

        def update(self,ID1,name1,mobile1,person1,date1,place1,floor1,flat1,price1,pp1,deposite1,way1,total1,still1):
             
             self.cr.execute("update company set name=?,mobile=?,person=?,date=?,place=?,floor=?,flat=?,price=?,pp=?,deposite=?,way=?,total=?,still=?"
                             )


        def getdata(event):
             selected_row= self.employe_table.focus()
             data = self.employe_table.item(selected_row)
             global row
             row = data["values"]
             

             self.ID1.set(row[0]) 
             self.name1.set(row[1])
             self.mobile1.set(row[2]) 
             self.person1.set(row[3])
             self.date1.set(row[4])
             self.place1.set(row[5])
             self.floor1.set(row[6])
             self.flat1.set(row[7])
             self.price1.set(row[8])
             self.pp1.set(row[9])
             self.deposite1.set(row[10])
             self.way1.set(row[11])
             self.total1.set(row[12])
             self.still1.set(row[13])
             getdata()

             def displayall(self):
               self.employe_table.delete(*self.employe_table.get_children())
             
                  # Clear the treeview
             conn = sqlite3.connect('company.db')
             cr = conn.cursor()
             cr.execute("SELECT * FROM company")
             rows = cr.fetchall()
             for row in rows:
                    self.employe_table.insert('', tk.END, values=row[0:]) # Insert the row into the treeview
                    displayall()
             

        
                 
                    
            
            
            



##########################################33









        













      #########TOOLS##############

        Manage_Frame=Frame(self.root , bg= '#2c3e50')
        Manage_Frame.place(x=1140,y=28,width=210,height=600)
        lbl_ID = Label(Manage_Frame,text="كود العميل",bg='silver')
        lbl_ID.pack()
        ID_Entry =Entry(Manage_Frame,bd='2',textvariable=self.ID1,justify="center")
        ID_Entry.pack()

        lbl_name = Label(Manage_Frame,bg="white",text='اسم العميل',border=2)
        lbl_name.pack()
        name_Entry = Entry(Manage_Frame,bd='2',textvariable=self.name1,justify="center")
        name_Entry.pack()

        lbl_mobile = Label(Manage_Frame,bg="white",text="رقم الهاتف")
        lbl_mobile.pack()
        mobile_Entry = Entry(Manage_Frame,bd='2',textvariable=self.mobile1,justify="center")
        mobile_Entry.pack()

        lbl_person = Label(Manage_Frame,bg="white",text='عدد الافراد')
        lbl_person.pack()
        person_Entry = Entry(Manage_Frame,bd='2',textvariable=self.person1,justify="center")
        person_Entry.pack()
        
        lbl_date = Label(Manage_Frame,bg="white",text="تاريخ الفوج")
        lbl_date.pack()
        date_Entry = Entry(Manage_Frame,bd='2',textvariable=self.date1,justify="center")
        date_Entry.pack()

        lbl_place = Label(Manage_Frame,bg="white",text='المكان')
        lbl_place.pack()
        place_Entry = Entry(Manage_Frame,bd='2',textvariable=self.place1,justify="center")
        place_Entry.pack()

        lbl_floor = Label(Manage_Frame,bg="white",text="الدور")
        lbl_floor.pack()
        floor_Entry = Entry(Manage_Frame,bd='2',textvariable=self.floor1,justify="center")
        floor_Entry.pack()

        lbl_flat = Label(Manage_Frame,bg="white",text="الشقة")
        lbl_flat.pack()
        flat_Entry = Entry(Manage_Frame,bd='2',textvariable=self.flat1,justify="center")
        flat_Entry.pack()

        lbl_price = Label(Manage_Frame,bg="white",text="ثمن الشقة")
        lbl_price.pack()
        price_Entry = Entry(Manage_Frame,bd='2',textvariable=self.price1,justify="center")
        price_Entry.pack()

        lbl_pp = Label(Manage_Frame,bg="white",text="سعر مواصلات الفرد")
        lbl_pp.pack()
        pp_Entry = Entry(Manage_Frame,bd='2',textvariable=self.pp1,justify="center")
        pp_Entry.pack()

        lbl_deposite = Label(Manage_Frame,bg="white",text="المدفوع")
        lbl_deposite.pack()
        deposite_Entry = Entry(Manage_Frame,bd='2',textvariable=self.deposite1,justify="center")
        deposite_Entry.pack()

        lbl_way = Label(Manage_Frame,bg="white",text="طريقة الدفع")
        lbl_way.pack()
        combo_way =ttk.Combobox(Manage_Frame,textvariable=self.way1)
        combo_way ["value"]=("كاش","قسط شهرى")
        combo_way.pack()


        lbl_total = Label(Manage_Frame,bg="white",text="اجمالى سعر الموصلات")
        lbl_total.pack()
        total_Entry = Entry(Manage_Frame,bd='2',textvariable=self.total1,justify="center")
        total_Entry.pack()

        lbl_still = Label(Manage_Frame,bg="white",text="باقى المبلغ")
        lbl_still.pack()
        still_Entry= Entry(Manage_Frame,bd='2',textvariable=self.still1,justify="center")
        still_Entry.pack()
        #########BUTTONS################
        btn_Frame = Frame(self.root,bg="yellow")
        btn_Frame.place(x=0,y=627,width=1370,height=65)

        add_btn =Button(btn_Frame,text="ادخال البيانات",font=14,bg="#2D7A87",fg='white', command=add_data)
        add_btn.place(x=100,y=20,width=120,height=30)

        retrive_btn =Button(btn_Frame,text="استعادة البيانات",bg="#2D7A87",fg='white',font=14,command=fetchall)
        retrive_btn.place(x=300,y=20,width=120,height=30)

        update_btn =Button(btn_Frame,text="تعديل البيانات",bg="#2D7A87",fg='white',font=14)
        update_btn.place(x=500,y=20,width=120,height=30)
        
        delete_btn =Button(btn_Frame,text="مسح بيانات عميل",bg="#2D7A87",fg='white',font=14)
        delete_btn.place(x=700,y=20,width=120,height=30)

        showdata_btn =Button(btn_Frame,text="اظهارالبيانات",bg="#2D7A87",fg='white',font=14)
        showdata_btn.place(x=900,y=20,width=120,height=30)
        
        ###########البحث search######################
        search_Frame =Frame(self.root,bg="red")
        search_Frame.place(x=1,y=28,width=1138,height=50)

        search_lbl=Label(search_Frame,text="بحث بيانات عميل",bg="white")
        search_lbl.place(x=1034,y=12)

        combo_search =ttk.Combobox(search_Frame,justify="center")
        combo_search['value'] = ('','name','place','date','flat')
        combo_search.place(x=880,y=12)

        search_Entry =Entry(search_Frame,justify="center")
        search_Entry.place(x=740,y=12)

        search_btn =Button(search_Frame,text='بحث',bg="silver")
        search_btn.place(x=600,y=12,width=120,height=20)

        #-------details window-----------#
        details_Frame = Frame(self.root,bg='silver')
        details_Frame.place(x=1,y=80,width=1138,height=549)
        
                     #-------scroll----------------
        scroll_y = Scrollbar(details_Frame,orient="vertical")
         
         #---------------------treeveiw----------------


        self.employe_table =ttk.Treeview(details_Frame,
                                          columns=('ID','اسم العميل',
                                                   'رقم الهاتف',
                                                   'عدد الافراد',
                                                   'تايخ الفوج',
                                                   'المكان',
                                                   'الدور',
                                                   'الشقة',
                                                   'ثمن الشقة',
                                                   'سعر المواصلات للفرد',
                                                   'المدفوع',
                                                   'طريقة الدفع',
                                                   'اجمالى سعر المواصلات',
                                                   'باقى المبلغ'),
                                                   yscrollcommand = scroll_y.set)
                                                   
        self.employe_table.place(x=1,y=1,width=1300,height=550)
        
        


        
             
             
         
        self.employe_table['show'] ='headings'
        self.employe_table.heading(0,text='ID')
        self.employe_table.heading(1,text='اسم العميل')
        self.employe_table.heading(2,text='رقم الهاتف')
        self.employe_table.heading(3,text='الافراد')
        self.employe_table.heading(4,text='الفوج')
        self.employe_table.heading(5,text='المكان')
        self.employe_table.heading(6,text='الدور')
        self.employe_table.heading(7,text='الشقة')
        self.employe_table.heading(8,text='ثمن الشقة')
        self.employe_table.heading(9,text='سعر المواصلات')
        self.employe_table.heading(10,text='المدفوع')
        self.employe_table.heading(11,text='طريقة الدفع')
        self.employe_table.heading(12,text='اجمالى المواصلات')
        self.employe_table.heading(13,text='باقى المبلغ')
        
        self.employe_table.column(0,width='1')
        self.employe_table.column(1,width='70')
        self.employe_table.column(2,width='70')
        self.employe_table.column(3,width='5')
        self.employe_table.column(4,width='5')
        self.employe_table.column(5,width='10')
        self.employe_table.column(6,width='5')
        self.employe_table.column(7,width='5')
        self.employe_table.column(8,width='10')
        self.employe_table.column(9,width='10')
        self.employe_table.column(10,width='15')
        self.employe_table.column(11,width='10')
        self.employe_table.column(12,width='10')
        self.employe_table.column(13,width='10')

        









    
root =Tk()
ob = student(root)
root.mainloop()