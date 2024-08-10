from tkinter import *
from tkinter import ttk
import random   
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        
        self.Nameoftabelts=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberOfTablets=StringVar()
        self.Lot=StringVar()
        self.IssueDate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInfomation=StringVar()
        self.storageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()
        
        
           
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="Hospital Management System",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill="x")
        
        #======================================Data Frame================================================================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)
        
        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                 font=("times new roman",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350) 
        
        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                  font=("times new roman",12,"bold"),text="Prescription")
        DataframeRight.place(x=990,y=5,width=460,height=350)
        
        
        #======================================Button Frame================================================================
        Buttonframe = Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        
        #======================================Details Frame================================================================
        Detailsframe = Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)
        
        #======================================DataframeLeft================================================================
        lblNameTablet = Label(DataframeLeft,text="Names Of Tablet",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)
        
        comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftabelts,state="readonly",font=("arial",12,"bold"),width=33)
        comNametablet["values"]=("Nice","Corona Vacacine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNametablet.grid(row=0,column=1)
        
        lblref = Label(DataframeLeft,text="Reference No:",font=("arial",12,"bold"),padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.ref ,width=35)
        txtref.grid(row=1,column=1)
        
        lblDose = Label(DataframeLeft,text="Dose:",font=("arial",12,"bold"),padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)
        
        lblNoOftablets = Label(DataframeLeft,text="No of Tablets::",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.NumberOfTablets,width=35)
        txtNoOftablets.grid(row=3,column=1)
        
        lblLot = Label(DataframeLeft,text="Lot:",font=("arial",12,"bold"),padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)
        
        lblissueDate = Label(DataframeLeft,text="Issue Date:",font=("arial",12,"bold"),padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.IssueDate,width=35)
        txtissueDate.grid(row=5,column=1)
        
        lblExpDate = Label(DataframeLeft,text="Exp Date:",font=("arial",12,"bold"),padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.ExpDate,width=35)
        txtExpDate.grid(row=6,column=1)
        
        lblDailyDose = Label(DataframeLeft,text="Daily Dose:",font=("arial",12,"bold"),padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.DailyDose, width=35)
        txtDailyDose.grid(row=7,column=1)
        
        lblSideEffect = Label(DataframeLeft,text="Side Effect:",font=("arial",12,"bold"),padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.sideEffect,width=35)
        txtSideEffect.grid(row=8,column=1)
        
        lblFurtherinfo = Label(DataframeLeft,text="Further Information:",font=("arial",12,"bold"),padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo = Entry(DataframeLeft,font=("arial", 13, "bold"),textvariable=self.FurtherInfomation ,width=35)
        txtFurtherinfo.grid(row=0,column=3)
        
        lblBloodPressue = Label(DataframeLeft,text="Blood Pressure:",font=("arial",12,"bold"),padx=2,pady=6)
        lblBloodPressue.grid(row=1,column=2,sticky=W)
        txtBloodPressue = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.DrivingUsingMachine,width=35)
        txtBloodPressue.grid(row=1,column=3)
        
        lblStorage = Label(DataframeLeft,text="Storage:",font=("arial",12,"bold"),padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.storageAdvice ,width=35)
        txtStorage.grid(row=2,column=3)
        
        lblMedicine = Label(DataframeLeft,text="Medicine:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.HowToUseMedication,width=35)
        txtMedicine.grid(row=3,column=3)
        
        lblPatientId = Label(DataframeLeft,text="Patient ID:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.PatientId,width=35)
        txtPatientId.grid(row=4,column=3)
        
        lblNhsNumber = Label(DataframeLeft,text="Nhs Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.nhsNumber,width=35)
        txtNhsNumber.grid(row=5,column=3)
        
        lblPatientname = Label(DataframeLeft,text="Patient Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.PatientName, width=35)
        txtPatientname.grid(row=6,column=3)
        
        lblDateOfBirth = Label(DataframeLeft,text="Date Of Birth:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.DateOfBirth ,width=35)
        txtDateOfBirth.grid(row=7,column=3)
        
        lblPatientAddress = Label(DataframeLeft,text="Patient Address:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.PatientAddress,width=35)
        txtPatientAddress .grid(row=8,column=3)
        
         #======================================DataframeRight================================================================

        self.txtPrescription=Text(DataframeRight, font=("arial", 12, "bold"), width=23,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
         
         #======================================Button================================================================
        btnPrescription=Button(Buttonframe,command = self.iPrescription,bd=5,fg="black",bg="lightblue",font=("ariel",12,"bold"),width=23,height=16,text="Prescription",padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)
        
        btnPrescriptionData = Button(Buttonframe, text="Prescription Data", bg="navy", fg="black", font=("arial", 12, "bold"), width=23, height=16, padx=2, pady=6,command=self.iPrescriptionData)
        btnPrescriptionData.grid(row=0, column=1)
        
        btnUpdate=Button(Buttonframe,command=self.Update,text="Update",bg="blue",fg="black",font=("arial", 12, "bold"),width=23,height=16,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)
        
        btnDelete=Button(Buttonframe,command= self.idelete,text="Delete",bg="white",fg="black",font=("arial", 12, "bold"),width=23,height=16,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)
        
        btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="black",fg="black",font=("arial", 12, "bold"),width=23,height=16,padx=2,pady=6)
        btnClear.grid(row=0,column=4)
        
        btnExit=Button(Buttonframe,command =self.iExit,text="Exit",bg="red",fg="black",font=("arial", 12, "bold"),width=23,height=16,padx=2,pady=6)
        btnExit.grid(row=0,column=5)
        
        #======================================Table================================================================
        #======================================Scroll Bar================================================================
        
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftablets","ref","dose","nooftablets","lot","issuedate",
                                                              "expdate","dailynose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)  
        
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        
        self.hospital_table.heading("nameoftablets",text="Name Of Tablets")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="Name Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailynose",text="Daily Nose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="Nhs Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")
        
        self.hospital_table["show"]="headings"
        
        self.hospital_table.column("nameoftablets",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailynose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)
        
        self.hospital_table.pack(fill=BOTH,expand=1)
        
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()



    #======================================Fuctionality Declaration================================================================
        
    def iPrescriptionData(self):
        if self.Nameoftabelts.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="0905657088",database="sys")
            my_cursor=conn.cursor()
            my_cursor.execute("INSERT INTO hospital VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
            self.Nameoftabelts.get(),
            self.ref.get(),
            self.Dose.get(),
            self.NumberOfTablets.get(),
            self.Lot.get(),
            self.IssueDate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.sideEffect.get(),
            self.FurtherInfomation.get(),
            self.storageAdvice.get(),
            self.DrivingUsingMachine.get(),
            self.HowToUseMedication.get(),
            self.PatientId.get(),
            self.nhsNumber.get(),
            self.PatientName.get(),
            self.DateOfBirth.get(),
            self.PatientAddress.get(),
        ))

            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Record Successfully",)
            
    def Update(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="0905657088",database="sys")
            my_cursor=conn.cursor()
            update_query = (
            "UPDATE hospital SET Nameoftablets=%s, dose=%s, Numberoftablets=%s, lot=%s, issuedate=%s, expdate=%s,"
            " dailydose=%s, sideeffect=%s, futherinformation=%s, bloodpressure=%s, storage=%s, medicine=%s, ID=%s,"
            " Nhsnumber=%s, patientname=%s, DOB=%s, patientaddress=%s WHERE `Reference_No`=%s"
        )
            my_cursor.execute(update_query,(
                self.Nameoftabelts.get(),
                self.Dose.get(),
                self.NumberOfTablets.get(),
                self.Lot.get(),
                self.IssueDate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.sideEffect.get(),
                self.FurtherInfomation.get(),
                self.storageAdvice.get(),
                self.DrivingUsingMachine.get(),
                self.HowToUseMedication.get(),
                self.PatientId.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get(),
                self.ref.get()
            ))
            
            conn.commit()  
            conn.close()
            self.fatch_data()  
        except Exception as e:
            print("Error during update:", e) 
            
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="0905657088",database="sys")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftabelts.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberOfTablets.set(row[3])
        self.Lot.set(row[4])
        self.IssueDate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.sideEffect.set(row[8])
        self.FurtherInfomation.set(row[9])
        self.storageAdvice.set(row[10])
        self.DrivingUsingMachine.set(row[11])
        self.HowToUseMedication.set(row[12])
        self.PatientId.set(row[13])
        self.nhsNumber.set(row[14])
        self.PatientName.set(row[15])
        self.DateOfBirth.set(row[16])
        self.PatientAddress.set(row[17])
        
    def iPrescription(self):
        self.txtPrescription.insert(END,"Name of Tablets:" + self.Nameoftabelts.get() + "\n")
        self.txtPrescription.insert(END,"Reference No:" + self.ref.get() +"\n")
        self.txtPrescription.insert(END,"Dose:" + self.Dose.get() +"\n")
        self.txtPrescription.insert(END,"Number of Tablets: " + self.NumberOfTablets.get() +"\n")
        self.txtPrescription.insert(END,"lot: " + self.Lot.get() +"\n")
        self.txtPrescription.insert(END,"Issue date:" + self.IssueDate.get() +"\n")
        self.txtPrescription.insert(END,"Exp date: " + self.ExpDate.get() +"\n")
        self.txtPrescription.insert(END,"Daily dose: " + self.DailyDose.get() +"\n")
        self.txtPrescription.insert(END,"side effect:  "+ self.sideEffect.get() +"\n")
        self.txtPrescription.insert(END,"Further information: " + self.FurtherInfomation.get() +"\n")
        self.txtPrescription.insert(END,"Storage advice: " + self.storageAdvice.get() +"\n")
        self.txtPrescription.insert(END,"Driving Using Machine: " + self.DrivingUsingMachine.get() +"\n")
        self.txtPrescription.insert(END,"Medicaution: " + self.HowToUseMedication.get() +"\clean")
        self.txtPrescription.insert(END,"ID: " + self.PatientId.get() +"\n")
        self.txtPrescription.insert(END,"NHs number: " + self.nhsNumber.get() +"\n")
        self.txtPrescription.insert(END,"Patient Name: " + self.PatientName.get() +"\n")
        self.txtPrescription.insert(END,"Date Of Birth: " + self.DateOfBirth.get() +"\n")
        self.txtPrescription.insert(END,"Patient Address: " + self.PatientAddress.get() +"\n")
        
    def idelete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="0905657088",database="sys")
        my_cursor=conn.cursor()
        query = "delete from hospital WHERE `Reference_No`=%s"
        value =(self.ref.get(),)
        my_cursor.execute(query,value)
        
        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("DELETED")
        
    def clear(self):
        self.Nameoftabelts.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberOfTablets.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInfomation.set("")
        self.storageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)

    def iExit(self):
        iExit = messagebox.askyesno("Hospital management system","Comfirm you want to exit")
        if iExit>0:
            root.destroy()
            return
        
root = Tk()
ob=Hospital(root)
root.mainloop()

