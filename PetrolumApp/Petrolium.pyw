import sqlite3
from tkinter import *
import tkinter.ttk as ttk
from tkinter.ttk import Progressbar
import random
import tkinter.messagebox as messagebox
from PIL import ImageTk, Image
from tkinter.ttk import Notebook, Style
from time import sleep
import datetime
import os
import customtkinter as ctk

# from tabulate import tabulate #  This library is for Printing Documents with lines table creations
from prettytable import PrettyTable
import prettytable
from tkinter import filedialog


DEFAULTHCRBG = "#4B4B4B"  # 72959F
SaveExtensions = [
    ("نوع فایل تان را انتخاب کنید ", "*.*"),
    ("تکست فایل ", "*.TXT"),
    ("پی دی اف ", "*.PDF"),
    ("اچ تی ام ال ", "*.HTML"),
]


root = ctk.CTk()
root.geometry("1300x760")
root.configure(bg="light gray")
root.iconbitmap("hcrIcon.ico")
root.title("Niazi Petrolium")
root.state("zoomed")


DateNow = datetime.date.today()


# ================== Main Functions =================


def ExitBtnFunc():
    extmsg = messagebox.askyesno("تانگ تیل نیازی ", "مطمئن هستی میخواهی خارج شوی ؟")
    if extmsg == 1:
        root.destroy()


def ProApp():
    messagebox.showerror("HCR-BLUE", "!این گزینه در نسخهء پروفیشنل قابل اجرا است ")


menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Open")
file_menu.add_command(label="Backup")
file_menu.add_command(label="Import")
file_menu.add_command(label="Export")
file_menu.add_command(label="Exit", command=ExitBtnFunc, image="")


seti_menu = Menu(menubar, tearoff=0)
seti_menu.add_command(label="Dark Theme", command=ProApp)
seti_menu.add_command(label="Default Theme", command=ProApp)
seti_menu.add_command(label="White Theme", command=ProApp)

# seti_menu.add_command(label="Default Theme", command=DEFAULTTHEME)

menubar.add_cascade(label="فایل ", menu=file_menu)
menubar.add_cascade(label="تنظیمات ", menu=seti_menu)
menubar.add_cascade(label="مشاهده ")
menubar.add_cascade(label="پنجره ")
menubar.add_cascade(label="درباره ")


mygreen = "#d2ffd2"
myred = "#dd0505"
mylightblue = "light blue"

BGCOL1 = "#003A45"
BGCOL2 = "#2f2f2f"
FGCOL1 = "#FFFFFF"
FGCOL2 = "#6f7f3f"
FGCOL3 = "#ffffff"
FGCOL4 = "dark red"
BGCOL4 = "white"
BGGRAY = "#6f8f9f"
BGLIGHTBLUE = "light blue"
BGBLUE = "blue"
BGBLACK = "black"
BGYELLOW = "yellow"
BGGREEN = "green"
BGRED = "red"
BGLIGHTYELLOW = "light yellow"
BGDEFAULT = "DFDFDF"
BGORANGE = "orange"
BGLIGHTGREEN = "light green"
BGWHITE = "white"
BGLIGHTGRAY = "light gray"
BGDARKSKY = "#0F1F3F"
MODERNBACK = "#420052"
MODERNFORGROUND = "#8F49A6"
MODERNBACKBLUE = "#5D96A1"
MODERNFORGROUNDBLUE = "#454D9C"
MODERNLIGHTBLUE = "#5D96A1"
MODERNPINK = "#410070"
CTKDARK = "#2B2B2B"
DarkBlue = "#39003D"


rim1 = Image.open("DataFiles/RadioImage1.png")
rim2 = rim1.resize((25, 25))
RadioImage1 = ImageTk.PhotoImage(rim2)

BG1 = Image.open("DataFiles/RadioActiveImage1.png")
BG2 = BG1.resize((25, 25))
RadioActiveImage1 = ImageTk.PhotoImage(BG2)

# ============ importing image icons with standard sizes ===================
SaveImage1 = PhotoImage(file=r"DataFiles/SaveImage1.png")
UpdateImage1 = PhotoImage(file=r"DataFiles/UpdateImage1.png")
ClearImage1 = PhotoImage(file=r"DataFiles/ClearImage1.png")
ExitImage2 = PhotoImage(file=r"DataFiles/ExitImage2.png")
RefreshImage1 = PhotoImage(file=r"DataFiles/RefreshImage1.png")
# -------- Focused -----------
SaveImageFocused1 = PhotoImage(file=r"DataFiles/SaveImageFocused1.png")
UpdateImageFocused1 = PhotoImage(file=r"DataFiles/UpdateImageFocused1.png")
ClearImageFocused1 = PhotoImage(file=r"DataFiles/ClearImageFocused1.png")
ExitImageFocused1 = PhotoImage(file=r"DataFiles/ExitImageFocused1.png")
RefreshImageFocused1 = PhotoImage(file=r"DataFiles/RefreshImageFocused1.png")

# ============= Popup option icons =======================
Recycle1 = PhotoImage(file=r"DataFiles/Recycle1.png")
PopupExit1 = PhotoImage(file=r"DataFiles/PopupExit1.png")
PopupEdit1 = PhotoImage(file=r"DataFiles/PopupEdit1.png")
PopupRefresh1 = PhotoImage(file=r"DataFiles/PopupRefresh1.png")
PopupPrint1 = PhotoImage(file=r"DataFiles/PopupPrint1.png")

# ==========================================


style = Style()
style.theme_use("default")
style.configure(
    "TNotebook.Tab",
    background=MODERNPINK,
    foreground=BGLIGHTYELLOW,
    padding=[64, 0],
    tabmargins=[0, 0, 0, 0],
    font=("Swis721 BlkCn BT", 12),
)
style.configure("TNotebook", background=DEFAULTHCRBG)
style.map(
    "TNotebook.Tab",
    background=[("selected", BGORANGE)],
    foreground=[("selected", BGDARKSKY)],
)
style.layout("cb.TNotebook.Tab", [("TNotebook.Tab", {"side": "right", "sticky": "ne"})])


style2 = ttk.Style()
style2.configure(
    "Treeview.Heading",
    background=BGDARKSKY,
    foreground=BGLIGHTYELLOW,
    padding=[3, 4],
    tabmargins=[2, 5, 2, 0],
    font=("Arial", 8, "bold"),
)
style2.configure(
    "Treeview",
    background="#7c9f9f",
    foreground="black",
    font=("Bahnschrift SemiBold SemiConden", 10),
    rowheight=27,
    fieldbackground=BGDARKSKY,
)
style2.map(
    "Treeview",
    background=[("selected", "#0f0f1f")],
    foreground=[("selected", "yellow")],
)
style2.layout(
    "cb.Treeview.Row",
    [
        ("Treeitme.row", {"sticky": "nsew"}),
        ("Treeitme.image", {"side": "right", "sticky": "e"}),
    ],
)


tabControl = ttk.Notebook(root)

tab2 = Frame(tabControl, bg=DEFAULTHCRBG)
tab3 = Frame(tabControl, bg=DEFAULTHCRBG)
tab4 = Frame(tabControl, bg=DEFAULTHCRBG)
tab5 = Frame(tabControl, bg=DEFAULTHCRBG)
tab6 = Frame(tabControl, bg=DEFAULTHCRBG)
tab7 = Frame(tabControl, bg=DEFAULTHCRBG)


tabControl.add(tab2, text="Data Entry")
tabControl.add(tab3, text="Disal-02")
tabControl.add(tab4, text="Petrol-95")
tabControl.add(tab5, text="Petrol-92")
tabControl.add(tab6, text="Gas")
tabControl.add(tab7, text="Check Documents")


tabControl.pack(padx=2, side=RIGHT, anchor=NE)


# ========================================================================== Side Bar ==============
"""
min_w = 40
max_w = 200
cur_width = min_w
expanded = False

def Expand_1():
    global cur_width, expanded
    cur_width += 10
    rep = root.after(5,Expand_1)
    frame.config(width=cur_width)
    if cur_width >= max_w:
        expanded = True
        root.after_cancel(rep)
        fill()

def Contract_1():
    global cur_width, expanded
    cur_width -= 10
    rep = root.after(10,Contract_1)
    frame.config(width=cur_width)
    if cur_width <= min_w:
        expanded = False
        root.after_cancel(rep)
        fill()


def fill():
    if expanded:
        ProductsBtn.config(text="  محصولات", image=ProductsImage1,font=("B Mehr",10))
        CustomersBtn.config(text="  مشتریان ", image=CustomerImage1,font=("B Mehr",10))
        OrdersBtn.config(text="  سفارشات ", image=OrderImage2,font=("B Mehr",10))
        EmployeesBtn.config(text="  کارمندان ", image=StuffImage1,font=("B Mehr",10))
        ExpensesBtn.config(text="  مخارج ", image=ExpesesImage1,font=("B Mehr",10))
        TaxBtn.config(text="  مالیات ", image=TaxImage1,font=("B Mehr",10))
        ShowBtn.config(text="  مشاهده ", image=ShowImage1,font=("B Mehr",10))
        ExitBtn.config(text="  خخارج شدن", image=ExitImage1,font=("B Mehr",10))

        #Need to delete thme
        ProLbl.config(image=Profile1)

    else:
        ProductsBtn.config(text="",image=ProductsImage1,font=("B Mehr",10))
        CustomersBtn.config(text="",image=CustomerImage1,font=("B Mehr",10))
        OrdersBtn.config(text="",image=OrderImage2,font=("B Mehr",10))
        EmployeesBtn.config(text="", image=StuffImage1,font=("B Mehr",10))
        ExpensesBtn.config(text="", image=ExpesesImage1,font=("B Mehr",10))
        TaxBtn.config(text="", image=TaxImage1,font=("B Mehr",10))
        ShowBtn.config(text="", image=ShowImage1,font=("B Mehr",10))
        ExitBtn.config(text="", image=ExitImage1,font=("B Mehr",10))

        #Need to delete thme
        ProLbl.config(image=PersonM)
       	"""
# =========================================================================================

# SLID
SALERNAME = StringVar()
SLPNUM = StringVar()
SLFUELTYPE = StringVar()
SLCURRLTR = StringVar()
SLPASTLTR = StringVar()
SLPRICE = StringVar()
SLSEARCH = StringVar()
DISALSEARCH = StringVar()
PET95SEARCH = StringVar()
PET92SEARCH = StringVar()
GASSEARCH = StringVar()
DATEID = StringVar()


with sqlite3.connect("NiaziPetrolium.db") as db:
    cur = db.cursor()
    cur.execute(
        """
	CREATE TABLE IF NOT EXISTS DisalInfo(
	SLID INTEGER PRIMARY KEY AUTOINCREMENT,
	SALERNAME TEXT NOT NULL,
	SLPNUM TEXT NOT NULL,
	SLFUELTYPE TEXT NOT NULL,
	SLCURRLTR INTEGER NOT NULL,
	SLPASTLTR INTEGER NOT NULL,
	SLPRICE INTEGER NOT NULL,
	DATEID DATE);
	"""
    )

    cur.execute(
        """
	CREATE TABLE IF NOT EXISTS Pet95Info(
	SLID INTEGER PRIMARY KEY AUTOINCREMENT,
	SALERNAME TEXT NOT NULL,
	SLPNUM TEXT NOT NULL,
	SLFUELTYPE TEXT NOT NULL,
	SLCURRLTR INTEGER NOT NULL,
	SLPASTLTR INTEGER NOT NULL,
	SLPRICE INTEGER NOT NULL,
	DATEID DATE);
	"""
    )

    cur.execute(
        """
	CREATE TABLE IF NOT EXISTS Pet92Info(
	SLID INTEGER PRIMARY KEY AUTOINCREMENT,
	SALERNAME TEXT NOT NULL,
	SLPNUM TEXT NOT NULL,
	SLFUELTYPE TEXT NOT NULL,
	SLCURRLTR INTEGER NOT NULL,
	SLPASTLTR INTEGER NOT NULL,
	SLPRICE INTEGER NOT NULL,
	DATEID DATE);
	"""
    )

    cur.execute(
        """
	CREATE TABLE IF NOT EXISTS GasInfo(
	SLID INTEGER PRIMARY KEY AUTOINCREMENT,
	SALERNAME TEXT NOT NULL,
	SLPNUM TEXT NOT NULL,
	SLFUELTYPE TEXT NOT NULL,
	SLCURRLTR INTEGER NOT NULL,
	SLPASTLTR INTEGER NOT NULL,
	SLPRICE INTEGER NOT NULL,
	DATEID DATE);
	"""
    )


def submit():
    DateNow = datetime.date.today()

    if SALERNAME.get() == "" or SLPNUM.get() == "":
        messagebox.showinfo("تانگ تیل نیازی ", "!ورودی ها نباید خالی باشد ")
    else:
        conn1 = sqlite3.connect("NiaziPetrolium.db")
        cur1 = conn1.cursor()

        if SLFUELTYPE.get() == DSL:
            if SLCURRLTR.get() > SLPASTLTR.get():
                messagebox.showwarning(
                    "خطای ورودی ", "!حالیه نمیتواند بزرگتر از گذشته باشد "
                )
            else:
                cur1.execute(
                    f"insert into DisalInfo (DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLCURRLTR,SLPASTLTR,SLPRICE) values ('{DateNow}','{SALERNAME.get()}','{SLPNUM.get()}','{SLFUELTYPE.get()}',\
					'{SLCURRLTR.get()}','{SLPASTLTR.get()}',\
					'{SLPRICE.get()}')"
                )
        elif SLFUELTYPE.get() == PET1:
            if SLCURRLTR.get() > SLPASTLTR.get():
                messagebox.showwarning(
                    "خطای ورودی ", "!حالیه نمیتواند بزرگتر از گذشته باشد "
                )
            else:
                cur1.execute(
                    f"insert into Pet95Info (DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLCURRLTR,SLPASTLTR,SLPRICE) values ('{DateNow}','{SALERNAME.get()}','{SLPNUM.get()}','{SLFUELTYPE.get()}',\
					'{SLCURRLTR.get()}','{SLPASTLTR.get()}',\
					'{SLPRICE.get()}') "
                )
        elif SLFUELTYPE.get() == PET2:
            if SLCURRLTR.get() > SLPASTLTR.get():
                messagebox.showwarning(
                    "خطای ورودی ", "!حالیه نمیتواند بزرگتر از گذشته باشد "
                )
            else:
                cur1.execute(
                    f"insert into Pet92Info (DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLCURRLTR,SLPASTLTR,SLPRICE) values ('{DateNow}','{SALERNAME.get()}','{SLPNUM.get()}','{SLFUELTYPE.get()}',\
					'{SLCURRLTR.get()}','{SLPASTLTR.get()}',\
					'{SLPRICE.get()}') "
                )
        elif SLFUELTYPE.get() == GS:
            if SLCURRLTR.get() > SLPASTLTR.get():
                messagebox.showwarning(
                    "خطای ورودی ", "!حالیه نمیتواند بزرگتر از گذشته باشد "
                )
            else:
                cur1.execute(
                    f"insert into GasInfo (DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLCURRLTR,SLPASTLTR,SLPRICE) values ('{DateNow}','{SALERNAME.get()}','{SLPNUM.get()}','{SLFUELTYPE.get()}',\
					'{SLCURRLTR.get()}','{SLPASTLTR.get()}',\
					'{SLPRICE.get()}') "
                )
        else:
            messagebox.showwarning(
                "اووووه ", "قبل از ذخیره داده نوعیت تیل ره مشخص کنید "
            )

        conn1.commit()
        conn1.close()

        Ent0.delete(0, END)
        # Ent1.delete(0, END)
        Ent3.delete(0, END)
        Ent4.delete(0, END)
        Ent6.delete(0, END)
        Ent0.focus()
        Ref1()
        total1Show()


# >>>>>>>>>>>>>>>>


def ClearEntry():
    Ent0.delete(0, END)
    # Ent1.delete(0, END)
    Ent3.delete(0, END)
    Ent4.delete(0, END)
    Ent6.delete(0, END)
    Ent0.focus()


def SearchByName():
    if SLSEARCH.get() != "":
        tree1.delete(*tree1.get_children())
        Sconn = sqlite3.connect("NiaziPetrolium.db")
        Scur = Sconn.execute(
            "SELECT SLID,SALERNAME,SLPNUM,SLFUELTYPE,SLCURRLTR,SLPASTLTR,SLPRICE FROM DisalInfo WHERE SALERNAME LIKE?",
            ("%" + str(SLSEARCH.get()) + "%",),
        )
        Sfetch = Scur.fetchall()
        for Sdata in Sfetch:
            tree1.insert("", "end", values=(Sdata))
    else:
        messagebox.showinfo("جستجوی  فروشنده ", "!لطفاً نام فروشنده را وارد کنید ")


"""

def DeleteDslRec():
	conn = sqlite3.connect("NiaziPetrolium.db")
	cur = conn.cursor()
	messageDelete = messagebox.askyesno("درخواست حذف داده ", "؟ آیا واقعاً  میخواهید این داده را حذف کنید ")
	if messageDelete > 0:
		selected_item = Dtree1.selection()[0]
		for selected_item in Dtree1.selection():
			cur.execute("DELETE FROM DisalInfo WHERE SLID=?",(Dtree1.set(selected_item, "SLID"),))
		conn.commit()
		Dtree1.delete(selected_item)
	conn.close()
	Ref1()
	total1Show()
"""


def FUpdate1():
    dt2 = SALERNAME.get()
    dt5 = SLCURRLTR.get()
    dt6 = SLPASTLTR.get()
    dt7 = SLPRICE.get()

    for selected_item in tree1.selection():
        conn1 = sqlite3.connect("NiaziPetrolium.db")
        if SALERNAME.get() != "":
            Ent0.delete(0, END)
            cur1 = conn1.cursor()
            cur1.execute(
                "UPDATE DisalInfo SET SALERNAME=? WHERE SLID=?",
                (dt2, tree1.set(selected_item, "#1")),
            )

        elif SLCURRLTR.get() != "":
            Ent3.delete(0, END)
            cur1 = conn1.cursor()
            cur1.execute(
                "UPDATE DisalInfo SET SLCURRLTR=? WHERE SLID=?",
                (dt5, tree1.set(selected_item, "#1")),
            )

        elif SLPASTLTR.get() != "":
            Ent4.delete(0, END)
            cur1 = conn1.cursor()
            cur1.execute(
                "UPDATE DisalInfo SET SLPASTLTR=? WHERE SLID=?",
                (dt6, tree1.set(selected_item, "#1")),
            )

        elif SLPRICE.get() != "":
            Ent6.delete(0, END)
            cur1 = conn1.cursor()
            cur1.execute(
                "UPDATE DisalInfo SET SLPRICE=? WHERE SLID=?",
                (dt7, tree1.set(selected_item, "#1")),
            )

        else:
            messagebox.showerror(
                "اووووه", "! لطفاً به ورودی مربوطه متن تان را وارد کنید "
            )

        conn1.commit()
        conn1.close()
        Ref1()
        Ent0.focus()


# ===================== Left Right


def Ref1():
    tree1.delete(*tree1.get_children())
    conn = sqlite3.connect("NiaziPetrolium.db")
    cur = conn.execute(
        """SELECT DisalInfo.SLID,DisalInfo.DATEID,DisalInfo.SALERNAME,DisalInfo.SLPNUM,DisalInfo.SLFUELTYPE,
		Pet95Info.DATEID,Pet95Info.SALERNAME,Pet95Info.SLPNUM,Pet95Info.SLFUELTYPE, 
		Pet92Info.DATEID,Pet92Info.SALERNAME,Pet92Info.SLPNUM,Pet92Info.SLFUELTYPE, 
		GasInfo.DATEID,GasInfo.SALERNAME,GasInfo.SLPNUM,GasInfo.SLFUELTYPE 
		FROM DisalInfo JOIN Pet95Info ON DisalInfo.DATEID = Pet95Info.DATEID 
		JOIN Pet92Info ON Pet95Info.DATEID = Pet92Info.DATEID 
		JOIN GasInfo ON Pet92Info.DATEID = GasInfo.DATEID"""
    )

    fetch = cur.fetchall()
    for data in fetch:
        tree1.insert("", "end", values=(data))
    cur.close()
    conn.close()
    total1Show()


def SaveFocusIn(event):
    Btn4.config(image=SaveImageFocused1)


def SaveFocusOut(event):
    Btn4.config(image=SaveImage1)


def UpdateFocusIn(event):
    Btn3.config(image=UpdateImageFocused1)


def UpdateFocusOut(event):
    Btn3.config(image=UpdateImage1)


def ClearFocusIn(event):
    Btn2.config(image=ClearImageFocused1)


def ClearFocusOut(event):
    Btn2.config(image=ClearImage1)


def RefreshFocusIn(event):
    Btn1.config(image=RefreshImageFocused1)


def RefreshFocusOut(event):
    Btn1.config(image=RefreshImage1)


def ExitFocusIn(event):
    Btn0.config(image=ExitImageFocused1)


def ExitFocusOut(event):
    Btn0.config(image=ExitImage2)


# ==============--------=== Tab2 ===============================
# ==============--------=== Tab2 ===============================
# ==============--------=== Tab2 ===============================
# ==============--------=== Tab2 ===============================
# ==============--------=== Tab2 ===============================

tab1_frame = Frame(tab2, bg=DEFAULTHCRBG)
tab1_frame.grid(row=0, column=0, sticky=W)

frame1 = Frame(tab1_frame, bg=DEFAULTHCRBG)
frame1.grid(row=0, column=0, sticky=W)

frame2 = Frame(frame1, bg=DEFAULTHCRBG)
frame2.grid(row=0, column=0)

frame2Top = Frame(frame2, bg=DEFAULTHCRBG)
frame2Top.grid(row=0, column=0, padx=500, sticky=W)

frame2Bottom = Frame(frame2, bg=DEFAULTHCRBG)
frame2Bottom.grid(row=1, column=0, sticky=E)


# ==================== Option functions and most of Inner Frames ========================

BottomFrameWhole = Frame(tab1_frame, bg=DEFAULTHCRBG)
BottomFrameWhole.grid(row=1, column=0, sticky=W)
BtnFrame = LabelFrame(
    BottomFrameWhole, bg=DEFAULTHCRBG, bd=0, relief=SOLID, text="Buttons"
)
BtnFrame.grid(row=0, column=0, sticky=NW)

SearchFrame1 = Frame(BottomFrameWhole, bg=DEFAULTHCRBG, bd=0)
SearchFrame1.place(x=30, y=250)
# BtnFrame.place(x=350,y=500)
PrFrame = Frame(BottomFrameWhole, bg=DEFAULTHCRBG, bd=0)
PrFrame.grid(row=0, column=1, padx=60, pady=20, sticky=E)

# =================== Searching ===============================
EntSearch = ctk.CTkEntry(
    SearchFrame1,
    border_width=2,
    corner_radius=30,
    fg_color=("light blue"),
    text_color="black",
    border_color=DarkBlue,
    width=300,
    textvariable=SLSEARCH,
    font=("Arial", 18, "bold"),
    justify=RIGHT,
)
EntSearch.grid(row=0, column=0, padx=10, pady=5, sticky=W)

BtnSearch = ctk.CTkButton(
    SearchFrame1,
    text="جستجو ",
    font=("Arial", 13, "bold"),
    width=20,
    border_width=1,
    border_color="light gray",
    command=SearchByName,
)
BtnSearch.grid(row=0, column=1, padx=10, pady=10, sticky=W)

# =================== Searching End ===========================


# =============== Entries ==============
Ent0 = ctk.CTkEntry(
    PrFrame,
    border_width=2,
    corner_radius=30,
    fg_color=BGLIGHTGREEN,
    text_color="black",
    border_color="dark blue",
    width=350,
    textvariable=SALERNAME,
    font=("Arial", 17, "bold"),
    justify=RIGHT,
)
Ent0.grid(row=0, column=0, padx=5, pady=5, sticky=E)
Ent0.focus()


PNumbers = [
    "P1",
    "P2",
    "P3",
    "P4",
    "P5",
    "P6",
    "P7",
    "P8",
    "P9",
    "P10",
    "P11",
    "P12",
    "P13",
    "P14",
    "P15",
    "P16",
    "P17",
    "P18",
    "P19",
    "P20",
    "P21",
    "P22",
    "P23",
    "P24",
    "P25",
    "P26",
    "P27",
    "P28",
    "P29",
    "P30",
]
SLPNUM.set("Choose pump number")

Ent1 = ctk.CTkComboBox(
    PrFrame,
    width=250,
    values=PNumbers,
    border_color=BGGRAY,
    variable=SLPNUM,
    text_color="white",
    fg_color=(DarkBlue, MODERNPINK),
)
Ent1.grid(row=1, column=0, padx=5, pady=5, sticky=E)


"""Ent2 = ctk.CTkEntry(PrFrame, border_width=2,corner_radius=30,fg_color=("light yellow"),text_color="black",border_color="dark blue",width=200,
	textvariable=SLFUELTYPE,font=("Arial",17,"bold"),justify=RIGHT)
Ent2.grid(row=1, column=0,padx=60,pady=5,sticky=E)
"""

DSL = "Disal_02"
PET1 = "Petrol_95"
PET2 = "Petrol_92"
GS = "Gas"

RadioFrame1 = Frame(PrFrame, bg=DEFAULTHCRBG)
RadioFrame1.grid(row=2, column=0, padx=5, pady=5, sticky=E)

Ent_2_0 = Radiobutton(
    master=RadioFrame1,
    compound=RIGHT,
    wraplength=False,
    indicatoron=False,
    image=RadioImage1,
    selectimage=RadioActiveImage1,
    bd=0,
    selectcolor=DEFAULTHCRBG,
    text="Disal-02",
    activebackground=DEFAULTHCRBG,
    bg=DEFAULTHCRBG,
    fg=BGORANGE,
    font=("Arial", 8, "bold"),
    variable=SLFUELTYPE,
    value=DSL,
)
Ent_2_0.grid(row=0, column=0, padx=5, pady=5, sticky=E)
Ent_2_1 = Radiobutton(
    master=RadioFrame1,
    compound=RIGHT,
    wraplength=False,
    indicatoron=False,
    image=RadioImage1,
    selectimage=RadioActiveImage1,
    bd=0,
    selectcolor=DEFAULTHCRBG,
    text="Petrol-95",
    activebackground=DEFAULTHCRBG,
    bg=DEFAULTHCRBG,
    fg=BGORANGE,
    font=("Arial", 8, "bold"),
    variable=SLFUELTYPE,
    value=PET1,
)
Ent_2_1.grid(row=0, column=1, padx=5, pady=5, sticky=E)
Ent_2_2 = Radiobutton(
    master=RadioFrame1,
    compound=RIGHT,
    wraplength=False,
    indicatoron=False,
    image=RadioImage1,
    selectimage=RadioActiveImage1,
    bd=0,
    selectcolor=DEFAULTHCRBG,
    text="Petrol-92",
    activebackground=DEFAULTHCRBG,
    bg=DEFAULTHCRBG,
    fg=BGORANGE,
    font=("Arial", 8, "bold"),
    variable=SLFUELTYPE,
    value=PET2,
)
Ent_2_2.grid(row=0, column=2, padx=5, pady=5, sticky=E)
Ent_2_3 = Radiobutton(
    master=RadioFrame1,
    compound=RIGHT,
    wraplength=False,
    indicatoron=False,
    image=RadioImage1,
    selectimage=RadioActiveImage1,
    bd=0,
    selectcolor=DEFAULTHCRBG,
    text="Gas",
    activebackground=DEFAULTHCRBG,
    bg=DEFAULTHCRBG,
    fg=BGORANGE,
    font=("Arial", 8, "bold"),
    variable=SLFUELTYPE,
    value=GS,
)
Ent_2_3.grid(row=0, column=3, padx=5, pady=5, sticky=E)


Ent3 = ctk.CTkEntry(
    PrFrame,
    border_width=2,
    corner_radius=30,
    fg_color=(BGLIGHTGREEN),
    text_color="black",
    border_color="dark blue",
    width=200,
    textvariable=SLCURRLTR,
    font=("Arial", 17, "bold"),
    justify=RIGHT,
)
Ent3.grid(row=3, column=0, padx=5, pady=5, sticky=E)

Ent4 = ctk.CTkEntry(
    PrFrame,
    border_width=2,
    corner_radius=30,
    fg_color=(BGLIGHTGREEN),
    text_color="black",
    border_color="dark blue",
    width=200,
    textvariable=SLPASTLTR,
    font=("Arial", 17, "bold"),
    justify=RIGHT,
)
Ent4.grid(row=4, column=0, padx=5, pady=5, sticky=E)

Ent6 = ctk.CTkEntry(
    PrFrame,
    border_width=2,
    corner_radius=30,
    fg_color=(BGLIGHTGREEN),
    text_color="black",
    border_color="dark blue",
    width=200,
    textvariable=SLPRICE,
    font=("Arial", 17, "bold"),
    justify=RIGHT,
)
Ent6.grid(row=5, column=0, padx=5, pady=5, sticky=E)
"""
Ent7 = ctk.CTkCheckBox(PrFrame,text="استفاده از تاریخ دستی ",border_color=BGLIGHTGRAY,font=("B Titr",12),text_color=BGLIGHTBLUE)
Ent7.grid(row=6, column=0,padx=5,pady=5,sticky=E)
"""


# =============== Buttons ==============
Btn4 = Button(
    BtnFrame,
    bg=DEFAULTHCRBG,
    bd=0,
    image=SaveImage1,
    activebackground=DEFAULTHCRBG,
    command=submit,
)
Btn4.grid(row=0, column=4, padx=5, pady=10, sticky=E)
Btn4.focus()
Btn3 = Button(
    BtnFrame,
    bg=DEFAULTHCRBG,
    bd=0,
    image=UpdateImage1,
    activebackground=DEFAULTHCRBG,
    command=FUpdate1,
)
Btn3.grid(row=0, column=3, padx=5, pady=10, sticky=E)
Btn2 = Button(
    BtnFrame,
    bg=DEFAULTHCRBG,
    bd=0,
    image=ClearImage1,
    activebackground=DEFAULTHCRBG,
    command=ClearEntry,
)
Btn2.grid(row=0, column=2, padx=5, pady=10, sticky=E)
Btn1 = Button(
    BtnFrame,
    bg=DEFAULTHCRBG,
    bd=0,
    image=RefreshImage1,
    activebackground=DEFAULTHCRBG,
    command=Ref1,
)
Btn1.grid(row=0, column=1, padx=5, pady=10, sticky=E)
Btn0 = Button(
    BtnFrame,
    bg=DEFAULTHCRBG,
    bd=0,
    image=ExitImage2,
    activebackground=DEFAULTHCRBG,
    command=ExitBtnFunc,
)
Btn0.grid(row=0, column=0, padx=5, pady=10, sticky=E)


# ================ Labels ==============
PrLblFrame = Frame(BottomFrameWhole, bg=DEFAULTHCRBG, bd=0)
PrLblFrame.grid(row=0, column=2, sticky=E)

Lbl0 = Label(
    PrFrame, bg=DEFAULTHCRBG, fg=BGORANGE, text=":نام فروشنده", font=("B Titr", 12)
)
Lbl0.grid(row=0, column=1, pady=2, sticky=E, padx=3)
Lbl1 = Label(
    PrFrame, bg=DEFAULTHCRBG, fg=BGORANGE, text=":نمبر پایه ", font=("B Titr", 12)
)
Lbl1.grid(row=1, column=1, pady=2, sticky=E, padx=3)
Lbl2 = Label(
    PrFrame, bg=DEFAULTHCRBG, fg=BGORANGE, text=": نوعیت ", font=("B Titr", 12)
)
Lbl2.grid(row=2, column=1, pady=2, sticky=E, padx=3)
Lbl3 = Label(PrFrame, bg=DEFAULTHCRBG, fg=BGORANGE, text=":حالیه ", font=("B Titr", 12))
Lbl3.grid(row=3, column=1, pady=2, sticky=E, padx=3)
Lbl4 = Label(PrFrame, bg=DEFAULTHCRBG, fg=BGORANGE, text=":گذشته ", font=("B Titr", 12))
Lbl4.grid(row=4, column=1, pady=2, sticky=E, padx=3)
Lbl6 = Label(PrFrame, bg=DEFAULTHCRBG, fg=BGORANGE, text=":قیمت ", font=("B Titr", 12))
Lbl6.grid(row=5, column=1, pady=2, sticky=E, padx=3)

Lbl8 = Label(PrFrame, bg=DEFAULTHCRBG, fg=BGORANGE, text="", font=("B Titr", 12))
Lbl8.grid(row=6, column=1, pady=2, sticky=E, padx=3)


# ==================== Display Totals of some Compunents ===============================
def total1Show():
    TotalMainFrame = LabelFrame(tab2, bg=DEFAULTHCRBG, bd=0, text="Display Total")
    TotalMainFrame.place(x=40, y=430)

    TtlFrame1 = Frame(TotalMainFrame, bg=DEFAULTHCRBG)
    TtlFrame1.grid(row=0, column=0)
    TtlFrame2 = Frame(TotalMainFrame, bg=DEFAULTHCRBG)
    TtlFrame2.grid(row=0, column=1)
    TtlFrame3 = Frame(TotalMainFrame, bg=DEFAULTHCRBG)
    TtlFrame3.grid(row=0, column=2)

    # >>>>>>>>>>>>>>>> Fuel type Total 1 >>>>>>>>>>>>>>>>>>
    TWindow = Label(TtlFrame1, bd=0, bg=DEFAULTHCRBG)
    TWindow.grid(row=0, column=0, sticky=E)
    Ttree1 = ttk.Treeview(TWindow, columns=("SLTOTAL"), selectmode="browse", height=2)
    Ttree1.heading("SLTOTAL", text="مجموعه فروش دیزل / لیتر", anchor=E)
    # setting width of the columns
    Ttree1.column("#0", stretch=NO, minwidth=0, width=0)
    Ttree1.column("#1", stretch=NO, minwidth=0, width=150)
    Ttree1.grid()
    Ttree1.delete(*Ttree1.get_children())

    Tconn = sqlite3.connect("NiaziPetrolium.db")
    Ttree1.delete(*Ttree1.get_children())
    Tcur = Tconn.execute("SELECT SUM(SLPASTLTR-SLCURRLTR) FROM DisalInfo")
    Tfetch = Tcur.fetchall()
    for Tdata in Tfetch:
        Ttree1.insert("", "end", values=(Tdata))
    Tcur.close()
    Tconn.close()

    TWindow1 = Label(TtlFrame2, bd=0, bg=DEFAULTHCRBG)
    TWindow1.grid(row=0, column=0, sticky=E)
    Ttree2 = ttk.Treeview(
        TWindow1, columns=("TOTALPRICE"), selectmode="browse", height=2
    )
    Ttree2.heading("TOTALPRICE", text="مجموعه قیمت /اف ", anchor=E)
    # setting width of the columns
    Ttree2.column("#0", stretch=NO, minwidth=0, width=0)
    Ttree2.column("#1", stretch=NO, minwidth=0, width=150)
    Ttree2.grid()
    Ttree2.delete(*Ttree2.get_children())

    Tconn1 = sqlite3.connect("NiaziPetrolium.db")
    Ttree2.delete(*Ttree2.get_children())
    Tcur1 = Tconn1.execute("SELECT SUM(SLPRICE*(SLPASTLTR-SLCURRLTR)) FROM DisalInfo")
    Tfetch1 = Tcur1.fetchall()
    for Tdata1 in Tfetch1:
        Ttree2.insert("", "end", values=(Tdata1))
    Tcur1.close()
    Tconn1.close()

    TWindow3 = Label(TtlFrame3, bd=0, bg=DEFAULTHCRBG)
    TWindow3.grid(row=0, column=0, sticky=E)
    Ttree3 = ttk.Treeview(
        TWindow3, columns=("TOTALPRICE3"), selectmode="browse", height=2
    )
    Ttree3.heading("TOTALPRICE3", text="پایه ها ", anchor=E)
    # setting width of the columns
    Ttree3.column("#0", stretch=NO, minwidth=0, width=0)
    Ttree3.column("#1", stretch=NO, minwidth=0, width=150)
    Ttree3.grid()
    Ttree3.delete(*Ttree3.get_children())

    Tconn3 = sqlite3.connect("NiaziPetrolium.db")
    Ttree3.delete(*Ttree3.get_children())
    Tcur3 = Tconn3.execute("SELECT COUNT(SLID) FROM DisalInfo")
    Tfetch3 = Tcur3.fetchall()
    for Tdata3 in Tfetch3:
        Ttree3.insert("", "end", values=(Tdata3))
    Tcur3.close()
    Tconn3.close()


Fminiwin1 = Label(frame2Bottom, bg="dark blue")
Fminiwin1.grid(row=0, column=0, sticky=W)
scrollbarx = Scrollbar(frame2Bottom, orient=HORIZONTAL)
scrollbary = Scrollbar(frame2Bottom, orient=VERTICAL)
tree1 = ttk.Treeview(
    Fminiwin1,
    columns=(
        "ID1",
        "DAT1",
        "SLN1",
        "PNR1",
        "FTP1",
        "DAT2",
        "SLN2",
        "PNR2",
        "FTP2",
        "DAT3",
        "SLN3",
        "PNR3",
        "FTP3",
        "DAT4",
        "SLN4",
        "PNR4",
        "FTP4",
    ),
    selectmode="browse",
    height=10,
    yscrollcommand=scrollbary.set,
    xscrollcommand=scrollbarx.set,
)
scrollbary.config(command=tree1.yview)
scrollbary.grid(row=0, column=1, ipady=125, sticky=N)
scrollbarx.config(command=tree1.xview)
scrollbarx.grid(row=1, column=0, ipadx=628, sticky=W)
# =====setting headings for the columns


tree1.heading("ID1", text="No", anchor=W)
tree1.heading("DAT1", text="Date", anchor=W)
tree1.heading("SLN1", text="Saler Name", anchor=W)
tree1.heading("PNR1", text="P-No", anchor=W)
tree1.heading("FTP1", text="Fuel Type", anchor=W)


tree1.heading("DAT2", text="Date", anchor=W)
tree1.heading("SLN2", text="Saler Name", anchor=W)
tree1.heading("PNR2", text="P-No", anchor=W)
tree1.heading("FTP2", text="Fuel Type", anchor=W)


tree1.heading("DAT3", text="Date", anchor=W)
tree1.heading("SLN3", text="Saler Name", anchor=W)
tree1.heading("PNR3", text="P-No", anchor=W)
tree1.heading("FTP3", text="Fuel Type", anchor=W)


tree1.heading("DAT4", text="Date", anchor=W)
tree1.heading("SLN4", text="Saler Name", anchor=W)
tree1.heading("PNR4", text="P-No", anchor=W)
tree1.heading("FTP4", text="Fuel Type", anchor=W)


# setting width of the columns
tree1.column("#0", stretch=NO, minwidth=0, width=0)

tree1.column("#1", stretch=NO, minwidth=0, width=40)
tree1.column("#2", stretch=NO, minwidth=0, width=65)
tree1.column("#3", stretch=NO, minwidth=0, width=120)
tree1.column("#4", stretch=NO, minwidth=0, width=50)
tree1.column("#5", stretch=NO, minwidth=0, width=80)

tree1.column("#6", stretch=NO, minwidth=0, width=65)
tree1.column("#7", stretch=NO, minwidth=0, width=120)
tree1.column("#8", stretch=NO, minwidth=0, width=50)
tree1.column("#9", stretch=NO, minwidth=0, width=80)


tree1.column("#10", stretch=NO, minwidth=0, width=65)
tree1.column("#11", stretch=NO, minwidth=0, width=120)
tree1.column("#12", stretch=NO, minwidth=0, width=50)
tree1.column("#13", stretch=NO, minwidth=0, width=80)


tree1.column("#14", stretch=NO, minwidth=0, width=65)
tree1.column("#15", stretch=NO, minwidth=0, width=120)
tree1.column("#16", stretch=NO, minwidth=0, width=50)
tree1.column("#17", stretch=NO, minwidth=0, width=80)

tree1.grid()


tree1.delete(*tree1.get_children())
conn1 = sqlite3.connect("NiaziPetrolium.db")
cur1 = conn1.execute(
    """SELECT DisalInfo.SLID,DisalInfo.DATEID,DisalInfo.SALERNAME,DisalInfo.SLPNUM,DisalInfo.SLFUELTYPE,
	Pet95Info.DATEID,Pet95Info.SALERNAME,Pet95Info.SLPNUM,Pet95Info.SLFUELTYPE, 
	Pet92Info.DATEID,Pet92Info.SALERNAME,Pet92Info.SLPNUM,Pet92Info.SLFUELTYPE, 
	GasInfo.DATEID,GasInfo.SALERNAME,GasInfo.SLPNUM,GasInfo.SLFUELTYPE 
	FROM DisalInfo JOIN Pet95Info ON DisalInfo.DATEID = Pet95Info.DATEID 
	JOIN Pet92Info ON Pet95Info.DATEID = Pet92Info.DATEID 
	JOIN GasInfo ON Pet92Info.DATEID = GasInfo.DATEID"""
)
# cur1 = conn1.execute("SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLCURRLTR,SLPASTLTR,SLPRICE FROM DisalInfo")

fetch1 = cur1.fetchall()
for data1 in fetch1:
    tree1.insert("", "end", values=(data1))
cur1.close()
conn1.close()


Btn4.bind("<Enter>", SaveFocusIn)
Btn4.bind("<Leave>", SaveFocusOut)
Btn4.bind("<FocusIn>", SaveFocusIn)
Btn4.bind("<FocusOut>", SaveFocusOut)

Btn3.bind("<Enter>", UpdateFocusIn)
Btn3.bind("<Leave>", UpdateFocusOut)
Btn3.bind("<FocusIn>", UpdateFocusIn)
Btn3.bind("<FocusOut>", UpdateFocusOut)

Btn2.bind("<Enter>", ClearFocusIn)
Btn2.bind("<Leave>", ClearFocusOut)
Btn2.bind("<FocusIn>", ClearFocusIn)
Btn2.bind("<FocusOut>", ClearFocusOut)

Btn1.bind("<Enter>", RefreshFocusIn)
Btn1.bind("<Leave>", RefreshFocusOut)
Btn1.bind("<FocusIn>", RefreshFocusIn)
Btn1.bind("<FocusOut>", RefreshFocusOut)

Btn0.bind("<Enter>", ExitFocusIn)
Btn0.bind("<Leave>", ExitFocusOut)
Btn0.bind("<FocusIn>", ExitFocusIn)
Btn0.bind("<FocusOut>", ExitFocusOut)


def Disaldo_popup(event):
    try:
        FFmu.tk_popup(event.x_root, event.y_root)
    finally:
        FFmu.grab_release()


FFmu = Menu(tree1, tearoff=0)
FFmu.add_command(label="تازه سازی ", command=Ref1, image=PopupRefresh1, compound=LEFT)
FFmu.add_command(label="چاپ اطلاعات ", command="", image=PopupPrint1, compound=LEFT)

tree1.bind("<Button-3>", Disaldo_popup)


def timshow():
    from time import strftime

    string = strftime(" %H:%M - %S   %p")
    stringdate = strftime("%Y-%m-%d - %a")
    clocklbl.configure(text=string, font=("Humnst777 Blk BT", 15))
    datelbl.configure(text=stringdate, font=("Humnst777 Blk BT", 15))

    clocklbl.after(1000, timshow)


clocklbl = Label(tab2, bg=DEFAULTHCRBG, fg=BGYELLOW, bd=0)
clocklbl.place(x=500, y=595)
datelbl = Label(tab2, bg=DEFAULTHCRBG, fg=BGLIGHTGRAY, bd=0)
datelbl.place(x=700, y=595)


timshow()

total1Show()


# ========================= Tab3 ================================
# ========================= Tab3 ================================
# ========================= Tab3 ================================
# ========================= Tab3 ================================
# ========================= Tab3 ================================
# ========================= Tab3 ================================


def Ref3():
    Dtree1.delete(*Dtree1.get_children())
    conn = sqlite3.connect("NiaziPetrolium.db")
    cur = conn.execute(
        "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLCURRLTR,SLPASTLTR,SLPRICE FROM DisalInfo"
    )
    fetch = cur.fetchall()
    for data in fetch:
        Dtree1.insert("", "end", values=(data))
    cur.close()
    conn.close()


def DeleteDslRecDisal():
    conn = sqlite3.connect("NiaziPetrolium.db")
    cur = conn.cursor()
    messageDelete = messagebox.askyesno(
        "درخواست حذف داده ", "؟ آیا واقعاً  میخواهید این داده را حذف کنید "
    )
    if messageDelete > 0:
        selected_item = Dtree1.selection()[0]
        for selected_item in Dtree1.selection():
            cur.execute(
                "DELETE FROM DisalInfo WHERE SLID=?",
                (Dtree1.set(selected_item, "SLID"),),
            )
        conn.commit()
        Dtree1.delete(selected_item)
    conn.close()
    Ref3()
    total1ShowDisal()


def total1ShowDisal():
    Ref3()
    TotalMainFrameDisal = LabelFrame(
        TabDisalFrame1, bg=DEFAULTHCRBG, bd=0, text="مشاهده مجموعه  دیزل ", fg=BGWHITE
    )
    TotalMainFrameDisal.grid(row=0, column=0, sticky=W)
    TtlFrameDisal = Frame(TotalMainFrameDisal, bg=DEFAULTHCRBG)
    TtlFrameDisal.grid(row=0, column=0)
    TtlFrame2Disal = Frame(TotalMainFrameDisal, bg=DEFAULTHCRBG)
    TtlFrame2Disal.grid(row=0, column=1)
    TtlFrame3Disal = Frame(TotalMainFrameDisal, bg=DEFAULTHCRBG)
    TtlFrame3Disal.grid(row=0, column=2)
    TtlFrame4Disal = Frame(TotalMainFrameDisal, bg=DEFAULTHCRBG)
    TtlFrame4Disal.grid(row=0, column=3)

    # >>>>>>>>>>>>>>>> Fuel type Total 1 >>>>>>>>>>>>>>>>>>
    TWindowDisal = Label(TtlFrameDisal, bd=0, bg=DEFAULTHCRBG)
    TWindowDisal.grid(row=0, column=0, sticky=E)
    Ttree1Disal = ttk.Treeview(
        TWindowDisal, columns=("SLTOTAL"), selectmode="browse", height=2
    )
    Ttree1Disal.heading("SLTOTAL", text="مجموعه فروش دیزل / لیتر", anchor=E)
    # setting width of the columns
    Ttree1Disal.column("#0", stretch=NO, minwidth=0, width=0)
    Ttree1Disal.column("#1", stretch=NO, minwidth=0, width=150)
    Ttree1Disal.grid()
    Ttree1Disal.delete(*Ttree1Disal.get_children())

    TconnDisal = sqlite3.connect("NiaziPetrolium.db")
    Ttree1Disal.delete(*Ttree1Disal.get_children())
    TcurDisal = TconnDisal.execute("SELECT SUM(SLPASTLTR-SLCURRLTR) FROM DisalInfo")
    TfetchDisal = TcurDisal.fetchall()
    for TdataDisal in TfetchDisal:
        Ttree1Disal.insert("", "end", values=(TdataDisal))
    TcurDisal.close()
    TconnDisal.close()

    TWindow1Disal = Label(TtlFrame2Disal, bd=0, bg=DEFAULTHCRBG)
    TWindow1Disal.grid(row=0, column=0, sticky=E)
    Ttree2Disal = ttk.Treeview(
        TWindow1Disal, columns=("TOTALPRICE"), selectmode="browse", height=2
    )
    Ttree2Disal.heading("TOTALPRICE", text="مجموعه قیمت /اف ", anchor=E)
    # setting width of the columns
    Ttree2Disal.column("#0", stretch=NO, minwidth=0, width=0)
    Ttree2Disal.column("#1", stretch=NO, minwidth=0, width=150)
    Ttree2Disal.grid()
    Ttree2Disal.delete(*Ttree2Disal.get_children())

    Tconn1Disal = sqlite3.connect("NiaziPetrolium.db")
    Ttree2Disal.delete(*Ttree2Disal.get_children())
    Tcur195 = Tconn1Disal.execute(
        "SELECT SUM(SLPRICE*(SLPASTLTR-SLCURRLTR)) FROM DisalInfo"
    )
    Tfetch195 = Tcur195.fetchall()
    for Tdata195 in Tfetch195:
        Ttree2Disal.insert("", "end", values=(Tdata195))
    Tcur195.close()
    Tconn1Disal.close()

    TWindow3Disal = Label(TtlFrame3Disal, bd=0, bg=DEFAULTHCRBG)
    TWindow3Disal.grid(row=0, column=0, sticky=E)
    Ttree3Disal = ttk.Treeview(
        TWindow3Disal, columns=("TOTALPRICE3"), selectmode="browse", height=2
    )
    Ttree3Disal.heading("TOTALPRICE3", text="پایه ها ", anchor=E)
    # setting width of the columns
    Ttree3Disal.column("#0", stretch=NO, minwidth=0, width=0)
    Ttree3Disal.column("#1", stretch=NO, minwidth=0, width=70)
    Ttree3Disal.grid()
    Ttree3Disal.delete(*Ttree3Disal.get_children())

    Tconn3Disal = sqlite3.connect("NiaziPetrolium.db")
    Ttree3Disal.delete(*Ttree3Disal.get_children())
    Tcur3Disal = Tconn3Disal.execute("SELECT COUNT(SLPNUM) FROM DisalInfo")
    # Tcur3Disal = Tconn3Disal.execute("SELECT DATEID FROM DisalInfo WHERE DATEID BETWEEN date('now','-7 day') AND date('now')") #Showing the bettween dates
    Tfetch3Disal = Tcur3Disal.fetchall()
    for Tdata3Disal in Tfetch3Disal:
        Ttree3Disal.insert("", "end", values=(Tdata3Disal))
    Tcur3Disal.close()
    Tconn3Disal.close()
    DisplayBtnDisal.configure(fg_color=("dark blue", "green"), text="تازه سازی ")

    TWindow4Disal = Label(TtlFrame4Disal, bd=0, bg=DEFAULTHCRBG)
    TWindow4Disal.grid(row=0, column=0, sticky=E)
    Ttree4Disal = ttk.Treeview(
        TWindow4Disal, columns=("TOTALPRICE4"), selectmode="browse", height=2
    )
    Ttree4Disal.heading("TOTALPRICE4", text="فروشات این هفته/ اف", anchor=E)
    # setting width of the columns
    Ttree4Disal.column("#0", stretch=NO, minwidth=0, width=0)
    Ttree4Disal.column("#1", stretch=NO, minwidth=0, width=150)
    Ttree4Disal.grid()
    Ttree4Disal.delete(*Ttree4Disal.get_children())

    Tconn4Disal = sqlite3.connect("NiaziPetrolium.db")
    Ttree4Disal.delete(*Ttree4Disal.get_children())
    Tcur4Disal = Tconn4Disal.execute(
        "SELECT SUM(SLPRICE*(SLPASTLTR-SLCURRLTR)) FROM DisalInfo WHERE DATEID BETWEEN date('now','-7 day') AND date('now')"
    )
    # Tcur3Disal = Tconn3Disal.execute("SELECT DATEID FROM DisalInfo WHERE DATEID BETWEEN date('now','-7 day') AND date('now')") #Showing the bettween dates
    Tfetch4Disal = Tcur4Disal.fetchall()
    for Tdata4Disal in Tfetch4Disal:
        Ttree4Disal.insert("", "end", values=(Tdata4Disal))
    Tcur4Disal.close()
    Tconn4Disal.close()


"""
tablePrint = [['No','Date','Name','Sales amount','P number'],[1,DateNow,SALERNAME.get(),SLPRICE.get(),SLPNUM.get()]]

tabCreate = PrettyTable(tablePrint[0])
tabCreate.add_rows(tablePrint[1:])
tabCreate.add_column('Total',[-123, 43], align='r',
	valign='t')
tablePrint.append('Columns True')
print(tabCreate)

def savefile():
    fileObject = open('PrintDocs/PrintDocs.txt', 'a')
    fileObject.write(str(tabCreate)+"\n\n"+"File 1"+"\n\n")
    fileObject.close()
    if fileObject == "":
    	print("File 1")
    else:
    	print("File 2")
savefile()

"""


# ====================================== Printing Table contents ============================================
def SaveDisalInfo():
    # DateNow1 = datetime.date.today()
    connDisal = sqlite3.connect("NiaziPetrolium.db")
    cur = connDisal.execute(
        "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLPASTLTR,SLCURRLTR,SLPRICE FROM DisalInfo"
    )
    MyTable = prettytable.from_db_cursor(cur)
    cur = connDisal.cursor()
    rows = cur.fetchall()

    for row in rows:
        MyTable.add_row(row)
    cur.close()
    connDisal.close()

    filesave = filedialog.asksaveasfile(
        mode="w",
        title="ذخیره اطلاعات دیزل 02",
        filetypes=SaveExtensions,
        defaultextension=SaveExtensions,
    )
    if filesave is None:
        return
    file2Save = str(MyTable)
    filesave.write(file2Save)
    filesave.close()
    messagebox.showinfo(
        "نیازی پطرولیم ",
        "برای بهبود کیفیت جدول لطفا قبل از چاپ داده نوع فونت زیر را به نوت پد تان انتخاب کنید \n 	<<< Consolas >>>",
    )


def SaveLastWeekDisalInfo():
    # DateNow1 = datetime.date.today()
    connDisal = sqlite3.connect("NiaziPetrolium.db")
    cur = connDisal.execute(
        "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLPASTLTR,SLCURRLTR,SLPRICE FROM DisalInfo WHERE DATEID BETWEEN date('now','-7 day') AND date('now')"
    )
    MyTable = prettytable.from_db_cursor(cur)
    cur = connDisal.cursor()
    rows = cur.fetchall()

    for row in rows:
        MyTable.add_row(row)
    cur.close()
    connDisal.close()

    filesave = filedialog.asksaveasfile(
        mode="w",
        title="ذخیره اطلاعات این هفته دیزل 02",
        filetypes=SaveExtensions,
        defaultextension=SaveExtensions,
    )
    if filesave is None:
        return
    file2Save = str(MyTable)
    filesave.write(file2Save)
    filesave.close()
    messagebox.showinfo(
        "نیازی پطرولیم ",
        "برای بهبود کیفیت جدول لطفا قبل از چاپ داده نوع فونت زیر را به نوت پد تان انتخاب کنید \n 	<<< Consolas >>>",
    )


def SaveDisalSelectedInfo():
    # DateNow1 = datetime.date.today()
    connDisal = sqlite3.connect("NiaziPetrolium.db")
    selected_item = Dtree1.selection()[0]
    for selected_item in Dtree1.selection():
        cur = connDisal.execute(
            "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLPASTLTR,SLCURRLTR,SLPRICE FROM DisalInfo  WHERE SLID=?",
            (Dtree1.set(selected_item, "SLID"),),
        )
        MyTable = prettytable.from_db_cursor(cur)
        cur = connDisal.cursor()
        rows = cur.fetchall()

        for row in rows:
            MyTable.add_row(row)
        cur.close()
        connDisal.close()

        # =========Save Part ===============
        filesave = filedialog.asksaveasfile(
            mode="w",
            title="ذخیره اطلاعات دیزل 02",
            filetypes=SaveExtensions,
            defaultextension=SaveExtensions,
        )
        if filesave is None:
            return
        file2Save = str(MyTable)
        filesave.write(file2Save)
        filesave.close()
        messagebox.showinfo(
            "نیازی پطرولیم ",
            "برای بهبود کیفیت جدول لطفا قبل از چاپ داده نوع فونت زیر را به نوت پد تان انتخاب کنید \n 	<<< Consolas >>>",
        )


def SearchDisalFunc():
    if DISALSEARCH.get() != "":
        Dtree1.delete(*Dtree1.get_children())
        Dconn = sqlite3.connect("NiaziPetrolium.db")
        Dcur = Dconn.execute(
            "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLPASTLTR,SLCURRLTR,SLPRICE FROM DisalInfo WHERE SALERNAME LIKE?",
            ("%" + str(DISALSEARCH.get()) + "%",),
        )
        Dfetch = Dcur.fetchall()
        for Ddata in Dfetch:
            Dtree1.insert("", "end", values=(Ddata))
    else:
        messagebox.showinfo("جستجوی  فروشنده ", "!لطفاً نام فروشنده را وارد کنید ")


TabDisalFrame = Frame(tab3, bg=DEFAULTHCRBG)
TabDisalFrame.grid(row=0, column=0, padx=10)

TabDisalFrame1 = Frame(tab3, bg=DEFAULTHCRBG)
TabDisalFrame1.grid(row=1, column=0, padx=10, sticky=W)

DisplayBtnDisal = ctk.CTkButton(
    tab3, text=" دیدن مجموعه ", font=("Arial", 13, "bold"), command=total1ShowDisal
)
DisplayBtnDisal.place(x=1180, y=580)

PrintBtnDisal = ctk.CTkButton(
    tab3,
    text="ذخیره  و چاپ اطلاعات دیزل ",
    font=("Arial", 13, "bold"),
    command=SaveDisalInfo,
)  # There is no command still added
PrintBtnDisal.place(x=1025, y=580)

PrintBtnDisal = ctk.CTkButton(
    tab3,
    text="ذخیره اطلاعات این هفته دیزل ",
    font=("Arial", 13, "bold"),
    command=SaveLastWeekDisalInfo,
)  # There is no command still added
PrintBtnDisal.place(x=865, y=580)

# ========================== Search Parts =================================

DisalSearchFrame = Frame(tab3, bg=DEFAULTHCRBG, bd=0)
DisalSearchFrame.place(x=560, y=580)

EntDisalSearch = ctk.CTkEntry(
    DisalSearchFrame,
    border_width=2,
    corner_radius=30,
    fg_color=("light blue"),
    text_color="black",
    border_color=DarkBlue,
    width=200,
    textvariable=DISALSEARCH,
    font=("Arial", 18, "bold"),
    justify=RIGHT,
)
EntDisalSearch.grid(row=0, column=0, padx=10, sticky=E)

BtnDisalSearch = ctk.CTkButton(
    DisalSearchFrame,
    text="جستجو ",
    font=("Arial", 13, "bold"),
    width=20,
    border_width=1,
    fg_color="green",
    border_color="light gray",
    command=SearchDisalFunc,
)
BtnDisalSearch.grid(row=0, column=1, padx=10, sticky=E)


# ==================== Main Tabs ^^^^^^^^^^^^^^^=-=========
"""
def select():
	curItems = Dtree1.selection()
	Label(TabDisalFrame, text="\n".join([str(Dtree1.item(i)['values']) for i in curItems])).grid()
"""
PFminiwin1Disal = Label(TabDisalFrame, bg="dark blue")
PFminiwin1Disal.grid(row=0, column=0, sticky=EW)
PscrollbarxDisal = Scrollbar(TabDisalFrame, orient=HORIZONTAL)
PscrollbaryDisal = Scrollbar(TabDisalFrame, orient=VERTICAL)
Dtree1 = ttk.Treeview(
    PFminiwin1Disal,
    columns=(
        "SLID",
        "DATEID",
        "SALERNAME",
        "SLPNUM",
        "SLFUELTYPE",
        "SLCURRLTR",
        "SLPASTLTR",
        "SLPRICE",
    ),
    selectmode="browse",
    height=18,
    yscrollcommand=PscrollbaryDisal.set,
    xscrollcommand=PscrollbarxDisal.set,
)
PscrollbaryDisal.config(command=Dtree1.yview)
PscrollbaryDisal.grid(row=0, column=1, ipady=233, sticky=N)
PscrollbarxDisal.config(command=Dtree1.xview)
PscrollbarxDisal.grid(row=1, column=0, ipadx=628, sticky=W)
# =====setting headings for the columns

Dtree1.heading("SLID", text="No", anchor=W)
Dtree1.heading("DATEID", text="قید تاریخ ", anchor=W)
Dtree1.heading("SALERNAME", text="نام فروشنده", anchor=W)
Dtree1.heading("SLPNUM", text="نمبر پایه ", anchor=W)
Dtree1.heading("SLFUELTYPE", text="نوعیت تیل ", anchor=W)
Dtree1.heading("SLCURRLTR", text="مقدار فعلی  / لیتر ", anchor=W)
Dtree1.heading("SLPASTLTR", text="مقدار گذشته / لیتر ", anchor=W)
Dtree1.heading("SLPRICE", text="قیمت فی لیتر ", anchor=W)


# setting width of the columns
Dtree1.column("#0", stretch=NO, minwidth=0, width=0)
Dtree1.column("#1", stretch=NO, minwidth=0, width=90)
Dtree1.column("#2", stretch=NO, minwidth=0, width=152)
Dtree1.column("#3", stretch=NO, minwidth=0, width=300)
Dtree1.column("#4", stretch=NO, minwidth=0, width=152)
Dtree1.column("#5", stretch=NO, minwidth=0, width=152)
Dtree1.column("#6", stretch=NO, minwidth=0, width=152)
Dtree1.column("#7", stretch=NO, minwidth=0, width=152)
Dtree1.column("#8", stretch=NO, minwidth=0, width=152)

Dtree1.grid()
# Dtree1.bind("<Return>", lambda e: select())


Dtree1.delete(*Dtree1.get_children())
Pconn1 = sqlite3.connect("NiaziPetrolium.db")
Pcur1 = Pconn1.execute(
    "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLCURRLTR,SLPASTLTR,SLPRICE FROM DisalInfo"
)

Pfetch1 = Pcur1.fetchall()
for Pdata1 in Pfetch1:
    Dtree1.insert("", "end", values=(Pdata1))
Pcur1.close()
Pconn1.close()


def Pet95do_popup(event):
    try:
        selectedRow = Dtree1.selection()[0]
        FFmu = Menu(Dtree1, tearoff=0)
        FFmu.add_command(label="Edit", command="", image=PopupEdit1, compound=LEFT)
        FFmu.add_command(
            label="Delete", command=DeleteDslRecDisal, image=Recycle1, compound=LEFT
        )
        FFmu.add_command(
            label="Refresh", command=Ref3, image=PopupRefresh1, compound=LEFT
        )
        FFmu.add_command(
            label="Print",
            command=SaveDisalSelectedInfo,
            image=PopupPrint1,
            compound=LEFT,
        )

        try:
            FFmu.tk_popup(event.x_root, event.y_root)
        finally:
            FFmu.grab_release()
    except:
        messagebox.showinfo("اوووه", "! اول فایل را انتخاب کنید ")


Dtree1.bind("<Button-3>", Pet95do_popup)


# total1ShowDisal()


# ========================= Tab4 ================================
# ========================= Tab4 ================================
# ========================= Tab4 ================================
# ========================= Tab4 ================================
# ========================= Tab4 ================================
# ========================= Tab4 ================================


def Ref4():
    Ptree1.delete(*Ptree1.get_children())
    conn = sqlite3.connect("NiaziPetrolium.db")
    cur = conn.execute(
        "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLCURRLTR,SLPASTLTR,SLPRICE FROM Pet95Info"
    )
    fetch = cur.fetchall()
    for data in fetch:
        Ptree1.insert("", "end", values=(data))
    cur.close()
    conn.close()


def DeleteDslRecPet95():
    conn = sqlite3.connect("NiaziPetrolium.db")
    cur = conn.cursor()
    messageDelete = messagebox.askyesno(
        "درخواست حذف داده ", "؟ آیا واقعاً  میخواهید این داده را حذف کنید "
    )
    if messageDelete > 0:
        selected_item = Ptree1.selection()[0]
        for selected_item in Ptree1.selection():
            cur.execute(
                "DELETE FROM Pet95Info WHERE SLID=?",
                (Ptree1.set(selected_item, "SLID"),),
            )
        conn.commit()
        Ptree1.delete(selected_item)
    conn.close()
    Ref4()
    total1ShowPet95()


def total1ShowPet95():
    Ref4()
    TotalMainFrame95 = LabelFrame(
        Tab4Frame2, bg=DEFAULTHCRBG, bd=0, text="مشاهده مجموعه  پطرول", fg=BGWHITE
    )
    TotalMainFrame95.grid(row=0, column=0, sticky=W)
    TtlFrame195 = Frame(TotalMainFrame95, bg=DEFAULTHCRBG)
    TtlFrame195.grid(row=0, column=0)
    TtlFrame295 = Frame(TotalMainFrame95, bg=DEFAULTHCRBG)
    TtlFrame295.grid(row=0, column=1)
    TtlFrame395 = Frame(TotalMainFrame95, bg=DEFAULTHCRBG)
    TtlFrame395.grid(row=0, column=2)
    TtlFrame495 = Frame(TotalMainFrame95, bg=DEFAULTHCRBG)
    TtlFrame495.grid(row=0, column=3)

    # >>>>>>>>>>>>>>>> Fuel type Total 1 >>>>>>>>>>>>>>>>>>
    TWindow95 = Label(TtlFrame195, bd=0, bg=DEFAULTHCRBG)
    TWindow95.grid(row=0, column=0, sticky=E)
    Ttree195 = ttk.Treeview(
        TWindow95, columns=("SLTOTAL"), selectmode="browse", height=2
    )
    Ttree195.heading("SLTOTAL", text="مجموعه فروش دیزل / لیتر", anchor=E)
    # setting width of the columns
    Ttree195.column("#0", stretch=NO, minwidth=0, width=0)
    Ttree195.column("#1", stretch=NO, minwidth=0, width=150)
    Ttree195.grid()
    Ttree195.delete(*Ttree195.get_children())

    Tconn95 = sqlite3.connect("NiaziPetrolium.db")
    Ttree195.delete(*Ttree195.get_children())
    Tcur95 = Tconn95.execute("SELECT SUM(SLPASTLTR-SLCURRLTR) FROM Pet95Info")
    Tfetch95 = Tcur95.fetchall()
    for Tdata95 in Tfetch95:
        Ttree195.insert("", "end", values=(Tdata95))
    Tcur95.close()
    Tconn95.close()

    TWindow195 = Label(TtlFrame295, bd=0, bg=DEFAULTHCRBG)
    TWindow195.grid(row=0, column=0, sticky=E)
    Ttree295 = ttk.Treeview(
        TWindow195, columns=("TOTALPRICE295"), selectmode="browse", height=2
    )
    Ttree295.heading("TOTALPRICE295", text="مجموعه قیمت /اف ", anchor=E)
    # setting width of the columns
    Ttree295.column("#0", stretch=NO, minwidth=0, width=0)
    Ttree295.column("#1", stretch=NO, minwidth=0, width=150)
    Ttree295.grid()
    Ttree295.delete(*Ttree295.get_children())

    Tconn195 = sqlite3.connect("NiaziPetrolium.db")
    Ttree295.delete(*Ttree295.get_children())
    Tcur195 = Tconn195.execute(
        "SELECT SUM(SLPRICE*(SLPASTLTR-SLCURRLTR)) FROM Pet95Info"
    )
    Tfetch195 = Tcur195.fetchall()
    for Tdata195 in Tfetch195:
        Ttree295.insert("", "end", values=(Tdata195))
    Tcur195.close()
    Tconn195.close()

    TWindow395 = Label(TtlFrame395, bd=0, bg=DEFAULTHCRBG)
    TWindow395.grid(row=0, column=0, sticky=E)
    Ttree395 = ttk.Treeview(
        TWindow395, columns=("TOTALPRICE395"), selectmode="browse", height=2
    )
    Ttree395.heading("TOTALPRICE395", text="پایه ها ", anchor=E)
    # setting width of the columns
    Ttree395.column("#0", stretch=NO, minwidth=0, width=0)
    Ttree395.column("#1", stretch=NO, minwidth=0, width=70)
    Ttree395.grid()
    Ttree395.delete(*Ttree395.get_children())

    Tconn395 = sqlite3.connect("NiaziPetrolium.db")
    Ttree395.delete(*Ttree395.get_children())
    Tcur395 = Tconn395.execute("SELECT COUNT(SLPNUM) FROM Pet95Info")
    Tfetch395 = Tcur395.fetchall()
    for Tdata395 in Tfetch395:
        Ttree395.insert("", "end", values=(Tdata395))
    Tcur395.close()
    Tconn395.close()

    DisplayBtn.configure(fg_color=("dark blue", "green"), text="تازه سازی ")

    TWindow495 = Label(TtlFrame495, bd=0, bg=DEFAULTHCRBG)
    TWindow495.grid(row=0, column=0, sticky=E)
    Ttree495 = ttk.Treeview(
        TWindow495, columns=("TOTALPRICE495"), selectmode="browse", height=2
    )
    Ttree495.heading("TOTALPRICE495", text="فروشات این هفته/ اف", anchor=E)
    # setting width of the columns
    Ttree495.column("#0", stretch=NO, minwidth=0, width=0)
    Ttree495.column("#1", stretch=NO, minwidth=0, width=150)
    Ttree495.grid()
    Ttree495.delete(*Ttree495.get_children())

    Tconn495 = sqlite3.connect("NiaziPetrolium.db")
    Ttree495.delete(*Ttree495.get_children())
    Tcur495 = Tconn495.execute(
        "SELECT SUM(SLPRICE*(SLPASTLTR-SLCURRLTR)) FROM Pet95Info WHERE DATEID BETWEEN date('now','-7 day') AND date('now')"
    )
    Tfetch495 = Tcur495.fetchall()
    for Tdata495 in Tfetch495:
        Ttree495.insert("", "end", values=(Tdata495))
    Tcur495.close()
    Tconn495.close()


def SavePet95SelectedInfo():
    # DateNow1 = datetime.date.today()
    connDisal = sqlite3.connect("NiaziPetrolium.db")
    selected_item = Ptree1.selection()[0]
    for selected_item in Ptree1.selection():
        db = connDisal.execute(
            "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLPASTLTR,SLCURRLTR,SLPRICE FROM Pet95Info  WHERE SLID=?",
            (Ptree1.set(selected_item, "SLID"),),
        )
        MyTable = prettytable.from_db_cursor(db)
        cur = connDisal.cursor()
        rows = db.fetchall()
        for row in rows:
            MyTable.add_row(row)
        cur.close()
        connDisal.close()

        # file = asksaveasfile(filetypes = SaveExtensions, defaultextension=SaveExtensions)
        filesave = filedialog.asksaveasfile(
            mode="w",
            filetypes=SaveExtensions,
            title="ذخیره اطلاعات پطرول 95",
            defaultextension=SaveExtensions,
        )
        if filesave is None:
            return
        file2Save = str(MyTable)
        filesave.write(file2Save)
        filesave.close()
        messagebox.showinfo("HCR-BLUE", "! ذخیره موفقانه انجام شد")


def SavePet95Info():
    # DateNow1 = datetime.date.today()
    connDisal = sqlite3.connect("NiaziPetrolium.db")
    db = connDisal.execute(
        "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLPASTLTR,SLCURRLTR,SLPRICE FROM Pet95Info"
    )
    MyTable = prettytable.from_db_cursor(db)
    cur = connDisal.cursor()
    rows = db.fetchall()

    for row in rows:
        MyTable.add_row(row)
    cur.close()
    connDisal.close()

    # file = asksaveasfile(filetypes = SaveExtensions, defaultextension=SaveExtensions)
    filesave = filedialog.asksaveasfile(
        mode="w",
        filetypes=SaveExtensions,
        title="ذخیره اطلاعات پطرول 95",
        defaultextension=SaveExtensions,
    )
    if filesave is None:
        return
    file2Save = str(MyTable)
    filesave.write(file2Save)
    filesave.close()


def SearchPet95Func():
    if PET95SEARCH.get() != "":
        Ptree1.delete(*Ptree1.get_children())
        Dconn = sqlite3.connect("NiaziPetrolium.db")
        Dcur = Dconn.execute(
            "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLPASTLTR,SLCURRLTR,SLPRICE FROM Pet95Info WHERE SALERNAME LIKE?",
            ("%" + str(PET95SEARCH.get()) + "%",),
        )
        Dfetch = Dcur.fetchall()
        for Ddata in Dfetch:
            Ptree1.insert("", "end", values=(Ddata))
    else:
        messagebox.showinfo("جستجوی  فروشنده ", "!لطفاً نام فروشنده را وارد کنید ")


def SaveLastWeekPet95Info():
    # DateNow1 = datetime.date.today()
    connDisal = sqlite3.connect("NiaziPetrolium.db")
    cur = connDisal.execute(
        "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLPASTLTR,SLCURRLTR,SLPRICE FROM Pet95Info WHERE DATEID BETWEEN date('now','-7 day') AND date('now')"
    )
    MyTable = prettytable.from_db_cursor(cur)
    cur = connDisal.cursor()
    rows = cur.fetchall()

    for row in rows:
        MyTable.add_row(row)
    cur.close()
    connDisal.close()

    filesave = filedialog.asksaveasfile(
        mode="w",
        title="ذخیره اطلاعات این هفته پطرول 95",
        filetypes=SaveExtensions,
        defaultextension=SaveExtensions,
    )
    if filesave is None:
        return
    file2Save = str(MyTable)
    filesave.write(file2Save)
    filesave.close()
    messagebox.showinfo(
        "نیازی پطرولیم ",
        "برای بهبود کیفیت جدول لطفا قبل از چاپ داده نوع فونت زیر را به نوت پد تان انتخاب کنید \n 	<<< Consolas >>>",
    )


Tab4Frame1 = Frame(tab4, bg=DEFAULTHCRBG)
Tab4Frame1.grid(row=0, column=0, padx=10)

Tab4Frame2 = Frame(tab4, bg=DEFAULTHCRBG)
Tab4Frame2.grid(row=1, column=0, padx=10, sticky=W)

DisplayBtn = ctk.CTkButton(
    tab4, text=" دیدن مجموعه ", font=("Arial", 13, "bold"), command=total1ShowPet95
)
DisplayBtn.place(x=1180, y=580)

PrintPet95Btn = ctk.CTkButton(
    tab4,
    text="ذخیره اطلاعات پطرول 95",
    font=("Arial", 13, "bold"),
    command=SavePet95Info,
)
PrintPet95Btn.place(x=1025, y=580)

PrintBtnPet95 = ctk.CTkButton(
    tab4,
    text="ذخیره اطلاعات این هفته پطرول 95 ",
    font=("Arial", 13, "bold"),
    command=SaveLastWeekPet95Info,
)  # There is no command still added
PrintBtnPet95.place(x=835, y=580)


# =========================== Search Box Contents ================================

Pet95SearchFrame = Frame(tab4, bg=DEFAULTHCRBG, bd=0)
Pet95SearchFrame.place(x=540, y=580)

EntPet95Search = ctk.CTkEntry(
    Pet95SearchFrame,
    border_width=2,
    corner_radius=30,
    fg_color=("light blue"),
    text_color="black",
    border_color=DarkBlue,
    width=200,
    textvariable=PET95SEARCH,
    font=("Arial", 18, "bold"),
    justify=RIGHT,
)
EntPet95Search.grid(row=0, column=0, padx=10, sticky=E)

BtnPet95Search = ctk.CTkButton(
    Pet95SearchFrame,
    text="جستجو ",
    font=("Arial", 13, "bold"),
    width=20,
    border_width=1,
    fg_color="green",
    border_color="light gray",
    command=SearchPet95Func,
)
BtnPet95Search.grid(row=0, column=1, padx=10, sticky=E)

# ==================== Main Tabs ^^^^^^^^^^^^^^^=-=========


PFminiwin1 = Label(Tab4Frame1, bg=DEFAULTHCRBG)
PFminiwin1.grid(row=0, column=0, sticky=EW)
Pscrollbarx = Scrollbar(Tab4Frame1, orient=HORIZONTAL)
Pscrollbary = Scrollbar(Tab4Frame1, orient=VERTICAL)
Ptree1 = ttk.Treeview(
    PFminiwin1,
    columns=(
        "SLID",
        "DATEID",
        "SALERNAME",
        "SLPNUM",
        "SLFUELTYPE",
        "SLCURRLTR",
        "SLPASTLTR",
        "SLPRICE",
    ),
    selectmode="browse",
    height=18,
    yscrollcommand=Pscrollbary.set,
    xscrollcommand=Pscrollbarx.set,
)
Pscrollbary.config(command=Ptree1.yview)
Pscrollbary.grid(row=0, column=1, ipady=233, sticky=N)
Pscrollbarx.config(command=Ptree1.xview)
Pscrollbarx.grid(row=1, column=0, ipadx=628, sticky=W)
# =====setting headings for the columns

Ptree1.heading("SLID", text="No", anchor=W)
Ptree1.heading("DATEID", text="قید تاریخ ", anchor=W)
Ptree1.heading("SALERNAME", text="نام فروشنده", anchor=W)
Ptree1.heading("SLPNUM", text="نمبر پایه ", anchor=W)
Ptree1.heading("SLFUELTYPE", text="نوعیت تیل ", anchor=W)
Ptree1.heading("SLCURRLTR", text="مقدار فعلی  / لیتر ", anchor=W)
Ptree1.heading("SLPASTLTR", text="مقدار گذشته / لیتر ", anchor=W)
Ptree1.heading("SLPRICE", text="قیمت فی لیتر ", anchor=W)


# setting width of the columns
Ptree1.column("#0", stretch=NO, minwidth=0, width=0)
Ptree1.column("#1", stretch=NO, minwidth=0, width=90)
Ptree1.column("#2", stretch=NO, minwidth=0, width=152)
Ptree1.column("#3", stretch=NO, minwidth=0, width=300)
Ptree1.column("#4", stretch=NO, minwidth=0, width=152)
Ptree1.column("#5", stretch=NO, minwidth=0, width=152)
Ptree1.column("#6", stretch=NO, minwidth=0, width=152)
Ptree1.column("#7", stretch=NO, minwidth=0, width=152)
Ptree1.column("#8", stretch=NO, minwidth=0, width=152)
Ptree1.grid()


Ptree1.delete(*Ptree1.get_children())
Pconn1 = sqlite3.connect("NiaziPetrolium.db")
Pcur1 = Pconn1.execute(
    "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLCURRLTR,SLPASTLTR,SLPRICE FROM Pet95Info"
)

Pfetch1 = Pcur1.fetchall()
for Pdata1 in Pfetch1:
    Ptree1.insert("", "end", values=(Pdata1))
Pcur1.close()
Pconn1.close()


def Pet95do_popup(event):
    try:
        selectedRow = Ptree1.selection()[0]
        FFmu = Menu(Ptree1, tearoff=0)
        FFmu.add_command(label="Edit", command="", image=PopupEdit1, compound=LEFT)
        FFmu.add_command(
            label="Delete", command=DeleteDslRecPet95, image=Recycle1, compound=LEFT
        )
        FFmu.add_command(
            label="Refresh", command=Ref4, image=PopupRefresh1, compound=LEFT
        )
        FFmu.add_command(
            label="Print",
            command=SavePet95SelectedInfo,
            image=PopupPrint1,
            compound=LEFT,
        )

        try:
            FFmu.tk_popup(event.x_root, event.y_root)
        finally:
            FFmu.grab_release()
    except:
        messagebox.showinfo("اوووه", "! اول فایل را انتخاب کنید ")


Ptree1.bind("<Button-3>", Pet95do_popup)


# total1ShowPet95()

# ========================= Tab 5 ================================
# ========================= Tab 5 ================================
# ========================= Tab 5 ================================
# ========================= Tab 5 ================================
# ========================= Tab 5 ================================
# ========================= Tab 5 ================================


def Ref5():
    Ptree92.delete(*Ptree92.get_children())
    conn = sqlite3.connect("NiaziPetrolium.db")
    cur = conn.execute(
        "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLCURRLTR,SLPASTLTR,SLPRICE FROM Pet92Info"
    )
    fetch = cur.fetchall()
    for data in fetch:
        Ptree92.insert("", "end", values=(data))
    cur.close()
    conn.close()


def DeletPet92():
    conn = sqlite3.connect("NiaziPetrolium.db")
    cur = conn.cursor()
    messageDelete = messagebox.askyesno(
        "درخواست حذف داده ", "؟ آیا واقعاً  میخواهید این داده را حذف کنید "
    )
    if messageDelete > 0:
        selected_item = Ptree92.selection()[0]
        for selected_item in Ptree92.selection():
            cur.execute(
                "DELETE FROM Pet92Info WHERE SLID=?",
                (Ptree92.set(selected_item, "SLID"),),
            )
        conn.commit()
        Ptree92.delete(selected_item)
    conn.close()
    Ref5()
    total1ShowPet92()


def total1ShowPet92():
    Ref5()
    TotalMainFrame92 = LabelFrame(
        Tab5Frame2, bg=DEFAULTHCRBG, bd=0, text="مشاهده مجموعه  پطرول 92", fg=BGWHITE
    )
    TotalMainFrame92.grid(row=0, column=0, sticky=W)
    TtlFrame192 = Frame(TotalMainFrame92, bg=DEFAULTHCRBG)
    TtlFrame192.grid(row=0, column=0)
    TtlFrame292 = Frame(TotalMainFrame92, bg=DEFAULTHCRBG)
    TtlFrame292.grid(row=0, column=1)
    TtlFrame392 = Frame(TotalMainFrame92, bg=DEFAULTHCRBG)
    TtlFrame392.grid(row=0, column=2)
    TtlFrame492 = Frame(TotalMainFrame92, bg=DEFAULTHCRBG)
    TtlFrame492.grid(row=0, column=3)

    # >>>>>>>>>>>>>>>> Fuel type Total 1 >>>>>>>>>>>>>>>>>>
    TWindow92 = Label(TtlFrame192, bd=0, bg=DEFAULTHCRBG)
    TWindow92.grid(row=0, column=0, sticky=E)
    Ttree192 = ttk.Treeview(
        TWindow92, columns=("SLTOTAL292"), selectmode="browse", height=2
    )
    Ttree192.heading("SLTOTAL292", text="مجموعه فروش دیزل / لیتر", anchor=E)
    # setting width of the columns
    Ttree192.column("#0", stretch=NO, minwidth=0, width=0)
    Ttree192.column("#1", stretch=NO, minwidth=0, width=150)
    Ttree192.grid()
    Ttree192.delete(*Ttree192.get_children())

    Tconn92 = sqlite3.connect("NiaziPetrolium.db")
    Ttree192.delete(*Ttree192.get_children())
    Tcur92 = Tconn92.execute("SELECT SUM(SLPASTLTR-SLCURRLTR) FROM Pet92Info")
    Tfetch92 = Tcur92.fetchall()
    for Tdata92 in Tfetch92:
        Ttree192.insert("", "end", values=(Tdata92))
    Tcur92.close()
    Tconn92.close()

    TWindow192 = Label(TtlFrame292, bd=0, bg=DEFAULTHCRBG)
    TWindow192.grid(row=0, column=0, sticky=E)
    Ttree292 = ttk.Treeview(
        TWindow192, columns=("TOTALPRICE392"), selectmode="browse", height=2
    )
    Ttree292.heading("TOTALPRICE392", text="مجموعه قیمت /اف ", anchor=E)
    # setting width of the columns
    Ttree292.column("#0", stretch=NO, minwidth=0, width=0)
    Ttree292.column("#1", stretch=NO, minwidth=0, width=150)
    Ttree292.grid()
    Ttree292.delete(*Ttree292.get_children())

    Tconn192 = sqlite3.connect("NiaziPetrolium.db")
    Ttree292.delete(*Ttree292.get_children())
    Tcur192 = Tconn192.execute(
        "SELECT SUM(SLPRICE*(SLPASTLTR-SLCURRLTR)) FROM Pet92Info"
    )
    Tfetch192 = Tcur192.fetchall()
    for Tdata192 in Tfetch192:
        Ttree292.insert("", "end", values=(Tdata192))
    Tcur192.close()
    Tconn192.close()

    TWindow392 = Label(TtlFrame392, bd=0, bg=DEFAULTHCRBG)
    TWindow392.grid(row=0, column=0, sticky=E)
    Ttree392 = ttk.Treeview(
        TWindow392, columns=("TOTALPRICE492"), selectmode="browse", height=2
    )
    Ttree392.heading("TOTALPRICE492", text="پایه ها ", anchor=E)
    # setting width of the columns
    Ttree392.column("#0", stretch=NO, minwidth=0, width=0)
    Ttree392.column("#1", stretch=NO, minwidth=0, width=70)
    Ttree392.grid()
    Ttree392.delete(*Ttree392.get_children())

    Tconn392 = sqlite3.connect("NiaziPetrolium.db")
    Ttree392.delete(*Ttree392.get_children())
    Tcur392 = Tconn392.execute("SELECT COUNT(SLPNUM) FROM Pet92Info")
    Tfetch392 = Tcur392.fetchall()
    for Tdata392 in Tfetch392:
        Ttree392.insert("", "end", values=(Tdata392))
    Tcur392.close()
    Tconn392.close()

    DisplayBtn92.configure(fg_color=("dark blue", "green"), text="تازه سازی ")

    TWindow492 = Label(TtlFrame492, bd=0, bg=DEFAULTHCRBG)
    TWindow492.grid(row=0, column=0, sticky=E)
    Ttree492 = ttk.Treeview(
        TWindow492, columns=("TOTALPRICE592"), selectmode="browse", height=2
    )
    Ttree492.heading("TOTALPRICE592", text="فروشات این هفته/ اف", anchor=E)
    # setting width of the columns
    Ttree492.column("#0", stretch=NO, minwidth=0, width=0)
    Ttree492.column("#1", stretch=NO, minwidth=0, width=150)
    Ttree492.grid()
    Ttree492.delete(*Ttree492.get_children())

    Tconn492 = sqlite3.connect("NiaziPetrolium.db")
    Ttree492.delete(*Ttree492.get_children())
    Tcur492 = Tconn492.execute(
        "SELECT SUM(SLPRICE*(SLPASTLTR-SLCURRLTR)) FROM Pet92Info WHERE DATEID BETWEEN date('now','-7 day') AND date('now')"
    )
    # Tcur3Disal = Tconn3Disal.execute("SELECT DATEID FROM DisalInfo WHERE DATEID BETWEEN date('now','-7 day') AND date('now')") #Showing the bettween dates
    Tfetch492 = Tcur492.fetchall()
    for Tdata492 in Tfetch492:
        Ttree492.insert("", "end", values=(Tdata492))
    Tcur492.close()
    Tconn492.close()


def SavePet92Info():
    # DateNow1 = datetime.date.today()
    connDisal = sqlite3.connect("NiaziPetrolium.db")
    db = connDisal.execute(
        "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLPASTLTR,SLCURRLTR,SLPRICE FROM Pet92Info"
    )
    MyTable = prettytable.from_db_cursor(db)
    cur = connDisal.cursor()
    rows = db.fetchall()

    for row in rows:
        MyTable.add_row(row)
    cur.close()
    connDisal.close()

    filesave = filedialog.asksaveasfile(
        mode="w",
        filetypes=SaveExtensions,
        title="ذخیره اطلاعات پطرول 92",
        defaultextension=SaveExtensions,
    )
    if filesave is None:
        return
    file2Save = str(MyTable)
    filesave.write(file2Save)
    filesave.close()


def SaveLastWeekPet92Info():
    # DateNow1 = datetime.date.today()
    connDisal = sqlite3.connect("NiaziPetrolium.db")
    cur = connDisal.execute(
        "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLPASTLTR,SLCURRLTR,SLPRICE FROM Pet92Info WHERE DATEID BETWEEN date('now','-7 day') AND date('now')"
    )
    MyTable = prettytable.from_db_cursor(cur)
    cur = connDisal.cursor()
    rows = cur.fetchall()

    for row in rows:
        MyTable.add_row(row)
    cur.close()
    connDisal.close()

    filesave = filedialog.asksaveasfile(
        mode="w",
        title="ذخیره اطلاعات این هفته دیزل 02",
        filetypes=SaveExtensions,
        defaultextension=SaveExtensions,
    )
    if filesave is None:
        return
    file2Save = str(MyTable)
    filesave.write(file2Save)
    filesave.close()
    messagebox.showinfo(
        "نیازی پطرولیم ",
        "برای بهبود کیفیت جدول لطفا قبل از چاپ داده نوع فونت زیر را به نوت پد تان انتخاب کنید \n 	<<< Consolas >>>",
    )


def SearchPet92Func():
    if PET92SEARCH.get() != "":
        Ptree92.delete(*Ptree92.get_children())
        Dconn = sqlite3.connect("NiaziPetrolium.db")
        Dcur = Dconn.execute(
            "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLPASTLTR,SLCURRLTR,SLPRICE FROM Pet92Info WHERE SALERNAME LIKE?",
            ("%" + str(PET92SEARCH.get()) + "%",),
        )
        Dfetch = Dcur.fetchall()
        for Ddata in Dfetch:
            Ptree92.insert("", "end", values=(Ddata))
    else:
        messagebox.showinfo("جستجوی  فروشنده ", "!لطفاً نام فروشنده را وارد کنید ")


Tab5Frame1 = Frame(tab5, bg=DEFAULTHCRBG)
Tab5Frame1.grid(row=0, column=0, padx=10)

Tab5Frame2 = Frame(tab5, bg=DEFAULTHCRBG)
Tab5Frame2.grid(row=1, column=0, padx=10, sticky=W)

DisplayBtn92 = ctk.CTkButton(
    tab5, text=" دیدن مجموعه ", font=("Arial", 13, "bold"), command=total1ShowPet92
)
DisplayBtn92.place(x=1180, y=580)

PrintBtn92 = ctk.CTkButton(
    tab5,
    text="ذخیره اطلاعات پطرول 92",
    font=("Arial", 13, "bold"),
    command=SavePet92Info,
)
PrintBtn92.place(x=1025, y=580)

PrintBtnPet92 = ctk.CTkButton(
    tab5,
    text="ذخیره اطلاعات این هفته پطرول 92 ",
    font=("Arial", 13, "bold"),
    command=SaveLastWeekPet92Info,
)  # There is no command still added
PrintBtnPet92.place(x=835, y=580)


# =========================== Search Box Contents ================================

Pet92SearchFrame = Frame(tab5, bg=DEFAULTHCRBG, bd=0)
Pet92SearchFrame.place(x=540, y=580)

EntPet92Search = ctk.CTkEntry(
    Pet92SearchFrame,
    border_width=2,
    corner_radius=30,
    fg_color=("light blue"),
    text_color="black",
    border_color=DarkBlue,
    width=200,
    textvariable=PET92SEARCH,
    font=("Arial", 18, "bold"),
    justify=RIGHT,
)
EntPet92Search.grid(row=0, column=0, padx=10, sticky=E)

BtnPet92Search = ctk.CTkButton(
    Pet92SearchFrame,
    text="جستجو ",
    font=("Arial", 13, "bold"),
    width=20,
    border_width=1,
    fg_color="green",
    border_color="light gray",
    command=SearchPet92Func,
)
BtnPet92Search.grid(row=0, column=1, padx=10, sticky=E)
# ==================== Main Tabs ^^^^^^^^^^^^^^^=-=========


PFminiwin192 = Label(Tab5Frame1, bg="dark blue")
PFminiwin192.grid(row=0, column=0, sticky=EW)
Pscrollbarx92 = Scrollbar(Tab5Frame1, orient=HORIZONTAL)
Pscrollbary92 = Scrollbar(Tab5Frame1, orient=VERTICAL)
Ptree92 = ttk.Treeview(
    PFminiwin192,
    columns=(
        "SLID",
        "DATEID",
        "SALERNAME",
        "SLPNUM",
        "SLFUELTYPE",
        "SLCURRLTR",
        "SLPASTLTR",
        "SLPRICE",
    ),
    selectmode="browse",
    height=18,
    yscrollcommand=Pscrollbary92.set,
    xscrollcommand=Pscrollbarx92.set,
)
Pscrollbary92.config(command=Ptree92.yview)
Pscrollbary92.grid(row=0, column=1, ipady=233, sticky=N)
Pscrollbarx92.config(command=Ptree92.xview)
Pscrollbarx92.grid(row=1, column=0, ipadx=628, sticky=W)
# =====setting headings for the columns

Ptree92.heading("SLID", text="No", anchor=W)
Ptree92.heading("DATEID", text="قید تاریخ ", anchor=W)
Ptree92.heading("SALERNAME", text="نام فروشنده", anchor=W)
Ptree92.heading("SLPNUM", text="نمبر پایه ", anchor=W)
Ptree92.heading("SLFUELTYPE", text="نوعیت تیل ", anchor=W)
Ptree92.heading("SLCURRLTR", text="مقدار فعلی  / لیتر ", anchor=W)
Ptree92.heading("SLPASTLTR", text="مقدار گذشته / لیتر ", anchor=W)
Ptree92.heading("SLPRICE", text="قیمت فی لیتر ", anchor=W)


# setting width of the columns
Ptree92.column("#0", stretch=NO, minwidth=0, width=0)
Ptree92.column("#1", stretch=NO, minwidth=0, width=90)
Ptree92.column("#2", stretch=NO, minwidth=0, width=152)
Ptree92.column("#3", stretch=NO, minwidth=0, width=300)
Ptree92.column("#4", stretch=NO, minwidth=0, width=152)
Ptree92.column("#5", stretch=NO, minwidth=0, width=152)
Ptree92.column("#6", stretch=NO, minwidth=0, width=152)
Ptree92.column("#7", stretch=NO, minwidth=0, width=152)
Ptree92.column("#8", stretch=NO, minwidth=0, width=152)
Ptree92.grid()


Ptree92.delete(*Ptree92.get_children())
Pconn192 = sqlite3.connect("NiaziPetrolium.db")
Pcur192 = Pconn192.execute(
    "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLCURRLTR,SLPASTLTR,SLPRICE FROM Pet92Info"
)

Pfetch192 = Pcur192.fetchall()
for Pdata192 in Pfetch192:
    Ptree92.insert("", "end", values=(Pdata192))
Pcur192.close()
Pconn192.close()


def Pet92do_popup(event):
    try:
        selectedRow = Ptree92.selection()[0]
        FFmu = Menu(Ptree92, tearoff=0)
        FFmu.add_command(label="Edit", command="", image=PopupEdit1, compound=LEFT)
        FFmu.add_command(
            label="Delete", command=DeletPet92, image=Recycle1, compound=LEFT
        )
        FFmu.add_command(
            label="Refresh", command=Ref5, image=PopupRefresh1, compound=LEFT
        )
        FFmu.add_command(label="Print", command="", image=PopupPrint1, compound=LEFT)

        try:
            FFmu.tk_popup(event.x_root, event.y_root)
        finally:
            FFmu.grab_release()
    except:
        messagebox.showinfo("اوووه", "! اول فایل را انتخاب کنید ")


Ptree92.bind("<Button-3>", Pet92do_popup)


# total1ShowPet92()

# ========================= Tab 6 ================================
# ========================= Tab 6 ================================
# ========================= Tab 6 ================================
# ========================= Tab 6 ================================
# ========================= Tab 6 ================================
# ========================= Tab 6 ================================


def Ref6():
    Gtree1.delete(*Gtree1.get_children())
    conn = sqlite3.connect("NiaziPetrolium.db")
    cur = conn.execute(
        "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLCURRLTR,SLPASTLTR,SLPRICE FROM GasInfo"
    )
    fetch = cur.fetchall()
    for data in fetch:
        Gtree1.insert("", "end", values=(data))
    cur.close()
    conn.close()


def DeleteGas1():
    conn = sqlite3.connect("NiaziPetrolium.db")
    cur = conn.cursor()
    messageDelete = messagebox.askyesno(
        "درخواست حذف داده ", "؟ آیا واقعاً  میخواهید این داده را حذف کنید "
    )
    if messageDelete > 0:
        selected_item = Gtree1.selection()[0]
        for selected_item in Gtree1.selection():
            cur.execute(
                "DELETE FROM GasInfo WHERE SLID=?", (Gtree1.set(selected_item, "SLID"),)
            )
        conn.commit()
        Gtree1.delete(selected_item)
    conn.close()
    Ref6()
    total1ShowGas1()


def total1ShowGas1():
    Ref6()
    TotalMainFrameGas1 = LabelFrame(
        Tab6Frame2, bg=DEFAULTHCRBG, bd=0, text="مشاهده مجموعه گاز ", fg=BGWHITE
    )
    TotalMainFrameGas1.grid(row=0, column=0, sticky=W)
    TtlFrame1Gas1 = Frame(TotalMainFrameGas1, bg=DEFAULTHCRBG)
    TtlFrame1Gas1.grid(row=0, column=0)
    TtlFrame2Gas1 = Frame(TotalMainFrameGas1, bg=DEFAULTHCRBG)
    TtlFrame2Gas1.grid(row=0, column=1)
    TtlFrame3Gas1 = Frame(TotalMainFrameGas1, bg=DEFAULTHCRBG)
    TtlFrame3Gas1.grid(row=0, column=2)
    TtlFrame4Gas1 = Frame(TotalMainFrameGas1, bg=DEFAULTHCRBG)
    TtlFrame4Gas1.grid(row=0, column=3)

    # >>>>>>>>>>>>>>>> Fuel type Total 1 >>>>>>>>>>>>>>>>>>
    TWindowGas1 = Label(TtlFrame1Gas1, bd=0, bg=DEFAULTHCRBG)
    TWindowGas1.grid(row=0, column=0, sticky=E)
    Ttree1Gas1 = ttk.Treeview(
        TWindowGas1, columns=("SLTOTAL"), selectmode="browse", height=2
    )
    Ttree1Gas1.heading("SLTOTAL", text="مجموعه فروش دیزل / لیتر", anchor=E)
    # setting width of the columns
    Ttree1Gas1.column("#0", stretch=NO, minwidth=0, width=0)
    Ttree1Gas1.column("#1", stretch=NO, minwidth=0, width=150)
    Ttree1Gas1.grid()
    Ttree1Gas1.delete(*Ttree1Gas1.get_children())

    TconnGas1 = sqlite3.connect("NiaziPetrolium.db")
    Ttree1Gas1.delete(*Ttree1Gas1.get_children())
    TcurGas1 = TconnGas1.execute("SELECT SUM(SLPASTLTR-SLCURRLTR) FROM GasInfo")
    TfetchGas1 = TcurGas1.fetchall()
    for TdataGas1 in TfetchGas1:
        Ttree1Gas1.insert("", "end", values=(TdataGas1))
    TcurGas1.close()
    TconnGas1.close()

    TWindow1Gas1 = Label(TtlFrame2Gas1, bd=0, bg=DEFAULTHCRBG)
    TWindow1Gas1.grid(row=0, column=0, sticky=E)
    Ttree2Gas1 = ttk.Treeview(
        TWindow1Gas1, columns=("TOTALPRICE"), selectmode="browse", height=2
    )
    Ttree2Gas1.heading("TOTALPRICE", text="مجموعه قیمت /اف ", anchor=E)
    # setting width of the columns
    Ttree2Gas1.column("#0", stretch=NO, minwidth=0, width=0)
    Ttree2Gas1.column("#1", stretch=NO, minwidth=0, width=150)
    Ttree2Gas1.grid()
    Ttree2Gas1.delete(*Ttree2Gas1.get_children())

    Tconn1Gas1 = sqlite3.connect("NiaziPetrolium.db")
    Ttree2Gas1.delete(*Ttree2Gas1.get_children())
    Tcur1Gas1 = Tconn1Gas1.execute(
        "SELECT SUM(SLPRICE*(SLPASTLTR-SLCURRLTR)) FROM GasInfo"
    )
    Tfetch1Gas1 = Tcur1Gas1.fetchall()
    for Tdata1Gas1 in Tfetch1Gas1:
        Ttree2Gas1.insert("", "end", values=(Tdata1Gas1))
    Tcur1Gas1.close()
    Tconn1Gas1.close()

    TWindow3Gas1 = Label(TtlFrame3Gas1, bd=0, bg=DEFAULTHCRBG)
    TWindow3Gas1.grid(row=0, column=0, sticky=E)
    Ttree3Gas1 = ttk.Treeview(
        TWindow3Gas1, columns=("TOTALPRICE3"), selectmode="browse", height=2
    )
    Ttree3Gas1.heading("TOTALPRICE3", text="پایه ها ", anchor=E)
    # setting width of the columns
    Ttree3Gas1.column("#0", stretch=NO, minwidth=0, width=0)
    Ttree3Gas1.column("#1", stretch=NO, minwidth=0, width=70)
    Ttree3Gas1.grid()
    Ttree3Gas1.delete(*Ttree3Gas1.get_children())

    Tconn3Gas1 = sqlite3.connect("NiaziPetrolium.db")
    Ttree3Gas1.delete(*Ttree3Gas1.get_children())
    Tcur3Gas1 = Tconn3Gas1.execute("SELECT COUNT(SLPNUM) FROM GasInfo")
    Tfetch3Gas1 = Tcur3Gas1.fetchall()
    for Tdata3Gas1 in Tfetch3Gas1:
        Ttree3Gas1.insert("", "end", values=(Tdata3Gas1))
    Tcur3Gas1.close()
    Tconn3Gas1.close()

    DisplayBtnGas1.configure(fg_color=("dark blue", "green"), text="تازه سازی ")

    TWindow4Gas1 = Label(TtlFrame4Gas1, bd=0, bg=DEFAULTHCRBG)
    TWindow4Gas1.grid(row=0, column=0, sticky=E)
    Ttree4Gas1 = ttk.Treeview(
        TWindow4Gas1, columns=("TOTALPRICE3"), selectmode="browse", height=2
    )
    Ttree4Gas1.heading("TOTALPRICE3", text="پایه ها ", anchor=E)
    # setting width of the columns
    Ttree4Gas1.column("#0", stretch=NO, minwidth=0, width=0)
    Ttree4Gas1.column("#1", stretch=NO, minwidth=0, width=150)
    Ttree4Gas1.grid()
    Ttree4Gas1.delete(*Ttree4Gas1.get_children())

    Tconn4Gas1 = sqlite3.connect("NiaziPetrolium.db")
    Ttree4Gas1.delete(*Ttree4Gas1.get_children())
    Tcur4Gas1 = Tconn4Gas1.execute(
        "SELECT SUM(SLPRICE*(SLPASTLTR-SLCURRLTR)) FROM GasInfo WHERE DATEID BETWEEN date('now','-7 day') AND date('now')"
    )

    Tfetch4Gas1 = Tcur4Gas1.fetchall()
    for Tdata4Gas1 in Tfetch4Gas1:
        Ttree4Gas1.insert("", "end", values=(Tdata4Gas1))
    Tcur4Gas1.close()
    Tconn4Gas1.close()


def SaveGasInfo():
    # DateNow1 = datetime.date.today()
    connDisal = sqlite3.connect("NiaziPetrolium.db")
    db = connDisal.execute(
        "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLPASTLTR,SLCURRLTR,SLPRICE FROM GasInfo"
    )
    MyTable = prettytable.from_db_cursor(db)
    cur = connDisal.cursor()
    rows = db.fetchall()

    for row in rows:
        MyTable.add_row(row)
    cur.close()
    connDisal.close()

    filesave = filedialog.asksaveasfile(
        mode="w",
        filetypes=SaveExtensions,
        title="ذخیره اطلاعات گاز",
        defaultextension=".TXT",
    )
    if filesave is None:
        return
    file2Save = str(MyTable)
    filesave.write(file2Save)
    filesave.close()


def SaveLastWeekGasInfo():
    # DateNow1 = datetime.date.today()
    connDisal = sqlite3.connect("NiaziPetrolium.db")
    cur = connDisal.execute(
        "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLPASTLTR,SLCURRLTR,SLPRICE FROM GasInfo WHERE DATEID BETWEEN date('now','-7 day') AND date('now')"
    )
    MyTable = prettytable.from_db_cursor(cur)
    cur = connDisal.cursor()
    rows = cur.fetchall()

    for row in rows:
        MyTable.add_row(row)
    cur.close()
    connDisal.close()

    filesave = filedialog.asksaveasfile(
        mode="w",
        title="ذخیره اطلاعات این هفته گاز ",
        filetypes=SaveExtensions,
        defaultextension=SaveExtensions,
    )
    if filesave is None:
        return
    file2Save = str(MyTable)
    filesave.write(file2Save)
    filesave.close()
    messagebox.showinfo(
        "نیازی پطرولیم ",
        "برای بهبود کیفیت جدول لطفا قبل از چاپ داده نوع فونت زیر را به نوت پد تان انتخاب کنید \n 	<<< Consolas >>>",
    )


def SearchGasFunc():
    if GASSEARCH.get() != "":
        Gtree1.delete(*Gtree1.get_children())
        Gconn = sqlite3.connect("NiaziPetrolium.db")
        Gcur = Gconn.execute(
            "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLPASTLTR,SLCURRLTR,SLPRICE FROM GasInfo WHERE SALERNAME LIKE?",
            ("%" + str(GASSEARCH.get()) + "%",),
        )
        Gfetch = Gcur.fetchall()
        for Gdata in Gfetch:
            Gtree1.insert("", "end", values=(Gdata))
    else:
        messagebox.showinfo("جستجوی  فروشنده ", "!لطفاً نام فروشنده را وارد کنید ")


Tab6Frame1 = Frame(tab6, bg=DEFAULTHCRBG)
Tab6Frame1.grid(row=0, column=0, padx=10)

Tab6Frame2 = Frame(tab6, bg=DEFAULTHCRBG)
Tab6Frame2.grid(row=1, column=0, padx=10, sticky=W)

DisplayBtnGas1 = ctk.CTkButton(
    tab6, text=" دیدن مجموعه ", font=("Arial", 13, "bold"), command=total1ShowGas1
)
DisplayBtnGas1.place(x=1180, y=580)

PrintGasBtn = ctk.CTkButton(
    tab6, text="ذخیره اطلاعات گاز", font=("Arial", 13, "bold"), command=SaveGasInfo
)
PrintGasBtn.place(x=1025, y=580)

PrintBtnGas = ctk.CTkButton(
    tab6,
    text="ذخیره اطلاعات این هفته  گاز ",
    font=("Arial", 13, "bold"),
    command=SaveLastWeekGasInfo,
)  # There is no command still added
PrintBtnGas.place(x=835, y=580)


# =========================== Search Box Contents ================================

GasSearchFrame = Frame(tab6, bg=DEFAULTHCRBG, bd=0)
GasSearchFrame.place(x=540, y=580)

EntGasSearch = ctk.CTkEntry(
    GasSearchFrame,
    border_width=2,
    corner_radius=30,
    fg_color=("light blue"),
    text_color="black",
    border_color=DarkBlue,
    width=200,
    textvariable=GASSEARCH,
    font=("Arial", 18, "bold"),
    justify=RIGHT,
)
EntGasSearch.grid(row=0, column=0, padx=10, sticky=E)

BtnGasSearch = ctk.CTkButton(
    GasSearchFrame,
    text="جستجو ",
    font=("Arial", 13, "bold"),
    width=20,
    border_width=1,
    fg_color="green",
    border_color="light gray",
    command=SearchGasFunc,
)
BtnGasSearch.grid(row=0, column=1, padx=10, sticky=E)
# ==================== Main Tabs ^^^^^^^^^^^^^^^=-=========


PFminiwin1Gas1 = Label(Tab6Frame1, bg=DEFAULTHCRBG)
PFminiwin1Gas1.grid(row=0, column=0, sticky=EW)
PscrollbarxGas1 = Scrollbar(Tab6Frame1, orient=HORIZONTAL)
PscrollbaryGas1 = Scrollbar(Tab6Frame1, orient=VERTICAL)
Gtree1 = ttk.Treeview(
    PFminiwin1Gas1,
    columns=(
        "SLID",
        "DATEID",
        "SALERNAME",
        "SLPNUM",
        "SLFUELTYPE",
        "SLCURRLTR",
        "SLPASTLTR",
        "SLPRICE",
    ),
    selectmode="browse",
    height=18,
    yscrollcommand=PscrollbaryGas1.set,
    xscrollcommand=PscrollbarxGas1.set,
)
PscrollbaryGas1.config(command=Gtree1.yview)
PscrollbaryGas1.grid(row=0, column=1, ipady=233, sticky=N)
PscrollbarxGas1.config(command=Gtree1.xview)
PscrollbarxGas1.grid(row=1, column=0, ipadx=628, sticky=W)
# =====setting headings for the columns

Gtree1.heading("SLID", text="No", anchor=W)
Gtree1.heading("DATEID", text="قید تاریخ ", anchor=W)
Gtree1.heading("SALERNAME", text="نام فروشنده", anchor=W)
Gtree1.heading("SLPNUM", text="نمبر پایه ", anchor=W)
Gtree1.heading("SLFUELTYPE", text="نوعیت تیل ", anchor=W)
Gtree1.heading("SLCURRLTR", text="مقدار فعلی  / لیتر ", anchor=W)
Gtree1.heading("SLPASTLTR", text="مقدار گذشته / لیتر ", anchor=W)
Gtree1.heading("SLPRICE", text="قیمت فی لیتر ", anchor=W)


# setting width of the columns
Gtree1.column("#0", stretch=NO, minwidth=0, width=0)
Gtree1.column("#1", stretch=NO, minwidth=0, width=90)
Gtree1.column("#2", stretch=NO, minwidth=0, width=152)
Gtree1.column("#3", stretch=NO, minwidth=0, width=300)
Gtree1.column("#4", stretch=NO, minwidth=0, width=152)
Gtree1.column("#5", stretch=NO, minwidth=0, width=152)
Gtree1.column("#6", stretch=NO, minwidth=0, width=152)
Gtree1.column("#7", stretch=NO, minwidth=0, width=152)
Gtree1.column("#8", stretch=NO, minwidth=0, width=152)
Gtree1.grid()


Gtree1.delete(*Gtree1.get_children())
Gconn1 = sqlite3.connect("NiaziPetrolium.db")
Gcur1 = Gconn1.execute(
    "SELECT SLID,DATEID,SALERNAME,SLPNUM,SLFUELTYPE,SLCURRLTR,SLPASTLTR,SLPRICE FROM GasInfo"
)

Gfetch1 = Gcur1.fetchall()
for Gdata1 in Gfetch1:
    Gtree1.insert("", "end", values=(Gdata1))
Gcur1.close()
Gconn1.close()


def Gas1do_popup(event):
    try:
        selectedRow = Gtree1.selection()[0]
        FFmu = Menu(Gtree1, tearoff=0)
        FFmu.add_command(label="Edit", command="", image=PopupEdit1, compound=LEFT)
        FFmu.add_command(
            label="Delete", command=DeleteGas1, image=Recycle1, compound=LEFT
        )
        FFmu.add_command(
            label="Refresh", command=Ref6, image=PopupRefresh1, compound=LEFT
        )
        FFmu.add_command(label="Print", command="", image=PopupPrint1, compound=LEFT)

        try:
            FFmu.tk_popup(event.x_root, event.y_root)
        finally:
            FFmu.grab_release()
    except:
        messagebox.showinfo("اوووه", "! اول فایل را انتخاب کنید ")


Gtree1.bind("<Button-3>", Gas1do_popup)


# total1ShowGas1()

# ========================= Tab 7 ================================
# ========================= Tab 7 ================================
# ========================= Tab 7 ================================
# ========================= Tab 7 ================================
# ========================= Tab 7 ================================
# ========================= Tab 7 ================================


CommingSoon = ctk.CTkFrame(
    tab7,
    bg_color=MODERNPINK,
    corner_radius=20,
    border_color=BGLIGHTGRAY,
    border_width=3,
)
CommingSoon.grid(row=0, column=0, sticky=E)

CommingSoonText = Label(
    CommingSoon,
    text="!بزودی ارائه خواهد شد  ",
    font=("B Titr", 100),
    bg=MODERNPINK,
    fg="white",
)
CommingSoonText.grid(row=0, column=0, sticky=E)
contactMe = Label(
    CommingSoon,
    text="!برای گذارش اشکال برنامه با ما ارتباط بگیرید \nhcrgroup.info@gmail.com",
    font=("Arial", 10),
    fg=BGYELLOW,
    bg=MODERNPINK,
)
contactMe.grid(row=1, column=0, sticky=NSEW)


# =================================== Do not use other widgets under this line of code ================================
"""
root.update()



frame = Frame(root,bg=DarkBlue,width=40,height=root.winfo_height())
frame.place(x=0,y=0)

ProductsBtn = Button(frame,image=ProductsImage1,bg=DarkBlue,activebackground=DarkBlue,bd=0,fg="white", relief="flat",compound=LEFT,takefocus=False,command=changeProf)
ProductsBtn.grid(row=0,column=0,pady=10,padx=5,sticky=W)
ProductsBtn.bind('<Enter>',change_fontColor1)
ProductsBtn.bind('<Leave>',change_fontColor2)

CustomersBtn = Button(frame,image=CustomerImage1,bg=DarkBlue,activebackground=DarkBlue,bd=0,fg="white", relief="flat",compound=LEFT,takefocus=False,command="")
CustomersBtn.grid(row=1,column=0,pady=10,padx=5,sticky=W)

OrdersBtn = Button(frame,image=OrderImage2,bg=DarkBlue,activebackground=DarkBlue,bd=0,fg="white", relief="flat",compound=LEFT,takefocus=False, command="")
OrdersBtn.grid(row=2,column=0,pady=10,padx=5,sticky=W)

EmployeesBtn = Button(frame,image=StuffImage1,bg=DarkBlue,activebackground=DarkBlue,bd=0,fg="white", relief="flat",takefocus=False,compound=LEFT)
EmployeesBtn.grid(row=3,column=0,pady=10,padx=5,sticky=W)

ExpensesBtn = Button(frame,image=ExpesesImage1,bg=DarkBlue,activebackground=DarkBlue,bd=0,fg="white", relief="flat",takefocus=False,compound=LEFT)
ExpensesBtn.grid(row=4,column=0,pady=10,padx=5,sticky=W)

TaxBtn = Button(frame,image=TaxImage1,bg=DarkBlue,activebackground=DarkBlue,bd=0,fg="white", relief="flat",takefocus=False,compound=LEFT)
TaxBtn.grid(row=5,column=0,pady=10,padx=5,sticky=W)

ShowBtn = Button(frame,image=ShowImage1,bg=DarkBlue,activebackground=DarkBlue,bd=0,fg="white", relief="flat",takefocus=False,compound=LEFT)
ShowBtn.grid(row=6,column=0,pady=10,padx=5,sticky=W)

ExitBtn = Button(frame,image=ExitImage1,bg=DarkBlue,activebackground=DarkBlue,bd=0,fg="white", relief="flat",takefocus=False,compound=LEFT)
ExitBtn.grid(row=7,column=0,pady=10,padx=5,sticky=W)




ProLbl = Label(frame, image=PersonM, bd=0,bg=DarkBlue)
ProLbl.grid(row=9,column=0,padx=5,pady=50)



frame.bind('<Enter>',lambda e: Expand_1())
frame.bind('<Leave>',lambda e: Contract_1())

frame.grid_propagate(False)

"""


root.mainloop()
