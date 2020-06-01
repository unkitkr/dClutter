import os
import engine

try:
    import Tkinter as tk
    from Tkinter import StringVar
except ImportError:
    import tkinter as tk
    from tkinter import StringVar

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import ClutterUI_support



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    ClutterUI_support.init(root, top)
    root.overrideredirect(True)
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='favico.png'))
    root.mainloop()
    
    

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    ClutterUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

xwin = 0
ywin = 0

def get_pos(event):
    global xwin, ywin
    xwin = root.winfo_x()
    ywin = root.winfo_y()
    startx = event.x_root
    starty = event.y_root

    ywin = ywin - starty
    xwin = xwin - startx


def move_window(event):
    global xwin, ywin
    root.geometry("739x475" + '+{0}+{1}'.format(event.x_root + xwin, event.y_root + ywin))
    startx = event.x_root
    starty = event.y_root

class Toplevel1:

    #Window Minimizer Function
    def min_win(self):
        root.update_idletasks()
        root.overrideredirect(False)
        root.iconify()

    def frame_mapped(self,e):
        root.update_idletasks()
        root.overrideredirect(True)
        root.state('normal')
      

    #Window Annimation Functions    
    def close_on_enter(self,e):
        self.close_btn.configure(background = "#E81123")
    def close_on_leave(self,e):
        self.close_btn.configure(background = "#221F2E")
    
    def min_on_enter(self,e):
        self.min_btn.configure(background = "#2F2B3F")
    def min_on_leave(self,e):
        self.min_btn.configure(background = "#221F2E")


    # Functions for tab switch

    def initialize(self):
        self.menuplane.place_forget()
        self.cleanbtn.place_forget()
        self.actionsplane.place_forget()
        self.settingsplane.place_forget()
        

    def click_menu(self):
        self.menuplane.place(relx=0.101, rely=0.074, relheight=0.926
                , relwidth=0.9)
        self.pointer.place(rely = 0.177*2)
        self.homeplane.place_forget()
        self.actionsplane.place_forget()
        self.settingsplane.place_forget()

    def click_home(self):
        self.menuplane.place_forget()
        self.pointer.place(rely = 0.177*1)
        self.homeplane.place(relx=0.101, rely=0.074, relheight=0.926
                , relwidth=0.9)
        self.actionsplane.place_forget()
        self.settingsplane.place_forget()

    def click_action(self):
        self.homeplane.place_forget()
        self.menuplane.place_forget()
        self.actionsplane.place(relx=0.101, rely=0.074, relheight=0.926
                , relwidth=0.9)
        self.pointer.place(rely = 0.177*3)
        self.settingsplane.place_forget()

    def click_settings(self):
        self.homeplane.place_forget()
        self.menuplane.place_forget()
        self.actionsplane.place_forget()
        self.settingsplane.place(relx=0.101, rely=0.074, relheight=0.926
                , relwidth=0.9)
        self.pointer.place(rely = 0.177*4 )


        


    #Functions for utility

    def load_locations(self):
        locs = engine.load_paths()
        self.dladdrfront.delete('1.0', "end")
        self.dladdrfront.insert('end',locs[0])
        self.otaddrfront.delete("1.0","end")
        self.otaddrfront.insert('end',locs[1])
        




    def system_info(self):
        #call to engine for system_details
        ''' sinfo holds all the required system details '''
        sinfo = engine.system_details()
        ram_percent = (sinfo[8]/100)*255
        memory_percent = (sinfo[7]/100)*255
        osname = sinfo[0]
        processor = sinfo[1]
        node = sinfo[2]
        used_ram = round(sinfo[4],2)
        used_hdd = round(sinfo[6],2)
        free_ram = round(sinfo[3]-used_ram,2)
        free_hdd = round(sinfo[5]-used_hdd,2)

        self.ramfront.configure(width = ram_percent)
        self.hddfront.configure(width = memory_percent)
        self.osnamelbl.configure(text = osname)
        self.processorlbl.configure(text = processor)
        self.nodelbl.configure(text = node)
        self.ramusedstlbl.configure(text = str(used_ram)+" "+"GB")
        self.hddusedstlbl.configure(text = str(used_hdd)+" "+"GB")
        self.ramfreestlbl.configure(text = str(free_ram)+" "+"GB")
        self.hddfreestlbl.configure(text = str(free_hdd)+" "+"GB")
    
    def clutter_info(self):
        status = engine.download_clutter_counter()
        percentages = status[0]
        actual = status[1]

        fill_percentages = []
        for x in percentages:
            per = (x/100)*75
            if per < 1:
                per = 1
            fill_percentages.append(per)

        self.totimage.configure(text = actual[1])
        self.totaudio.configure(text = actual[4])
        self.totdocs.configure(text = actual[2])
        self.totarchive.configure(text = actual[5])
        self.totothers.configure(text = actual[6])
        self.totvideos.configure(text = actual[3])
        self.totalflst.configure(text = actual[0])

        self.audiofront.configure(width = fill_percentages[3])
        self.vidfront.configure(width = fill_percentages[2])
        self.docsfront.configure(width = fill_percentages[1])
        self.archivefront.configure(width = fill_percentages[4])
        self.othersfront.configure(width = fill_percentages[5])
        self.imgfront.configure(width= fill_percentages[0])
        self.total_download_files = actual[0]
        # For total files in menu plane

        self.cltrsizelbl_2.configure(text = actual[0] )



    def clutter_size_info(self):
        self.total_download_size = engine.clutter_size(engine.get_download_path())
        if self.total_download_size> int(self.total_download_size):
            self.cltrsizelbl.configure(text = int(self.total_download_size))

    def status_changer(self):
        if self.total_download_files > 5 and self.total_download_files < 20:
            self._img90 = tk.PhotoImage(file="statusattn.png")
            self.statuslbl.configure(image=self._img90)
            self.statusdesclbl.configure(text = 'Your Downloads folder looks medley.')
            self.statusdesclb2.configure(text = 'Actions are recommended')
            self.cleanbtn.place(relx=0.406, rely=0.67, height=33, width=106)
            self.cleanbtn.configure(background="#FFC107")
            self.cleanbtn.configure(activebackground="#FFC107")
        elif self.total_download_files> 20:
            self._img90 = tk.PhotoImage(file="statusurgent.png")
            self.statuslbl.configure(image=self._img90)
            self.statusdesclbl.configure(text = 'Your Downloads folder is a chaos.')
            self.statusdesclb2.configure(text = 'Immediate actions are Required')
            self.cleanbtn.place(relx=0.406, rely=0.67, height=33, width=106)
            self.cleanbtn.configure(background="#D61425")
            self.cleanbtn.configure(activebackground="#D61425")

    

    def browse_location(self):
        from tkinter import filedialog
        self.fldrloc = filedialog.askdirectory(initialdir = "C:")
        self.addrfront.delete('1.0', "end")
        self.addrfront.insert('end', self.fldrloc)
        print(self.fldrloc)


    def browse_download_path(self):
        from tkinter import filedialog
        self.fldrloc = filedialog.askdirectory(initialdir = "C:")
        self.dladdrfront.delete('1.0', "end")
        self.dladdrfront.insert('end', self.fldrloc)   


    def browse_others_path(self):

        from tkinter import filedialog
        self.fldrloc = filedialog.askdirectory(initialdir = "C:")
        self.otaddrfront.delete('1.0', "end")
        self.otaddrfront.insert('end', self.fldrloc)  

    def save_create_locs(self):
        dpath= self.dladdrfront.get('1.0', "end").strip()
        opath = self.otaddrfront.get('1.0', "end").strip()
        engine.save_download_path(dpath,opath)
        print(dpath)
        print(engine.create_space_download(dpath))
        print(engine.create_space_others(opath))

    def scan_folder(self):
        paths = self.addrfront.get("1.0","end").strip()
        paths = os.path.normpath(paths)
        
        details = engine.seperate_file_folder(paths)
        size = engine.clutter_size(paths)
        self.clutter_files_fldr.configure(text = details[1][0])
        self.clutter_size_fldr.configure(text = round(size,2))
        self.hiderframe.place_forget()
        self.movingdesc.place_forget()

    def clear_scan_folder(self):
        paths = self.addrfront.get("1.0","end").strip()
        paths = os.path.normpath(paths)
        task_progress = engine.move_clutter('others')
        self.movingdesc.place(relx=0.270, rely=0.886, height=36, width=300)
        moved_counter = 0 
        for m in task_progress:
            self.movingdesc.config(text = m)
            self.movingdesc.update()
            moved_counter += 1
            all_file_sum = len(engine.images)+len(engine.documents)+len(engine.audios)+len(engine.videos)+len(engine.archives)+len(engine.others)
            status_len = (moved_counter/all_file_sum)*665
            self.copy_status.configure(width = status_len)

    def clear_download_folder(self):
        task_progress = engine.move_clutter('downloads')
        moved_counter = 0
        for x in task_progress:
            moved_counter += 1
            all_file_sum = len(engine.images)+len(engine.documents)+len(engine.audios)+len(engine.videos)+len(engine.archives)+len(engine.others)
            status_len = (moved_counter/all_file_sum)*655
            self.copy_status_download.configure(width = status_len)



      
     

    # onload function. This must start as the app starts

    def on_load(self):
        self.initialize()
        self.system_info()
        self.clutter_info()
        self.clutter_size_info()
        self.status_changer()
        self.load_locations()
        

   

    def __init__(self, top=None):


        # Initialized variables in constructor, to be used in the toplevel class.

        self.total_download_size = 0
        self.total_download_files = 0
        self.fldrloc = " "

        # Variables ends here.

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        font11 = "-family Arial -size 20 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 10 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Segoe UI} -size 11 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font15 = "-family {Segoe UI} -size 11 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Segoe UI} -size 8 -weight bold -slant roman"  \
        " -underline 0 -overstrike 0"
        font17 = "-family {Segoe UI} -size 8 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font18 = "-family {Segoe UI} -size 30 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font19 = "-family {Segoe UI} -size 11 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font20 = "-family {Segoe UI} -size 20 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        font21 = "-family {Segoe UI} -size 14 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font22 = "-family {Segoe UI} -size 9 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"



        top.geometry("739x475+531+337")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.current_user_name = os.getenv("username")

        self.sidebar = tk.Frame(top)
        self.sidebar.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=0.101)
        self.sidebar.configure(relief='flat')
        self.sidebar.configure(borderwidth="2")
        self.sidebar.configure(background="#2F2B3F")
        self.sidebar.configure(highlightbackground="#d9d9d9")
        self.sidebar.configure(highlightcolor="black")
        self.sidebar.configure(width=75)

        self.logo = tk.Label(self.sidebar)
        self.logo.place(relx=0, rely=0, height=75, width= 75)
        self.logo.configure(activebackground="#f9f9f9")
        self.logo.configure(activeforeground="black")
        self.logo.configure(background="#2F2B3F")
        self.logo.configure(borderwidth="0")
        self.logo.configure(disabledforeground="#a3a3a3")
        self.logo.configure(foreground="#000000")
        self.logo.configure(highlightbackground="#d9d9d9")
        self.logo.configure(highlightcolor="black")
        self._img79 = tk.PhotoImage(file="./dclutter logo prd.png")
        self.logo.configure(image=self._img79)
        self.logo.configure(text='''Label''')

        self.Button2 = tk.Button(self.sidebar)
        self.Button2.place(relx=0.133, rely=0.177, height=66, width=66)
        self.Button2.configure(activebackground="#2F2B3F")
        self.Button2.configure(activeforeground="white")
        self.Button2.configure(activeforeground="#2F2B3F")
        self.Button2.configure(background="#2F2B3F")
        self.Button2.configure(borderwidth="0")
        self.Button2.configure(cursor="hand2")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(highlightthickness="0")
        self._img1 = tk.PhotoImage(file="./hometab.png")
        self.Button2.configure(image=self._img1)
        self.Button2.configure(padx="0")
        self.Button2.configure(pady="0")
        self.Button2.configure(relief='flat')
        self.Button2.configure(text='''Button''')
        self.Button2.configure(command = self.click_home)

        self.menu = tk.Button(self.sidebar)
        self.menu.place(relx=0.133, rely=0.177*2, height=66, width=66)
        self.menu.configure(activebackground="#2F2B3F")
        self.menu.configure(activeforeground="white")
        self.menu.configure(activeforeground="#2F2B3F")
        self.menu.configure(background="#2F2B3F")
        self.menu.configure(borderwidth="0")
        self.menu.configure(cursor="hand2")
        self.menu.configure(disabledforeground="#a3a3a3")
        self.menu.configure(foreground="#000000")
        self.menu.configure(highlightbackground="#d9d9d9")
        self.menu.configure(highlightcolor="black")
        self.menu.configure(highlightthickness="0")
        self._img2 = tk.PhotoImage(file="./menu.png")
        self.menu.configure(image=self._img2)
        self.menu.configure(padx="0")
        self.menu.configure(pady="0")
        self.menu.configure(relief='flat')
        self.menu.configure(text='''Button''')
        self.menu.configure(command = self.click_menu)

        self.options = tk.Button(self.sidebar)
        self.options.place(relx=0.133, rely=0.177*3, height=66, width=66)
        self.options.configure(activebackground="#2F2B3F")
        self.options.configure(activeforeground="white")
        self.options.configure(activeforeground="#2F2B3F")
        self.options.configure(background="#2F2B3F")
        self.options.configure(borderwidth="0")
        self.options.configure(cursor="hand2")
        self.options.configure(disabledforeground="#a3a3a3")
        self.options.configure(foreground="#000000")
        self.options.configure(highlightbackground="#d9d9d9")
        self.options.configure(highlightcolor="black")
        self.options.configure(highlightthickness="0")
        self._img3 = tk.PhotoImage(file="./optn.png")
        self.options.configure(image=self._img3)
        self.options.configure(padx="0")
        self.options.configure(pady="0")
        self.options.configure(relief='flat')
        self.options.configure(text='''Button''')
        self.options.configure(command = self.click_action)

        self.settings = tk.Button(self.sidebar)
        self.settings.place(relx=0.133, rely=0.177*4, height=66, width=66)
        self.settings.configure(activebackground="#2F2B3F")
        self.settings.configure(activeforeground="white")
        self.settings.configure(activeforeground="#2F2B3F")
        self.settings.configure(background="#2F2B3F")
        self.settings.configure(borderwidth="0")
        self.settings.configure(cursor="hand2")
        self.settings.configure(disabledforeground="#a3a3a3")
        self.settings.configure(foreground="#000000")
        self.settings.configure(highlightbackground="#d9d9d9")
        self.settings.configure(highlightcolor="black")
        self.settings.configure(highlightthickness="0")
        self._img4 = tk.PhotoImage(file="./settings.png")
        self.settings.configure(image=self._img4)
        self.settings.configure(padx="0")
        self.settings.configure(pady="0")
        self.settings.configure(relief='flat')
        self.settings.configure(text='''Button''')
        self.settings.configure(command = self.click_settings)
        

        self.pointer = tk.Frame(self.sidebar)
        self.pointer.place(relx=-0.067, rely=0.177, relheight=0.147
                , relwidth=0.107)
        self.pointer.configure(relief='flat')
        self.pointer.configure(borderwidth="0")
        self.pointer.configure(background="#C237B6")
        self.pointer.configure(highlightbackground="#d9d9d9")
        self.pointer.configure(highlightcolor="black")
        self.pointer.configure(width=15)
        
        # HomePlane starts here

        self.homeplane = tk.Frame(top)
        self.homeplane.place(relx=0.101, rely=0.074, relheight=0.926
                , relwidth=0.9)
        self.homeplane.configure(relief='flat')
        self.homeplane.configure(borderwidth="2")
        self.homeplane.configure(background="#221F2E")
        self.homeplane.configure(highlightbackground="#d9d9d9")
        self.homeplane.configure(highlightcolor="black")
        self.homeplane.configure(width=665)

        self.ovrvw = tk.Label(self.homeplane)
        self.ovrvw.place(relx=0.015, rely=0.0, height=16, width=92)
        self.ovrvw.configure(activebackground="#f9f9f9")
        self.ovrvw.configure(activeforeground="black")
        self.ovrvw.configure(background="#221F2E")
        self.ovrvw.configure(borderwidth="0")
        self.ovrvw.configure(disabledforeground="#a3a3a3")
        self.ovrvw.configure(font=font12)
        self.ovrvw.configure(foreground="#ffffff")
        self.ovrvw.configure(highlightbackground="#d9d9d9")
        self.ovrvw.configure(highlightcolor="black")
        self.ovrvw.configure(text='''Overview>''')

        self.lblhello = tk.Label(self.homeplane)
        self.lblhello.place(relx=0.015, rely=0.045, height=36, width=91)
        self.lblhello.configure(activebackground="#f9f9f9")
        self.lblhello.configure(activeforeground="black")
        self.lblhello.configure(background="#221F2E")
        self.lblhello.configure(disabledforeground="#a3a3a3")
        self.lblhello.configure(font=font11)
        self.lblhello.configure(foreground="#AC5CD9")
        self.lblhello.configure(highlightbackground="#d9d9d9")
        self.lblhello.configure(highlightcolor="black")
        self.lblhello.configure(justify='left')
        self.lblhello.configure(text='''Hello''')

        self.lblusername = tk.Label(self.homeplane)
        self.lblusername.place(relx=0.145, rely=0.045, height=36, width=241)
        self.lblusername.configure(activebackground="#f9f9f9")
        self.lblusername.configure(activeforeground="black")
        self.lblusername.configure(background="#221F2E")
        self.lblusername.configure(disabledforeground="#a3a3a3")
        self.lblusername.configure(font=font11)
        self.lblusername.configure(foreground="#DEA5E8")
        self.lblusername.configure(highlightbackground="#d9d9d9")
        self.lblusername.configure(highlightcolor="black")
        self.lblusername.configure(justify='left', anchor="w")
        self.lblusername.configure(width=241)
        self.lblusername.configure(text = self.current_user_name + " !")

        self.currdate = tk.Label(self.homeplane)
        self.currdate.place(relx= .028, rely=0.120, height=16, width=100)
        self.currdate.configure(activebackground="#f9f9f9")
        self.currdate.configure(activeforeground="black")
        self.currdate.configure(background="#221F2E")
        self.currdate.configure(borderwidth="0")
        self.currdate.configure(disabledforeground="#a3a3a3")
        self.currdate.configure(font=font13)
        self.currdate.configure(foreground="#ffffff")
        self.currdate.configure(highlightbackground="#d9d9d9")
        self.currdate.configure(highlightcolor="black")
        self.currdate.configure(justify='left')
        self.currdate.configure(text = engine.get_formatted_date())

        self.sysinfo = tk.Frame(self.homeplane)
        self.sysinfo.place(relx=0.03, rely=0.205, relheight=0.352
                , relwidth=0.504)
        self.sysinfo.configure(relief='flat')
        self.sysinfo.configure(borderwidth="2")
        self.sysinfo.configure(background="#2F2B3F")
        self.sysinfo.configure(width=335)

        self.sysinfolbl = tk.Label(self.sysinfo)
        self.sysinfolbl.place(relx=-0.015, rely=0.0, height=26, width=162)
        self.sysinfolbl.configure(activebackground="#2F2B3F")
        self.sysinfolbl.configure(activeforeground="white")
        self.sysinfolbl.configure(activeforeground="black")
        self.sysinfolbl.configure(background="#2F2B3F")
        self.sysinfolbl.configure(borderwidth="0")
        self.sysinfolbl.configure(disabledforeground="#a3a3a3")
        self.sysinfolbl.configure(font=font12)
        self.sysinfolbl.configure(foreground="#d9d9d9")
        self.sysinfolbl.configure(highlightbackground="#dbdbdb")
        self.sysinfolbl.configure(highlightcolor="black")
        self.sysinfolbl.configure(text='''System Information''')

        self.osico = tk.Label(self.sysinfo)
        self.osico.place(relx=0.03, rely=0.194, height=36, width=32)
        self.osico.configure(activebackground="#2F2B3F")
        self.osico.configure(activeforeground="white")
        self.osico.configure(activeforeground="black")
        self.osico.configure(background="#2F2B3F")
        self.osico.configure(borderwidth="0")
        self.osico.configure(disabledforeground="#a3a3a3")
        self.osico.configure(font=font12)
        self.osico.configure(foreground="#d9d9d9")
        self.osico.configure(highlightbackground="#dbdbdb")
        self.osico.configure(highlightcolor="black")
        self._img98 = tk.PhotoImage(file="os.png")
        self.osico.configure(image=self._img98)
        self.osico.configure(width=32)

        self.processorico = tk.Label(self.sysinfo)
        self.processorico.place(relx=0.03, rely=0.452, height=36, width=32)
        self.processorico.configure(activebackground="#2F2B3F")
        self.processorico.configure(activeforeground="white")
        self.processorico.configure(activeforeground="black")
        self.processorico.configure(background="#2F2B3F")
        self.processorico.configure(borderwidth="0")
        self.processorico.configure(disabledforeground="#a3a3a3")
        self.processorico.configure(font=font12)
        self.processorico.configure(foreground="#d9d9d9")
        self.processorico.configure(highlightbackground="#dbdbdb")
        self.processorico.configure(highlightcolor="black")
        self._img99 = tk.PhotoImage(file="processor.png")
        self.processorico.configure(image=self._img99)

        self.nodeico = tk.Label(self.sysinfo)
        self.nodeico.place(relx=0.03, rely=0.71, height=36, width=32)
        self.nodeico.configure(activebackground="#2F2B3F")
        self.nodeico.configure(activeforeground="white")
        self.nodeico.configure(activeforeground="black")
        self.nodeico.configure(background="#2F2B3F")
        self.nodeico.configure(borderwidth="0")
        self.nodeico.configure(disabledforeground="#a3a3a3")
        self.nodeico.configure(font=font12)
        self.nodeico.configure(foreground="#d9d9d9")
        self.nodeico.configure(highlightbackground="#dbdbdb")
        self.nodeico.configure(highlightcolor="black")
        self._img7 = tk.PhotoImage(file="node.png")
        self.nodeico.configure(image=self._img7)


        self.osnamelbl = tk.Label(self.sysinfo)
        self.osnamelbl.place(relx=0.149, rely=0.21, height=26, width=232)
        self.osnamelbl.configure(activebackground="#2F2B3F")
        self.osnamelbl.configure(activeforeground="white")
        self.osnamelbl.configure(activeforeground="black")
        self.osnamelbl.configure(background="#2F2B3F")
        self.osnamelbl.configure(borderwidth="0")
        self.osnamelbl.configure(disabledforeground="#a3a3a3")
        self.osnamelbl.configure(font=font15)
        self.osnamelbl.configure(foreground="#d9d9d9")
        self.osnamelbl.configure(highlightbackground="#dbdbdb")
        self.osnamelbl.configure(highlightcolor="black")
        self.osnamelbl.configure(anchor = 'w')
        self.osnamelbl.configure(width=232)

        self.processorlbl = tk.Label(self.sysinfo)
        self.processorlbl.place(relx=0.149, rely=0.48, height=26, width=272)
        self.processorlbl.configure(activebackground="#2F2B3F")
        self.processorlbl.configure(activeforeground="white")
        self.processorlbl.configure(activeforeground="black")
        self.processorlbl.configure(background="#2F2B3F")
        self.processorlbl.configure(borderwidth="0")
        self.processorlbl.configure(disabledforeground="#a3a3a3")
        self.processorlbl.configure(font=font9)
        self.processorlbl.configure(foreground="#d9d9d9")
        self.processorlbl.configure(highlightbackground="#dbdbdb")
        self.processorlbl.configure(highlightcolor="black")
        self.processorlbl.configure(anchor = 'w')
        self.processorlbl.configure(width=272)

        self.nodelbl = tk.Label(self.sysinfo)
        self.nodelbl.place(relx=0.149, rely=0.745, height=26, width=272)
        self.nodelbl.configure(activebackground="#2F2B3F")
        self.nodelbl.configure(activeforeground="white")
        self.nodelbl.configure(activeforeground="black")
        self.nodelbl.configure(background="#2F2B3F")
        self.nodelbl.configure(borderwidth="0")
        self.nodelbl.configure(disabledforeground="#a3a3a3")
        self.nodelbl.configure(font=font15)
        self.nodelbl.configure(foreground="#d9d9d9")
        self.nodelbl.configure(highlightbackground="#dbdbdb")
        self.nodelbl.configure(highlightcolor="black")
        self.nodelbl.configure(anchor = 'w')


        self.tabinfo = tk.Frame(self.homeplane)
        self.tabinfo.place(relx=0.03, rely=0.591, relheight=0.364
                , relwidth=0.504)
        self.tabinfo.configure(relief='flat')
        self.tabinfo.configure(borderwidth="2")
        self.tabinfo.configure(background="#2F2B3F")
        self.tabinfo.configure(highlightbackground="#d9d9d9")
        self.tabinfo.configure(highlightcolor="black")
        self.tabinfo.configure(width=335)

        self.meminfolbl = tk.Label(self.tabinfo)
        self.meminfolbl.place(relx=-0.015, rely=0.0, height=26, width=172)
        self.meminfolbl.configure(activebackground="#2F2B3F")
        self.meminfolbl.configure(activeforeground="white")
        self.meminfolbl.configure(activeforeground="black")
        self.meminfolbl.configure(background="#2F2B3F")
        self.meminfolbl.configure(borderwidth="0")
        self.meminfolbl.configure(disabledforeground="#a3a3a3")
        self.meminfolbl.configure(font=font12)
        self.meminfolbl.configure(foreground="#d9d9d9")
        self.meminfolbl.configure(highlightbackground="#dbdbdb")
        self.meminfolbl.configure(highlightcolor="black")
        self.meminfolbl.configure(text='''Memory Information''')

        self.ramico = tk.Label(self.tabinfo)
        self.ramico.place(relx=0.03, rely=0.188, height=36, width=32)
        self.ramico.configure(activebackground="#2F2B3F")
        self.ramico.configure(activeforeground="white")
        self.ramico.configure(activeforeground="black")
        self.ramico.configure(background="#2F2B3F")
        self.ramico.configure(borderwidth="0")
        self.ramico.configure(disabledforeground="#a3a3a3")
        self.ramico.configure(font=font12)
        self.ramico.configure(foreground="#d9d9d9")
        self.ramico.configure(highlightbackground="#dbdbdb")
        self.ramico.configure(highlightcolor="black")
        self._img8 = tk.PhotoImage(file="../UI/ram.png")
        self.ramico.configure(image=self._img8)

        self.hddico = tk.Label(self.tabinfo)
        self.hddico.place(relx=0.03, rely=0.438, height=36, width=32)
        self.hddico.configure(activebackground="#2F2B3F")
        self.hddico.configure(activeforeground="white")
        self.hddico.configure(activeforeground="black")
        self.hddico.configure(background="#2F2B3F")
        self.hddico.configure(borderwidth="0")
        self.hddico.configure(disabledforeground="#a3a3a3")
        self.hddico.configure(font=font12)
        self.hddico.configure(foreground="#d9d9d9")
        self.hddico.configure(highlightbackground="#dbdbdb")
        self.hddico.configure(highlightcolor="black")
        self._img9 = tk.PhotoImage(file="../UI/hdisk.png")
        self.hddico.configure(image=self._img9)

        self.ramback = tk.Frame(self.tabinfo)
        self.ramback.place(relx=0.179, rely=0.281, relheight=0.031
                , relwidth=0.761)
        self.ramback.configure(relief='flat')
        self.ramback.configure(borderwidth="0")
        self.ramback.configure(background="#61B2D3")
        self.ramback.configure(highlightbackground="#d9d9d9")
        self.ramback.configure(highlightcolor="black")
        self.ramback.configure(width=255)

        self.ramfront = tk.Frame(self.ramback)
        self.ramfront.place(relx=0.0, rely=0.0, relheight=1.0)
        self.ramfront.configure(relief='flat')
        self.ramfront.configure(borderwidth="0")
        self.ramfront.configure(background="#7667CC")
        self.ramfront.configure(highlightbackground="#d9d9d9")
        self.ramfront.configure(highlightcolor="black")
        self.ramfront.configure(width=345)

        self.hddback = tk.Frame(self.tabinfo)
        self.hddback.place(relx=0.179, rely=0.531, relheight=0.031
                , relwidth=0.761)
        self.hddback.configure(relief='flat')
        self.hddback.configure(borderwidth="0")
        self.hddback.configure(background="#61B2D3")
        self.hddback.configure(highlightbackground="#d9d9d9")
        self.hddback.configure(highlightcolor="black")
        self.hddback.configure(width=255)

        self.hddfront = tk.Frame(self.hddback)
        self.hddfront.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=0.392)
        self.hddfront.configure(relief='flat')
        self.hddfront.configure(borderwidth="0")
        self.hddfront.configure(background="#7667CC")
        self.hddfront.configure(highlightbackground="#d9d9d9")
        self.hddfront.configure(highlightcolor="black")
        self.hddfront.configure(width=345)

        self.usedmemlbl = tk.Frame(self.tabinfo)
        self.usedmemlbl.place(relx=0.06, rely=0.738, relheight=0.063
                , relwidth=0.03)
        self.usedmemlbl.configure(relief='flat')
        self.usedmemlbl.configure(borderwidth="2")
        self.usedmemlbl.configure(background="#7667CC")
        self.usedmemlbl.configure(width=-10)

        self.freememlbl = tk.Frame(self.tabinfo)
        self.freememlbl.place(relx=0.06, rely=0.865, relheight=0.063
                , relwidth=0.03)
        self.freememlbl.configure(relief='flat')
        self.freememlbl.configure(borderwidth="2")
        self.freememlbl.configure(background="#61B2D3")
        self.freememlbl.configure(highlightbackground="#d9d9d9")
        self.freememlbl.configure(highlightcolor="black")
        self.freememlbl.configure(width=20)

        self.freelbl = tk.Label(self.tabinfo)
        self.freelbl.place(relx=0.09, rely=0.719, height=16, width=42)
        self.freelbl.configure(activebackground="#2F2B3F")
        self.freelbl.configure(activeforeground="white")
        self.freelbl.configure(activeforeground="black")
        self.freelbl.configure(background="#2F2B3F")
        self.freelbl.configure(borderwidth="0")
        self.freelbl.configure(disabledforeground="#a3a3a3")
        self.freelbl.configure(font=font17)
        self.freelbl.configure(foreground="#d9d9d9")
        self.freelbl.configure(highlightbackground="#dbdbdb")
        self.freelbl.configure(highlightcolor="black")
        self.freelbl.configure(text='''Free''')
        self.freelbl.configure(width=42)

        self.usedlbl = tk.Label(self.tabinfo)
        self.usedlbl.place(relx=0.096, rely=0.844, height=16, width=42)
        self.usedlbl.configure(activebackground="#2F2B3F")
        self.usedlbl.configure(activeforeground="white")
        self.usedlbl.configure(activeforeground="black")
        self.usedlbl.configure(background="#2F2B3F")
        self.usedlbl.configure(borderwidth="0")
        self.usedlbl.configure(disabledforeground="#a3a3a3")
        self.usedlbl.configure(font=font17)
        self.usedlbl.configure(foreground="#d9d9d9")
        self.usedlbl.configure(highlightbackground="#dbdbdb")
        self.usedlbl.configure(highlightcolor="black")
        self.usedlbl.configure(text='''Used''')

        self.ramfreelbl = tk.Label(self.tabinfo)
        self.ramfreelbl.place(relx=0.284, rely=0.719, height=16, width=42)
        self.ramfreelbl.configure(activebackground="#2F2B3F")
        self.ramfreelbl.configure(activeforeground="white")
        self.ramfreelbl.configure(activeforeground="black")
        self.ramfreelbl.configure(background="#2F2B3F")
        self.ramfreelbl.configure(borderwidth="0")
        self.ramfreelbl.configure(disabledforeground="#a3a3a3")
        self.ramfreelbl.configure(font=font17)
        self.ramfreelbl.configure(foreground="#d9d9d9")
        self.ramfreelbl.configure(highlightbackground="#dbdbdb")
        self.ramfreelbl.configure(highlightcolor="black")
        self.ramfreelbl.configure(text='''RAM:''')

        self.ramfreestlbl = tk.Label(self.tabinfo)
        self.ramfreestlbl.place(relx=0.403, rely=0.719, height=16, width=52)
        self.ramfreestlbl.configure(activebackground="#2F2B3F")
        self.ramfreestlbl.configure(activeforeground="white")
        self.ramfreestlbl.configure(activeforeground="black")
        self.ramfreestlbl.configure(background="#2F2B3F")
        self.ramfreestlbl.configure(borderwidth="0")
        self.ramfreestlbl.configure(disabledforeground="#a3a3a3")
        self.ramfreestlbl.configure(font=font16)
        self.ramfreestlbl.configure(foreground="#d9d9d9")
        self.ramfreestlbl.configure(highlightbackground="#dbdbdb")
        self.ramfreestlbl.configure(highlightcolor="black")
        self.ramfreestlbl.configure(text='''RAM''')
        self.ramfreestlbl.configure(anchor = 'w')
        self.ramfreestlbl.configure(width=52)

        self.hddfreelbl = tk.Label(self.tabinfo)
        self.hddfreelbl.place(relx=0.597, rely=0.719, height=16, width=42)
        self.hddfreelbl.configure(activebackground="#2F2B3F")
        self.hddfreelbl.configure(activeforeground="white")
        self.hddfreelbl.configure(activeforeground="black")
        self.hddfreelbl.configure(background="#2F2B3F")
        self.hddfreelbl.configure(borderwidth="0")
        self.hddfreelbl.configure(disabledforeground="#a3a3a3")
        self.hddfreelbl.configure(font=font17)
        self.hddfreelbl.configure(foreground="#d9d9d9")
        self.hddfreelbl.configure(highlightbackground="#dbdbdb")
        self.hddfreelbl.configure(highlightcolor="black")
        self.hddfreelbl.configure(text='''HDD:''')

        self.hddfreestlbl = tk.Label(self.tabinfo)
        self.hddfreestlbl.place(relx=0.716, rely=0.719, height=16, width=52)
        self.hddfreestlbl.configure(activebackground="#2F2B3F")
        self.hddfreestlbl.configure(activeforeground="white")
        self.hddfreestlbl.configure(activeforeground="black")
        self.hddfreestlbl.configure(background="#2F2B3F")
        self.hddfreestlbl.configure(borderwidth="0")
        self.hddfreestlbl.configure(disabledforeground="#a3a3a3")
        self.hddfreestlbl.configure(font=font16)
        self.hddfreestlbl.configure(foreground="#d9d9d9")
        self.hddfreestlbl.configure(highlightbackground="#dbdbdb")
        self.hddfreestlbl.configure(highlightcolor="black")
        self.hddfreestlbl.configure(anchor = 'w')
        self.hddfreestlbl.configure(text='''RAM''')

        self.ramusedlbl = tk.Label(self.tabinfo)
        self.ramusedlbl.place(relx=0.284, rely=0.844, height=16, width=42)
        self.ramusedlbl.configure(activebackground="#2F2B3F")
        self.ramusedlbl.configure(activeforeground="white")
        self.ramusedlbl.configure(activeforeground="black")
        self.ramusedlbl.configure(background="#2F2B3F")
        self.ramusedlbl.configure(borderwidth="0")
        self.ramusedlbl.configure(disabledforeground="#a3a3a3")
        self.ramusedlbl.configure(font=font17)
        self.ramusedlbl.configure(foreground="#d9d9d9")
        self.ramusedlbl.configure(highlightbackground="#dbdbdb")
        self.ramusedlbl.configure(highlightcolor="black")
        self.ramusedlbl.configure(text='''RAM:''')

        self.ramusedstlbl = tk.Label(self.tabinfo)
        self.ramusedstlbl.place(relx=0.403, rely=0.844, height=16, width=52)
        self.ramusedstlbl.configure(activebackground="#2F2B3F")
        self.ramusedstlbl.configure(activeforeground="white")
        self.ramusedstlbl.configure(activeforeground="black")
        self.ramusedstlbl.configure(background="#2F2B3F")
        self.ramusedstlbl.configure(borderwidth="0")
        self.ramusedstlbl.configure(disabledforeground="#a3a3a3")
        self.ramusedstlbl.configure(font=font16)
        self.ramusedstlbl.configure(foreground="#d9d9d9")
        self.ramusedstlbl.configure(highlightbackground="#dbdbdb")
        self.ramusedstlbl.configure(highlightcolor="black")
        self.ramusedstlbl.config(anchor = 'w')
        self.ramusedstlbl.configure(text='''RAM''')

        self.hddusedlbl = tk.Label(self.tabinfo)
        self.hddusedlbl.place(relx=0.597, rely=0.844, height=16, width=42)
        self.hddusedlbl.configure(activebackground="#2F2B3F")
        self.hddusedlbl.configure(activeforeground="white")
        self.hddusedlbl.configure(activeforeground="black")
        self.hddusedlbl.configure(background="#2F2B3F")
        self.hddusedlbl.configure(borderwidth="0")
        self.hddusedlbl.configure(disabledforeground="#a3a3a3")
        self.hddusedlbl.configure(font=font17)
        self.hddusedlbl.configure(foreground="#d9d9d9")
        self.hddusedlbl.configure(highlightbackground="#dbdbdb")
        self.hddusedlbl.configure(highlightcolor="black")
        self.hddusedlbl.configure(text='''HDD:''')

        self.hddusedstlbl = tk.Label(self.tabinfo)
        self.hddusedstlbl.place(relx=0.716, rely=0.844, height=16, width=52)
        self.hddusedstlbl.configure(activebackground="#2F2B3F")
        self.hddusedstlbl.configure(activeforeground="white")
        self.hddusedstlbl.configure(activeforeground="black")
        self.hddusedstlbl.configure(background="#2F2B3F")
        self.hddusedstlbl.configure(borderwidth="0")
        self.hddusedstlbl.configure(disabledforeground="#a3a3a3")
        self.hddusedstlbl.configure(font=font16)
        self.hddusedstlbl.configure(foreground="#d9d9d9")
        self.hddusedstlbl.configure(highlightbackground="#dbdbdb")
        self.hddusedstlbl.configure(highlightcolor="black")
        self.hddusedstlbl.configure(anchor = 'w')
        self.hddusedstlbl.configure(text='''RAM''')

        self.memoinfo = tk.Frame(self.homeplane)
        self.memoinfo.place(relx=0.556, rely=0.205, relheight=0.75
                , relwidth=0.406)
        self.memoinfo.configure(relief='flat')
        self.memoinfo.configure(borderwidth="2")
        self.memoinfo.configure(background="#2F2B3F")
        self.memoinfo.configure(highlightbackground="#d9d9d9")
        self.memoinfo.configure(highlightcolor="black")
        self.memoinfo.configure(width=265)


        self.meminfo = tk.Frame(self.homeplane)
        self.meminfo.place(relx=0.558, rely=0.205, relheight=0.75
                , relwidth=0.406)
        self.meminfo.configure(relief='flat')
        self.meminfo.configure(borderwidth="2")
        self.meminfo.configure(background="#2F2B3F")
        self.meminfo.configure(highlightbackground="#d9d9d9")
        self.meminfo.configure(highlightcolor="black")
        self.meminfo.configure(width=265)

        self.downloadcltr = tk.Label(self.meminfo)
        self.downloadcltr.place(relx=-0.056, rely=0.0, height=26, width=162)
        self.downloadcltr.configure(activebackground="#2F2B3F")
        self.downloadcltr.configure(activeforeground="white")
        self.downloadcltr.configure(activeforeground="black")
        self.downloadcltr.configure(background="#2F2B3F")
        self.downloadcltr.configure(borderwidth="0")
        self.downloadcltr.configure(disabledforeground="#a3a3a3")
        self.downloadcltr.configure(font=font12)
        self.downloadcltr.configure(foreground="#d9d9d9")
        self.downloadcltr.configure(highlightbackground="#dbdbdb")
        self.downloadcltr.configure(highlightcolor="black")
        self.downloadcltr.configure(text='''Download Clutter''')

        self.totimage = tk.Label(self.meminfo)
        self.totimage.place(relx=0.074, rely=0.242, height=76, width=92)
        self.totimage.configure(activebackground="#2F2B3F")
        self.totimage.configure(activeforeground="white")
        self.totimage.configure(activeforeground="black")
        self.totimage.configure(background="#2F2B3F")
        self.totimage.configure(borderwidth="0")
        self.totimage.configure(disabledforeground="#a3a3a3")
        self.totimage.configure(font=font18)
        self.totimage.configure(foreground="#d9d9d9")
        self.totimage.configure(highlightbackground="#dbdbdb")
        self.totimage.configure(highlightcolor="black")
        self.totimage.configure(text='''00''')
        self.totimage.configure(width=92)

        self.totvideos = tk.Label(self.meminfo)
        self.totvideos.place(relx=0.556, rely=0.242, height=76, width=92)
        self.totvideos.configure(activebackground="#2F2B3F")
        self.totvideos.configure(activeforeground="white")
        self.totvideos.configure(activeforeground="black")
        self.totvideos.configure(background="#2F2B3F")
        self.totvideos.configure(borderwidth="0")
        self.totvideos.configure(disabledforeground="#a3a3a3")
        self.totvideos.configure(font=font18)
        self.totvideos.configure(foreground="#d9d9d9")
        self.totvideos.configure(highlightbackground="#dbdbdb")
        self.totvideos.configure(highlightcolor="black")
        self.totvideos.configure(text='''00''')

        self.totdocs = tk.Label(self.meminfo)
        self.totdocs.place(relx=0.074, rely=0.485, height=76, width=92)
        self.totdocs.configure(activebackground="#2F2B3F")
        self.totdocs.configure(activeforeground="white")
        self.totdocs.configure(activeforeground="black")
        self.totdocs.configure(background="#2F2B3F")
        self.totdocs.configure(borderwidth="0")
        self.totdocs.configure(disabledforeground="#a3a3a3")
        self.totdocs.configure(font=font18)
        self.totdocs.configure(foreground="#d9d9d9")
        self.totdocs.configure(highlightbackground="#dbdbdb")
        self.totdocs.configure(highlightcolor="black")
        self.totdocs.configure(text='''00''')

        self.totaudio = tk.Label(self.meminfo)
        self.totaudio.place(relx=0.556, rely=0.485, height=76, width=92)
        self.totaudio.configure(activebackground="#2F2B3F")
        self.totaudio.configure(activeforeground="white")
        self.totaudio.configure(activeforeground="black")
        self.totaudio.configure(background="#2F2B3F")
        self.totaudio.configure(borderwidth="0")
        self.totaudio.configure(disabledforeground="#a3a3a3")
        self.totaudio.configure(font=font18)
        self.totaudio.configure(foreground="#d9d9d9")
        self.totaudio.configure(highlightbackground="#dbdbdb")
        self.totaudio.configure(highlightcolor="black")
        self.totaudio.configure(text='''00''')

        self.totarchive = tk.Label(self.meminfo)
        self.totarchive.place(relx=0.074, rely=0.742, height=76, width=92)
        self.totarchive.configure(activebackground="#2F2B3F")
        self.totarchive.configure(activeforeground="white")
        self.totarchive.configure(activeforeground="black")
        self.totarchive.configure(background="#2F2B3F")
        self.totarchive.configure(borderwidth="0")
        self.totarchive.configure(disabledforeground="#a3a3a3")
        self.totarchive.configure(font=font18)
        self.totarchive.configure(foreground="#d9d9d9")
        self.totarchive.configure(highlightbackground="#dbdbdb")
        self.totarchive.configure(highlightcolor="black")
        self.totarchive.configure(text='''00''')

        self.totothers = tk.Label(self.meminfo)
        self.totothers.place(relx=0.556, rely=0.742, height=76, width=92)
        self.totothers.configure(activebackground="#2F2B3F")
        self.totothers.configure(activeforeground="white")
        self.totothers.configure(activeforeground="black")
        self.totothers.configure(background="#2F2B3F")
        self.totothers.configure(borderwidth="0")
        self.totothers.configure(disabledforeground="#a3a3a3")
        self.totothers.configure(font=font18)
        self.totothers.configure(foreground="#d9d9d9")
        self.totothers.configure(highlightbackground="#dbdbdb")
        self.totothers.configure(highlightcolor="black")
        self.totothers.configure(text='''00''')

        self.imgback = tk.Frame(self.meminfo)
        self.imgback.place(relx=0.111, rely=0.439, relheight=0.015
                , relwidth=0.278)
        self.imgback.configure(relief='flat')
        self.imgback.configure(borderwidth="0")
        self.imgback.configure(background="#61B2D3")
        self.imgback.configure(highlightbackground="#d9d9d9")
        self.imgback.configure(highlightcolor="black")
        self.imgback.configure(width=75)

        self.imgfront = tk.Frame(self.imgback)
        self.imgfront.place(relx=0.0, rely=0.0,relheight=1.0)
        self.imgfront.configure(relief='flat')
        self.imgfront.configure(borderwidth="0")
        self.imgfront.configure(background="#7667CC")
        self.imgfront.configure(highlightbackground="#d9d9d9")
        self.imgfront.configure(highlightcolor="black")
        self.imgfront.configure(width=300)

        self.vidback = tk.Frame(self.meminfo)
        self.vidback.place(relx=0.593, rely=0.439, relheight=0.015
                , relwidth=0.278)
        self.vidback.configure(relief='flat')
        self.vidback.configure(borderwidth="0")
        self.vidback.configure(background="#61B2D3")
        self.vidback.configure(highlightbackground="#d9d9d9")
        self.vidback.configure(highlightcolor="black")
        self.vidback.configure(width=75)

        self.vidfront = tk.Frame(self.vidback)
        self.vidfront.place(relx=0.0, rely=0.0, relheight=1.0)
        self.vidfront.configure(relief='flat')
        self.vidfront.configure(borderwidth="0")
        self.vidfront.configure(background="#7667CC")
        self.vidfront.configure(highlightbackground="#d9d9d9")
        self.vidfront.configure(highlightcolor="black")
        self.vidfront.configure(width=30)

        self.docsback = tk.Frame(self.meminfo)
        self.docsback.place(relx=0.111, rely=0.682, relheight=0.015
                , relwidth=0.278)
        self.docsback.configure(relief='flat')
        self.docsback.configure(borderwidth="0")
        self.docsback.configure(background="#61B2D3")
        self.docsback.configure(highlightbackground="#d9d9d9")
        self.docsback.configure(highlightcolor="black")
        self.docsback.configure(width=75)

        self.docsfront = tk.Frame(self.docsback)
        self.docsfront.place(relx=0.0, rely=0.0, relheight=1.0)
        self.docsfront.configure(relief='flat')
        self.docsfront.configure(borderwidth="0")
        self.docsfront.configure(background="#7667CC")
        self.docsfront.configure(highlightbackground="#d9d9d9")
        self.docsfront.configure(highlightcolor="black")
        self.docsfront.configure(width=0)

        self.audioback = tk.Frame(self.meminfo)
        self.audioback.place(relx=0.593, rely=0.682, relheight=0.015
                , relwidth=0.278)
        self.audioback.configure(relief='flat')
        self.audioback.configure(borderwidth="0")
        self.audioback.configure(background="#61B2D3")
        self.audioback.configure(highlightbackground="#d9d9d9")
        self.audioback.configure(highlightcolor="black")
        self.audioback.configure(width=75)

        self.audiofront = tk.Frame(self.audioback)
        self.audiofront.place(relx=0.0, rely=0.0, relheight=1.0)
        self.audiofront.configure(relief='flat')
        self.audiofront.configure(borderwidth="0")
        self.audiofront.configure(background="#7667CC")
        self.audiofront.configure(highlightbackground="#d9d9d9")
        self.audiofront.configure(highlightcolor="black")
        self.audiofront.configure(width=30)

        self.archiveback = tk.Frame(self.meminfo)
        self.archiveback.place(relx=0.111, rely=0.939, relheight=0.015
                , relwidth=0.278)
        self.archiveback.configure(relief='flat')
        self.archiveback.configure(borderwidth="0")
        self.archiveback.configure(background="#61B2D3")
        self.archiveback.configure(highlightbackground="#d9d9d9")
        self.archiveback.configure(highlightcolor="black")
        self.archiveback.configure(width=75)

        self.archivefront = tk.Frame(self.archiveback)
        self.archivefront.place(relx=0.0, rely=0.0, relheight=1.0)
        self.archivefront.configure(relief='flat')
        self.archivefront.configure(borderwidth="0")
        self.archivefront.configure(background="#7667CC")
        self.archivefront.configure(highlightbackground="#d9d9d9")
        self.archivefront.configure(highlightcolor="black")
        self.archivefront.configure(width=30)

        self.othersback = tk.Frame(self.meminfo)
        self.othersback.place(relx=0.593, rely=0.939, relheight=0.015
                , relwidth=0.278)
        self.othersback.configure(relief='flat')
        self.othersback.configure(borderwidth="0")
        self.othersback.configure(background="#61B2D3")
        self.othersback.configure(highlightbackground="#d9d9d9")
        self.othersback.configure(highlightcolor="black")
        self.othersback.configure(width=75)

        self.othersfront = tk.Frame(self.othersback)
        self.othersfront.place(relx=0.0, rely=0.0, relheight=1.0)
        self.othersfront.configure(relief='flat')
        self.othersfront.configure(borderwidth="0")
        self.othersfront.configure(background="#7667CC")
        self.othersfront.configure(highlightbackground="#d9d9d9")
        self.othersfront.configure(highlightcolor="black")
        self.othersfront.configure(width=30)

        self.imagelbl = tk.Label(self.meminfo)
        self.imagelbl.place(relx=0.13, rely=0.258, height=16, width=62)
        self.imagelbl.configure(activebackground="#2F2B3F")
        self.imagelbl.configure(activeforeground="white")
        self.imagelbl.configure(activeforeground="black")
        self.imagelbl.configure(background="#2F2B3F")
        self.imagelbl.configure(borderwidth="0")
        self.imagelbl.configure(disabledforeground="#a3a3a3")
        self.imagelbl.configure(font=font17)
        self.imagelbl.configure(foreground="#d9d9d9")
        self.imagelbl.configure(highlightbackground="#dbdbdb")
        self.imagelbl.configure(highlightcolor="black")
        self.imagelbl.configure(text='''IMAGES''')
        self.imagelbl.configure(width=62)

        self.videolbl = tk.Label(self.meminfo)
        self.videolbl.place(relx=0.611, rely=0.258, height=16, width=62)
        self.videolbl.configure(activebackground="#2F2B3F")
        self.videolbl.configure(activeforeground="white")
        self.videolbl.configure(activeforeground="black")
        self.videolbl.configure(background="#2F2B3F")
        self.videolbl.configure(borderwidth="0")
        self.videolbl.configure(disabledforeground="#a3a3a3")
        self.videolbl.configure(font=font17)
        self.videolbl.configure(foreground="#d9d9d9")
        self.videolbl.configure(highlightbackground="#dbdbdb")
        self.videolbl.configure(highlightcolor="black")
        self.videolbl.configure(text='''VIDEOS''')
        self.videolbl.configure(width=62)

        self.docslbl = tk.Label(self.meminfo)
        self.docslbl.place(relx=0.13, rely=0.5, height=16, width=62)
        self.docslbl.configure(activebackground="#2F2B3F")
        self.docslbl.configure(activeforeground="white")
        self.docslbl.configure(activeforeground="black")
        self.docslbl.configure(background="#2F2B3F")
        self.docslbl.configure(borderwidth="0")
        self.docslbl.configure(disabledforeground="#a3a3a3")
        self.docslbl.configure(font=font17)
        self.docslbl.configure(foreground="#d9d9d9")
        self.docslbl.configure(highlightbackground="#dbdbdb")
        self.docslbl.configure(highlightcolor="black")
        self.docslbl.configure(text='''D O C S''')

        self.audiolbl = tk.Label(self.meminfo)
        self.audiolbl.place(relx=0.611, rely=0.5, height=16, width=62)
        self.audiolbl.configure(activebackground="#2F2B3F")
        self.audiolbl.configure(activeforeground="white")
        self.audiolbl.configure(activeforeground="black")
        self.audiolbl.configure(background="#2F2B3F")
        self.audiolbl.configure(borderwidth="0")
        self.audiolbl.configure(disabledforeground="#a3a3a3")
        self.audiolbl.configure(font=font17)
        self.audiolbl.configure(foreground="#d9d9d9")
        self.audiolbl.configure(highlightbackground="#dbdbdb")
        self.audiolbl.configure(highlightcolor="black")
        self.audiolbl.configure(text='''AUDIOS''')

        self.archivelbl = tk.Label(self.meminfo)
        self.archivelbl.place(relx=0.13, rely=0.758, height=16, width=62)
        self.archivelbl.configure(activebackground="#2F2B3F")
        self.archivelbl.configure(activeforeground="white")
        self.archivelbl.configure(activeforeground="black")
        self.archivelbl.configure(background="#2F2B3F")
        self.archivelbl.configure(borderwidth="0")
        self.archivelbl.configure(disabledforeground="#a3a3a3")
        self.archivelbl.configure(font=font17)
        self.archivelbl.configure(foreground="#d9d9d9")
        self.archivelbl.configure(highlightbackground="#dbdbdb")
        self.archivelbl.configure(highlightcolor="black")
        self.archivelbl.configure(text='''ARCHIVE''')

        self.otherlbl = tk.Label(self.meminfo)
        self.otherlbl.place(relx=0.611, rely=0.758, height=16, width=62)
        self.otherlbl.configure(activebackground="#2F2B3F")
        self.otherlbl.configure(activeforeground="white")
        self.otherlbl.configure(activeforeground="black")
        self.otherlbl.configure(background="#2F2B3F")
        self.otherlbl.configure(borderwidth="0")
        self.otherlbl.configure(disabledforeground="#a3a3a3")
        self.otherlbl.configure(font=font17)
        self.otherlbl.configure(foreground="#d9d9d9")
        self.otherlbl.configure(highlightbackground="#dbdbdb")
        self.otherlbl.configure(highlightcolor="black")
        self.otherlbl.configure(text='''OTHERS''')

        self.totalflslbl = tk.Label(self.meminfo)
        self.totalflslbl.place(relx=0.056, rely=0.093, height=26, width=82)
        self.totalflslbl.configure(activebackground="#2F2B3F")
        self.totalflslbl.configure(activeforeground="white")
        self.totalflslbl.configure(activeforeground="black")
        self.totalflslbl.configure(background="#2F2B3F")
        self.totalflslbl.configure(borderwidth="0")
        self.totalflslbl.configure(disabledforeground="#a3a3a3")
        self.totalflslbl.configure(font=font14)
        self.totalflslbl.configure(foreground="#d9d9d9")
        self.totalflslbl.configure(highlightbackground="#dbdbdb")
        self.totalflslbl.configure(highlightcolor="black")
        self.totalflslbl.configure(text='''Total Files:''')
        self.totalflslbl.configure(width=82)

        self.Frame1_45 = tk.Frame(self.meminfo)
        self.Frame1_45.place(relx=0.056, rely=0.106, relheight=0.061
                , relwidth=0.011)
        self.Frame1_45.configure(relief='flat')
        self.Frame1_45.configure(borderwidth="1")
        self.Frame1_45.configure(background="#37CA54")
        self.Frame1_45.configure(highlightbackground="#d9d9d9")
        self.Frame1_45.configure(highlightcolor="black")
        self.Frame1_45.configure(width=-2)

        self.totalflst = tk.Label(self.meminfo)
        self.totalflst.place(relx=0.37, rely=0.093, height=26, width=82)
        self.totalflst.configure(activebackground="#2F2B3F")
        self.totalflst.configure(activeforeground="white")
        self.totalflst.configure(activeforeground="black")
        self.totalflst.configure(background="#2F2B3F")
        self.totalflst.configure(borderwidth="0")
        self.totalflst.configure(disabledforeground="#a3a3a3")
        self.totalflst.configure(font=font19)
        self.totalflst.configure(foreground="#d9d9d9")
        self.totalflst.configure(highlightbackground="#dbdbdb")
        self.totalflst.configure(anchor = 'w')
        self.totalflst.configure(highlightcolor="black")

        # homeplane ends here

        # menu plane starts here
        self.menuplane = tk.Frame(top)
        self.menuplane.place(relx=0.101, rely=0.074, relheight=0.926
                , relwidth=0.9)
        self.menuplane.configure(relief='flat')
        self.menuplane.configure(borderwidth="2")
        self.menuplane.configure(background="#221F2E")
        self.menuplane.configure(highlightbackground="#d9d9d9")
        self.menuplane.configure(highlightcolor="black")
        self.menuplane.configure(width=665)

        self.lblstatus = tk.Label(self.menuplane)
        self.lblstatus.place(relx=0.015, rely=0.045, height=36, width=101)
        self.lblstatus.configure(activebackground="#f9f9f9")
        self.lblstatus.configure(activeforeground="black")
        self.lblstatus.configure(background="#221F2E")
        self.lblstatus.configure(disabledforeground="#a3a3a3")
        self.lblstatus.configure(font=font11)
        self.lblstatus.configure(foreground="#AC5CD9")
        self.lblstatus.configure(highlightbackground="#d9d9d9")
        self.lblstatus.configure(highlightcolor="black")
        self.lblstatus.configure(justify='left')
        self.lblstatus.configure(text='''Status''')
        self.lblstatus.configure(width=101)

        self.menulbl = tk.Label(self.menuplane)
        self.menulbl.place(relx=0.013, rely=-0.011, height=26, width=72)
        self.menulbl.configure(activebackground="#f9f9f9")
        self.menulbl.configure(activeforeground="black")
        self.menulbl.configure(background="#221F2E")
        self.menulbl.configure(borderwidth="0")
        self.menulbl.configure(disabledforeground="#a3a3a3")
        self.menulbl.configure(font=font12)
        self.menulbl.configure(foreground="#ffffff")
        self.menulbl.configure(highlightbackground="#d9d9d9")
        self.menulbl.configure(highlightcolor="black")
        self.menulbl.configure(text='''Menu>''')

        self.statuslbl = tk.Label(self.menuplane)
        self.statuslbl.place(relx=0.376, rely=0.125, height=120, width=140)
        self.statuslbl.configure(background="#221F2E")
        self.statuslbl.configure(disabledforeground="#a3a3a3")
        self.statuslbl.configure(foreground="#000000")
        self._img90 = tk.PhotoImage(file="statusokay.png")
        self.statuslbl.configure(image=self._img90)
        self.statuslbl.configure(width=140)

        self.statusdesclbl = tk.Label(self.menuplane)
        self.statusdesclbl.place(relx=0.211, rely=0.409, height=36, width=362)
        self.statusdesclbl.configure(background="#221F2E")
        self.statusdesclbl.configure(disabledforeground="#a3a3a3")
        self.statusdesclbl.configure(font=font21)
        self.statusdesclbl.configure(foreground="#ffffff")
        self.statusdesclbl.configure(text='''Your Downloads folder looks neat!''')
        self.statusdesclbl.configure(width=362)

        self.statusdesclb2 = tk.Label(self.menuplane)
        self.statusdesclb2.place(relx=0.211, rely=0.466, height=36, width=362)
        self.statusdesclb2.configure(activebackground="#f9f9f9")
        self.statusdesclb2.configure(activeforeground="black")
        self.statusdesclb2.configure(background="#221F2E")
        self.statusdesclb2.configure(disabledforeground="#a3a3a3")
        self.statusdesclb2.configure(font=font21)
        self.statusdesclb2.configure(foreground="#ffffff")
        self.statusdesclb2.configure(highlightbackground="#d9d9d9")
        self.statusdesclb2.configure(highlightcolor="black")
        self.statusdesclb2.configure(text='''No actions required.''')

        self.opendownbtn = tk.Button(self.menuplane)
        self.opendownbtn.place(relx=0.406, rely=0.58, height=33, width=106)
        self.opendownbtn.configure(activebackground="#6534AC")
        self.opendownbtn.configure(activeforeground="white")
        self.opendownbtn.configure(activeforeground="#ffffff")
        self.opendownbtn.configure(background="#6534AC")
        self.opendownbtn.configure(borderwidth="0")
        self.opendownbtn.configure(cursor="hand2")
        self.opendownbtn.configure(disabledforeground="#a3a3a3")
        self.opendownbtn.configure(font=font22)
        self.opendownbtn.configure(foreground="#ffffff")
        self.opendownbtn.configure(highlightbackground="#d9d9d9")
        self.opendownbtn.configure(highlightcolor="black")
        self.opendownbtn.configure(pady="0")
        self.opendownbtn.configure(relief='flat')
        self.opendownbtn.configure(text='''Downloads ↗''')
        self.opendownbtn.configure(width=106)
        self.opendownbtn.configure(command = engine.open_downloads)

        self.cleanbtn = tk.Button(self.menuplane)
        self.cleanbtn.place(relx=0.406, rely=0.67, height=33, width=106)
        self.cleanbtn.configure(activebackground="#6534AC")
        self.cleanbtn.configure(activeforeground="white")
        self.cleanbtn.configure(activeforeground="#ffffff")
        self.cleanbtn.configure(background="#6534AC")
        self.cleanbtn.configure(borderwidth="0")
        self.cleanbtn.configure(cursor="hand2")
        self.cleanbtn.configure(disabledforeground="#a3a3a3")
        self.cleanbtn.configure(font=font22)
        self.cleanbtn.configure(foreground="#ffffff")
        self.cleanbtn.configure(highlightbackground="#d9d9d9")
        self.cleanbtn.configure(highlightcolor="black")
        self.cleanbtn.configure(pady="0")
        self.cleanbtn.configure(relief='flat')
        self.cleanbtn.configure(text='''Clean''')
        self.cleanbtn.configure(command = self.clear_download_folder )

        self.cltrsizelbl = tk.Label(self.menuplane)
        self.cltrsizelbl.place(relx=0.361, rely=0.818, height=36, width=72)
        self.cltrsizelbl.configure(background="#221F2E")
        self.cltrsizelbl.configure(disabledforeground="#a3a3a3")
        self.cltrsizelbl.configure(font=font20)
        self.cltrsizelbl.configure(foreground="#ffffff")
        self.cltrsizelbl.configure(text='''00''')
        self.cltrsizelbl.configure(width=72)

        self.gblbl = tk.Label(self.menuplane)
        self.gblbl.place(relx=0.44, rely=0.85, height=20, width=30)
        self.gblbl.configure(activebackground="#f9f9f9")
        self.gblbl.configure(activeforeground="black")
        self.gblbl.configure(background="#221F2E")
        self.gblbl.configure(borderwidth="0")
        self.gblbl.configure(disabledforeground="#a3a3a3")
        self.gblbl.configure(font=font12)
        self.gblbl.configure(foreground="#ffffff")
        self.gblbl.configure(highlightbackground="#d9d9d9")
        self.gblbl.configure(highlightcolor="black")
        self.gblbl.configure(anchor = 'w')
        self.gblbl.configure(text='''GB''')

        self.cltrsizelbl_2 = tk.Label(self.menuplane)
        self.cltrsizelbl_2.place(relx=0.504, rely=0.818, height=36, width=72)
        self.cltrsizelbl_2.configure(activebackground="#f9f9f9")
        self.cltrsizelbl_2.configure(activeforeground="black")
        self.cltrsizelbl_2.configure(background="#221F2E")
        self.cltrsizelbl_2.configure(disabledforeground="#a3a3a3")
        self.cltrsizelbl_2.configure(font=font20)
        self.cltrsizelbl_2.configure(foreground="#ffffff")
        self.cltrsizelbl_2.configure(highlightbackground="#d9d9d9")
        self.cltrsizelbl_2.configure(highlightcolor="black")
        self.cltrsizelbl_2.configure(text='''00''')
        self.cltrsizelbl_2.configure(width=72)

        self.szlbl = tk.Label(self.menuplane)
        self.szlbl.place(relx=0.369, rely=0.795, height=16, width=62)
        self.szlbl.configure(activebackground="#f9f9f9")
        self.szlbl.configure(activeforeground="black")
        self.szlbl.configure(background="#221F2E")
        self.szlbl.configure(disabledforeground="#a3a3a3")
        self.szlbl.configure(font=font9)
        self.szlbl.configure(foreground="#ffffff")
        self.szlbl.configure(highlightbackground="#d9d9d9")
        self.szlbl.configure(highlightcolor="black")
        self.szlbl.configure(text='''SIZE''')
        self.szlbl.configure(width=62)

        self.szlbl_4 = tk.Label(self.menuplane)
        self.szlbl_4.place(relx=0.511, rely=0.795, height=16, width=62)
        self.szlbl_4.configure(activebackground="#f9f9f9")
        self.szlbl_4.configure(activeforeground="black")
        self.szlbl_4.configure(background="#221F2E")
        self.szlbl_4.configure(disabledforeground="#a3a3a3")
        self.szlbl_4.configure(font=font9)
        self.szlbl_4.configure(foreground="#ffffff")
        self.szlbl_4.configure(highlightbackground="#d9d9d9")
        self.szlbl_4.configure(highlightcolor="black")
        self.szlbl_4.configure(text='''FILES''')

        self.underlineframe = tk.Frame(self.menuplane)
        self.underlineframe.place(relx=0.389, rely=0.909, relheight=0.011
                , relwidth=0.087)
        self.underlineframe.configure(relief='flat')
        self.underlineframe.configure(borderwidth="1")
        self.underlineframe.configure(background="#C237B6")
        self.underlineframe.configure(highlightbackground="#d9d9d9")
        self.underlineframe.configure(highlightcolor="black")
        self.underlineframe.configure(width=48)

        self.underlineframe_6 = tk.Frame(self.menuplane)
        self.underlineframe_6.place(relx=0.518, rely=0.909, relheight=0.011
                , relwidth=0.087)
        self.underlineframe_6.configure(relief='flat')
        self.underlineframe_6.configure(borderwidth="1")
        self.underlineframe_6.configure(background="#C237B6")
        self.underlineframe_6.configure(highlightbackground="#d9d9d9")
        self.underlineframe_6.configure(highlightcolor="black")
        self.underlineframe_6.configure(width=58)

        self.copy_status_download = tk.Frame(self.menuplane)
        self.copy_status_download.place(relx= -0, rely=0.99, relheight=0.021)
        self.copy_status_download.configure(relief='flat')
        self.copy_status_download.configure(borderwidth="1")
        self.copy_status_download.configure(background="#4FB7F9")
        self.copy_status_download.configure(highlightbackground="#d9d9d9")
        self.copy_status_download.configure(highlightcolor="black")
        self.copy_status_download.configure(width=0)

        # menu plane ends here



        #Extras Plane starts here

        self.actionsplane = tk.Frame(top)
        self.actionsplane.place(relx=0.101, rely=0.074, relheight=0.926
                , relwidth=0.9)
        self.actionsplane.configure(relief='flat')
        self.actionsplane.configure(borderwidth="2")
        self.actionsplane.configure(background="#221F2E")
        self.actionsplane.configure(highlightbackground="#d9d9d9")
        self.actionsplane.configure(highlightcolor="black")
        self.actionsplane.configure(width=665)

        self.lblcleaner = tk.Label(self.actionsplane)
        self.lblcleaner.place(relx=0.0, rely=0.045, height=36, width=131)
        self.lblcleaner.configure(activebackground="#f9f9f9")
        self.lblcleaner.configure(activeforeground="black")
        self.lblcleaner.configure(background="#221F2E")
        self.lblcleaner.configure(disabledforeground="#a3a3a3")
        self.lblcleaner.configure(font=font11)
        self.lblcleaner.configure(foreground="#A8C7FD")
        self.lblcleaner.configure(highlightbackground="#d9d9d9")
        self.lblcleaner.configure(highlightcolor="black")
        self.lblcleaner.configure(justify='left')
        self.lblcleaner.configure(text='''Cleaner''')
        self.lblcleaner.configure(width=131)

        self.actionlbl = tk.Label(self.actionsplane)
        self.actionlbl.place(relx=0.015, rely=-0.011, height=26, width=72)
        self.actionlbl.configure(activebackground="#f9f9f9")
        self.actionlbl.configure(activeforeground="black")
        self.actionlbl.configure(background="#221F2E")
        self.actionlbl.configure(borderwidth="0")
        self.actionlbl.configure(disabledforeground="#a3a3a3")
        self.actionlbl.configure(font=font12)
        self.actionlbl.configure(foreground="#ffffff")
        self.actionlbl.configure(highlightbackground="#d9d9d9")
        self.actionlbl.configure(highlightcolor="black")
        self.actionlbl.configure(text='''Actions>''')

        self.statusfldrdesc = tk.Label(self.actionsplane)
        self.statusfldrdesc.place(relx=0.220, rely=0.636, height=36, width=362)
        self.statusfldrdesc.configure(activebackground="#f9f9f9")
        self.statusfldrdesc.configure(activeforeground="black")
        self.statusfldrdesc.configure(background="#221F2E")
        self.statusfldrdesc.configure(disabledforeground="#a3a3a3")
        self.statusfldrdesc.configure(font=font14)
        self.statusfldrdesc.configure(foreground="#ffffff")
        self.statusfldrdesc.configure(highlightbackground="#d9d9d9")
        self.statusfldrdesc.configure(highlightcolor="black")
        self.statusfldrdesc.configure(text='''Your Downloads folder looks neat!''')

        self.clutter_size_fldr = tk.Label(self.actionsplane)
        self.clutter_size_fldr.place(relx=0.376, rely=0.5, height=36, width=72)
        self.clutter_size_fldr.configure(activebackground="#f9f9f9")
        self.clutter_size_fldr.configure(activeforeground="black")
        self.clutter_size_fldr.configure(background="#221F2E")
        self.clutter_size_fldr.configure(disabledforeground="#a3a3a3")
        self.clutter_size_fldr.configure(font=font20)
        self.clutter_size_fldr.configure(foreground="#ffffff")
        self.clutter_size_fldr.configure(highlightbackground="#d9d9d9")
        self.clutter_size_fldr.configure(highlightcolor="black")
        self.clutter_size_fldr.configure(text='''00''')

        self.clutter_files_fldr = tk.Label(self.actionsplane)
        self.clutter_files_fldr.place(relx=0.504, rely=0.5, height=36, width=72)
        self.clutter_files_fldr.configure(activebackground="#f9f9f9")
        self.clutter_files_fldr.configure(activeforeground="black")
        self.clutter_files_fldr.configure(background="#221F2E")
        self.clutter_files_fldr.configure(disabledforeground="#a3a3a3")
        self.clutter_files_fldr.configure(font=font20)
        self.clutter_files_fldr.configure(foreground="#ffffff")
        self.clutter_files_fldr.configure(highlightbackground="#d9d9d9")
        self.clutter_files_fldr.configure(highlightcolor="black")
        self.clutter_files_fldr.configure(text='''00''')

        self.sizefldrlbl = tk.Label(self.actionsplane)
        self.sizefldrlbl.place(relx=0.383, rely=0.477, height=16, width=62)
        self.sizefldrlbl.configure(activebackground="#f9f9f9")
        self.sizefldrlbl.configure(activeforeground="black")
        self.sizefldrlbl.configure(background="#221F2E")
        self.sizefldrlbl.configure(disabledforeground="#a3a3a3")
        self.sizefldrlbl.configure(font=font17)
        self.sizefldrlbl.configure(foreground="#ffffff")
        self.sizefldrlbl.configure(highlightbackground="#d9d9d9")
        self.sizefldrlbl.configure(highlightcolor="black")
        self.sizefldrlbl.configure(text='''SIZE''')

        self.filesfldrlbl = tk.Label(self.actionsplane)
        self.filesfldrlbl.place(relx=0.511, rely=0.477, height=16, width=62)
        self.filesfldrlbl.configure(activebackground="#f9f9f9")
        self.filesfldrlbl.configure(activeforeground="black")
        self.filesfldrlbl.configure(background="#221F2E")
        self.filesfldrlbl.configure(disabledforeground="#a3a3a3")
        self.filesfldrlbl.configure(font=font17)
        self.filesfldrlbl.configure(foreground="#ffffff")
        self.filesfldrlbl.configure(highlightbackground="#d9d9d9")
        self.filesfldrlbl.configure(highlightcolor="black")
        self.filesfldrlbl.configure(text='''FILES''')

        self.uline1 = tk.Frame(self.actionsplane)
        self.uline1.place(relx=0.385, rely=0.591, relheight=0.011
                , relwidth=0.087)
        self.uline1.configure(relief='flat')
        self.uline1.configure(borderwidth="1")
        self.uline1.configure(background="#C237B6")
        self.uline1.configure(highlightbackground="#d9d9d9")
        self.uline1.configure(highlightcolor="black")
        self.uline1.configure(width=48)

        self.uline2 = tk.Frame(self.actionsplane)
        self.uline2.place(relx=0.516, rely=0.593, relheight=0.011
                , relwidth=0.087)
        self.uline2.configure(relief='flat')
        self.uline2.configure(borderwidth="1")
        self.uline2.configure(background="#C237B6")
        self.uline2.configure(highlightbackground="#d9d9d9")
        self.uline2.configure(highlightcolor="black")
        self.uline2.configure(width=58)

        self.scanbtn = tk.Button(self.actionsplane)
        self.scanbtn.place(relx=0.325, rely=0.295, height=29, width=100)
        self.scanbtn.configure(activebackground="#6534AC")
        self.scanbtn.configure(activeforeground="white")
        self.scanbtn.configure(activeforeground="#ffffff")
        self.scanbtn.configure(background="#6534AC")
        self.scanbtn.configure(borderwidth="0")
        self.scanbtn.configure(cursor="hand2")
        self.scanbtn.configure(disabledforeground="#a3a3a3")
        self.scanbtn.configure(font=font16)
        self.scanbtn.configure(foreground="#ffffff")
        self.scanbtn.configure(highlightbackground="#d9d9d9")
        self.scanbtn.configure(highlightcolor="black")
        self.scanbtn.configure(pady="0")
        self.scanbtn.configure(relief='flat')
        self.scanbtn.configure(text='''Scan''')
        self.scanbtn.configure(command = self.scan_folder)

        self.browsebtn = tk.Button(self.actionsplane)
        self.browsebtn.place(relx=0.496, rely=0.295, height=29, width=100)
        self.browsebtn.configure(activebackground="#6534AC")
        self.browsebtn.configure(activeforeground="white")
        self.browsebtn.configure(activeforeground="#ffffff")
        self.browsebtn.configure(background="#6534AC")
        self.browsebtn.configure(borderwidth="0")
        self.browsebtn.configure(cursor="hand2")
        self.browsebtn.configure(disabledforeground="#a3a3a3")
        self.browsebtn.configure(font=font16)
        self.browsebtn.configure(foreground="#ffffff")
        self.browsebtn.configure(highlightbackground="#d9d9d9")
        self.browsebtn.configure(highlightcolor="black")
        self.browsebtn.configure(pady="0")
        self.browsebtn.configure(relief='flat')
        self.browsebtn.configure(text='''Browse ↗''')
        self.browsebtn.configure(command = self.browse_location)

        self.addrback = tk.Frame(self.actionsplane)
        self.addrback.place(relx=0.105, rely=0.205, relheight=0.065
                , relwidth=0.774)
        self.addrback.configure(relief='flat')
        self.addrback.configure(borderwidth="1")
        self.addrback.configure(background="#2FC0DF")
        self.addrback.configure(width=515)

        self.addrfront = tk.Text(self.addrback)
        self.addrfront.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)

        self.addrfront.configure(background="#221F2E")
        self.addrfront.configure(font=font15)
        self.addrfront.configure(foreground="#ffffff")
        self.addrfront.configure(highlightbackground="#221F2E")
        self.addrfront.configure(highlightcolor="#221F2E")
        self.addrfront.configure(insertbackground="#C237B6")
        self.addrfront.configure(relief='flat')
        self.addrfront.configure(selectbackground="#C237B6")
        self.addrfront.configure(selectforeground="#ffffff")
        self.addrfront.configure(width=482)
        self.addrfront.configure(wrap='word')
        self.addrfront.insert('end', 'Enter location')
        

        self.cleanfldrbtn = tk.Button(self.actionsplane)
        self.cleanfldrbtn.place(relx=0.410, rely=0.773, height=33, width=106)
        self.cleanfldrbtn.configure(activebackground="#6534AC")
        self.cleanfldrbtn.configure(activeforeground="white")
        self.cleanfldrbtn.configure(activeforeground="#ffffff")
        self.cleanfldrbtn.configure(background="#6534AC")
        self.cleanfldrbtn.configure(borderwidth="0")
        self.cleanfldrbtn.configure(cursor="hand2")
        self.cleanfldrbtn.configure(disabledforeground="#a3a3a3")
        self.cleanfldrbtn.configure(font=font16)
        self.cleanfldrbtn.configure(foreground="#ffffff")
        self.cleanfldrbtn.configure(highlightbackground="#d9d9d9")
        self.cleanfldrbtn.configure(highlightcolor="black")
        self.cleanfldrbtn.configure(pady="0")
        self.cleanfldrbtn.configure(relief='flat')
        self.cleanfldrbtn.configure(text='''Clean''')       
        self.cleanfldrbtn.configure(command = self.clear_scan_folder)

        self.movingdesc = tk.Label(self.actionsplane)
        self.movingdesc.place(relx=0.270, rely=0.886, height=36, width=300)
        self.movingdesc.configure(activebackground="#f9f9f9")
        self.movingdesc.configure(activeforeground="black")
        self.movingdesc.configure(background="#221F2E")
        self.movingdesc.configure(disabledforeground="#a3a3a3")
        self.movingdesc.configure(font=font14)
        self.movingdesc.configure(foreground="#FFFFFF")
        self.movingdesc.configure(highlightbackground="#d9d9d9")
        self.movingdesc.configure(highlightcolor="black")
        self.movingdesc.configure(text='''''')
        self.movingdesc.configure(width=192)
        self.movingdesc.configure(anchor = "center")

        self.hiderframe = tk.Frame(self.actionsplane)
        self.hiderframe.place(relx=0.09, rely=0.432, relheight=0.466
                , relwidth=0.82)
        self.hiderframe.configure(relief='flat')
        self.hiderframe.configure(borderwidth="2")
        self.hiderframe.configure(background="#221F2E")
        self.hiderframe.configure(highlightbackground="#d9d9d9")
        self.hiderframe.configure(highlightcolor="black")
        self.hiderframe.configure(width=545)

        self.copy_status = tk.Frame(self.actionsplane)
        self.copy_status.place(relx= -0, rely=0.99, relheight=0.021)
        self.copy_status.configure(relief='flat')
        self.copy_status.configure(borderwidth="1")
        self.copy_status.configure(background="#4FB7F9")
        self.copy_status.configure(highlightbackground="#d9d9d9")
        self.copy_status.configure(highlightcolor="black")
        self.copy_status.configure(width=0)

        #Extra Plane ends here

        #Settings plane Starts

        self.settingsplane = tk.Frame(top)
        self.settingsplane.place(relx=0.101, rely=0.074, relheight=0.926
                , relwidth=0.9)
        self.settingsplane.configure(relief='flat')
        self.settingsplane.configure(borderwidth="2")
        self.settingsplane.configure(background="#221F2E")
        self.settingsplane.configure(highlightbackground="#d9d9d9")
        self.settingsplane.configure(highlightcolor="black")
        self.settingsplane.configure(width=665)

        self.lbllocs = tk.Label(self.settingsplane)
        self.lbllocs.place(relx=0.023, rely=0.040, height=36, width=131)
        self.lbllocs.configure(activebackground="#f9f9f9")
        self.lbllocs.configure(activeforeground="black")
        self.lbllocs.configure(background="#221F2E")
        self.lbllocs.configure(disabledforeground="#a3a3a3")
        self.lbllocs.configure(font=font11)
        self.lbllocs.configure(foreground="#A8C7FD")
        self.lbllocs.configure(highlightbackground="#d9d9d9")
        self.lbllocs.configure(highlightcolor="black")
        self.lbllocs.configure(justify='left')
        self.lbllocs.configure(text='''Locations''')
        self.lbllocs.configure(width=131)

        self.settingslbl = tk.Label(self.settingsplane)
        self.settingslbl.place(relx=0.015, rely=-0.011, height=26, width=72)
        self.settingslbl.configure(activebackground="#f9f9f9")
        self.settingslbl.configure(activeforeground="black")
        self.settingslbl.configure(background="#221F2E")
        self.settingslbl.configure(borderwidth="0")
        self.settingslbl.configure(disabledforeground="#a3a3a3")
        self.settingslbl.configure(font=font12)
        self.settingslbl.configure(foreground="#ffffff")
        self.settingslbl.configure(highlightbackground="#d9d9d9")
        self.settingslbl.configure(highlightcolor="black")
        self.settingslbl.configure(text='''Settings>''')

        self.dcltrlbl = tk.Label(self.settingsplane)
        self.dcltrlbl.place(relx=0.0215, rely=0.222, height=16, width=80)
        self.dcltrlbl.configure(activebackground="#f9f9f9")
        self.dcltrlbl.configure(activeforeground="black")
        self.dcltrlbl.configure(background="#221F2E")
        self.dcltrlbl.configure(disabledforeground="#a3a3a3")
        self.dcltrlbl.configure(font=font17)
        self.dcltrlbl.configure(foreground="#ffffff")
        self.dcltrlbl.configure(highlightbackground="#d9d9d9")
        self.dcltrlbl.configure(highlightcolor="black")
        self.dcltrlbl.configure(text='''DOWNLOADS''')

        self.dladdrback = tk.Frame(self.settingsplane)
        self.dladdrback.place(relx=0.0285, rely=0.295, relheight=0.065
                , relwidth=0.774)
        self.dladdrback.configure(relief='flat')
        self.dladdrback.configure(borderwidth="1")
        self.dladdrback.configure(background="#2FC0DF")
        self.dladdrback.configure(width=515)

        self.dladdrfront = tk.Text(self.dladdrback)
        self.dladdrfront.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)

        self.dladdrfront.configure(background="#221F2E")
        self.dladdrfront.configure(font=font15)
        self.dladdrfront.configure(foreground="#ffffff")
        self.dladdrfront.configure(highlightbackground="#221F2E")
        self.dladdrfront.configure(highlightcolor="#221F2E")
        self.dladdrfront.configure(insertbackground="#C237B6")
        self.dladdrfront.configure(relief='flat')
        self.dladdrfront.configure(selectbackground="#C237B6")
        self.dladdrfront.configure(selectforeground="#ffffff")
        self.dladdrfront.configure(width=482)
        self.dladdrfront.configure(wrap='word')
        self.dladdrfront.insert('end', 'No Location')


        self.dclbrowsebtn = tk.Button(self.settingsplane)
        self.dclbrowsebtn.place(relx=0.816, rely=0.295, height=29, width=29)
        self.dclbrowsebtn.configure(activebackground="#6534AC")
        self.dclbrowsebtn.configure(activeforeground="white")
        self.dclbrowsebtn.configure(activeforeground="#ffffff")
        self.dclbrowsebtn.configure(background="#6534AC")
        self.dclbrowsebtn.configure(borderwidth="0")
        self.dclbrowsebtn.configure(cursor="hand2")
        self.dclbrowsebtn.configure(disabledforeground="#a3a3a3")
        self.dclbrowsebtn.configure(font=font16)
        self.dclbrowsebtn.configure(foreground="#ffffff")
        self.dclbrowsebtn.configure(highlightbackground="#d9d9d9")
        self.dclbrowsebtn.configure(highlightcolor="black")
        self.dclbrowsebtn.configure(pady="0")
        self.dclbrowsebtn.configure(relief='flat')
        self.dclbrowsebtn.configure(text='''↗''')
        self.dclbrowsebtn.configure(command = self.browse_download_path)



        self.ccltrlbl = tk.Label(self.settingsplane)
        self.ccltrlbl.place(relx=0.0215, rely=0.442, height=16, width=52)
        self.ccltrlbl.configure(activebackground="#f9f9f9")
        self.ccltrlbl.configure(activeforeground="black")
        self.ccltrlbl.configure(background="#221F2E")
        self.ccltrlbl.configure(disabledforeground="#a3a3a3")
        self.ccltrlbl.configure(font=font17)
        self.ccltrlbl.configure(foreground="#ffffff")
        self.ccltrlbl.configure(highlightbackground="#d9d9d9")
        self.ccltrlbl.configure(highlightcolor="black")
        self.ccltrlbl.configure(text='''OTHERS''')


        self.otaddrback = tk.Frame(self.settingsplane)
        self.otaddrback.place(relx=0.0285, rely=0.522, relheight=0.065
                , relwidth=0.774)
        self.otaddrback.configure(relief='flat')
        self.otaddrback.configure(borderwidth="1")
        self.otaddrback.configure(background="#2FC0DF")
        self.otaddrback.configure(width=515)

        self.otaddrfront = tk.Text(self.otaddrback)
        self.otaddrfront.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)

        self.otaddrfront.configure(background="#221F2E")
        self.otaddrfront.configure(font=font15)
        self.otaddrfront.configure(foreground="#ffffff")
        self.otaddrfront.configure(highlightbackground="#221F2E")
        self.otaddrfront.configure(highlightcolor="#221F2E")
        self.otaddrfront.configure(insertbackground="#C237B6")
        self.otaddrfront.configure(relief='flat')
        self.otaddrfront.configure(selectbackground="#C237B6")
        self.otaddrfront.configure(selectforeground="#ffffff")
        self.otaddrfront.configure(width=482)
        self.otaddrfront.configure(wrap='word')
        self.otaddrfront.insert('end', 'No Location')


        self.othbrowsebtn = tk.Button(self.settingsplane)
        self.othbrowsebtn.place(relx=0.816, rely=0.522, height=29, width=29)
        self.othbrowsebtn.configure(activebackground="#6534AC")
        self.othbrowsebtn.configure(activeforeground="white")
        self.othbrowsebtn.configure(activeforeground="#ffffff")
        self.othbrowsebtn.configure(background="#6534AC")
        self.othbrowsebtn.configure(borderwidth="0")
        self.othbrowsebtn.configure(cursor="hand2")
        self.othbrowsebtn.configure(disabledforeground="#a3a3a3")
        self.othbrowsebtn.configure(font=font16)
        self.othbrowsebtn.configure(foreground="#ffffff")
        self.othbrowsebtn.configure(highlightbackground="#d9d9d9")
        self.othbrowsebtn.configure(highlightcolor="black")
        self.othbrowsebtn.configure(pady="0")
        self.othbrowsebtn.configure(relief='flat')
        self.othbrowsebtn.configure(text='''↗''')
        self.othbrowsebtn.configure(command = self.browse_others_path)

        self.saveprefbtn = tk.Button(self.settingsplane)
        self.saveprefbtn.place(relx=0.0285, rely=0.722, height=29, width=80)
        self.saveprefbtn.configure(activebackground="#33C761")
        self.saveprefbtn.configure(activeforeground="white")
        self.saveprefbtn.configure(activeforeground="#ffffff")
        self.saveprefbtn.configure(background="#33C761")
        self.saveprefbtn.configure(borderwidth="0")
        self.saveprefbtn.configure(cursor="hand2")
        self.saveprefbtn.configure(disabledforeground="#a3a3a3")
        self.saveprefbtn.configure(font=font16)
        self.saveprefbtn.configure(foreground="#ffffff")
        self.saveprefbtn.configure(highlightbackground="#d9d9d9")
        self.saveprefbtn.configure(highlightcolor="black")
        self.saveprefbtn.configure(pady="0")
        self.saveprefbtn.configure(relief='flat')
        self.saveprefbtn.configure(text='''SAVE''')
        self.saveprefbtn.configure(command = self.save_create_locs)
       


        #Settings plane ends.






        self.titlebar = tk.Frame(top)
        self.titlebar.place(relx=0.101, rely=0.0, relheight=0.074, relwidth=0.9)
        self.titlebar.configure(relief='flat')
        self.titlebar.configure(borderwidth="2")
        self.titlebar.configure(cursor="circle")
        self.titlebar.configure(background="#221F2E")
        self.titlebar.configure(highlightbackground="#d9d9d9")
        self.titlebar.configure(highlightcolor="black")
        self.titlebar.configure(width=665)
        self.titlebar.bind('<B1-Motion>', move_window)
        self.titlebar.bind('<Button-1>', get_pos)
        self.titlebar.bind('<Map>',self.frame_mapped)

        self.close_btn = tk.Button(self.titlebar)
        self.close_btn.place(relx=0.947, rely=-0.143, height=36, width=36)
        self.close_btn.configure(activebackground="#E81123")
        self.close_btn.configure(activeforeground="#E81123")
        self.close_btn.configure(activeforeground="#E81123")
        self.close_btn.configure(background="#221F2E")
        self.close_btn.configure(borderwidth="0")
        self.close_btn.configure(cursor="hand2")
        self.close_btn.configure(disabledforeground="#a3a3a3")
        self.close_btn.configure(foreground="#221F2E")
        self.close_btn.configure(highlightbackground="#E81123")
        self.close_btn.configure(highlightcolor="#E81123")
        self.close_btn.configure(highlightthickness="0")
        self._img5 = tk.PhotoImage(file="./cut.png")
        self.close_btn.configure(image=self._img5)
        self.close_btn.configure(overrelief="flat")
        self.close_btn.configure(padx="0")
        self.close_btn.configure(pady="0")
        self.close_btn.configure(relief='flat')
        self.close_btn.configure(command = root.destroy)
        self.close_btn.bind('<Enter>',self.close_on_enter)
        self.close_btn.bind('<Leave>',self.close_on_leave)

        self.min_btn = tk.Button(self.titlebar)
        self.min_btn.place(relx=0.895, rely=-0.143, height=36, width=36)
        self.min_btn.configure(activebackground="#b5b5b5")
        self.min_btn.configure(activeforeground="#000000")
        self.min_btn.configure(background="#221F2E")
        self.min_btn.configure(borderwidth="0")
        self.min_btn.configure(cursor="hand2")
        self.min_btn.configure(disabledforeground="#a3a3a3")
        self.min_btn.configure(foreground="#221F2E")
        self.min_btn.configure(highlightbackground="#221F2E")
        self.min_btn.configure(highlightcolor="#221F2E")
        self.min_btn.configure(highlightthickness="0")
        self._img6 = tk.PhotoImage(file="./min.png")
        self.min_btn.configure(image=self._img6)
        self.min_btn.configure(overrelief="flat")
        self.min_btn.configure(padx="0")
        self.min_btn.configure(pady="0")
        self.min_btn.configure(relief='flat')
        self.min_btn.configure(command = self.min_win)
        self.min_btn.bind('<Enter>',self.min_on_enter)
        self.min_btn.bind('<Leave>',self.min_on_leave)

        self.on_load()


if __name__ == '__main__':
    vp_start_gui()





