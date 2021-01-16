from tkinter import *
import time


blue=(0,0,255)

class Atm:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x750+0+0")
        self.root.title("BASIC ATM PROCESS")
        title = Label(self.root, text="SBI ATM CARD SERVICE", bd=12, relief=GROOVE, bg='blue', fg="white",
                      font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        self.pin=IntVar()
        self.cashW=IntVar()
        self.cashD=IntVar()
        F1=Frame(self.root,bd=10, relief=GROOVE, bg="white")

        F1.place(x=0, y=55, width=1200,height=420)
        L1=Label(F1,text="ENTER DETAILS AS PER INSTRUCTIONS GIVEN BELOW",fg="purple", font=("times new roman", 14, "bold")).grid(padx=245)
        self.txtarea=Text(F1,bg="Blue",fg="white",height=15,width=66,x=300,y=400,relief=SUNKEN)
        self.txtarea.grid()

        self.s1()

    def s1(self):
        #self.txtarea.delete('1.0', END)

        self.txtarea.insert(END,"\n\n 1)WITHDRAWAL",)
        self.txtarea.insert(END, "\n\n 2)DEPOSIT", )
        self.txtarea.insert(END, "\n\n 3)BALANCE INQUIRY", )
        self.txtarea.insert(END, "\n\n 4)EXIT", )
        self.pin_F=Frame(self.root,bd=7,bg="purple")
        self.pin_F.place(x=253,width=531,height=50,y=335)
        btn_F=Frame(self.root,bd=7,)
        btn_F.place(x=200,width=50,height=220,y=120)
        btn2_F=Frame(self.root,bd=7,)
        btn2_F.place(x=785, width=70, height=200, y=120)

        b1 = Button(btn_F, text="-->", bg="silver", width=2, fg="black",command=self.Withdraw).grid(pady=2,padx=10,row=12, column=1)
        b2 = Button(btn_F, text="-->", bg="silver", width=2, fg="black",command=self.Depo1).grid(pady=2,padx=10, row=13, column=1)
        b3 = Button(btn_F, text="-->", bg="silver", width=2, fg="black",command=self.Bal).grid(pady=2, padx=10, row=14, column=1)
        b4 = Button(btn_F, text="-->", bg="silver", width=2, fg="black",command=self.exit).grid(pady=2, padx=10, row=15, column=1)
        b5 = Button(btn_F, text="Ent-W", bg="silver", width=4, fg="black",command=self.Withdraw2).grid(pady=2, padx=0, row=16, column=1)
        b52 = Button(btn_F, text="Ent-D", bg="silver", width=4, fg="black", command=self.Depo2).grid(pady=2, padx=0,
                                                                                                        row=17,
                                                                                                        column=1)
        b53 = Button(btn_F, text="Ent-B", bg="silver", width=4, fg="black", command=self.Bal2).grid(pady=2, padx=0,
                                                                                                     row=18,
                                                                                                     column=1)
        b6 = Button(btn2_F, text="Withdraw", bg="silver", width=7, fg="black", command=self.Withdraw3).grid(pady=2, padx=1,
                                                                                                        row=1,
                                                                                                        column=1)
        b7 = Button(btn2_F, text="Deposit", bg="silver", width=7, fg="black", command=self.Depo3).grid(pady=2,
                                                                                                            padx=1,
                                                                                                            row=2,
                                                                                                            column=1)
  #      b8 = Button(btn2_F, text="Balance", bg="silver", width=7, fg="black", command=self.Withdraw3).grid(pady=2,padx=1,row=3,column=1)
    def Withdraw(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\n\n ENTER THE 4 DIGIT PIN:", )
        self.pinent=Entry(self.pin_F,width=8,textvariable=self.pin,font="arial 12 bold", bd=7, relief=SUNKEN).grid(row=0, column=0, padx=7, pady=1)

    def Withdraw2(self):
        self.code=4545

        if self.pin.get() == self.code:
            self.txtarea.delete('1.0', END)
            self.txtarea.insert(END, "\n\n ENTER THE AMOUNT YOU WANT TO WITHDRAW:", )
            self.cashWent = Entry(self.pin_F, width=8, textvariable=self.cashW, font="arial 12 bold", bd=7,
                                relief=SUNKEN).grid(row=0, column=0, padx=7, pady=1)
            #
           #
        else:
            self.txtarea.delete('1.0', END)
            self.txtarea.insert(END, "\n\n PLEASE ENTER VALID PIN", )
            self.txtarea.insert(END, "\n\n TRA AGAIN LATER", )
    def Withdraw3(self):
        self.balance=100000
        self.txtarea.delete('1.0', END)
        self.availablebal=self.balance-self.cashW.get()
        self.txtarea.insert(END, "\n\n TRANSACTION COMPLETED.", )
        self.txtarea.insert(END, f"\n\n YOUR BALANCE IS Rs. {self.availablebal}/-", )
        self.txtarea.insert(END, "\n\n THANK YOUR FOR USING OUR SERVICES.", )
    def Depo1(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\n\n ENTER THE 4 DIGIT PIN:", )
        self.pinent = Entry(self.pin_F, width=8, textvariable=self.pin, font="arial 12 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=0, padx=7, pady=1)
    def Depo2(self):
        self.code = 4545

        if self.pin.get() == self.code:
            self.txtarea.delete('1.0', END)
            self.txtarea.insert(END, "\n\n ENTER THE AMOUNT YOU WANT TO DEPOSIT:", )
            self.cashDent = Entry(self.pin_F, width=8, textvariable=self.cashD, font="arial 12 bold", bd=7,
                                  relief=SUNKEN).grid(row=0, column=0, padx=7, pady=1)
            #
        #
        else:
            self.txtarea.delete('1.0', END)
            self.txtarea.insert(END, "\n\n PLEASE ENTER VALID PIN", )
            self.txtarea.insert(END, "\n\n TRA AGAIN LATER", )
    def Depo3(self):
        self.balance = 100000
        self.txtarea.delete('1.0', END)
        self.availablebal2 = self.balance + self.cashD.get()
        self.txtarea.insert(END, "\n\n TRANSACTION COMPLETED.", )
        self.txtarea.insert(END, f"\n\n YOUR BALANCE IS Rs. {self.availablebal2}/-", )
        self.txtarea.insert(END, "\n\n THANK YOUR FOR USING OUR SERVICES.", )
    def Bal(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\n\n ENTER THE 4 DIGIT PIN:", )
        self.pinent = Entry(self.pin_F, width=8, textvariable=self.pin, font="arial 12 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=0, padx=7, pady=1)

    def Bal2(self):
        self.balance = 100000
        self.code = 4545

        if self.pin.get() == self.code:
            self.txtarea.delete('1.0', END)
            self.txtarea.insert(END, f"\n\n YOUR AVAILABLE BALANCE IS Rs.{self.balance}/-", )
            self.txtarea.insert(END, "\n\n THANK YOUR FOR USING OUR SERVICES.", )

            #
        #
        else:
            self.txtarea.delete('1.0', END)
            self.txtarea.insert(END, "\n\n PLEASE ENTER VALID PIN", )
            self.txtarea.insert(END, "\n\n TRA AGAIN LATER", )

    def exit(self):
        time.sleep(3)
        self.root.destroy()











root=Tk()
obj=Atm(root)

root.mainloop()