import tkinter
import tkinter.messagebox
import pickle

window = tkinter.Tk()
window.title("Thamarai's To Do List")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="ATTENTION!", message="You must enter a task!")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="ATTENTION!", message="You must select a task!")

def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="ATTENTION!", message="Cannot find any tasks!")

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

frame_tasks = tkinter.Frame(window)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(window, width=60)
entry_task.pack()

add__task = tkinter.Button(window,text="Add task", font=("Comic Sans MS",10,"bold"),width=48,command=add_task)
add__task.pack()

delete__task = tkinter.Button(window,text="Delete task",font=("Comic Sans MS",10,"bold"), width=48,command=delete_task)
delete__task.pack()

load__tasks = tkinter.Button(window,text="Load tasks",font=("Comic Sans MS",10,"bold"), width=48,command=load_tasks)
load__tasks.pack()

save__tasks = tkinter.Button(window,text="Save tasks",font=("Comic Sans MS",10,"bold"), width=48,command=save_tasks)
save__tasks.pack()

window.mainloop()