import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#from tkdatetime import datetimecalen
from tkcalendar import *

root = Tk()
root.geometry("600x400")
root.title('Alfa team')

frame = Frame(root,)
# Labels

sign = Label(frame, text="Login", font=('Arial Bold', 16))
sign.grid(row=0, column=1, pady=(0, 20))

userLabel = Label(frame, text="Username: ")
userLabel.grid(
    row=1, column=0,)
PasswordLabel = Label(frame, text="Password: ")
PasswordLabel.grid(
    row=2, column=0, )


# Entrys
userName = Entry(frame, width=35, bd=2)
userName.grid(
    row=1, column=1, padx=10, pady=10)
Password = Entry(frame, width=35, show='*', bd=2)
Password.grid(
    row=2, column=1, padx=5, pady=10)


# functions


def time():
    # current date and time

    now = datetime.now()
    date_time = now.strftime("%I:%M:%S")
    time_label.config(text=date_time)


def verify_login():
    suffix = []
    user = userName.get()
    passw = Password.get()

    userName.delete(0, END)
    Password.delete(0, END)

    list_of_files = os.listdir()  # all these can be done with path glob**
    for i in list_of_files:
        r_i = i.split('.')
        suffix.append(r_i[0])

    if(user in suffix):
        user_file = open(str(user+".txt"), "r")
        verify = user_file.read().splitlines()
        print(verify)
        if(passw in verify):
            messagebox.showinfo(
                title="Successful", message="Login Successful")
            open_mainwindow()
        else:
            messagebox.showerror(title="Error", message="Wrong Password")
    else:
        messagebox.showerror(title="Error", message="No user found")

# open new Window and destroy previous ONE.


def show_frame(frame):
    frame.tkraise()


def open_mainwindow():
    global clockBtn
    root.destroy()

    mainWindow = Tk()
    mainWindow.geometry("950x500")
    mainWindow.title('Alfa ')
    # rootHeight = mainWindow.winfo_height()
    # rootWidth = mainWindow.winfo_width()
    my_menu = Menu(mainWindow)
    mainWindow.config(menu=my_menu)

    # MenuItems
    # File
    file_menu = Menu(my_menu)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Exit", command=mainWindow.quit)

    edit_menu = Menu(my_menu)
    my_menu.add_cascade(label="Edit", menu=edit_menu)

    option_menu = Menu(my_menu)
    my_menu.add_cascade(label="Options", menu=option_menu)

    Tools_menu = Menu(my_menu)
    my_menu.add_cascade(label="Tools", menu=Tools_menu)

    Help_menu = Menu(my_menu)
    my_menu.add_cascade(label="File", menu=Help_menu)


# ============================================================================================================

    # Frames
    frame_add = Frame(mainWindow, width=280, height=480,
                      )

    frame_add.grid(row=0, column=0, padx=10, pady=10, sticky='nw')
    frame_add.grid_propagate(False)
# ============================================================================================================

    frame_middle_1 = Frame(mainWindow, width=590, height=480,
                           )


# ============================================================================================================

    frame_middle_2 = Frame(mainWindow, width=590, height=480,
                           )
    frame_middle_3 = Frame(mainWindow, width=590, height=480,
                           )

    # frame_right = Frame(mainWindow, width=240, height=480,
    #                     )

    # frame_right.grid(row=0, column=3, padx=100, pady=10, sticky='nw')

    # frame_right.grid_propagate(False)

    for frame in (frame_middle_1, frame_middle_2, frame_middle_3):
        frame.grid(row=0, column=1, padx=10, pady=10, sticky='nw')
        frame.grid_propagate(False)

    show_frame(frame_middle_1)

# ============================================= Frame middle 1 Code ===============================================================
    weatherLabel = Label(
        frame_middle_1, text="weather with symbols and emojis maybe?", borderwidth=1, relief="solid", font=('Arial Bold', 10))
    weatherLabel.grid(
        row=0, column=0, pady=(0, 20), padx=20, ipadx=10, ipady=10,  sticky='ew')
    amountLabel = Label(
        frame_middle_1, text="Euros in the bank 10000000 EUR Currently", borderwidth=1, relief="solid", font=('Arial Bold', 10))
    amountLabel.grid(
        row=1, column=0, pady=(0, 20), padx=20, ipadx=10, ipady=10,  sticky='ew')
# ============================================= Frame middle 2 Code ===============================================================
    catLabel = Label(frame_middle_2, text="Category", font=("Arial Bold", 10))
    catLabel.grid(row=0, column=0, pady=(100, 20), padx=(20, 10))
    categoryCombo = ttk.Combobox(frame_middle_2, width=30, height=10)
    categoryCombo['values'] = ['Rent', 'Travel',
                               'Groceries', 'Subscription', 'Guilty Pleasures']
    categoryCombo.current(0)
    categoryCombo.grid(
        row=0, column=1, pady=(100, 20), padx=10, ipadx=5)

    amountLabel = Label(frame_middle_2, text="Amount",
                        font=("Arial Bold", 10))
    amountLabel.grid(row=1, column=0, pady=(0, 20), padx=(20, 10))

    amountEntry = Entry(frame_middle_2, width=35, bd=2)
    amountEntry.grid(row=1, column=1, pady=(0, 20), padx=10)

    dateLabel = Label(frame_middle_2, text="Date",
                      font=("Arial Bold", 10))
    dateLabel.grid(row=2, column=0, pady=(0, 20), padx=(20, 10))

    dateEntry = Entry(frame_middle_2, width=35, bd=2,
                      )
    dateEntry.insert(0, "Enter manual date or use picker")
    dateEntry.grid(row=2, column=1, pady=(0, 20), padx=10)

    moneyLabel = Label(frame_middle_2, text="Money in?",
                       font=("Arial Bold", 10))
    moneyLabel.grid(row=3, column=0, pady=(0, 20), padx=(20, 10))

    var = IntVar()
    moneyBox = Checkbutton(frame_middle_2, variable=var, fg="#4465f9",)
    moneyBox.grid(row=3, column=1, pady=(0, 20), padx=5, sticky='w')

# ============================================================================================================

    # Buttons
    logoutBtn = Button(frame_middle_1, text="Logout", bg="#4465f9",
                       fg="white", height=1, width=15, font="Raleway", command=mainWindow.quit)
    logoutBtn.grid(row=0, column=2, pady=20, padx=120)

    transacBtn = Button(frame_middle_1, text="Add Transaction", bg="#4465f9",
                        fg="white", height=1, width=15, font="Raleway", command=lambda: show_frame(frame_middle_2))
    transacBtn.grid(row=1, column=2, pady=20, padx=120)

    editBtn = Button(frame_middle_1, text="Edit account", bg="#4465f9",
                     fg="white", height=1, width=15, font="Raleway")
    editBtn.grid(row=2, column=2, pady=20, padx=120)

    setupBtn = Button(frame_middle_1, text="Setup", bg="#4465f9",
                      fg="white", height=1, width=15, font="Raleway")
    setupBtn.grid(row=3, column=2, pady=20, padx=120)

    summaryBtn = Button(frame_middle_1, text="Account Summary", bg="#4465f9",
                        fg="white", height=1, width=15, font="Raleway")
    summaryBtn.grid(row=4, column=2, pady=20, padx=120)
    playBtn = Button(frame_middle_1, text="Play Lotto", bg="#4465f9",
                     fg="white", height=1, width=15, font="Raleway")
    playBtn.grid(row=5, column=2, pady=20, padx=120)

    clockBtn = PhotoImage(file='images/clockv2.png')

    getTimeBtn = Button(frame_add, image=clockBtn, border=0,
                        command=time)

    getTimeBtn.grid(row=0, column=0, pady=20, padx=5, sticky="ew")

    # ========================================Form 2 button ====================================================================

    # logoutBtn_2 = Button(frame_middle_2, text="Logout", bg="#4465f9",
    #                      fg="white", height=1, width=15, font="Raleway", command=mainWindow.quit)
    # logoutBtn_2.grid(row=0, column=2, pady=20, padx=100)

    # transacBtn_2 = Button(frame_middle_2, text="Add Transaction", bg="#4465f9",
    #                       fg="white", height=1, width=15, font="Raleway", )
    # transacBtn_2.grid(row=1, column=2, pady=20, padx=100)

    # canelBtn = Button(frame_middle_2, text="Cancel and return", bg="#4465f9",
    #                   fg="white", height=1, width=15, font="Raleway", command=lambda: show_frame(frame_middle_1))
    # canelBtn.grid(row=2, column=2, pady=20, padx=100)


# ============================================================================================================

    # Time Label
    global time_label
    time_label = Label(frame_add, text="Pick Time", font=("Arial", 10))
    time_label.grid(row=1, column=0, pady=5, padx=20,)

    # Calender
    cal = Calendar(frame_add, selectmode="day", font="Arial 8", 
                   locale="fi_FI", disabledforeground="red",
                   cursor="hand2")
   
    cal.grid(row=2, column=0, pady=20, padx=20, )


# Buttons
loginBtn = Button(frame, text="login", bg="#4465f9",
                  fg="white", height=1, width=10, font="Raleway", command=verify_login)
loginBtn.grid(row=3, column=1, pady=5)


frame.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()
