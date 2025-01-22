import tkinter as tk
import button_functions as fnc


ix_wind = tk.Tk()
ix_wind.title("Pydio Player")
ix_wind.geometry("600x200")
ix_wind.resizable(False, False)
ix_wind.configure(background="light green")

#
# button frame for play buttons
#

button_frame = tk.Frame(ix_wind)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)
button_frame.columnconfigure(3, weight=1)

play_btn = tk.Button(button_frame, text="| >", font=('Ink Free', 14, 'bold'), bg="black", fg="light green",
                     command= lambda: fnc.play_btn_fnc(play_btn, pause_btn))
play_btn.grid(row=0, column=0, sticky="we")

pause_btn = tk.Button(button_frame, text="||", font=('Ink Free', 14, 'bold'), bg="black", fg="light green",
                      command= lambda: fnc.pause_btn_fnc(play_btn, pause_btn))
pause_btn.grid(row=0, column=1, sticky="we")

next_btn = tk.Button(button_frame, text=">>", font=('Ink Free', 14, 'bold'), bg="black", fg="light green", command=fnc.next_btn_fnc)
next_btn.grid(row=0, column=2, sticky="we")

prev_btn = tk.Button(button_frame, text="<<", font=('Ink Free', 14, 'bold'), bg="black", fg="light green", command=fnc.prev_btn_fnc)
prev_btn.grid(row=0, column=3, sticky="we")

button_frame.pack(padx=10, pady=10, fill='x')
button_frame.configure(background="light green")

#
# button frame for options buttons
#

option_frame = tk.Frame(ix_wind)
option_frame.columnconfigure(0, weight=1)
option_frame.columnconfigure(1, weight=1)
option_frame.columnconfigure(2, weight=1)

open_btn = tk.Button(option_frame, text="Open File(s)", font=('Ink Free', 13, 'bold'), bg="black", fg="light green",
                     command= lambda: fnc.open_btn_fnc(play_btn))
open_btn.grid(row=0, column=0, sticky="we", padx=10)

rand_btn = tk.Button(option_frame, text="Shuffle", font=('Ink Free', 13, 'bold'), bg="black", fg="light green", command= lambda: fnc.rand_btn_fnc(rand_btn))
rand_btn.grid(row=0, column=1, sticky="we", padx=10)

loop_btn = tk.Button(option_frame, text="Loop", font=('Ink Free', 13, 'bold'), bg="black", fg="light green", command= lambda: fnc.loop_btn_fnc(loop_btn))
loop_btn.grid(row=0, column=2, sticky="we", padx=10)

option_frame.pack(padx=10, pady=10, fill='x')
option_frame.configure(background="light green")

#
# reworked volume frame
#

hz_vol_frame = tk.Frame(ix_wind)
hz_vol_frame.columnconfigure(0, weight=1)
hz_vol_frame.columnconfigure(1, weight=1)
hz_vol_frame.columnconfigure(2, weight=1)
hz_vol_frame.columnconfigure(3, weight=1)
hz_vol_frame.columnconfigure(4, weight=1)
hz_vol_frame.columnconfigure(5, weight=1)
hz_vol_frame.columnconfigure(6, weight=1)

vbtn_p10 = tk.Button(hz_vol_frame, text="+10", font=('Ink Free', 12, 'bold'), bg="black", fg="light green",
                        command=lambda: fnc.vol_fnc(0.1, vol_label))
vbtn_p10.grid(row=0, column=6, sticky="we", padx=2, pady=5)

vbtn_p5 = tk.Button(hz_vol_frame, text="+5", font=('Ink Free', 12, 'bold'), bg="black", fg="light green",
                       command=lambda: fnc.vol_fnc(0.05, vol_label))
vbtn_p5.grid(row=0, column=5, sticky="we", padx=2, pady=5)

vbtn_p1 = tk.Button(hz_vol_frame, text="+1", font=('Ink Free', 12, 'bold'), bg="black", fg="light green",
                       command= lambda: fnc.vol_fnc(0.01, vol_label))
vbtn_p1.grid(row=0, column=4, sticky="we", padx=2, pady=5)

vol_label=tk.Label(hz_vol_frame, text="Volume", font=('Ink Free', 14, 'bold'))
vol_label.grid(row=0, column=3, sticky="we", padx=2, pady=5)
vol_label.configure(background="light green")

vbtn_m1 = tk.Button(hz_vol_frame, text="-1", font=('Ink Free', 12, 'bold'), bg="black", fg="light green",
                       command=lambda: fnc.vol_fnc(-0.01, vol_label))
vbtn_m1.grid(row=0, column=2, sticky="we", padx=2, pady=5)

vbtn_m5 = tk.Button(hz_vol_frame, text="-5", font=('Ink Free', 12, 'bold'), bg="black", fg="light green",
                       command=lambda: fnc.vol_fnc(-0.05, vol_label))
vbtn_m5.grid(row=0, column=1, sticky="we", padx=2, pady=5)

vbtn_m10 = tk.Button(hz_vol_frame, text="-10", font=('Ink Free', 12, 'bold'), bg="black", fg="light green",
                        command=lambda: fnc.vol_fnc(-0.1, vol_label))
vbtn_m10.grid(row=0, column=0, sticky="we", padx=2, pady=5)

hz_vol_frame.pack(padx=10, pady=10, fill='x')
hz_vol_frame.configure(background="light green")

ix_wind.mainloop()