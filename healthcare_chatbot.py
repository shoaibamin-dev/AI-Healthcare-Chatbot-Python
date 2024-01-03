import random
#import emoji
from tkinter import *
#from tkinter.ttk import *

#chemoji = emoji.emojize('Python is :thumbs_up:')
#print(chemoji)

#print("\U0001F600")


#c = '😆'

#print(chr(128522))
#print("The ASCII value of '" + c + "' is", ord(c))

diseases = {
    'fever':['temperature', 'cold', 'headache', 'cough', 'flu', 'tired', 'laziness', 'sinus', 'pain', 'weakness', 'vomiting', 'urination', 'vision']
}
diseases_prediction = {
    'fever': 0
}

random_questions = ['Is the fever accompanied by a headache?',
                    'Please tell me more about it. Are you vomiting lately?',
                    'Does your skin have a yellowing tinge?',
                    'Do you feel weakness?',
                    'Have you experienced fever before?',
                    'Are you experiencing problem with vision',
                    'Do you have pain with urination',
                    'Are you having neck pain that causes significant neck stiffness',
                    'Do you experience having difficulty breathing.']


general_questions = ['Hmmm, I see you are so much in trouble. What else are you feeling?',
                    'I am sorry to hear that you are sick. Please tell me more about it.',
                     'I am sorry to hear that you\'re not feeling well. Please state further.',
                     'I’m terribly sorry to hear that. Feel free to tell me your further problems.',
                     'People tend to get sick don\'t worry. Tell me more about it.']



global_current_answer = 'pain'
global_question_counter = 0


def get_random_questions(dis, ind):
    #i = random.randrange(len(random_questions))
    #new_msg = random_questions[i].replace("__DISEASE__", dis)
    new_msg = random_questions[ind]

    return new_msg


def get_general_questions():
    i = random.randrange(len(general_questions))
    new_msg = general_questions[i]
    return new_msg



#print(len(diseases['fever']))
#print()



v = Tk()

#canvas = Canvas(v,width=800, height=640)
#canvas.pack()

frame = Frame(v, bd=2, relief=SUNKEN)

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)


xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=E+W)

yscrollbar = Scrollbar(frame)
yscrollbar.grid(row=0, column=1, sticky=N+S)

canvas = Canvas(frame, width=800, height=520, bd=0,scrollregion=(0, 0, 100000000, 100000000),
                xscrollcommand=xscrollbar.set,
                yscrollcommand=yscrollbar.set)

canvas.grid(row=0, column=0, sticky=N+S+E+W)

xscrollbar.config(command=canvas.xview)
yscrollbar.config(command=canvas.yview)

frame.pack()



cc = canvas.create_text(400,25,text="Chat bot - Your personal assistant",font=('Courier',18))

#h_text = StringVar()
#h_label = Label(v, text='Chat bot - Your personal assistant', font=('Courier',18), padx=150, pady=6,bg="#C6C6C6",foreground = '#313b00')
#h_label.grid(row=0,column=1)

cpanel_msg = "\n\n\n Chatbot Said: How can I help you? What symptoms do you have?";
crpanel_msg = '\n\n'

def chatbot_init():
    global_current_answer = 'pain'
    #cpanel.insert(END, "\n Chatbot Said: How can I help you? What symptoms do you have?")
    canvas.itemconfig(cpanel, text=cpanel_msg)
    canvas.itemconfig(crpanel, text=crpanel_msg)



def addchat(self = NONE):
    #h_label.destroy()
    #canvas.itemconfig(cc, text="Goodbye, world")
    global global_question_counter
    global global_current_answer
    global cpanel_msg
    global crpanel_msg


    msg = mpanel.get('1.0',END)
    #cpanel.insert(END,"\n You Said: "+msg)
    crpanel_msg += "\n\n\n You Said: "+msg
    canvas.itemconfig(crpanel, text=crpanel_msg)



    mpanel.delete('1.0',END)




    split_msg = msg.split()
    single_word_found = False


    #I have headache very bad
    for j in range(len(split_msg)):
        single_word = split_msg[j]
        for k in (diseases['fever']):
            single_word_found = False
            if (single_word == k):
                global_current_answer = single_word
                diseases_prediction['fever'] = diseases_prediction['fever'] + 1
                single_word_found = True
                break
        if(single_word_found): break


    if (global_question_counter > 3):
        print("global_question_counter exceeded 5")
        if (diseases_prediction['fever'] > 2):
            #cpanel.insert(END, "\n\n Chatbot Said: 'Based on the symptoms that you have, this is a case of Fever. I would suggest that you meet our General Physician right away.'")
            cpanel_msg += "\n\n\n\n\n Chatbot Said: 'Based on the symptoms that you have, this is a case of Fever. I would suggest that you meet our General Physician right away.'"
            canvas.itemconfig(cpanel, text=cpanel_msg)
            return

    if(single_word_found):
        #cpanel.insert(END, "\n Chatbot Said: " + (get_random_questions(global_current_answer,global_question_counter) ))
        cpanel_msg += "\n\n\n\n Chatbot Said: " + (get_random_questions(global_current_answer,global_question_counter))
        canvas.itemconfig(cpanel, text=cpanel_msg)
    else:

        #cpanel.insert(END, "\n Chatbot Said: " + (get_general_questions()))
        cpanel_msg += "\n\n\n\n Chatbot Said: " + (get_general_questions())
        canvas.itemconfig(cpanel, text=cpanel_msg)



    global_question_counter += 1

    #print(global_question_counter)
    #print(global_current_answer)

    #cpanel.see("end")


#t_text = StringVar()
#t = Text(v, textvariable=t_text)
#t.grid(row=1,column=0)


#cpanel = Text(bd=3,bg="#fafafa",font = ('Verdana', 11),foreground="#5c0417")



cpanel = canvas.create_text(10,0,anchor='nw',font = ('Verdana', 12),fill="#034396")

crpanel = canvas.create_text(760,0,anchor='ne',font = ('Verdana', 12),fill="#961203")



#canvas.configure(yscrollcommand=scroll_y.set)
#canvas.configure(scrollregion=canvas.bbox("all"))
#cpanel.place(x = 50, y = 40, height = 500, width = 700)

mpanel = Text(bd=3,bg="#f5f2f2",font = ('Verdana', 10),foreground="#1e0347")
mpanel.place(x = 50, y = 550, height = 50, width = 600)

#style = Style()
#style.configure('W.TButton', )

send_button = Button(v,text="Send",command = addchat, bd=2,font = ('Helvetica', 13, 'bold'),foreground = '#fafafa',bg= "#544669", activebackground= "#897f99")
send_button.place(x = 660, y = 550, height = 50, width = 100)


#key_bind  = Entry(v)
#key_bind.bind("<Return>",addchat)

v.bind('<Return>',  addchat)

chatbot_init()

v.geometry('800x620+540+40')
v.configure(bg='#C6C6C6')

v.resizable(width=False, height=False)

v.title('ChatTalk')


v.mainloop()

