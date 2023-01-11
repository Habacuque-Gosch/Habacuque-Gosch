
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import DataUser

tela = Tk()
tela.title("HB Systems - Access Panel")
tela.geometry("600x300")
tela.config(background="Black")
tela.resizable(width=False, height=False)
tela.attributes("-alpha", 0.9)
tela.iconbitmap(default="fotos/icon.ico")

logo = PhotoImage(file="fotos/ft.png")

LeftFrame = Frame(tela, width=200, height=300, bg="White", relief="raise")
LeftFrame.pack(side= LEFT)

RightFrame = Frame(tela, width=395, height=300, bg="Black", relief="raise")
RightFrame.pack(side= RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="White")
LogoLabel.place(x=5,y=30)

WelcomeLabel = Label(LeftFrame, text="Welcome!", font=("Century Gothic", 20), bg="Black", fg="White")
WelcomeLabel.place(x=35,y=220)

UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="Black", fg="White")
UserLabel.place(x=5,y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150,y=110)

Password = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg="Black", fg="White")
Password.place(x=5,y=150)

PasswordUser = ttk.Entry(RightFrame, width=30, show="*")
PasswordUser.place(x=150,y=160)

def Login():
    User = UserEntry.get()
    Pass = PasswordUser.get()

    DataUser.cursor.execute("""
    SELECT * FROM Users
    WHERE User = ? and Password = ?
    """, (User,Pass))
    print('Bem-Vindo')
    VerifyLogin = DataUser.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Acesso confirmado, Bem-Vindo!")
    except:
        messagebox.showinfo(title="Login Info", message="acesso negado, verifique se esta cadastrado no sistema!")

LoginButton = ttk.Button(RightFrame,text= "Login",width=30, command=Login)
LoginButton.place(x=100,y=225)

def Register():
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    NomeLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 20), bg="Black", fg="White")
    NomeLabel.place(x=5, y=5)

    NomeEntry = Entry(RightFrame, width=40)
    NomeEntry.place(x=100,y=18)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="Black", fg="White")
    EmailLabel.place(x=5, y=55)

    EmailEntry = Entry(RightFrame, width=40)
    EmailEntry.place(x=100,y=66)

    def RegisterDataUser():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PasswordUser.get()

        if (Name == "" and Email == "" and User == "" and Pass == ""):
            messagebox.showerror(title="register error", message="preencha todos os campos")
        else:
            DataUser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?,?,?,?)
            """, (Name, Email, User, Pass))
            DataUser.conn.commit()
            messagebox.showinfo(title="Registe Info", message="conta criada com sucesso")

    Register = ttk.Button(RightFrame, text="Register", width=30, command=RegisterDataUser)
    Register.place(x=100, y=225)

    def BackLogin():
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        LoginButton.place(x=100)
        RegisterButton.place(x=125)

    Back = ttk.Button(RightFrame, text="Back", width=30, command=BackLogin)
    Back.place(x=100, y=260)

RegisterButton = ttk.Button(RightFrame,text= "Register",width=20, command=Register)
RegisterButton.place(x=125,y=260)

tela.mainloop()