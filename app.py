import tkinter as tk
import os
from getmac import get_mac_address


def do_popup(event): 
    try: 
        m.tk_popup(event.x_root, event.y_root) 
    finally: 
        m.grab_release()


WIDTH = 700
HEIGHT = 700

root = tk.Tk()
computer_name = os.environ['COMPUTERNAME']
copy_text = computer_name
m = tk.Menu(root, tearoff = 0) 

wifi_host_mac = get_mac_address(interface="Wi-Fi")
ethernet_host_mac = get_mac_address(interface="Ethernet")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#ffffff')
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

label_for_computer_name = tk.Label(frame, text="Nazwa Komputera", bg="#ffcccc", font=("Sans", 30))
label_for_computer_name.place(relx=0.5, rely=0.11, anchor="center")

computer_name_text = tk.Label(frame, text=computer_name, bg="#FFFFFF", font=("Sans", 30))
computer_name_text.place(relx=0.5, rely=0.2, anchor="center")

if isinstance(wifi_host_mac, str):

    label_for_wifi = tk.Label(frame, text="Wi-Fi", bg="#03dac5", font=("Sans", 30))
    label_for_wifi.place(relx=0.5, rely=0.31, anchor="center")

    wifi_mac_address_text = tk.Label(frame, text=wifi_host_mac, bg="#FFFFFF", font=("Sans", 30))
    wifi_mac_address_text.place(relx=0.5, rely=0.4, anchor="center")
    copy_text+=" wifi : "+wifi_host_mac+" "
if isinstance(ethernet_host_mac, str):

    label_for_ethernet = tk.Label(frame, text="Kabel", bg="#6200ee", font=("Sans", 30))
    label_for_ethernet.place(relx=0.5, rely=0.51, anchor="center")

    ethernet_mac_address_text = tk.Label(frame, text=ethernet_host_mac, bg="#FFFFFF", font=("Sans", 30))
    ethernet_mac_address_text.place(relx=0.5, rely=0.6, anchor="center")
    copy_text+=" ethernet : "+ethernet_host_mac+" "


m.add_command(label ="Copy", command=root.clipboard_append(copy_text))
frame.bind("<Button-3>", do_popup) 

root.mainloop()

