from tkinter import *
from tkinter import messagebox
import pyttsx3
import json
from difflib import get_close_matches




engine=pyttsx3.init()


# get_close_matches(word,possiblities,n,cutoff)

# close_match=get_close_matches('appel',['ape','apple','apps','faizan','khan']) #0.0-1.0
# print(close_match)




#functionality Part

def search():
    data=json.load(open('data.json'))

    word=entryField.get() #RAIN
    word=word.lower() #rain
    textarea.delete(0.0,END)

    if word in data:
        textarea.config(state=NORMAL)
        for meaning in data[word]:
            textarea.insert(END,u'\u2022'+meaning+'\n\n')
        textarea.config(state=DISABLED)



    elif len(get_close_matches(word,data.keys()))>0:
        best_match=get_close_matches(word,data.keys())[0]
        result=messagebox.askyesno('Confirm',f'Did you mean {best_match} instead?')
        if result==True:
            entryField.delete(0,END)
            entryField.insert(0,best_match)
            textarea.config(state=NORMAL)
            for m in data[best_match]:
                textarea.insert(END,u'\u2022'+m+'\n\n')

            textarea.config(state=DISABLED)

        else:
            closest_matches=get_close_matches(word, data.keys())
            result = messagebox.askyesno('Confirm', f'Did you mean {closest_matches[1]} instead?')
            if result==True:
                entryField.delete(0, END)
                entryField.insert(0, closest_matches[1])
                textarea.config(state=NORMAL)
                for m in data[closest_matches[1]]:

                    textarea.insert(END, u'\u2022' + m + '\n\n')

                textarea.config(state=DISABLED)

            else:
                messagebox.showerror('Error','Word doesnt exist Please double check it')







    else:
        print('word doesnt exist')





def meaningAudio():
    data_set=textarea.get(0.0,END)
    engine.getProperty('rate')
    engine.setProperty('rate', 100)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(data_set)
    engine.runAndWait()

def wordAudio():
    data=entryField.get()
    engine.getProperty('rate')
    engine.setProperty('rate', 200)
    voices = engine.getProperty('voices')
    print(voices)
    engine.setProperty('voice', voices[2].id)
    engine.say(data)
    engine.runAndWait()


def clear():
    textarea.config(state=NORMAL)
    textarea.delete(0.0,END)
    entryField.delete(0,END)
    textarea.config(state=DISABLED)


def exit_window():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result==True:
        root.destroy()

    else:
        messagebox.showinfo('Title','Ok as you wish,Continue Learning')




root=Tk()
root.title('Dictionary created by Faizan')
root.geometry('1000x626+10+30')
root.resizable(0,0)
bgImage=PhotoImage(file='background.png')

bgLabel=Label(root,image=bgImage)
bgLabel.pack()

wordLabel=Label(root,text='Enter Word',font=('Castellar',29,'bold'),fg='red3')

wordLabel.place(x=530,y=20)

entryField=Entry(root,font=('arial',23,'bold'),bd=6,relief=RIDGE,justify='center')
entryField.focus_set()

entryField.place(x=510,y=80)

searchImage=PhotoImage(file='search.png')

searchButton=Button(root,image=searchImage,bd=0,cursor='hand2',command=search)

searchButton.place(x=620,y=150)

micImage=PhotoImage(file='mic.png')

micButton=Button(root,image=micImage,bd=0,cursor='hand2',command=wordAudio)

micButton.place(x=710,y=153)

meaningLabel=Label(root,text='Meaning',font=('Castellar',29,'bold'),fg='red3')

meaningLabel.place(x=580,y=240)

textarea=Text(root,font=('Arial',18,'bold'),width=34,height=8,bd=8,
              relief=GROOVE,wrap='word',state=DISABLED)
textarea.place(x=460,y=300)

microphoneImage=PhotoImage(file='microphone.png')
microphoneButton=Button(root,image=microphoneImage,bd=0,cursor='hand2'
                        ,command=meaningAudio)
microphoneButton.place(x=530,y=555)

clearImage=PhotoImage(file='clear.png')
clearButton=Button(root,image=clearImage,bd=0,cursor='hand2',command=clear)
clearButton.place(x=660,y=555)

exitImage=PhotoImage(file='exit.png')
exitButton=Button(root,image=exitImage,bd=0,cursor='hand2',command=exit_window)
exitButton.place(x=790,y=555)

root.mainloop()



