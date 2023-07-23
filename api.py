from random import randint
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import re
root=Tk()
root.title("Cab Booking System")
root.geometry("1000x600+100+50")
root.resizable(False,False)

def create_update_profile():
    root7=Tk()
    root7.title("Cab Booking System")
    root7.geometry("1200x700+20+30")
    root7.resizable(False,False)
    ##-----------------------------------------------------------------------------------------------------------------------------------##
    def signup():
        v11=v5.get()
        
        if(v1.get()=="" or v2.get()==""  or v4.get()=="" or v5.get()=="" or v8.get()=="" or v9.get()==""):
            messagebox.showerror("Error","All fields are mandatory")
        elif(not(v11.isdigit()) or len(v11)!=10):
            messagebox.showerror("Error","Enter correct mobile number")
        else:
            try:
                con=mysql.connector.connect(host="localhost",user="root",password="password",database="booking")
                cur=con.cursor()
                cur.execute("update login_details set First_Name=%s,Last_Name=%s,Mobile=%s,state=%s,city=%s where E_mail=%s",
                        (v1.get(),v2.get(),v5.get(),v8.get(),v9.get(),v4.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Data Successfully Updated")
                root7.destroy()
                create_sel_choice()
            except Exception as es:
                messagebox.showerror("Error",f"Eroor due to: {str(es)}")
    def back_fn():
        root7.destroy()
        create_sel_choice()
    def reset_fn():
        f_n.delete(0,END)
        l_n.delete(0,END)
        Phoneno.delete(0,END)
        State_t.delete(0,END)
        city_t.delete(0,END)
    ##-----------------------------------------------------------------------------------------------------------------------------------##

    bg_image=ImageTk.PhotoImage(file="backg.jpg")
    bg_label=Label(root7,image=bg_image).place(x=0,y=0,relheight=1,relwidth=1)
    signup_frame=Frame(root7,bg="white",highlightbackground="grey",highlightthickness=3).place(x=85,y=100,height=500,width=480)
    Detail_label=Label(signup_frame,text="Enter Your Details",font=("Impact",35,"bold"),fg="white",bg="orange").place(x=115,y=65)
    l1=Label(signup_frame,text="First Name",font=(15),bg="white").place(x=110,y=170)
    v1=StringVar()
    f_n=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v1)
    f_n.place(x=300,y=170)
    l2=Label(signup_frame,text="Last Name",font=(15),bg="white").place(x=110,y=205)
    v2=StringVar()
    l_n=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v2)
    l_n.place(x=300,y=205)
    e_mail_label=Label(signup_frame,text="E-mail",font=(15),bg="white").place(x=110,y=275)
    v4=StringVar()
    e_mail=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v4)
    e_mail.place(x=300,y=275)
    e_mail.insert(0,v17.get())
    e_mail.configure(state='disabled')
    Phone_label=Label(signup_frame,text="Mobile No.",font=(15),bg="white").place(x=110,y=310)
    v5=StringVar()
    Phoneno=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v5)
    Phoneno.place(x=300,y=310)
    
    State_l=Label(signup_frame,text="State",font=(15),bg="white").place(x=110,y=415)
    v8=StringVar()
    State_t=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v8)
    State_t.place(x=300,y=415)
    City_l=Label(signup_frame,text="City",font=(15),bg="white").place(x=110,y=450)
    v9=StringVar()
    city_t=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v9)
    city_t.place(x=300,y=450)
    submit_button=Button(signup_frame,text="Update",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=signup).place(x=390,y=520)
    reset_button=Button(signup_frame,text="Reset",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=reset_fn).place(x=300,y=520)
    back_button=Button(signup_frame,text="Back",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=back_fn).place(x=215,y=520)
    root7.mainloop()

def create_forgot_pass():
    root5=Tk()
    root5.title("Cab Booking System")
    root5.geometry("700x500+300+170")
    root5.resizable(False,False)
    def submit_fn():
        v5=v1.get()
        v6=v2.get()
        if(v4.get()=="" or v1.get()=="" or v2.get()==""):
            messagebox.showerror("Error","All Fields Are Mandatory")
        elif(len(v5)<6):
            messagebox.showerror("Error","Password must be greater than six.")
        elif(v2.get()!=v1.get()):
            messagebox.showerror("Error","Confirm Password must be same as Password")
        else:
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",password="password",database="booking")
                cur=mydb.cursor() 
                cur.execute("select * from Login_details where E_mail=%s",(v4.get(),))
                result=cur.fetchone()
                print(result)
                if result==None:
                    messagebox.showerror("Error","User Not Found")
                else:
                    curr2=mydb.cursor()
                    curr2.execute("update login_details set password=%s,Confirm_password=%s where E_mail=%s",(v1.get(),v2.get(),v4.get()))
                    mydb.commit()
                    messagebox.showinfo("Sucess","Password successfully updated")
                mydb.close()
                root5.destroy()
                import api
            except Exception as es:
                messagebox.showerror("Error",f"Eroor due to: {str(es)}") 

    bg_image=ImageTk.PhotoImage(file="backg.jpg")
    bg_label=Label(root5,image=bg_image).place(x=0,y=0,relheight=1,relwidth=1)
    signup_frame=Frame(root5,bg="white",highlightbackground="grey",highlightthickness=3).place(x=85,y=100,height=280,width=480)
    Detail_label=Label(signup_frame,text="Change Password",font=("Impact",30,"bold"),fg="white",bg="orange").place(x=115,y=70)
    e_mail_label=Label(signup_frame,text="Enter Your E-mail",font=(15),bg="white").place(x=110,y=160)
    v4=StringVar()
    e_mail=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v4)
    e_mail.place(x=300,y=160)
    np_label=Label(signup_frame,text="New Password",font=(15),bg="white").place(x=110,y=195)
    v1=StringVar()
    np=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v1)
    np.place(x=300,y=195)
    npc_label=Label(signup_frame,text="Confirm Password",font=(15),bg="white").place(x=110,y=230)
    v2=StringVar()
    npc=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v2)
    npc.place(x=300,y=230)
    submit_button=Button(signup_frame,text="Submit",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=submit_fn).place(x=390,y=300)

    root5.mainloop()

def create_signup():
    root1=Tk()
    root1.title("Cab Booking System")
    root1.geometry("1200x700+20+30")
    root1.resizable(False,False)
    ##-----------------------------------------------------------------------------------------------------------------------------------##
    def signup():
        v10=StringVar()
        v10=v6.get()
        v11=v5.get()
        validate='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(validate,v4.get())):   
            pass   
        else:   
            messagebox.showerror("Error","Invalid Email")
        if(v1.get()=="" or v2.get()=="" or cmb_gender.get()=="Select" or v4.get()=="" or v5.get()=="" or v6.get()=="" or v7.get()=="" or v8.get()=="" or v9.get()==""):
            messagebox.showerror("Error","All fields are mandatory")
        elif(len(v10)<6):
            messagebox.showerror("Error","Password must be greater than six.")
        elif(v6.get()!=v7.get()):
            messagebox.showerror("Error","Password must be same")
        elif(not(v11.isdigit()) or len(v11)!=10):
            messagebox.showerror("Error","Enter correct mobile number")
        else:
            try:
                con=mysql.connector.connect(host="localhost",user="root",password="password",database="booking")
                cur=con.cursor()
                cur.execute("insert into Login_details() values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (v1.get(),v2.get(),cmb_gender.get(),v4.get(),v5.get(),v6.get(),v7.get(),v8.get(),v9.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Successfully Signed Up")
                root1.destroy()
                import api
            except Exception as es:
                messagebox.showerror("Error",f"Eroor due to: {str(es)}")
    def back_fn():
        root1.destroy()
        import api
    def reset_fn():
        f_n.delete(0,END)
        l_n.delete(0,END)
        cmb_gender.current(0)
        e_mail.delete(0,END)
        Phoneno.delete(0,END)
        pass_text.delete(0,END)
        passc_text.delete(0,END)
        State_t.delete(0,END)
        city_t.delete(0,END)
    ##-----------------------------------------------------------------------------------------------------------------------------------##

    bg_image=ImageTk.PhotoImage(file="backg.jpg")
    bg_label=Label(root1,image=bg_image).place(x=0,y=0,relheight=1,relwidth=1)
    signup_frame=Frame(root1,bg="white",highlightbackground="grey",highlightthickness=3).place(x=85,y=100,height=500,width=480)
    Detail_label=Label(signup_frame,text="Enter Your Details",font=("Impact",35,"bold"),fg="white",bg="orange").place(x=115,y=65)
    l1=Label(signup_frame,text="First Name",font=(15),bg="white").place(x=110,y=170)
    v1=StringVar()
    f_n=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v1)
    f_n.place(x=300,y=170)
    l2=Label(signup_frame,text="Last Name",font=(15),bg="white").place(x=110,y=205)
    v2=StringVar()
    l_n=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v2)
    l_n.place(x=300,y=205)
    gender_label=Label(signup_frame,text="Gender",font=(15),bg="white").place(x=110,y=240)
    cmb_gender=ttk.Combobox(signup_frame,font=("times new roman",15),state="readonly",justify="center")
    cmb_gender['values']=("Select","Male","Female","Other")
    cmb_gender.place(x=300,y=240,width=200)
    cmb_gender.current(0)
    e_mail_label=Label(signup_frame,text="E-mail",font=(15),bg="white").place(x=110,y=275)
    v4=StringVar()
    e_mail=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v4)
    e_mail.place(x=300,y=275)
    Phone_label=Label(signup_frame,text="Mobile No.",font=(15),bg="white").place(x=110,y=310)
    v5=StringVar()
    Phoneno=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v5)
    Phoneno.place(x=300,y=310)
    Password_label=Label(signup_frame,text="Password",font=(15),bg="white").place(x=110,y=345)
    v6=StringVar()
    pass_text=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v6)
    pass_text.place(x=300,y=345)
    Passwordc_label=Label(signup_frame,text="Confirm Password",font=(15),bg="white").place(x=110,y=380)
    v7=StringVar()
    passc_text=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v7)
    passc_text.place(x=300,y=380)
    State_l=Label(signup_frame,text="State",font=(15),bg="white").place(x=110,y=415)
    v8=StringVar()
    State_t=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v8)
    State_t.place(x=300,y=415)
    City_l=Label(signup_frame,text="City",font=(15),bg="white").place(x=110,y=450)
    v9=StringVar()
    city_t=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v9)
    city_t.place(x=300,y=450)
    submit_button=Button(signup_frame,text="Sign Up",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=signup).place(x=390,y=520)
    reset_button=Button(signup_frame,text="Reset",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=reset_fn).place(x=300,y=520)
    back_button=Button(signup_frame,text="Back",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=back_fn).place(x=215,y=520)
    root1.mainloop()

def create_booking_details():
    root6=Tk()
    root6.title("Cab Booking System")
    root6.geometry("1500x700+20+20")
    root6.resizable(False,False)
    mydb=mysql.connector.connect(host="localhost",user="root",password="password",database="booking")
    cur=mydb.cursor() 
    def show_fn():
        try:
            cur.execute("select * from Login_details where E_mail=%s",(v1.get(),))
            result=cur.fetchone()
            print(result)
            if result==None:
                messagebox.showerror("Error","User Not Found")
            else:
                curr2=mydb.cursor()
                curr2.execute("select Pickup_Location,Drop_Location,Pickup_date,Pickup_Time_hrs,Pickup_Time_min,Insurance_opted,Total_Amount from booking_details where Email=%s",(v1.get(),))
            
            
                i=0
                for val in curr2:
                    tree.insert('',i,text="",values=(val[0],val[1],val[2],val[3],val[4],val[5],val[6]))
                    i=i+1
                tree.place(x=110,y=250)
        except Exception as es:
                messagebox.showerror("Error",f"Eroor due to: {str(es)}")
    def back_fn():
        root6.destroy()
        create_sel_choice()
    def delete_fn():
        sel_item=tree.selection()[0]
        print(tree.item(sel_item)['values'])
        pic_l=tree.item(sel_item)['values'][0]
        query="delete from booking_details where Pickup_Location=%s"
        sel_data=(pic_l,)
        cur2=mydb.cursor()
        cur2.execute(query,sel_data)
        mydb.commit()
        tree.delete(sel_item)
        messagebox.showinfo("Sucess","Booking cancelled Sucessfully")
        mydb.close()
            

    bg_image=ImageTk.PhotoImage(file="backg.jpg")
    bg_label=Label(root6,image=bg_image).place(x=0,y=0,relheight=1,relwidth=1)
    frame1=Frame(root6,bg="white",highlightbackground="grey",highlightthickness=3).place(x=85,y=100,height=480,width=1100)
    tree=ttk.Treeview(frame1)
    tree['show']='headings'
    s=ttk.Style(frame1)
    s.theme_use("clam")
    tree["columns"]=("pickup","drop","date","time_hrs","time_min","insurance","total")
    tree.column("pickup",width=150,minwidth=150,anchor=CENTER)
    tree.column("drop",width=150,minwidth=150,anchor=CENTER)
    tree.column("date",width=150,minwidth=150,anchor=CENTER)
    tree.column("time_hrs",width=150,minwidth=150,anchor=CENTER)
    tree.column("time_min",width=150,minwidth=150,anchor=CENTER)
    tree.column("insurance",width=150,minwidth=150,anchor=CENTER)
    tree.column("total",width=150,minwidth=150,anchor=CENTER)
    tree.heading("pickup",text="Pickup Location",anchor=CENTER)
    tree.heading("drop",text="Drop Location",anchor=CENTER)
    tree.heading("date",text="Pickup Date",anchor=CENTER)
    tree.heading("time_hrs",text="Time_hrs",anchor=CENTER)
    tree.heading("time_min",text="Time_min",anchor=CENTER)
    tree.heading("insurance",text="Insurance Opted",anchor=CENTER)
    tree.heading("total",text="Total Amount",anchor=CENTER)
    l1=Label(frame1,text="Booking Details",font=("Impact",35,"bold"),bg="orange",fg="white").place(x=120,y=85)
    l2=Label(frame1,text="Your Email",font=(15),bg="white").place(x=110,y=180)
    v1=StringVar()
    email=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=v1)
    email.place(x=300,y=180,width=300)
    email.insert(0,v17.get())
    email.configure(state='disabled')
    show_button=Button(frame1,text="Show",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=show_fn).place(x=700,y=170)
    back_button=Button(frame1,text="Back",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=back_fn).place(x=1050,y=500)
    delete_button=Button(frame1,text="Cancel",font=("goudy old style",20),fg="white",bg="red",cursor="hand2",command=delete_fn).place(x=950,y=500)
    root6.mainloop()

def create_book_cab():
    root2=Tk()
    root2.title("Cab Booking System")
    root2.geometry("1000x700+300+50")
    root2.resizable(False,False)
    #--------------------------------------------------------------------------------------------------------------------------------#
    def reset_fn():
        txt_email.delete(0,END)
        pickup.delete(0,END)
        drop.delete(0,END)
        hrs_text.delete(0,END)
        min_text.delete(0,END)
        amount.delete(0,END)
        tax.delete(0,END)
        insurance.delete(0,END)
        total.delete(0,END)
        cmb_insurance.current(0)
    def calculate_fn():
        dummy_insurance=5
        dummy_charge=randint(150,2000)
        if pickup.get()=="" or drop.get()=="Select" or cmb_insurance.get()=="Select":
            messagebox.showerror("Error","Please fill all the details.")
        elif types.get()==1:
            amount.delete(0,END)
            amount.insert(END,dummy_charge)
        elif types.get()==2:
            dummy_charge=dummy_charge+100
            amount.delete(0,END)
            amount.insert(END,dummy_charge)
        elif cmb_insurance.get()=="Yes":
            insurance.delete(0,END)
            insurance.insert(0,dummy_insurance)
            
        elif cmb_insurance.get()=="No":
                insurance.delete(0,END)
                insurance.insert(0,dummy_insurance)
        else:
            messagebox.showerror("Error","Please Fill all details.")
        
        dummy_tax=0.05*dummy_charge
        
        total_charge=dummy_charge+dummy_tax+dummy_insurance
        tax.delete(0,END)
        tax.insert(0,dummy_tax)
        insurance.delete(0,END)
        insurance.insert(0,dummy_insurance)
        total.delete(0,END)
        total.insert(0,total_charge)
    def book_fn():
        validate='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        time_min_var=(int)(min_text.get())
        time_hrs_text=(int)(hrs_text.get())
        if(re.search(validate,v1.get())):   
            pass   
        else:   
            messagebox.showerror("Error","Invalid Email")   
        if(v1.get()=="" or pickup.get()=="" or drop.get()=="Select"  or hrs_text.get()=="" or min_text.get()=="" or cmb_insurance.get()=="Select"):
            messagebox.showerror("Error","All fields are mandatory")
        elif(time_hrs_text>=24 or time_hrs_text<=0):
            messagebox.showerror("Error","Enter correct time")
        elif(time_min_var>=59 or time_hrs_text<=0):
            messagebox.showerror("Eroor","Enter correct time")
        else:
            try:
                con=mysql.connector.connect(host="localhost",user="root",password="password",database="booking")
                cur=con.cursor()
                cur.execute("insert into booking_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (pickup.get(),drop.get(),cal.get_date(),hrs_text.get(),min_text.get(),cmb_insurance.get(),amount.get(),tax.get(),insurance.get(),total.get(),v1.get()))
                con.commit()
                messagebox.showinfo("Success","Cab Successfully Booked")
            except Exception as es:
                messagebox.showerror("Error",f"Eroor due to: {str(es)}")
        
    def exit_fn():
        root2.destroy()
    def  back_fn():
        root2.destroy()
        create_sel_choice()
        

    bg_image=ImageTk.PhotoImage(file="backg.jpg")
    bg_label=Label(root2,image=bg_image).place(x=0,y=0,relheight=1,relwidth=1)
    your_email=Label(root2,text="Enter Your E-mail",font=20,bg="white").place(x=85,y=75)
    v1=StringVar()
    txt_email=Entry(root2,font=("times new roman",15),bg="white",textvariable=v1)
    txt_email.place(x=275,y=75,width=250)
    txt_email.insert(0,v17.get())
    txt_email.configure(state='disabled')
    frame2=Frame(root2,bg="white",highlightbackground="grey",highlightthickness=3).place(x=85,y=480,height=100,width=480)
    l3=Label(frame2,text="Cab Type",font=("Impact",20,"bold"),bg="orange",fg="white").place(x=120,y=460)
    types=IntVar()
    gender_label=Label(frame2,text="Select Cab Type",font=(15),bg="white").place(x=110,y=520)
    mini=Radiobutton(frame2,text="Mini(Two Seater)",font=("times new roman",15),variable=types,value=1,bg="white")
    mini.place(x=300,y=500)
    prime=Radiobutton(frame2,text="Prime(Four Seater)",font=("times new roman",15),variable=types,value=2,bg="white")
    prime.place(x=300,y=535)
    frame3=Frame(root2,bg="white",highlightbackground="grey",highlightthickness=3).place(x=320,y=600,height=75,width=410) 
    frame4=Frame(root2,bg="white",highlightbackground="grey",highlightthickness=3).place(x=85,y=150,height=275,width=480)
    l5=Label(frame4,text="Booking Details",font=("Impact",20,"bold"),bg="orange",fg="white").place(x=120,y=130)
    l4=Label(frame4,text="Pickup Location",font=(15),bg="white").place(x=110,y=190)
    pickup=Entry(frame4,font=("times new roman",15),bg="lightgray")
    pickup.place(x=300,y=190)
    l6=Label(frame4,text="Drop Location",font=(15),bg="white").place(x=110,y=225)
    drop=Entry(frame4,font=("times new roman",15),bg="lightgray")
    drop.place(x=300,y=225)
    l7=Label(frame4,text="Pickup Date",font=(15),bg="white").place(x=110,y=260)
    cal = DateEntry(frame4, width= 16, background= "magenta3", foreground= "white",bd=2)
    cal.place(x=300,y=260,height=30,width=200)
    l8=Label(frame4,text="Pickup Time",font=(15),bg="white").place(x=110,y=295)
    hrs_text=Entry(frame4,font=("times new roman",15),bg="lightgray")
    hrs_text.place(x=300,y=295,width=85)
    l9=Label(frame4,text="hrs",font=(15),bg="white").place(x=400,y=295)
    min_text=Entry(frame4,font=("times new roman",15),bg="lightgray")
    min_text.place(x=450,y=295,width=55)
    l9=Label(frame4,text="min",font=(15),bg="white").place(x=510,y=295)
    l10=Label(frame4,text="Insurance",font=(15),bg="white").place(x=110,y=330)
    cmb_insurance=ttk.Combobox(frame4,font=("times new roman",15),state="readonly",justify="center")
    cmb_insurance['values']=("Select","Yes","No")
    cmb_insurance.place(x=300,y=330,width=200)
    cmb_insurance.current(0)

    resetbutt=Button(frame3,text="Reset",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=reset_fn)
    resetbutt.place(x=400,y=610,width=80)
    back_button=Button(frame3,text="Back",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=back_fn)
    back_button.place(x=500,y=610,width=80)
    Exit_button=Button(frame3,text="Exit",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=exit_fn)
    Exit_button.place(x=600,y=610,width=80)


    frame5=Frame(root2,bg="white",highlightbackground="grey",highlightthickness=3).place(x=600,y=480,height=100,width=340)
    book_button=Button(frame5,text="Book",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=book_fn)
    book_button.place(x=730,y=500) 

    frame6=Frame(root2,bg="white",highlightbackground="grey",highlightthickness=3).place(x=600,y=150,height=275,width=340)
    l10=Label(text="Amount Details",font=("Impact",20,"bold"),fg="white",bg="orange").place(x=620,y=130)
    Travel_amount=Label(frame6,text="Travel Amount",font=(15),bg="white").place(x=620,y=190)
    amount=Entry(frame6,font=("times new roman",15),bg="lightgray")
    amount.place(x=800,y=190,width=120)
    Tax_amount=Label(frame6,text="Tax Amount",font=(15),bg="white").place(x=620,y=225)
    tax=Entry(frame6,font=("times new roman",15),bg="lightgray")
    tax.place(x=800,y=225,width=120)
    ins_amount=Label(frame6,text="Insurance Amount",font=(15),bg="white").place(x=620,y=260)
    insurance=Entry(frame6,font=("times new roman",15),bg="lightgray")
    insurance.place(x=800,y=260,width=120)
    total_amount=Label(frame6,text="Total Amount",font=(15),bg="white").place(x=620,y=295)
    total=Entry(frame6,font=("times new roman",15),bg="lightgray")
    total.place(x=800,y=295,width=120)
    cal_button=Button(frame6,text="Calculate",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=calculate_fn).place(x=710,y=350)
    root2.mainloop()
def create_sel_choice():
    root3=Tk()
    root3.title("Cab Booking System")
    root3.geometry("1236x600+180+100")
    root3.resizable(False,False)
    #------------------------------------------------------------------------------------------------------------------------------------#
    def Book_command():
        root3.destroy()
        create_book_cab()
    def show_details():
        root3.destroy()
        create_booking_details()
    def update_fn():
        root3.destroy()
        create_update_profile()
    #-------------------------------------------------------------------------------------------------------------------------------------#
    bg_image=ImageTk.PhotoImage(file="backg.jpg")
    bg_label=Label(root3,image=bg_image).place(x=0,y=0,relheight=1,relwidth=1)
    frame1=Frame(root3,bg="white",highlightbackground="grey",highlightthickness=3).place(x=85,y=150,height=200,width=800)
    l1=Label(frame1,text="Choose Your Command",font=("Impact",35,"bold"),bg="orange",fg="white").place(x=120,y=125)
    Book_button=Button(frame1,text="Book Cab",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=Book_command).place(x=150,y=250)
    update_button=Button(frame1,text="Update Profile",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=update_fn).place(x=580,y=250)
    details_button=Button(frame1,text="Show Booking Details",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=show_details).place(x=300,y=250)
    root3.mainloop() 




def validate():
    v=v23.get()
    if(v17.get()=="" or v23.get()==""):
        messagebox.showerror("Error","All fields are required")
    else:
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",password="password",database="booking")
            cur=mydb.cursor()
            cur.execute("select * from Login_details where E_mail=%s and password=%s",(v17.get(),v23.get()))
            result=cur.fetchone()
            print(result)
            if result==None:
                messagebox.showerror("Error","User Not Found")
            else:
                root.destroy()
                create_sel_choice()
            mydb.close()
        except Exception as es:
            messagebox.showerror("Error",f"Eroor due to: {str(es)}")



def sign_up():
    root.destroy()
    create_signup()
def forgot_fn():
    root.destroy()
    create_forgot_pass()
bg=ImageTk.PhotoImage(file="backg.jpg")
bg_image=Label(image=bg).place(x=0,y=0,relwidth=1,relheight=1)
login_frame=Frame(root,bg="white",highlightbackground="grey",highlightthickness=3).place(x=100,y=150,height=350,width=300)
login_text=Label(login_frame,text="Login Here",font=("Impact",35,"bold"),fg="white",bg="orange").place(x=120,y=120)
username=Label(login_frame,text="Email ID",font=("goudy old style",20),fg="grey",bg="white").place(x=120,y=230)
v17=StringVar()
user_txt=Entry(login_frame,font=("times new roman",15),bg="lightgray",textvariable=v17)
user_txt.place(x=120,y=270)
userpass=Label(login_frame,text="Password",font=("goudy old style",20),fg="grey",bg="white").place(x=120,y=300)
v23=StringVar()
pass_txt=Entry(login_frame,font=("times new roman",15),bg="lightgray",textvariable=v23)
pass_txt.place(x=120,y=340)
forgot=Button(login_frame,text="Forgot Password?",bg="white",fg="#0271A2",font=("times new roman",12),bd=0,cursor="hand2",command=forgot_fn).place(x=120,y=375)
submit_button=Button(login_frame,text="Login",font=("goudy old style",20),fg="white",bg="#0271A2",command=validate,cursor="hand2").place(x=120,y=430)
signup_button=Button(login_frame,text="SignUp",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=sign_up).place(x=230,y=430)
root.mainloop()
