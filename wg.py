import subprocess
import ctypes, sys
import tkinter as tk
from tkinter import filedialog

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def enable_wg():    
    wg = 'C:/Users/tony.sl.kou/Downloads/wf/WG.conf'
    subprocess.call('cd /d C:/Program Files/WireGuard', shell=True)
    subprocess.call('wireguard /installtunnelservice '+wg, shell=True)

def disable_wg():
    wg = 'C:/Users/tony.sl.kou/Downloads/wf/WG.conf'
    subprocess.call('cd /d C:/Program Files/WireGuard', shell=True)
    subprocess.call('wireguard /uninstalltunnelservice WG', shell=True)

def GUI_design():
    window = tk.Tk()
    window.title('WireGuard')
    window.geometry('300x100')
    window.resizable(False, False)

    enable = tk.Button(text="enable wg", command=enable_wg)
    disable = tk.Button(text="disable wg", command=disable_wg)
    
    enable.place(x=150,y=30,anchor='center')
    disable.place(x=150,y=70,anchor='center')

    return window

def main():
    GUI = GUI_design()

    if is_admin()==False:        
        ctypes.windll.shell32.ShellExecuteW(None,"runas", sys.executable, __file__, None, 1)
        GUI.destroy()
        
    GUI.mainloop()

if __name__ == '__main__':
    main()

