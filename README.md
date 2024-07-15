# fx_wspaces
A quick an easy to use workspace selector

This tool was made in python for linux

Tested on Arch and debian based distros

tool on workspace 1 
![2024-07-15-063216_1366x768_scrot](https://github.com/user-attachments/assets/83ba2625-e145-4102-8c17-125ff0616e3c)

tool on workspace 2
![2024-07-15-064443_1366x768_scrot](https://github.com/user-attachments/assets/8db59dfc-b7ff-471d-b03a-7a28156195b7)

# if you have a tilling wm like i3 follow these steps: exaple on i3

#you can change the: $mod+Shift+w

#if you changed the 'app_title=fx_wspaces' on the fx_wspaces.config you also need to change the "[title="fx_wspaces$"]" on the i3 config
#--------------------------------------------------------------------------------------------------------------------------------------#

go to your i3 config file and add these lines on bottom: 

bindsym $mod+Shift+w exec /bin/python PATH TO fx_wspaces.py

for_window [title="fx_wspaces$"] floating enable

then save the config file and run the program

For further info about the i3 config go to the official documentation: https://i3wm.org/docs/userguide.html
