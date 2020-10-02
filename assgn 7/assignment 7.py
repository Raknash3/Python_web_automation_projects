from tkinter import *
import psutil
import platform
from datetime import datetime
import os
from tkinter import messagebox


  
def CPU():
    #print("Physical cores:", psutil.cpu_count(logical=False))
    #print("Total cores:", psutil.cpu_count(logical=True))
    
    cpufreq = psutil.cpu_freq()
    #print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    #print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    #print(f"Current Frequency: {cpufreq.current:.2f}Mhz")

    #print("CPU Usage Per Core:")
    #for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        #print(f"Core {i}: {percentage}%")
    #print(f"Total CPU Usage: {psutil.cpu_percent()}%")
    
    a= str(psutil.cpu_count(logical=False))
    b= str(psutil.cpu_count(logical=True))
    c= str(cpufreq.max)
    d= str(cpufreq.min)
    e= str( cpufreq.current)
    f= str(psutil.cpu_percent())
    
    l16=Label(root,text='Physical Cores:'+' '+a,fg='light blue',bg='black' )
    l17=Label(root,text='Total cores:'+' '+b,fg='light blue',bg='black' )
    l18=Label(root,text='Max Frequency:'+' '+c+'Mhz',fg='light blue',bg='black' )
    #l19=Label(root,text='Min Frequency:'+' '+d+'Mhz',fg='light blue',bg='black' )
    l20=Label(root,text='Current Frequency:'+' '+e+'Mhz',fg='light blue',bg='black' )
    l21=Label(root,text='Total CPU Usage:'+' '+f+'%',fg='light blue',bg='black' )
    
    l16.grid(row=20,column= 50)
    l17.grid(row=22,column= 50)
    l18.grid(row=24,column= 50)
    #l19.grid(row=26,column= 50)
    l20.grid(row=28,column=50)
    l21.grid(row=30,column=50)
    
    
    
    
def ram():
    def format_bytes(B):  
       B = float(B)
       KB = float(1024)
       MB = float(KB ** 2) # 1,048,576
       GB = float(KB ** 3) # 1,073,741,824
       TB = float(KB ** 4) # 1,099,511,627,776

       if B < KB:
           return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
       elif KB <= B < MB:
           return '{0:.2f} KB'.format(B/KB)
       elif MB <= B < GB:
           return '{0:.2f} MB'.format(B/MB)
       elif GB <= B < TB:
           return '{0:.2f} GB'.format(B/GB)
       elif TB <= B:
           return '{0:.2f} TB'.format(B/TB)
       
    
    svmem = psutil.virtual_memory()
    a=format_bytes(svmem.total)
    b=format_bytes(svmem.available)
    c=format_bytes(svmem.used)
    d=svmem.percent
    d=str(d)
    
    l12=Label(root,text='Total:'+' '+a,fg='light blue',bg='black' )
    l13=Label(root,text='Available:'+' '+b,fg='light blue',bg='black' )
    l14=Label(root,text='Used:'+' '+c,fg='light blue',bg='black' )
    l15=Label(root,text='Percentage:'+' '+d+'%',fg='light blue',bg='black' )
    
    l12.grid(row=36,column= 50)
    l13.grid(row=38,column= 50)
    l14.grid(row=40,column= 50)
    l15.grid(row=42,column= 50)
    
    #print('Total',format_bytes(svmem.total))
    #print('Available',format_bytes(svmem.available))
    #print('Used',format_bytes(svmem.used))
    #print('Percent',svmem.percent,'%')
    
def information():
    uname = platform.uname()
    a=uname.system
    b=uname.node
    c=uname.release
    d=uname.version
    e=uname.machine
    f=uname.processor
    
    l6=Label(root,text='System:'+' '+a,fg='light blue',bg='black' )
    l7=Label(root,text='Node name:'+' '+b,fg='light blue',bg='black' )
    l8=Label(root,text='Release:'+' '+c,fg='light blue',bg='black' )
    l9=Label(root,text='Version:'+' '+d,fg='light blue',bg='black' )
    #l10=Label(root,text='Machine:'+' '+e,fg='light blue',bg='black' )
    l11=Label(root,text='Processor:'+' '+f,fg='light blue',bg='black' )
    
    l6.grid(row=6,column= 50)
    l7.grid(row=8,column= 50)
    l8.grid(row=10,column= 50)
    l9.grid(row=12,column= 50)
    l11.grid(row=14,column=50)
    

root=Tk()
root.configure(background='light blue')
root.title("System Configuration")
root.geometry("1000x1000")

headlabel = Label(root, text = 'System Information', 
					fg = 'light blue', bg = "black" ,justify="center",height="2")
headlabel.grid(row=2,column=50)


label1=Label(root,text="",bg='light blue')
label2=Label(root,text="" ,bg='light blue')
label3=Label(root,text="" ,bg='light blue')


label1.grid(row=3,column=1)
label2.grid(row=16,column=2)
label3.grid(row=32,column=2)


button1 = Button(root, text = "Display System Information", bg = "white", 
					fg = "black", command = information) 

button2 = Button(root, text = "Display CPU usuage", bg = "white", 
					fg = "black", command = CPU)

button3 = Button(root, text = "Display RAM usuage", bg = "white", 
					fg = "black", command = ram) 

button1.grid(row = 4, column = 2)
button2.grid(row = 18, column = 2)
button3.grid(row = 34, column = 2)

root.mainloop()