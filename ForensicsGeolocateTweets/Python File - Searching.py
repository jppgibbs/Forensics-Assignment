import tkinter as tk
import json
from tkinter import ttk

from tkinter import scrolledtext
from tkinter import Combobox

import folium
import webbrowser

# Create instance
win = tk.Tk()

# Add a title
win.title("Tweet Analyser")

win.minsize(width=850, height=500)
win.maxsize(width=850, height=500)

# Disable resizing the GUI
win.resizable(0,0)

# Modify adding a Label
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)
#Modified Button Click Function

def SearchJSON():
    map_osm = folium.Map(location=[53.472328361821766,-2.23959064483645])
    #action.configure(text='Hello ' + name.get())
    #print("you have entered ... "+name.get())
    searchkeyword = name.get()
    print("you have entered ... "+searchkeyword)
    
    with open('Manchester_Part-1.json') as data_file:
        countt = 0
        for row in data_file:
            data = json.loads(row)
            tempText = data['text']
            latt = data['geoLocation']['latitude']
            longg = data['geoLocation']['longitude']


            print("you have entered ... "+tempText)
            
            if searchkeyword in tempText:
                countt = countt + 1
                StringToScroll = "\n\n["+str(countt)+"] Date: " + data['createdAt']['$date'] + "Tweet Text:" + data['text']
                folium.Marker([latt,longg], popup=tempText).add_to(map_osm)
                scr.insert(tk.INSERT,StringToScroll)

            else:
               # scr.insert(tk.INSERT,"Nothing Found")
                print("Nothing Found")    
        map_osm.save('plotted.html')
    
def ShowPlottedSearchResults():
    webbrowser.open_new_tab('plotted.html')

"""
    with open('Manchester_Part-1.json') as data_file:
        for row in data_file:
            data = json.loads(row)
            StringToScroll = "Date: " + data['createdAt']['$date'] + " latitude:" + str(data['geoLocation']['latitude']) + "Tweet Text:" + data['text']            
            createdAt= data['createdAt']['$date']
            #print("Geo-Location "+str(data['geoLocation']['latitude']))
            print("Tweet Text "+data['text'])
            print("Place Name: "+data['place']['name'])
            print("Place Full Name: "+data['place']['fullName'])
            print(" ...... Next Record ........")
            
    scr.insert(tk.INSERT,StringToScroll)

"""
# Changing our Label
ttk.Label(win, text="Search String:").grid(column=0, row=0)
# Adding a Textbox Entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=40, textvariable=name)
nameEntered.grid(column=0, row=1)

# Adding a Button
action = ttk.Button(win, text="Search!", command=SearchJSON)
action.grid(column=0, row=6)

# Adding a ComboBox
root = tk.Tk()
cb = ttk.Combobox(root,state='readonly')
labName = ttk.Label(root,text='Names: ')
labTel = ttk.Label(root,text='TelNum:')
labCity = ttk.Label(root,text='City: ')
entTel = ttk.Entry(root,state='readonly')
entCity = ttk.Entry(root,state='readonly')

with open('file.csv','r',newline='') as file:
    reader = csv.reader(file,delimiter='\t')    


cb.grid(row=0,column=1)
labName.grid(row=0,column=0)
labTel.grid(row=1,column=0)
entTel.grid(row=1,column=1)
labCity.grid(row=2,column=0)
entCity.grid(row=2,column=1)

# Using a scrolled Text control
scrolW = 100
scrolH = 20
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

# Adding a Button
loadingJsonButton = ttk.Button(win, text=" Show Plotted Search Results ",
command=ShowPlottedSearchResults)
loadingJsonButton.grid(column=0, columnspan=3)
# Place cursor into name Entry
nameEntered.focus()
#======================
# Start GUI
#======================
win.mainloop()