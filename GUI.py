# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 14:04:40 2021

@author: DiiCo
"""

#Libraries
from tkinter import *
import sqlite3
import webbrowser

#Window Creation
root = Tk()
root.title('Notlandırma Programı')
root.geometry('400x400')

#Create Database & Tables
conn = sqlite3.connect('database.db')
#Create Cursor
c = conn.cursor()
# =============================================================================
# #Creating Database (Use only once)
# c.execute("""CREATE TABLE addresses (
#     Kategori text,
#     Hiç integer,
#     Bazen integer,
#     Sık integer
#     )""")
# =============================================================================

#Database Connection
conn = sqlite3.connect('database.db')
#Create Cursor
c = conn.cursor()

#Categories
ctg = ['Kaygı (8)','Obsesyon (7)','Sosyal Fobi (3)','İçedönüklük (3)','Somatizasyon (7)','Travma (3)','Anoreksiya (3)','Bulimia (3)','Depresyon (12)','Hipomani (9)','Uyku Bozukluğu (2)','Dehb (17)','Öfke Kontrolü (8)','Sosyopati (18)','Psikotik Belirti(12)','İmpuls Kontrolü (5)','Bağımlılık (7)','Disosyatif Belirti (3)','Borderline (8)']

lst= []

a= 0
#Create Submit Function for the Database
def submit():
    global a
    a += 1   
    if a == 19:
       f = open("Hasta Test Notlandırma Cıktısı.txt", "w",encoding="utf-8")
       for i in range(24):
           f.write(lst[i])
       f.close()
       webbrowser.open("Hasta Test Notlandırma Cıktısı.txt") 
       a = 0
    #Database Creation & Connection
    conn = sqlite3.connect('database.db')
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
    #Fetch Data from Categories to Write into a Notepad
    c.execute("SELECT Hiç FROM addresses")
    cnt1 = c.fetchall()
    c.execute("SELECT Bazen FROM addresses")
    cnt2 = c.fetchall()
    c.execute("SELECT Sık FROM addresses")
    cnt3 = c.fetchall()
    lst.append((str(ctg)+'\t\tHiç/'+str(*cnt1[-1])+'\tBazen/'+str(*cnt2[-1])+'\tSık/'+str(*cnt3[-1])))
    print(lst[-1])
    #Change Label when Button is Pressed
    ctg_label.config(text=ctg[a])
    #Commit Changes
    conn.commit()
    #Close Connection
    conn.close()        
    #Clear The Text Boxes
    ax.delete(0,END)
    bx.delete(0,END)
    cx.delete(0,END)
    
#Create Query Function
def query():
    #Database Creation & Connection
    conn = sqlite3.connect('database.db')
    #Create Cursor
    c = conn.cursor()
    #Query the Database
    c.execute("SELECT * FROM addresses")
    records= c.fetchall()
    #Loop Through Results
    print_records = ''
    for record in records:
            print_records += str(record) + "\n"
    query_label = Label(root, text=print_records)
    query_label.grid(row=6, column=0, columnspan=2)
    #Commit Changes
    conn.commit()
    #Close Connection
    conn.close()       

#Category Label
global ctg_label
ctg_label = Label(root,text=ctg[a])
ctg_label.grid(row=0, column=1, columnspan=2)

#Entry Boxes
ax=Entry(root, width=30)
ax.grid(row=1, column=1, padx=20)
bx=Entry(root, width=30)
bx.grid(row=2, column=1)
cx=Entry(root, width=30)
cx.grid(row=3, column=1)

#Text Box Labels
ax_lbl = Label(root, text='Hiç')
ax_lbl.grid(row=1, column=0)
bx_lbl = Label(root, text='Bazen')
bx_lbl.grid(row=2, column=0)
cx_lbl = Label(root, text='Sık')
cx_lbl.grid(row=3, column=0)

#Create Submit Button
submit_btn= Button(root, text='Gönder', command=submit)
submit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Create Query Button
query_btn = Button(root, text="Sonuçları Göster", command=query)
query_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

#Commit Changes
conn.commit()
#Close Connection
conn.close()    
#Main Loop
root.mainloop()