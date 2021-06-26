# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 14:04:40 2021

@author: DiiCo
"""

#Libraries
from matplotlib import pyplot as plt
from tkinter import *
import sqlite3
import webbrowser
import os
import random

#Window Creation
root = Tk()
root.title('Notlandırma Programı')
root.geometry('250x270')
root.resizable(0,0)
root.attributes('-topmost', True)

#Random Seed for the Database
seed = random.randint(1,999999)

#Grid Configs
Grid.columnconfigure(root,1,weight=1)
Grid.rowconfigure(root,0,weight=1)
Grid.rowconfigure(root,1,weight=1)
Grid.rowconfigure(root,2,weight=1)
Grid.rowconfigure(root,3,weight=1)
Grid.rowconfigure(root,4,weight=1)
Grid.rowconfigure(root,5,weight=1)
Grid.rowconfigure(root,6,weight=1)

#Create Checkbox
checkbox_status = IntVar()
checkbox = Checkbutton(root, text="Veri Figürü Yarat", variable = checkbox_status)
checkbox.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=50,sticky="NSEW")

# =============================================================================
# #Checking Whether a Database Exists
# check = os.path.exists('./'+str(seed)+'.db')
# =============================================================================

#Connect to a Database
conn = sqlite3.connect('./'+str(seed)+'.db')

#Create Cursor
c = conn.cursor() 

#Checking Existence of and Creating the Database if Needed (Parts of it might be needed later)
# =============================================================================
# def chck():
#     global conn
#     global c
#     if check == 'True':
#         conn = sqlite3.connect('./'+str(seed)+'.db')
#         c = conn.cursor()
#         c.execute("""CREATE TABLE addresses (
#             Kategori text,
#             Hiç integer,
#             Bazen integer, 
#             Sık integer
#             )""") 
#     else:
#         pass
#     c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='addresses' ''')
#     if c.fetchone()[0]==1 : 
#         print('...')
#     else :
#         conn = sqlite3.connect('./'+str(seed)+'.db')
#         c = conn.cursor()
#         c.execute("""CREATE TABLE addresses (
#             Kategori text,
#             Hiç integer,
#             Bazen integer, 
#             Sık integer
#             )""") 
# chck()
# =============================================================================

#Categories & Some Global Variables
ctg = ['Kaygı (8)','Obsesyon (7)','Sosyal Fobi (3)','İçedönüklük (3)','Somatizasyon (7)','Travma (3)','Anoreksiya (3)','Bulimia (3)','Depresyon (12)','Hipomani (9)','Uyku Bozukluğu (2)','Dehb (17)','Öfke Kontrolü (8)','Sosyopati (18)','Psikotik Belirti(12)','İmpuls Kontrolü (5)','Bağımlılık (7)','Disosyatif Belirti (3)','Borderline (8)']
lst= []
figure_list = []
a= 0
txt = 0
b = 0
int_cnt = 0
seed_old = 0

#Create Adressess within the Current Database
c.execute("""CREATE TABLE addresses (
    Kategori text,
    Hiç integer,
    Bazen integer, 
    Sık integer
    )""") 

#Proper Notepad Text Function
def bettertxt():
    global a
    global int_cnt
    global cnt1
    global cnt2
    global cnt3
    if ctg[int_cnt] == 'Somatizasyon (7)' or ctg[int_cnt] == 'Uyku Bozukluğu (2)' or ctg[int_cnt] == 'Öfke Kontrolü (8)' or ctg[int_cnt] == 'Psikotik Belirti(12)' or ctg[int_cnt] == 'İmpuls Kontrolü (5)' or ctg[int_cnt] == 'Disosyatif Belirti (3)':
        lst.append(("\n"+str(ctg[int_cnt])+'\tHiç/'+str(*cnt1[-1])+'\tBazen/'+str(*cnt2[-1])+'\tSık/'+str(*cnt3[-1])))
        figure_list.append(*cnt1[-1])
        figure_list.append(*cnt2[-1])
        figure_list.append(*cnt3[-1])
        figure_list.append(ctg[int_cnt])
    else:
        lst.append(("\n"+str(ctg[int_cnt])+'\t\tHiç/'+str(*cnt1[-1])+'\tBazen/'+str(*cnt2[-1])+'\tSık/'+str(*cnt3[-1]))) 
        figure_list.append(*cnt1[-1])
        figure_list.append(*cnt2[-1])
        figure_list.append(*cnt3[-1])
        figure_list.append(ctg[int_cnt])

#Graph Function
def veri(yx1,yx2,yx3,lbl,fignum,placement):
    plt.figure(fignum)
    plt.subplot(3,3,placement)
    x = 0
    y1 = int(yx1)
    y2 = int(yx2)
    y3 = int(yx3)
    width = 0.25
    plt.bar(x-0.2, y1, width, color='cyan')
    plt.bar(x, y2, width, color='orange')
    plt.bar(x+0.2, y3, width, color='green')
    plt.xticks([1], [''])
    plt.xlabel("Sıklık İndikatörü")
    plt.ylabel(str(lbl))
    plt.legend(["Hiç", "Bazen", "Sık"])
#Automatic Full Screen Function for Graphs (Use once after every last item of a Figure)
def maximize():
   figManager = plt.get_current_fig_manager()
   figManager.window.showMaximized()  
   
    
#Submit Function
def submit(event = None):
    global a
    global b
    global cnt1
    global cnt2
    global cnt3
    global txt
    global seed
    global conn
    global lst
    global int_cnt
    global figure_list
    global seed_old
    a += 1
    if a == 19:
        a = 0
        txt = 1
    if a == 0:
        b = 1
    if b == 1:
        seed_old = seed
        seed = random.randint(1,999999)
        seed_lbl.config(text='No: '+str(seed))
        check = os.path.exists('./'+str(seed)+'.db')
        conn = sqlite3.connect('./'+str(seed)+'.db')         
        c = conn.cursor()
        c.execute("""CREATE TABLE addresses (
             Kategori text,
             Hiç integer,
            Bazen integer, 
            Sık integer
             )""") 
        b = 0
    #Database Creation & Connection
    conn = sqlite3.connect('./'+str(seed)+'.db')
    #Create Cursor
    c = conn.cursor()
    #Insert Into Table
    c.execute("INSERT INTO addresses VALUES (:Kategori, :Hiç, :Bazen, :Sık)",
            {
                'Kategori': ctg[a-1],
                'Hiç': ax.get(),
                'Bazen': bx.get(),
                'Sık':cx.get()
            })
    #Fetch Data from Adressess to Write into a Notepad
    c.execute("SELECT Hiç FROM addresses")
    cnt1 = c.fetchall()
    c.execute("SELECT Bazen FROM addresses")
    cnt2 = c.fetchall()
    c.execute("SELECT Sık FROM addresses")
    cnt3 = c.fetchall()
    bettertxt()
    #Create Graphs
    place_count1 = [1,2,3]
    place_count2 = 0  
    int_cnt += 1
    if int_cnt == 19:
        int_cnt = 0
    if int_cnt == 0 and checkbox_status.get() == 1:
        for i in range(0,36,4):
            place_count2 += 1
            veri(figure_list[i],figure_list[i+1],figure_list[i+2],str(figure_list[i+3]),place_count1[0],place_count2)
        maximize()
        place_count2 = 0
        for i in range(36,72,4):
            place_count2 += 1
            veri(figure_list[i],figure_list[i+1],figure_list[i+2],str(figure_list[i+3]),place_count1[1],place_count2)
            maximize()
        for i in range (72,76,4):
            veri(figure_list[i],figure_list[i+1],figure_list[i+2],str(figure_list[i+3]),place_count1[2],1)
            maximize()
        figure_list = []
    #Automatically Write into and Open the Created Notepad
    if txt == 1:
        f = open("Hasta Test Notlandırma Cıktısı ("+str(seed_old)+").txt" , "w",encoding="utf-8")
        for i in range(19):
            f.write(lst[i-1])
        f.close()
        webbrowser.open("Hasta Test Notlandırma Cıktısı ("+str(seed_old)+").txt") 
        txt = 0
        lst = []
    #Change Category Label when Button is Pressed
    ctg_label.config(text=ctg[a])
    #Commit Changes
    conn.commit()
    #Close Connection
    conn.close()        
    #Clear The Text Boxes
    ax.delete(0,END)
    bx.delete(0,END)
    cx.delete(0,END)
    #Relocate the Focus of the Submit Button
    submit_btn.bind('<Return>', ax.focus_set())

# =============================================================================
# #   MIGHT BE USEFUL LATER
# #Query Function
# def query():
#     #Database Creation & Connection
#     conn = sqlite3.connect('./'+str(seed)+'.db')
#     c = conn.cursor()
#     #Query the Database
#     c.execute("SELECT * FROM addresses")
#     records= c.fetchall()
#     #Loop Through Results
#     print_records = ''
#     for record in records:
#             print_records += str(record) + "\n"
#     query_label = Label(root, text=print_records)
#     query_label.grid(row=6, column=0, columnspan=2) 
#     #Commit Changes
#     conn.commit()
#     #Close Connection
#     conn.close()       
# =============================================================================

#Category Label
global ctg_label
ctg_label = Label(root,text=ctg[a])
ctg_label.grid(row=0, column=1, columnspan=2,sticky="NSEW")

#Entry Boxes
ax=Entry(root, width= 30)
ax.grid(row=1, column=1,sticky="E")
bx=Entry(root, width=30)
bx.grid(row=2, column=1,sticky="E")
cx=Entry(root, width=30)
cx.grid(row=3, column=1,sticky="E")

#Text Box Labels
seed_lbl = Label(root, text='No: '+str(seed))
seed_lbl.grid(row=0, column=0,sticky="W")
ax_lbl = Label(root, text='Hiç')
ax_lbl.grid(row=1, column=0,sticky="W")
bx_lbl = Label(root, text='Bazen')
bx_lbl.grid(row=2, column=0,sticky="W")
cx_lbl = Label(root, text='Sık')
cx_lbl.grid(row=3, column=0,sticky="W")

#Create Submit Button
submit_btn= Button(root, text='Gönder', command=submit)
submit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100,sticky="NSEW")
    
#Controlling the Keyboard Flow in the Interface
ax.focus()
def focus(x1,x2):
    def go_to_next_entry(event):
        x2.focus_set()
    x1.bind('<Return>', go_to_next_entry)
focus(ax,bx)
focus(bx,cx)
focus(cx,submit_btn)
submit_btn.bind('<Return>', submit)

#Commit Changes
conn.commit()
#Close Connection  
conn.close()
#Main Loop
root.mainloop()