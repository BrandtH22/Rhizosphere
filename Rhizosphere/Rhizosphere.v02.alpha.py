from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, Text
from tkinter.filedialog import askopenfilename, asksaveasfilename
import TKlighter
import os
import subprocess


root = Tk()
root.geometry('800x750')
root.resizable(True, True)
root.title('Rhizosphere IDE V02 - ChiaLisp')

#define tabs

tab_master = ttk.Notebook(root)

tab1 = ttk.Frame(tab_master)
tab2 = ttk.Frame(tab_master)
tab3 = ttk.Frame(tab_master)

tab_master.add(tab1, text="Develop")
tab_master.add(tab2, text="Serialize")
tab_master.add(tab3, text="Deploy")

tab_master.place(relwidth=1, relheight=.89, relx=0.0, rely=.11)

#define variables
gpath = ''
psFile_path = "C:/example/path/file.ps1"
envFile_path = "C:/example/path/venv"
clspFile_path = "C:/example/path/file.clsp"
defaultsFile_path = "./defaults.txt"
defaultsPath_var = [psFile_path, envFile_path, clspFile_path]


hexResult_var = "hex result will display here"
curryResult_var = "curry result will display here"
treeHashResult_var = "treehash result will display here"
walletResult_var = "wallet result will display here"
resultsFile_var = "results file path will display here"
arg1_var = tk.StringVar()
arg1_var = "enter arg as '-a xxx'"
arg2_var = tk.StringVar()
arg2_var = "enter arg as '-a xxx'"
prefix_var = "txch"

#pull default file paths from save files

if os.path.isfile('defaults.txt'):
    defaultsFile = open(defaultsFile_path)
    defaults_array = defaultsFile.readlines()
    psFile_path = defaults_array[0]
    envFile_path = defaults_array[1]
    clspFile_path = defaults_array[2]
    print("*********************Thank you for using Rhizosphere*********************")
    print("Default ps File Path: " + psFile_path.strip())
    print("Default env Folder Path: " + envFile_path.strip())
    print("Default clsp File Path: " + clspFile_path.strip())
    defaultsFile.close()

#define serialize (tab2) frames
bg_logo_frame = tk.Frame(root, bg="#006400")
bg_logo_frame.place(relwidth=1, relheight=.1, relx=0.0, rely=.01)

bg_main_frame = tk.Frame(tab2, bg='#2d6a4f')
bg_main_frame.place(relwidth=1, relheight=1, relx=0, rely=0)

bg_top_frame = tk.Frame(tab2, bg="gray")
bg_top_frame.place(relwidth=0.45, relheight=.2, relx=0.05, rely=.12)

bg_topclspLabel_frame = tk.Frame(tab2, bg='#2d6a4f')
bg_topclspLabel_frame.place(relwidth=.19, relheight=.05, relx=0.05, rely=.04)

bg_topclsp_frame = tk.Frame(tab2, bg="gray")
bg_topclsp_frame.place(relwidth=.7, relheight=.04, relx=.25, rely=.043)

bg_topr_frame = tk.Frame(tab2, bg="gray")
bg_topr_frame.place(relwidth=1, relheight=.2, relx=0, rely=.12)

bg_mid_frame = tk.Frame(tab2, bg="#1b4332")
bg_mid_frame.place(relwidth=1, relheight=.1, relx=0.0, rely=.35)

bg_bot_frame = tk.Frame(tab2, bg="gray")
bg_bot_frame.place(relwidth=0.9, relheight=.45, relx=0.05, rely=.49)

bg_hexR_frame = tk.Frame(tab2, bg="gray")
bg_hexR_frame.place(relwidth=0.67, relheight=.082, relx=0.25, rely=.51)

bg_curryR_frame = tk.Frame(tab2, bg="gray")
bg_curryR_frame.place(relwidth=0.67, relheight=.082, relx=0.25, rely=.62)

bg_treeHashR_frame = tk.Frame(tab2, bg="gray")
bg_treeHashR_frame.place(relwidth=0.67, relheight=.082, relx=0.25, rely=.735)

bg_walletR_frame = tk.Frame(tab2, bg="gray")
bg_walletR_frame.place(relwidth=0.67, relheight=.082, relx=0.25, rely=.84)

bg_resultsF_frame = tk.Frame(tab2, bg="gray")
bg_resultsF_frame.place(relwidth=0.7, relheight=.04, relx=0.25, rely=.95)

bg_resultsLabel_frame = tk.Frame(tab2, bg='#2d6a4f')
bg_resultsLabel_frame.place(relwidth=.19, relheight=.05, relx=0.05, rely=.95)

bg_deploy_frame = tk.Frame(tab3, bg="gray")
bg_deploy_frame.place(relwidth=1, relheight=1, relx=0, rely=0)

#define serialize (tab2) textboxes and labels
header_text = tk.Label(bg_logo_frame, text="Rhizosphere", bd="0", fg="#1b4332", bg="#006400", font="Copperplate, 40", relief="sunken")
header_text.place(relx=0.3, rely=0.1)

comingSoon_text = tk.Label(bg_deploy_frame, text="Coming Soon", bd="0", fg="black", bg="#006400", font="Copperplate, 40", relief="sunken")
comingSoon_text.place(relx=.28, rely=.2)

clspFile_label = tk.Label(bg_topclspLabel_frame, text="Working CLSP File:", bg="#74c69d", justify="right", padx=10, pady=3, relief="sunken")
clspFile_label.place(relx=0, rely=0.04)

clspFile_text = tk.Text(bg_topclsp_frame, height=50, width=100, bd="0", fg="#1b4332", bg="gray", font="Arial, 12", relief="sunken")
clspFile_text.pack(fill='both', expand=True)
clspFile_text.tag_config('justified', justify="right", wrap="none", underline=True)
clspFile_text.insert(1.0, clspFile_path, 'justified')

hexResult_label = tk.Label(bg_bot_frame, text="Hex Result:", bg="#74c69d", justify="right", padx=35, pady=15, relief="sunken")
hexResult_label.place(relx=0.01, rely=0.04)

hexResult_text = tk.Text(bg_hexR_frame, height=50, width=100, bd="0", fg="#1b4332", bg="gray", font="Arial, 12", relief="sunken")
hexResult_text.pack(fill='both', expand=True)
hexResult_text.tag_config('justified', justify="right")
hexResult_text.insert(1.0, hexResult_var, 'justified')

curryResult_label = tk.Label(bg_bot_frame, text="Curry Result:", bg="#74c69d", justify="right", padx=30, pady=15, relief="sunken")
curryResult_label.place(relx=0.01, rely=0.28)

curryResult_text = tk.Text(bg_curryR_frame, height=50, width=100, bd="0", fg="#1b4332", bg="gray", font="Arial, 12", relief="sunken")
curryResult_text.pack(fill='both', expand=True)
curryResult_text.tag_config('justified', justify="right")
curryResult_text.insert(1.0, curryResult_var, 'justified')

treeHashResult_label = tk.Label(bg_bot_frame, text="Tree Hash Result:", bg="#74c69d", justify="right", padx=18, pady=15, relief="sunken")
treeHashResult_label.place(relx=0.01, rely=0.52)

treeHashResult_text = tk.Text(bg_treeHashR_frame, height=50, width=100, bd="0", fg="#1b4332", bg="gray", font="Arial, 12", relief="sunken")
treeHashResult_text.pack(fill='both', expand=True)
treeHashResult_text.tag_config('justified', justify="right")
treeHashResult_text.insert(1.0, treeHashResult_var, 'justified')

walletResult_label = tk.Label(bg_bot_frame, text="Encoded Wallet Result:", bg="#74c69d", justify="right", padx=3, pady=15, relief="sunken")
walletResult_label.place(relx=0.01, rely=0.76)

walletResult_text = tk.Text(bg_walletR_frame, height=50, width=100, bd="0", fg="#1b4332", bg="gray", font="Arial, 12", relief="sunken")
walletResult_text.pack(fill='both', expand=True)
walletResult_text.tag_config('justified', justify="right")
walletResult_text.insert(1.0, walletResult_var, 'justified')

resultFile_label = tk.Label(bg_resultsLabel_frame, text="Results File:", bg="#74c69d", justify="right", padx=33, pady=3, relief="sunken")
resultFile_label.place(relx=0.04, rely=0)

resultsFile_text = tk.Text(bg_resultsF_frame, height=50, width=100, bd="0", fg="#1b4332", bg="gray", font="Arial, 12", relief="sunken")
resultsFile_text.pack(fill='both', expand=True)
resultsFile_text.tag_config('justified', justify="right", wrap="none", underline=True)
resultsFile_text.insert(1.0, resultsFile_var, 'justified')

args_label = tk.Label(bg_topr_frame, text="Arguments to Curry", bg="gray", justify="right", padx=3, pady=3, relief="flat")
args_label.place(relx=0.24, rely=0.1)

arg1_label = tk.Label(bg_topr_frame, text="arg1: ", bg="gray", justify="right", padx=3, pady=3, relief="flat")
arg1_label.place(relx=0.1, rely=0.4)

arg2_label = tk.Label(bg_topr_frame, text="arg2: ", bg="gray", justify="right", padx=3, pady=3, relief="flat")
arg2_label.place(relx=0.1, rely=0.7)

prefix_label = tk.Label(bg_topr_frame, text="Wallet Prefix", bg="gray", justify="right", padx=3, pady=3, relief="flat")
prefix_label.place(relx=0.75, rely=0.1)



#define menu bar functions

def setDefaults():
    global psFile_text
    global envFile_text
    global psFile_path
    global envFile_path
    global defaults_array
    defaults_w = tk.Toplevel(root)
    defaults_w.geometry('700x200')
    defaults_w.grab_set()
    defaults_w.focus_force()
    def defClose_toggle():
        defaults_w.destroy()
    bg_defaults_frame = tk.Frame(defaults_w, bg="gray")
    bg_defaults_frame.place(relwidth=1, relheight=1, relx=0, rely=0)

    bg_topps_frame = tk.Frame(bg_defaults_frame, bg="gray")
    bg_topps_frame.place(relwidth=0.75, relheight=.12, relx=0.2, rely=.12)

    bg_topenv_frame = tk.Frame(bg_defaults_frame, bg="gray")
    bg_topenv_frame.place(relwidth=0.75, relheight=.12, relx=0.2, rely=.4)

    psFile_text = tk.Text(bg_topps_frame, height=50, width=100, bd="0", fg="#1b4332", bg="gray", font="Arial, 12", relief="sunken")
    psFile_text.pack(fill='both', expand=True)
    psFile_text.tag_config('justified', justify="right", wrap="none", underline=True)
    psFile_text.insert(1.0, psFile_path, 'justified')

    envFile_text = tk.Text(bg_topenv_frame, height=50, width=100, bd="0", fg="#1b4332", bg="gray", font="Arial, 12", relief="sunken")
    envFile_text.pack(fill='both', expand=True)
    envFile_text.tag_config('justified', justify="right", wrap="none", underline=True)
    envFile_text.insert(1.0, envFile_path, 'justified')

    psFile_btn = tk.Button(defaults_w, text="PowerShell File", command=psFile_toggle, width=16, relief="raised", bg="white")
    psFile_btn.place(relx=0.01, rely=0.11)

    envFile_btn = tk.Button(defaults_w, text="Virtual Environment", command=envFile_toggle, width=16, relief="raised", bg="white")
    envFile_btn.place(relx=0.01, rely=0.4)

    defClose_btn = tk.Button(defaults_w, text="Save Defaults and Close", command=defClose_toggle, width=22, relief="raised", bg="white")
    defClose_btn.place(relx=0.45, rely=0.8)



def openMyFile():
    path = askopenfilename(filetypes=[('ChiaLisp','*.clsp'), ('CLVM','*.clvm')])
    with open(path, 'r') as file:
        code = file.read()
        textEditor.delete('1.0', END)
        textEditor.insert('1.0', code)
        global gpath
        gpath = path
        global clspFile_path
        global clspFile_text
        global defaults_array
        clspFile_path = path
        defaults_array[2] = clspFile_path
        clspFile_text.configure(state="normal")
        clspFile_text.delete(1.0, "end")
        clspFile_text.insert(1.0, clspFile_path, 'justified')

def saveMyFileAs():
    global gpath
    global clspFile_path
    global clspFile_text
    global defaults_array
    if gpath =='':
        path = asksaveasfilename(filetypes=[('ChiaLisp','*.clsp'), ('CLVM','*.clvm')])
        clspFile_path = path
    else:
        path = gpath
        clspFile_path = path
    with open(path, 'w') as file:
        code = textEditor.get('1.0', END)
        file.write(code)
        defaults_array[2] = clspFile_path
        clspFile_text.configure(state="normal")
        clspFile_text.delete(1.0, "end")
        clspFile_text.insert(1.0, clspFile_path, 'justified')

#define clsp highlighting for tab1

def light(event):
    hlight_1 = ['AGG_SIG_UNSAFE',
        'AGG_SIG_ME',
        'CREATE_COIN',
        'ASSERT_FEE',
        'CREATE_COIN_ANNOUNCEMENT',
        'ASSERT_COIN_ANNOUNCEMENT',
        'CREATE_PUZZLE_ANNOUNCEMENT',
        'ASSERT_PUZZLE_ANNOUNCEMENT',
        'ASSERT_MY_COIN_ID',
        'ASSERT_MY_PARENT_ID',
        'ASSERT_MY_PUZZLE_HASH',
        'ASSERT_MY_AMOUNT',
        'ASSERT_SECONDS_RELATIVE',
        'ASSERT_SECONDS_ABSOLUTE',
        'ASSERT_HEIGHT_RELATIVE',
        'ASSERT_HEIGHT_ABSOLUTE']
    hlight_2 = ['run',
                'mod',
                'main',
                'include',
                'sha256 1',
                'sha256 2',
                'defun',
                'defun-inline',
                'defmacro',
                'defconstant',
                'list',
                'if',
                'qq',
                'unquote',
                '@',
                ';']
    hlight_3 = ['brun',
                'f',
                'r',
                'c',
                'a',
                'x',
                'i',
                'q',
                'all',
                'any',
                'div mod',
                'logand',
                'logior',
                'logxor',
                'lognot',
                'ash',
                'lsh',
                'substr',
                'strlen',
                'concat']
    hlight_4 = ['point_add',
                'pubkey_for_exp']
    for p in hlight_1:
        TKlighter.custom_h(textEditor, p, '#32bebe')
    for b in hlight_2:
        TKlighter.custom_h(textEditor, b, '#189ac7')
    for g in hlight_3:
        TKlighter.custom_h(textEditor, g, '#66c856')
    for h in hlight_4:
        TKlighter.custom_h(textEditor, h, '#d6d14a')

#define serialize (tab2) functions

def clickarg1(event):
   arg1_text.configure(state="normal")
   arg1_text.delete(0, "end")
   arg1_text.unbind('<Button-1>', clicked1)

def clickarg2(event):
   arg2_text.configure(state="normal")
   arg2_text.delete(0, "end")
   arg2_text.unbind('<Button-1>', clicked2)

def txch_toggle():
    global prefix_var
    if prefix_txch_btn.config('relief')[-1] == 'sunken':
        prefix_txch_btn.configure(relief="raised", bg="white")
        prefix_xch_btn.configure(relief="sunken", bg="gray")
        prefix_var = "xch"
        print("txch click - change to raised")
        print("prefix: ", prefix_var)
    else:
        prefix_txch_btn.configure(relief="sunken", bg="gray")
        prefix_xch_btn.configure(relief="raised", bg="white")
        prefix_var = "txch"
        print("txch click - change to sunken")
        print("prefix: ", prefix_var)

def xch_toggle():
    global prefix_var
    if prefix_xch_btn.config('relief')[-1] == 'sunken':
        prefix_xch_btn.configure(relief="raised", bg="white")
        prefix_txch_btn.configure(relief="sunken", bg="gray")
        prefix_var = "txch"
        print("xch click - change to raised")
        print("prefix: ", prefix_var)
    else:
        prefix_xch_btn.configure(relief="sunken", bg="gray")
        prefix_txch_btn.configure(relief="raised", bg="white")
        prefix_var = "xch"
        print("xch click - change to sunken")
        print("prefix: ", prefix_var)

def psFile_toggle():
    global psFile_path
    global psFile_text
    global defaults_array
    psFile_path = filedialog.askopenfilename(initialdir="/", title="Select create_hex.ps1 file",
                                            filetypes= (("Powershell", "*.ps1"), ("all files", "*.*")))
    psFile_text.configure(state="normal")
    psFile_text.delete(1.0, "end")
    psFile_text.insert(1.0, psFile_path, 'justified')
    defaults_array[0] = psFile_path + "\n"

def envFile_toggle():
    global envFile_path
    global envFile_text
    global defaults_array
    envFile_path = filedialog.askdirectory(initialdir="/", title="Select Virtual Environment Directory")
    envFile_text.configure(state="normal")
    envFile_text.delete(1.0, "end")
    envFile_text.insert(1.0, envFile_path, 'justified')
    defaults_array[1] = envFile_path + "\n"

def create_hex():
    import subprocess
    global psFile_path
    global envFile_path
    global clspFile_path
    psFile_path = psFile_path.strip()
    envFile_path = envFile_path.strip()
    clspFile_path = clspFile_path.strip()
    completed = subprocess.run(["powershell.exe",
                "-File",
                psFile_path,
                envFile_path,
                clspFile_path,
                arg1_var,
                arg2_var,
                prefix_var])
    return completed


def display_results():
    global arg1_var
    global arg2_var
    print("arg1 = ", arg1_var)
    print("arg2 = ", arg2_var)
    print("Prefix = ", prefix_var)
    print("PS File Path: ", psFile_path)
    print("Env File Path: ", envFile_path)
    print("CLSP File Path: ", clspFile_path)
    print("*********************Processing Complete*********************")

    resultsFile_var = clspFile_path + ".results.txt"
    resultsFile = open(resultsFile_var)
    results_array = resultsFile.readlines()
    resultsFile.close()

    hexResult_var = results_array[0]
    hexResult_text.configure(state="normal")
    hexResult_text.delete(1.0, "end")
    hexResult_text.insert(1.0, hexResult_var, 'justified')

    curryResult_var = results_array[1]
    curryResult_text.configure(state="normal")
    curryResult_text.delete(1.0, "end")
    curryResult_text.insert(1.0, curryResult_var, 'justified')

    treeHashResult_var = results_array[2]
    treeHashResult_text.configure(state="normal")
    treeHashResult_text.delete(1.0, "end")
    treeHashResult_text.insert(1.0, treeHashResult_var, 'justified')

    walletResult_var = results_array[3]
    walletResult_text.configure(state="normal")
    walletResult_text.delete(1.0, "end")
    walletResult_text.insert(1.0, walletResult_var, 'justified')

    resultsFile_text.configure(state="normal")
    resultsFile_text.delete(1.0, "end")
    resultsFile_text.insert(1.0, resultsFile_var, 'justified')


def submit_click():
    global arg1_var
    global arg2_var

    if arg1_text.get() in {"", " ", "enter arg as '-a xxx'"}:
        if arg2_text.get() in {"", " ", "enter arg as '-a xxx'"}:
            arg1_var = ""
            arg2_var = ""
            create_hex()
            display_results()
        else:
            arg1_var = ""
            arg2_var=arg2_text.get()
            create_hex()
            display_results()
    elif arg2_text.get() in {"", " ", "enter arg as '-a xxx'"}:
        arg1_var=arg1_text.get()
        arg2_var = ""
        create_hex()
        display_results()
    else:
        arg1_var=arg1_text.get()
        arg2_var=arg2_text.get()
        create_hex()
        display_results()




#define editor (tab1) window

textEditor = Text(tab1)
textEditor.config(bg='#1b1b1b', fg='#d2ded1', insertbackground='white')
textEditor.pack(fill='both', expand=True)
textEditor.bind('<Key>', light)

#define menubar

menuBar = Menu(tab1)

fileBar = Menu(menuBar, tearoff=0)
fileBar.add_command(label='Set Defaults', command = setDefaults)
fileBar.add_command(label='Open CLSP/CLVM', command = openMyFile)
fileBar.add_command(label='Save CLSP/CLVM', command = saveMyFileAs)
fileBar.add_command(label='SaveAs CLSP/CLVM', command = saveMyFileAs)
fileBar.add_command(label='Exit', command = exit)
menuBar.add_cascade(label='File', menu = fileBar)


#define serialize (tab2) entry widget

arg1_text = tk.Entry(bg_topr_frame, width=22)
arg1_text.insert(0, arg1_var)
arg1_text.place(relx=0.25, rely=0.42)
clicked1 = arg1_text.bind('<Button-1>', clickarg1)

arg2_text = tk.Entry(bg_topr_frame, width=22)
arg2_text.insert(0, arg2_var)
arg2_text.place(relx=0.25, rely=0.72)
clicked2 = arg2_text.bind('<Button-1>', clickarg2)

#define serialize (tab2) buttons

prefix_txch_btn = tk.Button(bg_topr_frame, text="txch ", command=txch_toggle, bg="gray", justify="right", padx=3, pady=3, relief="sunken")
prefix_txch_btn.place(relx=0.8, rely=0.38)

prefix_xch_btn = tk.Button(bg_topr_frame, text="xch ", command=xch_toggle, bg="white", justify="right", padx=5, pady=3, relief="raised")
prefix_xch_btn.place(relx=0.8, rely=0.68)

begin_btntext = tk.StringVar()
begin_btn = tk.Button(bg_mid_frame, textvariable=begin_btntext, command=submit_click, font="Perpetua, 12", width=16, height=2, relief="raised", bg="white")
begin_btntext.set("Click to Begin")
begin_btn.place(relx=0.4, rely=0.16)

root.config(menu=menuBar)
root.mainloop()

#create default files

with open('defaults.txt', 'w') as s:
    s.writelines(defaults_array)
