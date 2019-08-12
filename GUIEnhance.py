#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Todd Ward
#
# Created:     05/08/2019
# Copyright:   (c) Todd Ward 2019
# Licence:     fEEL fREE TO USE AS TESTING
# i HAVE FOUND THAT THE SLEEP FUNCTIONS FOR GATHERING THE DINT DATA FROM THE
# PLC SLOW DOWN THE PROCESS RESPONSES AFTER A WHILE.  I AM RESEARCHING ON A
# MORE EFFICIENT WAY TO ACCOMPLISH THE READS.
# THE PLC PROGRAM IS VERY RUDIMENTARY AS I AM USING IT FOR TESTING PURPOSES
#IT WILL GIVE YOU A BASELINE FROM WHICH TO START.  I DID CONNECT TO A PLC
# COMPACT LOGIX L23 E FOR TESTING V20.  HAPPY HUNTING
#-------------------------------------------------------------------------------
from tkinter import *
from pylogix import PLC
import os
import sys
import time
#! window create
window = Tk()
window.title("Bead Seater :TF 6142 TW")
window.configure(background ='black')
width_of_window = 930
height_of_window= 900
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_cord = (screen_width/2) - (width_of_window/2)
y_cord = (screen_height/2) - (height_of_window/2)
window.geometry("%dx%d+%d+%d" % (width_of_window,height_of_window,x_cord,y_cord))

#! Functions
def Emergency():
        comm = PLC()
        comm.IPAddress = '169.254.215.82'
        comm.Write('EmergencyPB', False)
        time.sleep(.250)
        comm.Write('EmergencyPB', True)
        comm.Close()
        return
def MasterOn():
        comm = PLC()
        comm.IPAddress = '169.254.215.82'
        comm.Write('MasterStart', True)
        time.sleep(.25)
        comm.Write('MasterStart', False)
        comm.Close()
        return
def StopSEQ():
        comm = PLC()
        comm.IPAddress = '169.254.215.82'
        comm.Write('StopSeq', False)
        time.sleep(.25)
        comm.Write('StopSeq', True)
        comm.Close()
        return
def StartSEQ():
        comm = PLC()
        comm.IPAddress = '169.254.215.82'
        comm.Write('StartSeq', True)
        time.sleep(.3)
        comm.Write('StartSeq', False)
        comm.Close()
        return
def PauseSEQ():
        comm = PLC()
        comm.IPAddress = '169.254.215.82'
        comm.Write('SEQPause', True)
        time.sleep(.25)
        comm.Write('SEQPause', False)
        comm.Close()
        return
def SeqResume():
    comm = PLC()
    comm.IPAddress = '169.254.215.82'
    comm.Write('SEQResume', False)
    time.sleep(.3)
    comm.Write('SEQResume',True)
    comm.Close()
    return
def WriteSEQCount():
    comm = PLC()
    comm.IPAddress = '169.254.215.82'
    seqcount = entry1.get()
    seqcount = int (seqcount)
    comm.Write('SEQCount',seqcount)
    time.sleep(.22)
    comm.Close()
    return
def ReadOutWord():
    comm = PLC()
    comm.IPAddress = '169.254.215.82'
    value = comm.Read('OutWord')
    lbl3 = Label(window, text="OutWord|Value",bg="white",fg="Black", bd=2, relief ="solid",width=15, height=2)
    lbl3.place(x=410, y=20)
    lbl4 = Label(window,text=value,bg="Black",fg="lime", bd=3, relief ="raised",width=15, height=5)
    lbl4.place(x=410, y=60)
    window.after(550,ReadOutWord)
    return
def ReadSEQCount():
    comm = PLC()
    comm.IPAddress = '169.254.215.82'
    valueseqcount = comm.Read('SEQCount')
    lbl6 = Label(window, text="Sequence Count",bg="white",fg="Black", bd=2, relief ="solid",width=15, height=2)
    lbl6.place(x=540, y=180)
    lbl7 = Label(window,text=valueseqcount,bg="Black",fg="lime", bd=3, relief ="raised",width=15, height=5)
    lbl7.place(x=540, y=220)
    window.after(550,ReadSEQCount)
    return
def ReadConditions():
    comm = PLC()
    comm.IPAddress = '169.254.215.82'
    ECR = comm.Read('indicate.0')#!Estop Control Relay PLC
    MCR = comm.Read('indicate.1')#Master Control Relay PLC
    SCR = comm.Read('indicate.2')#!Sequence Control Relay PLC
    SSR = comm.Read('indicate.3')#Sequence Stop Relay PLC
    SPR = comm.Read('indicate.4')#Sequence Pause Relay PLC
    SRR = comm.Read('indicate.5')#Sequence Resume Relay PLC
    window.after(2000,ReadConditions)
    if ECR == True:
        lbl18 = Label(window, text="EStop On",fg="yellow", bg="red" ,bd=2, relief ="raised",width=12, height=2)
        lbl18.place(x=31, y=150)
    elif ECR == False:
        lbl18 = Label(window, text="No_EStop",fg="red", bg="yellow" ,bd=2, relief ="flat",width=12, height=2)
        lbl18.place(x=31, y=150)
    if MCR == True:
        lbl19 = Label(window, text="Master On",fg="White", bg="Firebrick4" ,bd=2, relief ="raised",width=12, height=2)
        lbl19.place(x=161, y=150)
    elif MCR == False:
        lbl19 = Label(window, text="Master Off",fg="Firebrick4", bg="white" ,bd=2, relief ="flat",width=12, height=2)
        lbl19.place(x=161, y=150)
    if SCR == True:
        lbl20 = Label(window, text="Seq On",fg="White", bg="Green" ,bd=2, relief ="raised",width=12, height=2)
        lbl20.place(x=291, y=400)
    elif SCR == False:
        lbl20 = Label(window, text="Seq Off",fg="Green", bg="white" ,bd=2, relief ="flat",width=12, height=2)
        lbl20.place(x=291, y=400)
    if SSR == True:
        lbl21 = Label(window, text="Seq Off",fg="White", bg="Red" ,bd=2, relief ="raised",width=12, height=2)
        lbl21.place(x=291, y=440)
    elif SSR == False:
        lbl21 = Label(window, text="Seq On",fg="Red", bg="white" ,bd=2, relief ="flat",width=12, height=2)
        lbl21.place(x=291, y=440)
    if SPR == True:
        lbl22 = Label(window, text="Paused",fg="White", bg="Navy" ,bd=2, relief ="raised",width=12, height=2)
        lbl22.place(x=291, y=480)
    elif SPR == False:
        lbl22 = Label(window, text="Resumed",fg="Navy", bg="White" ,bd=2, relief ="flat",width=12, height=2)
        lbl22.place(x=291, y=480)
    if SRR == True:
        lbl23 = Label(window, text="Resumed",fg="White", bg="Olive Drab" ,bd=2, relief ="raised",width=12, height=2)
        lbl23.place(x=291, y=520)
    elif SRR == False:
        lbl23 = Label(window, text="Paused",fg="Olive Drab", bg="White" ,bd=2, relief ="flat",width=12, height=2)
        lbl23.place(x=291, y=520)
    return
#!DATA Screen and Functions b5window Data Screen
def b5Window():
    b5window = Toplevel()
    b5window.title("DATA_ENTRY")
    b5window.configure(background ='black')
    b5window.geometry("%dx%d+%d+%d" % (width_of_window,height_of_window,x_cord,y_cord))
    btn105 = Button(b5window, text="Return ",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b5window.destroy)
    btn105.place(x=20, y=730)
    btn106 = Button(b5window, text="Calculate Target",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b6Window)
    btn106.place(x=150, y=730)
    btn107 = Button(b5window, text="Transfer Axis",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b7Window)
    btn107.place(x=280, y=730)
    btn108 = Button(b5window, text="Lifter Axis",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b8Window)
    btn108.place(x=410, y=730)
    btn109 = Button(b5window, text="Carrier/Press Axis",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b9Window)
    btn109.place(x=540,y=730)
    btn110=Button(b5window, text="Roller Axis",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b10Window)
    btn110.place(x=670, y=730)
    btn111=Button(b5window, text="Bead Seat",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b11Window)
    btn111.place(x=800, y=730)
    lbl00 = Label(b5window, text="DATA_FUNCTIONS HERE",bg="white",fg="Black", bd=2, relief ="solid",width=25, height=5)
    lbl00.place(x=400, y=300)
    return
#!CALCULATE Screen and Functions b6window Calculate
def b6Window():
    b6window = Toplevel()
    b6window.title("CALCULATE")
    b6window.configure(background ='black')
    b6window.geometry("%dx%d+%d+%d" % (width_of_window,height_of_window,x_cord,y_cord))
    btn205 = Button(b6window, text="Return ",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b6window.destroy)
    btn205.place(x=20, y=730)
    btn206 = Button(b6window, text="Data",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b5Window)
    btn206.place(x=150, y=730)
    btn207 = Button(b6window, text="Transfer",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b7Window)
    btn207.place(x=280, y=730)
    btn208 = Button(b6window, text="Lifter",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b8Window)
    btn208.place(x=410, y=730)
    btn209 = Button(b6window, text="Carrier/Press",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b9Window)
    btn209.place(x=540,y=730)
    btn210=Button(b6window, text="Roller",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b10Window)
    btn210.place(x=670, y=730)
    btn211=Button(b6window, text="Bead Seat",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b11Window)
    btn211.place(x=800, y=730)
    lbl200 = Label(b6window, text="CALCULATE_FUNCTIONS HERE",bg="white",fg="Black", bd=2, relief ="solid",width=25, height=5)
    lbl200.place(x=400, y=300)
    return
#!TRANSFER Screen and Functions b7window
def b7Window():
    b7window = Toplevel()
    b7window.title("TRANSFER")
    b7window.configure(background ='black')
    b7window.geometry("%dx%d+%d+%d" % (width_of_window,height_of_window,x_cord,y_cord))
    btn305 = Button(b7window, text="Return ",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b7window.destroy)
    btn305.place(x=20, y=730)
    btn306 = Button(b7window, text="Data.",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b5Window)
    btn306.place(x=150, y=730)
    btn307 = Button(b7window, text="Calc.",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b6Window)
    btn307.place(x=280, y=730)
    btn308 = Button(b7window, text="Lifter Axis",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b8Window)
    btn308.place(x=410, y=730)
    btn309 = Button(b7window, text="Carrier/Press Axis",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b9Window)
    btn309.place(x=540,y=730)
    btn310=Button(b7window, text="Roller Axis",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b10Window)
    btn310.place(x=670, y=730)
    btn311=Button(b7window, text="Bead Seat",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b11Window)
    btn311.place(x=800, y=730)
    lbl300 = Label(b7window, text="TRANSFER_FUNCTIONS HERE",bg="white",fg="Black", bd=2, relief ="solid",width=25, height=5)
    lbl300.place(x=400, y=300)
    return
#!LIFTER Screen and Functions b8window
def b8Window():
    b8window = Toplevel()
    b8window.title("LIFTER AXIS")
    b8window.configure(background ='black')
    b8window.geometry("%dx%d+%d+%d" % (width_of_window,height_of_window,x_cord,y_cord))
    btn405 = Button(b8window, text="Return ",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b8window.destroy)
    btn405.place(x=20, y=730)
    btn406 = Button(b8window, text="Data",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b5Window)
    btn406.place(x=150, y=730)
    btn407 = Button(b8window, text="Calc",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b6Window)
    btn407.place(x=280, y=730)
    btn408 = Button(b8window, text="Transfer",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b7Window)
    btn408.place(x=410, y=730)
    btn409 = Button(b8window, text="Carrier/Press Axis",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b9Window)
    btn409.place(x=540,y=730)
    btn410=Button(b8window, text="Roller Axis",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b10Window)
    btn410.place(x=670, y=730)
    btn411=Button(b8window, text="Bead Seat",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b11Window)
    btn411.place(x=800, y=730)
    lbl400 = Label(b8window, text="LIFTER FUNCTIONS HERE",bg="white",fg="Black", bd=2, relief ="solid",width=25, height=5)
    lbl400.place(x=400, y=300)
    return
#!CARRIER AND PRESS Screen and Functions b9window
def b9Window():
    b9window = Toplevel()
    b9window.title("CARRIER AXIS")
    b9window.configure(background ='black')
    b9window.geometry("%dx%d+%d+%d" % (width_of_window,height_of_window,x_cord,y_cord))
    btn505 = Button(b9window, text="Return ",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b9window.destroy)
    btn505.place(x=20, y=730)
    btn506 = Button(b9window, text="Data",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b5Window)
    btn506.place(x=150, y=730)
    btn507 = Button(b9window, text="Calc",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b6Window)
    btn507.place(x=280, y=730)
    btn508 = Button(b9window, text="Transfer",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b7Window)
    btn508.place(x=410, y=730)
    btn509 = Button(b9window, text="Lifter",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b8Window)
    btn509.place(x=540,y=730)
    btn510=Button(b9window, text="Roller Axis",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b10Window)
    btn510.place(x=670, y=730)
    btn511=Button(b9window, text="Bead Seat",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b11Window)
    btn511.place(x=800, y=730)
    lbl500 = Label(b9window, text="CARRIER|PRESS_FUNCTIONS HERE",bg="white",fg="Black", bd=2, relief ="solid",width=25, height=5)
    lbl500.place(x=400, y=300)
    return
#! ROLLER SERVO Screen and Functions b10 Window
def b10Window():
    b10window = Toplevel()
    b10window.title("ROLLER AXIS")
    b10window.configure(background ='black')
    b10window.geometry("%dx%d+%d+%d" % (width_of_window,height_of_window,x_cord,y_cord))
    btn605 = Button(b10window, text="Return ",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b10window.destroy)
    btn605.place(x=20, y=730)
    btn606 = Button(b10window, text="Data",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b5Window)
    btn606.place(x=150, y=730)
    btn607 = Button(b10window, text="Calculate",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b6Window)
    btn607.place(x=280, y=730)
    btn608 = Button(b10window, text="Transfer",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b7Window)
    btn608.place(x=410, y=730)
    btn609 = Button(b10window, text="Lifter",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b8Window)
    btn609.place(x=540,y=730)
    btn610=Button(b10window, text="Carrier",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b9Window)
    btn610.place(x=670, y=730)
    btn611=Button(b10window, text="Bead Seat",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b11Window)
    btn611.place(x=800, y=730)
    lbl600 = Label(b10window, text="ROLLER FUNCTIONS HERE",bg="white",fg="Black", bd=2, relief ="solid",width=25, height=5)
    lbl600.place(x=400, y=300)
def b11Window():
    b11window = Toplevel()
    b11window.title("BEAD_SEAT")
    b11window.configure(background ='black')
    b11window.geometry("%dx%d+%d+%d" % (width_of_window,height_of_window,x_cord,y_cord))
    btn705 = Button(b11window, text="Return ",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b11window.destroy)
    btn705.place(x=20, y=730)
    btn706 = Button(b11window, text="Data",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b5Window)
    btn706.place(x=150, y=730)
    btn707 = Button(b11window, text="Calculate",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b6Window)
    btn707.place(x=280, y=730)
    btn708 = Button(b11window, text="Transfer",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b7Window)
    btn708.place(x=410, y=730)
    btn709 = Button(b11window, text="Lifter",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b8Window)
    btn709.place(x=540,y=730)
    btn710=Button(b11window, text="Carrier",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b9Window)
    btn710.place(x=670, y=730)
    btn711=Button(b11window, text="Roller",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b10Window)
    btn711.place(x=800, y=730)
    lbl700 = Label(b11window, text="BEAD_SEAT_FUNCTIONS HERE",bg="white",fg="Black", bd=2, relief ="solid",width=25, height=5)
    lbl700.place(x=400, y=300)
#! Window Setup for Main Window

window.after(1000,ReadSEQCount,)
window.after(1000,ReadOutWord,)
window.after(1000,ReadConditions,)

#! Special Calls/Entrys
#!lbl5 = Label(window, text="Seq Count",bg="white",highlightcolor="lime", bd=2, relief ="solid",width=15, height=2)
#!lbl5.place(x=540, y=20)
entry1 = Entry(window,width=18)
entry1.place(x=540,y=60)
#! Button Labels Follow Here
lbl = Label(window, text="Emergency",highlightcolor="lime",bg="white", bd=2, relief ="solid",width=15, height=2,)
lbl.place(x=20, y=20)
lbl1 = Label(window, text="Master Start",bg="white",highlightcolor="lime", bd=2, relief ="solid",width=15, height=2)
lbl1.place(x=150, y=20)
lbl2 = Label(window, text="Sequencer",bg="white",highlightcolor="lime", bd=2, relief ="solid",width=15, height=2)
lbl2.place(x=280, y=20)
#!PLC Function Buttons Follow Here.......
btn1 = Button(window, text="Emergency ",bg="red", fg="yellow",bd=1,relief="solid",width=14,height=5,command=Emergency,highlightcolor="lime")
btn1.place(x=20, y=60)
btn2 = Button(window, text="Master",bg="Firebrick4", fg="White",bd=3,relief="solid",width=14,height=5,command=MasterOn,highlightcolor="lime")
btn2.place(x=150, y=60)
btn3 = Button(window, text="Start_Seq",bg="Green", fg="White",bd=3,relief="solid",width=14,height=5,highlightcolor="lime",command=StartSEQ)
btn3.place(x=280, y=60)
btn4 = Button(window, text="Stop_Seq",bg="Red", fg="White",bd=3,relief="solid",width=14,height=5,highlightcolor="lime",command=StopSEQ)
btn4.place(x=280, y=140)
btn12 = Button(window, text="Pause_Seq",bg="Navy", fg="White",bd=3,relief="solid",width=14,height=5,highlightcolor="lime",command=PauseSEQ)
btn12.place(x=280, y=220)
btn14 = Button(window, text="Seq Resume",bg="Olive Drab", fg="White",bd=3,relief="solid",width=14,height=5,highlightcolor="lime",command=SeqResume)
btn14.place(x=280, y=300)
btn13 = Button(window, text="Set_Seq_Count",bg="brown4", fg="White",bd=3,relief="solid",width=14,height=5,highlightcolor="lime",command=WriteSEQCount)
btn13.place(x=540, y=80)
#!Navigation  Buttons Main Page Follow .........
btn5 = Button(window, text="Data Ent ",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b5Window)
btn5.place(x=20, y=730)
btn6 = Button(window, text="Calculate Target",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b6Window)
btn6.place(x=150, y=730)
btn7 = Button(window, text="Transfer Axis",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b7Window)
btn7.place(x=280, y=730)
btn8 = Button(window, text="Lifter Axis",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b8Window)
btn8.place(x=410, y=730)
btn9 = Button(window, text="Carrier/Press Axis",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b9Window)
btn9.place(x=540,y=730)
btn10=Button(window, text="Roller Axis",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b10Window)
btn10.place(x=670, y=730)
btn11=Button(window, text="Bead Seat",bg="Blue", fg="white",bd=3,relief="solid",width=14,height=5,command=b11Window)
btn11.place(x=800, y=730)
#!End of Page One

#! Navigation Buttons Data Ent Screen Follow......


window.mainloop()



