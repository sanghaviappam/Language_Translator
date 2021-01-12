from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
from textblob import TextBlob
from tkinter import ttk
root = tk.Tk()
root.geometry('700x600')
root.title('Language Translater')
root.iconbitmap('translator.ico')
root.resizable(False,False)
root.configure(bg='skyblue')
lan_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu', 'Filipino': 'fil', 'Hebrew': 'he'}
def tt():
    try:
       word3 = TextBlob(varname1.get())
       lan = word3.detect_language()
       lan_todict = languages.get()
       lan_to = lan_dict[lan_todict]
       word3 = word3.translate(from_lang=lan,to=lan_to)
       label3.configure(text=word3)
       varname2.set(word3)
    except:
       varname2.set('Try another keyword')
def main_exit():
    rr = messagebox.askyesnocancel('Notification','Are you want to exit !',parent=root)
    if(rr == True):
      root.destroy()
##########################################################################Combo Box
ttk.Label(root, text = "Choose Language:",font=('times',15,'italic bold')).grid(column = 100, row = 50)# Button Action

languages= tk.StringVar()
monthchoosen = ttk.Combobox(root, width=27,
                             textvariable=languages)

#languages = StringVar()
font_box = Combobox(root,width=25,textvariable=languages,state='readonly')
font_box['values'] = [e for e in lan_dict.keys()]
font_box.current(37)
font_box.place(x=550,y=0)


########################################################################## Entry BOx
varname1 = StringVar()
entry1 = Entry(root,width = 30,textvariable = varname1,font =('times',15,'italic bold'))
entry1.place(x=220,y=75,width=400,height=100)

varname2 = StringVar()
entry2 = Entry(root,width = 30,textvariable = varname2,font =('times',15,'italic bold'))
entry2.place(x=220,y=220,width=400,height = 100)
###########################################################################Labels
label1 = Label(root,text='Enter Words:',font=('times',20,'italic bold'),bg='orange')
label1.place(x=20,y=120)

label2 = Label(root,text ='Translated:',font=('times',20,'italic bold'),bg='orange')
label2.place(x=20,y=250)

label3 = Label(root,text = ' ',font =('times',20,'bold'))      #turquoise1
label3.place(x=220,y=250)

########################################################################BUttons
btn1=Button(root,text='Click',bd=10,bg='yellow',activebackground='red',width=10,
            font=('times',17,'italic bold'),command = tt)
btn1.place(x=200,y=400)

btn2=Button(root,text='Exit',bd = 10,bg='yellow',activebackground='red',width=10,
            font=('times',17,'italic bold'),compound = RIGHT,command=main_exit)
btn2.place(x=400,y=400)
root.mainloop()