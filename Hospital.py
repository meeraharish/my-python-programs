from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0") #x and y axis starts from 0
        labeltitle=Label(self.root,bd=20,relief=RIDGE,text="Hospital Management System",fg="blue",bg="white",font=("times new roman",50,"bold"))
        labeltitle.pack(side=TOP,fill=X)
        #------------------------------DATAFRAME-------------------------------------------#
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        Dataframeleft=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,font=("arial",12,"bold"),text="Patient Information")
        Dataframeleft.place(x=0,y=5,width=980,height=350)
        Dataframeright=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,font=("arial",12,"bold"),text="Prescription")
        Dataframeright.place(x=990,y=5,width=460,height=360)
        #------------------------------BUTTON FRAME-------------------------------------------#
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        #------------------------------DETAILS FRAME-------------------------------------------#
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)
        #------------------------------DATAFRAMELEFT-------------------------------------------#
        lblNameTablet=Label(Dataframeleft,font=("arial",12,"bold"),text="Name Of Tablets:",padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNameTablet=ttk.Combobox(Dataframeleft,state="readonly",
        font=("arial",12,"bold"),width=33)
        comNameTablet['value']=("Nice","Corona Vaccine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1)

        lblref=Label(Dataframeleft,font=("arial",12,"bold"),text="Reference No:",padx=2)
        lblref.grid(row=0,column=2,sticky=W)
        txtref=Entry(Dataframeleft,font=("arial",13,"bold"),width=35)
        txtref.grid(row=0,column=3)

        lblDose=Label(Dataframeleft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(Dataframeleft,font=("arial",13,"bold"),width=35)
        txtDose.grid(row=2,column=1)

        lblNoOfTablets=Label(Dataframeleft,font=("arial",12,"bold"),text="No Of Tablets:",padx=2,pady=6)
        lblNoOfTablets.grid(row=3,column=0,sticky=W)
        txtNoOfTablets=Entry(Dataframeleft,font=("arial",13,"bold"),width=35)
        txtNoOfTablets.grid(row=3,column=1)

        lblLot=Label(Dataframeleft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(Dataframeleft,font=("arial",13,"bold"),width=35)
        txtLot.grid(row=4,column=1)

        lblIssueDate=Label(Dataframeleft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(Dataframeleft,font=("arial",13,"bold"),width=35)
        txtIssueDate.grid(row=5,column=1)

        lblExpDate=Label(Dataframeleft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(Dataframeleft,font=("arial",13,"bold"),width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(Dataframeleft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(Dataframeleft,font=("arial",13,"bold"),width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(Dataframeleft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(Dataframeleft,font=("arial",13,"bold"),width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherInfo=Label(Dataframeleft,font=("arial",12,"bold"),text="Further Information:",padx=2)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        txtFurtherInfo=Entry(Dataframeleft,font=("arial",13,"bold"),width=35)
        txtFurtherInfo.grid(row=0,column=3)

        lblBloodPressure=Label(Dataframeleft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(Dataframeleft,font=("arial",13,"bold"),width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(Dataframeleft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(Dataframeleft,font=("arial",13,"bold"),width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(Dataframeleft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(Dataframeleft,font=("arial",13,"bold"),width=35)
        txtMedicine.grid(row=3,column=3)

        lblPatientId=Label(Dataframeleft,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(Dataframeleft,font=("arial",13,"bold"),width=35)
        txtPatientId.grid(row=4,column=3)

        lblNHSNumber=Label(Dataframeleft,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=6)
        lblNHSNumber.grid(row=5,column=2,sticky=W)
        txtNHSNumber=Entry(Dataframeleft,font=("arial",13,"bold"),width=35)
        txtNHSNumber.grid(row=5,column=3)

        lblPatientName=Label(Dataframeleft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(Dataframeleft,font=("arial",13,"bold"),width=35)
        txtPatientName.grid(row=6,column=3)

        lblDateofBirth=Label(Dataframeleft,font=("arial",12,"bold"),text="Date Of Birth:",padx=2,pady=6)
        lblDateofBirth.grid(row=7,column=2,sticky=W)
        txtDateofBirth=Entry(Dataframeleft,font=("arial",13,"bold"),width=35)
        txtDateofBirth.grid(row=7,column=3)

        lblPatientAddress=Label(Dataframeleft,font=("arial",12,"bold"),text="PatientAddress:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(Dataframeleft,font=("arial",13,"bold"),width=35)
        txtPatientAddress.grid(row=8,column=3)



root=Tk()
ob=Hospital(root)
root.mainloop()