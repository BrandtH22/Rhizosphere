import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.geometry('700x700')
root.resizable(True, True)
root.title('Rhynosphere.v01 - ChiaLisp')


#define variables for testing
psFile_path = "C:/example/path/file.ps1"
envFile_path = "C:/example/path/venv"
clspFile_path = "C:/example/path/file.clsp"
hexResult_var = "hex result will display here"
hexFile_var = "hex file path will display here"
curryResult_var = "curry result will display here"
curryFile_var = "curry file path will display here"
treeHashResult_var = "treehash result will display here"
treeHashFile_var = "treehash file path will display here"
walletResult_var = "wallet result will display here"
walletFile_var = "wallet file path will display here"
arg1_var = tk.StringVar()
arg1_var = "enter arg as '-a xxx'"
arg2_var = tk.StringVar()
arg2_var = "enter arg as '-a xxx'"
prefix_var = "txch"

#pull default file paths from save files

if os.path.isfile('envPath.txt'):
    with open('envPath.txt', 'r') as f:
        envdef = f.read()
        envFile_path = envdef

if os.path.isfile('psPath.txt'):
    with open('psPath.txt', 'r') as g:
        psdef = g.read()
        psFile_path = psdef

if os.path.isfile('clspPath.txt'):
    with open('clspPath.txt', 'r') as h:
        clspdef = h.read()
        clspFile_path = clspdef

#define frames
bg_main_frame = tk.Frame(root, bg='#2d6a4f')
bg_main_frame.place(relwidth=1, relheight=1, relx=0, rely=0)

bg_logo_frame = tk.Frame(root, bg="#006400")
bg_logo_frame.place(relwidth=1, relheight=.1, relx=0.0, rely=.01)

bg_top_frame = tk.Frame(root, bg="gray")
bg_top_frame.place(relwidth=0.45, relheight=.2, relx=0.05, rely=.12)

bg_topps_frame = tk.Frame(root, bg="gray")
bg_topps_frame.place(relwidth=0.25, relheight=.05, relx=0.25, rely=.14)

bg_topenv_frame = tk.Frame(root, bg="gray")
bg_topenv_frame.place(relwidth=0.25, relheight=.05, relx=0.25, rely=.2)

bg_topclsp_frame = tk.Frame(root, bg="gray")
bg_topclsp_frame.place(relwidth=0.25, relheight=.05, relx=0.25, rely=.26)

bg_topr_frame = tk.Frame(root, bg="gray")
bg_topr_frame.place(relwidth=0.45, relheight=.2, relx=0.5, rely=.12)

bg_mid_frame = tk.Frame(root, bg="#1b4332")
bg_mid_frame.place(relwidth=1, relheight=.1, relx=0.0, rely=.35)

bg_bot_frame = tk.Frame(root, bg="gray")
bg_bot_frame.place(relwidth=0.9, relheight=.45, relx=0.05, rely=.49)

bg_hexR_frame = tk.Frame(root, bg="gray")
bg_hexR_frame.place(relwidth=0.67, relheight=.03, relx=0.25, rely=.51)

bg_hexF_frame = tk.Frame(root, bg="gray")
bg_hexF_frame.place(relwidth=0.67, relheight=.03, relx=0.25, rely=.56)

bg_curryR_frame = tk.Frame(root, bg="gray")
bg_curryR_frame.place(relwidth=0.67, relheight=.03, relx=0.25, rely=.62)

bg_curryF_frame = tk.Frame(root, bg="gray")
bg_curryF_frame.place(relwidth=0.67, relheight=.03, relx=0.25, rely=.68)

bg_treeHashR_frame = tk.Frame(root, bg="gray")
bg_treeHashR_frame.place(relwidth=0.67, relheight=.03, relx=0.25, rely=.735)

bg_treeHashF_frame = tk.Frame(root, bg="gray")
bg_treeHashF_frame.place(relwidth=0.67, relheight=.03, relx=0.25, rely=.785)

bg_walletR_frame = tk.Frame(root, bg="gray")
bg_walletR_frame.place(relwidth=0.67, relheight=.03, relx=0.25, rely=.84)

bg_walletF_frame = tk.Frame(root, bg="gray")
bg_walletF_frame.place(relwidth=0.67, relheight=.03, relx=0.25, rely=.89)

#define textboxes and labels
header_text = tk.Text(bg_logo_frame, height=50, width=100, bd="0", fg="#1b4332", bg="#006400", font="Copperplate, 40", relief="sunken")
header_text.place(relx=0.3, rely=0.1)
header_text.insert(1.0, "Rhynosphere")

psFile_text = tk.Text(bg_topps_frame, height=50, width=100, bd="0", fg="#1b4332", bg="gray", font="Arial, 12", relief="sunken")
psFile_text.pack(fill='both', expand=True)
psFile_text.tag_config('justified', justify="right", wrap="none", underline=True)
psFile_text.insert(1.0, psFile_path, 'justified')

envFile_text = tk.Text(bg_topenv_frame, height=50, width=100, bd="0", fg="#1b4332", bg="gray", font="Arial, 12", relief="sunken")
envFile_text.pack(fill='both', expand=True)
envFile_text.tag_config('justified', justify="right", wrap="none", underline=True)
envFile_text.insert(1.0, envFile_path, 'justified')

clspFile_text = tk.Text(bg_topclsp_frame, height=50, width=100, bd="0", fg="#1b4332", bg="gray", font="Arial, 12", relief="sunken")
clspFile_text.pack(fill='both', expand=True)
clspFile_text.tag_config('justified', justify="right", wrap="none", underline=True)
clspFile_text.insert(1.0, clspFile_path, 'justified')

hexResult_label = tk.Label(bg_bot_frame, text="Hex Result:", bg="#74c69d", justify="right", padx=35, pady=3, relief="sunken")
hexResult_label.place(relx=0.01, rely=0.04)

hexResult_text = tk.Text(bg_hexR_frame, height=50, width=100, bd="0", fg="#1b4332", bg="gray", font="Arial, 12", relief="sunken")
hexResult_text.pack(fill='both', expand=True)
hexResult_text.tag_config('justified', justify="right", wrap="none")
hexResult_text.insert(1.0, hexResult_var, 'justified')

hexFile_label = tk.Label(bg_bot_frame, text="Hex File:", bg="#74c69d", justify="right", padx=41, pady=3, relief="sunken")
hexFile_label.place(relx=0.01, rely=0.16)

hexFile_text = tk.Text(bg_hexF_frame, height=50, width=100, bd="0", fg="#1b4332", bg="gray", font="Arial, 12", relief="sunken")
hexFile_text.pack(fill='both', expand=True)
hexFile_text.tag_config('justified', justify="right", wrap="none", underline=True)
hexFile_text.insert(1.0, hexFile_var, 'justified')

curryResult_label = tk.Label(bg_bot_frame, text="Curry Result:", bg="#74c69d", justify="right", padx=30, pady=3, relief="sunken")
curryResult_label.place(relx=0.01, rely=0.28)

curryResult_text = tk.Text(bg_curryR_frame, height=50, width=100, bd="0", fg="#1b4332", bg="gray", font="Arial, 12", relief="sunken")
curryResult_text.pack(fill='both', expand=True)
curryResult_text.tag_config('justified', justify="right", wrap="none")
curryResult_text.insert(1.0, curryResult_var, 'justified')

curryFile_label = tk.Label(bg_bot_frame, text="Curry File:", bg="#74c69d", justify="right", padx=37, pady=3, relief="sunken")
curryFile_label.place(relx=0.01, rely=0.4)

curryFile_text = tk.Text(bg_curryF_frame, height=50, width=100, bd="0", fg="#1b4332", bg="gray", font="Arial, 12", relief="sunken")
curryFile_text.pack(fill='both', expand=True)
curryFile_text.tag_config('justified', justify="right", wrap="none", underline=True)
curryFile_text.insert(1.0, curryFile_var, 'justified')

treeHashResult_label = tk.Label(bg_bot_frame, text="Tree Hash Result:", bg="#74c69d", justify="right", padx=18, pady=3, relief="sunken")
treeHashResult_label.place(relx=0.01, rely=0.52)

treeHashResult_text = tk.Text(bg_treeHashR_frame, height=50, width=100, bd="0", fg="#1b4332", bg="gray", font="Arial, 12", relief="sunken")
treeHashResult_text.pack(fill='both', expand=True)
treeHashResult_text.tag_config('justified', justify="right", wrap="none")
treeHashResult_text.insert(1.0, treeHashResult_var, 'justified')

treeHashFile_label = tk.Label(bg_bot_frame, text="Tree Hash File:", bg="#74c69d", justify="right", padx=25, pady=3, relief="sunken")
treeHashFile_label.place(relx=0.01, rely=0.64)

treeHashFile_text = tk.Text(bg_treeHashF_frame, height=50, width=100, bd="0", fg="#1b4332", bg="gray", font="Arial, 12", relief="sunken")
treeHashFile_text.pack(fill='both', expand=True)
treeHashFile_text.tag_config('justified', justify="right", wrap="none", underline=True)
treeHashFile_text.insert(1.0, treeHashFile_var, 'justified')

walletResult_label = tk.Label(bg_bot_frame, text="Encoded Wallet Result:", bg="#74c69d", justify="right", padx=3, pady=3, relief="sunken")
walletResult_label.place(relx=0.01, rely=0.76)

walletResult_text = tk.Text(bg_walletR_frame, height=50, width=100, bd="0", fg="#1b4332", bg="gray", font="Arial, 12", relief="sunken")
walletResult_text.pack(fill='both', expand=True)
walletResult_text.tag_config('justified', justify="right", wrap="none")
walletResult_text.insert(1.0, walletResult_var, 'justified')

walletFile_label = tk.Label(bg_bot_frame, text="Encoded Wallet File:", bg="#74c69d", justify="right", padx=10, pady=3, relief="sunken")
walletFile_label.place(relx=0.01, rely=0.88)

walletFile_text = tk.Text(bg_walletF_frame, height=50, width=100, bd="0", fg="#1b4332", bg="gray", font="Arial, 12", relief="sunken")
walletFile_text.pack(fill='both', expand=True)
walletFile_text.tag_config('justified', justify="right", wrap="none", underline=True)
walletFile_text.insert(1.0, walletFile_var, 'justified')

args_label = tk.Label(bg_topr_frame, text="Arguments to Curry", bg="gray", justify="right", padx=3, pady=3, relief="flat")
args_label.place(relx=0.24, rely=0.1)

arg1_label = tk.Label(bg_topr_frame, text="arg1: ", bg="gray", justify="right", padx=3, pady=3, relief="flat")
arg1_label.place(relx=0.1, rely=0.4)

arg2_label = tk.Label(bg_topr_frame, text="arg2: ", bg="gray", justify="right", padx=3, pady=3, relief="flat")
arg2_label.place(relx=0.1, rely=0.7)

prefix_label = tk.Label(bg_topr_frame, text="Wallet Prefix", bg="gray", justify="right", padx=3, pady=3, relief="flat")
prefix_label.place(relx=0.75, rely=0.1)


#define functions

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
    psFile_path = filedialog.askopenfilename(initialdir="/", title="Select create_hex.ps1 file",
                                            filetypes= (("Powershell", "*.ps1"), ("all files", "*.*")))
    psFile_text.configure(state="normal")
    psFile_text.delete(1.0, "end")
    psFile_text.insert(1.0, psFile_path, 'justified')

def envFile_toggle():
    global envFile_path
    global envFile_text
    envFile_path = filedialog.askdirectory(initialdir="/", title="Select Virtual Environment Directory")
    envFile_text.configure(state="normal")
    envFile_text.delete(1.0, "end")
    envFile_text.insert(1.0, envFile_path, 'justified')

def clspFile_toggle():
    global clspFile_path
    global clspFile_text
    clspFile_path = filedialog.askopenfilename(initialdir="/", title="Select ChiaLisp file",
                                            filetypes= (("ChiaLisp", "*.clsp"), ("all files", "*.*")))
    clspFile_text.configure(state="normal")
    clspFile_text.delete(1.0, "end")
    clspFile_text.insert(1.0, clspFile_path, 'justified')

def create_hex():
    import subprocess
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

    hexFile_var = clspFile_path + ".hex"
    curryFile_var = clspFile_path + ".curry.txt"
    treeHashFile_var = clspFile_path + ".treehash.txt"
    walletFile_var = clspFile_path + ".wallet.txt"

    with open(hexFile_var, 'r') as reader1:
        hexResult_var = reader1.readlines()
    hexResult_text.configure(state="normal")
    hexResult_text.delete(1.0, "end")
    hexResult_text.insert(1.0, hexResult_var, 'justified')

    hexFile_text.configure(state="normal")
    hexFile_text.delete(1.0, "end")
    hexFile_text.insert(1.0, hexFile_var, 'justified')

    with open(curryFile_var, 'r') as reader2:
        curryResult_var = reader2.readlines()
    curryResult_text.configure(state="normal")
    curryResult_text.delete(1.0, "end")
    curryResult_text.insert(1.0, curryResult_var, 'justified')

    curryFile_text.configure(state="normal")
    curryFile_text.delete(1.0, "end")
    curryFile_text.insert(1.0, curryFile_var, 'justified')

    with open(treeHashFile_var, 'r') as reader3:
        treeHashResult_var = reader3.readlines()
    treeHashResult_text.configure(state="normal")
    treeHashResult_text.delete(1.0, "end")
    treeHashResult_text.insert(1.0, treeHashResult_var, 'justified')

    treeHashFile_text.configure(state="normal")
    treeHashFile_text.delete(1.0, "end")
    treeHashFile_text.insert(1.0, treeHashFile_var, 'justified')

    with open(walletFile_var, 'r') as reader4:
        walletResult_var = reader4.readlines()
    walletResult_text.configure(state="normal")
    walletResult_text.delete(1.0, "end")
    walletResult_text.insert(1.0, walletResult_var, 'justified')

    walletFile_text.configure(state="normal")
    walletFile_text.delete(1.0, "end")
    walletFile_text.insert(1.0, walletFile_var, 'justified')


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

#define entry widget

arg1_text = tk.Entry(bg_topr_frame, width=22)
arg1_text.insert(0, arg1_var)
arg1_text.place(relx=0.25, rely=0.42)
clicked1 = arg1_text.bind('<Button-1>', clickarg1)

arg2_text = tk.Entry(bg_topr_frame, width=22)
arg2_text.insert(0, arg2_var)
arg2_text.place(relx=0.25, rely=0.72)
clicked2 = arg2_text.bind('<Button-1>', clickarg2)

#define buttons

psFile_btn = tk.Button(bg_top_frame, text="PowerShell File", command=psFile_toggle, width=16, relief="raised", bg="white")
psFile_btn.place(relx=0.01, rely=0.11)

envFile_btn = tk.Button(bg_top_frame, text="Virtual Environment", command=envFile_toggle, width=16, relief="raised", bg="white")
envFile_btn.place(relx=0.01, rely=0.4)

clspFile_btn = tk.Button(bg_top_frame, text="ChiaLisp File", command=clspFile_toggle, width=16, relief="raised", bg="white")
clspFile_btn.place(relx=0.01, rely=0.7)

prefix_txch_btn = tk.Button(bg_topr_frame, text="txch ", command=txch_toggle, bg="gray", justify="right", padx=3, pady=3, relief="sunken")
prefix_txch_btn.place(relx=0.8, rely=0.38)

prefix_xch_btn = tk.Button(bg_topr_frame, text="xch ", command=xch_toggle, bg="white", justify="right", padx=5, pady=3, relief="raised")
prefix_xch_btn.place(relx=0.8, rely=0.68)

begin_btntext = tk.StringVar()
begin_btn = tk.Button(bg_mid_frame, textvariable=begin_btntext, command=submit_click, font="Perpetua, 12", width=16, height=2, relief="raised", bg="white")
begin_btntext.set("Click to Begin")
begin_btn.place(relx=0.4, rely=0.16)




root.mainloop()

#create default files
with open('envPath.txt', 'w') as f:
    f.write(envFile_path)

with open('psPath.txt', 'w') as g:
    g.write(psFile_path)

with open('clspPath.txt', 'w') as h:
    h.write(clspFile_path)
