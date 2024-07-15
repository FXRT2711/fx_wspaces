#creator: Fxrt2711
#version: 1.0
#date: 15/07/24
#
try:
    import os
except:
    print("Main lib missing: 'os' \n install it with: 'pip install os'")
    exit()
#
try:
    from time import sleep
except:
    time_c = input("Lib missing: 'time' \n do you want to install it? (y/n): ")
    if time_c == "y" or "Y":
        os.system("pip install time")
#
try:
    import customtkinter as ctk
except:
    customtkinter_c = input("Lib missing: 'customtkinter' \n do you want to install it? (y/n): ")
    if customtkinter_c == "y" or "Y":
        os.system("pip install customtkinter")
#
try:
    import tkinter as tk
except:
    tkinter_c = input("Lib missing: 'tkinter' \n do you want to install it? (y/n): ")
    if tkinter_c == "y" or "Y":
        os.system("pip install tkinter")
#
try:
    import pyautogui
except:
    pagui_c = input("Lib missing: 'pyautogui' \n do you want to install it? (y/n): ")
    if pagui_c == "y" or "Y":
        os.system("pip install pyautogui")
#
#
#config_file
user = os.popen("echo $USER")
user = user.read()
user = user.replace('\n', '')
#
conf_ex = 0
conf_list = []
#
#
try:
    config_file = open(f'/home/{user}/.config/fx_wspace/fx_wspace.conf', 'r+') 
    print("config exist \n")
    conf_ex = 1
except:
    print("did not find config file...")
    sleep(0.5)
    print("creating config file...")
    os.system(f"mkdir /home/$USER/.config/fx_wspace")
    os.system(f"cp /fx_wspace.conf /home/$USER/.config/fx_wspace/")
    print("config file created...")
    sleep(0.5)
    print("please restart...")
    exit()
#
#
for data in config_file:
    conf_list.append(data.replace('\n' , ''))
print (conf_list)
#
#
theme_start = "theme="
x_start = "width="
y_start = "height="
app_title_start = "app_title="
bg_color_start = "bg_color="
text_color_start = "text_color="
main_ws_color_start = "main_ws_color="
other_ws_volor_start = "other_ws_volor="
#
#
#
for i in range(len(conf_list)):
    if conf_list[i].startswith(theme_start):
        theme = conf_list[i]
        theme = theme.replace(theme_start,'')
#
for i in range(len(conf_list)):
    if conf_list[i].startswith(x_start):
        x = conf_list[i]
        x = x.replace(x_start,'')
#
for i in range(len(conf_list)):
    if conf_list[i].startswith(y_start):
        y = conf_list[i]
        y = y.replace(y_start,'')
#
for i in range(len(conf_list)):
    if conf_list[i].startswith(app_title_start):
        app_title = conf_list[i]
        app_title = app_title.replace(app_title_start,'')
#
for i in range(len(conf_list)):
    if conf_list[i].startswith(bg_color_start):
         bg_c = conf_list[i]
         bg_c = bg_c.replace(bg_color_start,'')
         if bg_c == 'tp':
            bg_c = 'transparent'
#
for i in range(len(conf_list)):
    if conf_list[i].startswith(text_color_start):
         text_c = conf_list[i]
         text_c = text_c.replace(text_color_start,'')
         if text_c == 'tp':
            text_c = 'transparent'
#
for i in range(len(conf_list)):
    if conf_list[i].startswith(main_ws_color_start):
         main_ws_c = conf_list[i]
         main_ws_c = main_ws_c.replace(main_ws_color_start,'')
         if main_ws_c == 'tp':
            main_ws_c = 'transparent'
#
for i in range(len(conf_list)):
    if conf_list[i].startswith(other_ws_volor_start):
         other_ws_c = conf_list[i]
         other_ws_c = other_ws_c.replace(other_ws_volor_start,'')
         if other_ws_c == 'tp':
            other_ws_c = 'transparent'
#
print(theme)
print(x)
print(y)
print(app_title)
print(bg_c)
print(text_c)
print(main_ws_c)
print(other_ws_c)
#
ctk.set_appearance_mode(theme)
ctk.set_default_color_theme("dark-blue")
#
#
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
#
        cws = os.popen("xprop -root -notype _NET_CURRENT_DESKTOP")
        cws = cws.read()
        cws = cws.replace('\n','')
        cws = int(cws.replace('_NET_CURRENT_DESKTOP = ',''))
#
#        
#
        self.title(app_title)
        self.geometry(f"{int(x)}x{int(y)}")
#
        def go_to_f():
            pyautogui.hotkey('win',f"{cws}")
            exit()
#
        def go_to_s():
            pyautogui.hotkey('win',f"{cws + 1}")
#            
        def go_to_t():
            pyautogui.hotkey('win',f"{cws + 2}")
            exit()
#       
        self.nothing = ctk.CTkLabel(self,text="")
        self.nothing.grid(row=0, column=0,padx=17, pady=int(y) / 2 - 100,sticky="ew")
#
        self.nothing2 = ctk.CTkLabel(self,text="")
        if cws + 1 == 1:
            self.nothing2.grid(row=0, column=0,padx=110, pady=int(y) / 2 - 100,sticky="ew")
#
        self.back_ws = ctk.CTkButton(self,text=cws,font=("Arial", 150),fg_color=bg_c,text_color=other_ws_c,command=go_to_f)
#
        if cws + 1 != 1:
            self.back_ws.grid(row=0, column=cws + 1,padx=int(x) / 8 - 75, pady=int(y) / 2 - 100,sticky="ew")
#        
#
        self.current_ws = ctk.CTkButton(self,text=cws + 1,font=("Arial", 200),fg_color=bg_c,text_color=main_ws_c,command=go_to_s)
        self.current_ws.grid(row=0, column=cws + 2,padx=int(x) / 8, pady=int(y) / 2 - 100,sticky="ew")
#       
#
        self.next_ws = ctk.CTkButton(self,text=cws + 2,font=("Arial", 150),fg_color=bg_c,text_color=other_ws_c,command=go_to_t)
        self.next_ws.grid(row=0, column=cws + 3,padx=int(x) / 8 - 75,pady=int(y) / 2 - 100,sticky="ew")
#        
if __name__ == "__main__":
	app = App()
	app.mainloop()
