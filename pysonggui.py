#!/usr/bin/python
#coding=utf8

import Pmw
from Tkinter import *
from tkFileDialog import askdirectory
import string
import pafy
from pygoogle import pygoogle
import webbrowser
import urllib2
import sys
import csv
import os

#------------------------------------------------------------------------------#
#                                                                              #
#                                  pysonggui                                   #
#                                                                              #
#------------------------------------------------------------------------------#


def scrape(urls, location='.'):
    try:
        os.makedirs(location)
    except OSError:
        pass
    for song in urls:
        print song
        try:
            video = pafy.new(song)
            print '''Downloading ''' + video.title
            video.getbestaudio().download(filepath=location)
        except IOError: 
            print "Video Not Available"
    print '''Finished'''

class pysonggui(Frame):
    def __init__(self,Master=None,*pos,**kw):
        #
        #Your code here
        #

        apply(Frame.__init__,(self,Master),kw)
        self._Frame15 = Frame(self)
        self._Frame15.pack(side='top')
        self._Label1 = Label(self._Frame15,text='Youtube Music Downloader')
        self._Label1.pack(side='top')
        self._Frame1 = Frame(self)
        self._Frame1.pack(side='top')
        self._Frame6 = Frame(self,borderwidth='10')
        self._Frame6.pack(side='top')

        self._Frame20 = Frame(self._Frame6,borderwidth='3')
        self._Frame20.pack(side='left')
        self._Button3 = Button(self._Frame20,borderwidth='3',text='Refresh ♻'
            ,width='30')
        self._Button3.pack(side='top')
        self._Button3.bind('<ButtonRelease-1>',
                    self._on_Button3_ButRel_1)
        self._Frame27 = Frame(self._Frame6)
        self._Frame27.pack(side='left')

        self._Frame21 = Frame(self._Frame6,borderwidth='3')
        self._Frame21.pack(side='left')
        self._Label11 = Label(self._Frame21,text='Pages to Download\n(Four songs per page)')
        self._Label11.pack(side='top')
        self._Entry2 = Entry(self._Frame21)
        self._Entry2.pack(side='left')
        self._Entry2.insert(0,"1")

        self._Frame25 = Frame(self._Frame6)
        self._Frame25.pack(side='left')
        self._Frame2 = Frame(self)
        self._Frame2.pack(side='top')
        self._Frame3 = Frame(self)
        self._Frame3.pack(side='top')
        self._Frame5 = Frame(self._Frame1)
        self._Frame5.pack(side='left')
        self._Label2 = Label(self._Frame5,text='Directory')
        self._Label2.pack(side='right')
        self._Frame4 = Frame(self._Frame1)
        self._Frame4.pack(side='left')
        self._Entry1 = Entry(self._Frame4)
        self._Entry1.pack(side='right')
        self._Entry1.insert(0,".")
        self._Frame19 = Frame(self._Frame1)
        self._Frame19.pack(side='left')
        self._Button4 = Button(self._Frame19,text='Browse')
        self._Button4.pack(side='left')
        self._Button4.bind('<ButtonRelease-1>',
                    self._on_Button4_ButRel_1)

        self._Frame7 = Frame(self._Frame2,borderwidth='10')
        self._Frame7.pack(side='left')
        self._Frame16 = Frame(self._Frame2)
        self._Frame16.pack(side='left')
        self._Frame8 = Frame(self._Frame2,borderwidth='10')
        self._Frame8.pack(side='left')
        self._Frame12 = Frame(self._Frame3,borderwidth='10')
        self._Frame12.pack(side='left')
        self._Button2 = Button(self._Frame12,text='Download All',width='20')
        self._Button2.pack(side='bottom')
        self._Button2.bind('<ButtonRelease-1>',
                    self._on_Button2_ButRel_1)

        self._Frame14 = Frame(self._Frame3,borderwidth='010')
        self._Frame14.pack(side='left')
        self._Button1 = Button(self._Frame14,text='Visit URL',width='20')
        self._Button1.pack(side='top')
        self._Button1.bind('<ButtonRelease-1>',
                    self._on_Button1_ButRel_1)
        self._Frame33 = Frame(self._Frame3,borderwidth='10')
        self._Frame33.pack(side='left')
        self._Button5 =Button(self._Frame33,text='Resolve Title',width='20')
        self._Button5.pack(side='top')        
        self._Button5.bind('<ButtonRelease-1>',
                    self._on_Button5_ButRel_1)

        self._Frame9 = Frame(self._Frame7)
        self._Frame9.pack(side='top')
        self._Label3 = Label(self._Frame9,text='Song & Artist Edit Box')
        self._Label3.pack(side='top')
        self._Frame10 = Frame(self._Frame7)
        self._Frame10.pack(side='top')
        self._ScrolledText1 = Pmw.ScrolledText(self._Frame10
            ,horizscrollbar_width='13',text_height='15',text_width='40'
            ,text_wrap='none')
        self._ScrolledText1.pack(side='bottom')
        self._Frame18 = Frame(self._Frame16)
        self._Frame18.pack(side='top')
        self._Label5 = Label(self._Frame18,text='Select Song')
        self._Label5.pack(side='top')
        self._Frame17 = Frame(self._Frame16)
        self._Frame17.pack(side='top')
        self._ScrolledListBox2 = Pmw.ScrolledListBox(self._Frame17
            ,listbox_height='15',listbox_width='30',selectioncommand=self._on_ScrolledListBox2_selection)
        self._ScrolledListBox2.pack(side='top')
        self._Frame11 = Frame(self._Frame8)
        self._Frame11.pack(side='top')
        self._Label4 = Label(self._Frame11,text='Select Youtube Search Match')
        self._Label4.pack(side='top')
        self._Frame13 = Frame(self._Frame8)
        self._Frame13.pack(side='top')
        self._ScrolledListBox1 = Pmw.ScrolledListBox(self._Frame13
            ,listbox_height='15',listbox_width='70',selectioncommand=self._on_ScrolledListBox1_selection)
        self._ScrolledListBox1.pack(side='top')
        self._Label6 = Label(self._Frame25,text='Google Quick Mode\n(Only downloads first name)')
        self._Label6.pack(side='top')
        self._CheckVar1 = IntVar()
        self._CheckVar1.set(1)
        self._Checkbutton1 = Checkbutton(self._Frame25, variable = self._CheckVar1, state=NORMAL)
        self._Checkbutton1.pack(side='top')
        self._Label10 = Label(self._Frame27,text='Search API')
        self._Label10.pack(side='top')
        self._Frame51 = Frame(self._Frame27)
        self._Frame51.pack(side='left')       
        self._Frame52 = Frame(self._Frame27)
        self._Frame52.pack(side='left')       
        #
        self._Frame53 = Frame(self._Frame51)
        self._Frame53.pack(side='top')
        self._Frame54 = Frame(self._Frame51)
        self._Frame54.pack(side='top')
        self._RadioVar1 = IntVar()
        self._RadioVar1.set(1)
        #self._Radiobutton1 = Radiobutton(self._Frame51, text="DuckDuckGo",
        #                variable=self._RadioVar1, value=1,command=self._on_RadioButton1_selection)
        #self._Radiobutton1.pack(side='top')

        #
        self._Frame55 = Frame(self._Frame52)
        self._Frame55.pack(side='top')
        self._Frame56 = Frame(self._Frame55)
        self._Frame56.pack(side='top')
        self._Radiobutton2 = Radiobutton(self._Frame55, text="Google",
                        variable=self._RadioVar1, value=1,command=self._on_RadioButton2_selection)
        self._Radiobutton2.pack(side='top')

        #
        #Your code here
        #
        self.songlist = []
        self.selectedurllist = []
        self.currentselection1 = 0
        self.currentselection2 = 0
        self.searchapi = self._RadioVar1.get()
    #
    #Start of event handler methods
    #

    def _google_search(self, songs):
        for song in songs:
            print '''fetching ''' + song
            googsearch = pygoogle(song + ' site:youtube.com/watch')
            googsearch.pages = int(self._Entry2.get())
            namelist = []
            index = 0
            for url in googsearch.get_urls():
                if self._CheckVar1.get() > 0 and index > 0:
                    namelist.append(url)
                else:
                    try:
                        video = pafy.new(url)
                        namelist.append(video.title + ''' : ''' + video.author)
                        index = index+1
                    except IOError:
                        namelist.append("Video Not Available")
            self.songlist.append((namelist,googsearch.get_urls()))
            self.selectedurllist.append(0)
    def _on_Button4_ButRel_1(self, Event=None):
        filename = askdirectory()
        self._Entry1.delete(0, END)
        self._Entry1.insert(0, filename)
    def _on_Button1_ButRel_1(self, Event=None):
        if(self._ScrolledListBox1.size() > 0):
            webbrowser.open(self.songlist[self.currentselection2][1][self.currentselection1])
        
    def _on_Button2_ButRel_1(self, Event=None):
        urllist = []
        for x in range(0,self._ScrolledListBox2.size()):
            urllist.append(self.songlist[x][1][self.selectedurllist[x]])
        scrape(urllist, self._Entry1.get())
    def _on_Button5_ButRel_1(self, Event=None):
        if string.find(self.songlist[self.currentselection2][0][self.currentselection1],'youtube.com/watch') > -1:
            try:
                print '''fetching title of ''' + self.songlist[self.currentselection2][0][self.currentselection1]
                video = pafy.new(self.songlist[self.currentselection2][0][self.currentselection1])
                self.songlist[self.currentselection2][0][self.currentselection1] = video.title + ''' : ''' + video.author
            except IOError:
                self.songlist[self.currentselection2][0][self.currentselection1] = "Video Not Available"
            self._ScrolledListBox2.selection_set(self.currentselection2)
            self._on_ScrolledListBox2_selection()
            print '''Finished'''

    def _on_Button3_ButRel_1(self, Event=None):
        self._ScrolledText1.settext(self._ScrolledText1.get().encode('ascii', 'ignore'))
        self.songlist = []
        self.selectedurllist = []
        songs = self._ScrolledText1.getvalue()
        songs = string.split(songs,'''\n''')
        songs = filter(lambda a: a != u'', songs)
        self._ScrolledListBox2.setlist(songs)
        self.searchapi = self._RadioVar1.get()
        if self.searchapi == 1:
            self._google_search(songs)
        self._ScrolledListBox2.selection_set(0)
        self._on_ScrolledListBox2_selection()
        print 'ready'
    def _on_ScrolledListBox2_selection(self, Event=None):
        if(self._ScrolledListBox2.size() > 0):
            self.currentselection2 = int(self._ScrolledListBox2.curselection()[0])
            namelist = []
            for x in self.songlist[self.currentselection2][0]:
                namelist.append(x)
            self._ScrolledListBox1.setlist(namelist)
    def _on_ScrolledListBox1_selection(self, Event=None):
        if(self._ScrolledListBox1.size() > 0):
            self.currentselection1 = int(self._ScrolledListBox1.curselection()[0])
            self.selectedurllist[self.currentselection2] = self.currentselection1
    def _on_RadioButton2_selection(self, Event=None):
        self._Checkbutton1.config(state=NORMAL)
    def _on_RadioButton1_selection(self, Event=None):
        self._Checkbutton1.config(state=NORMAL)

    #
    #Start of non-Rapyd user code
    #


pass 
#---end-of-form---

    #--------------------------------------------------------------------------#
    # User code should go after this comment so it is inside the "try".        #
    #     This allows rpErrorHandler to gain control on an error so it         #
    #     can properly display a Rapyd-aware error message.                    #
    #--------------------------------------------------------------------------#
def main():
    urls = []
    if len(sys.argv) > 1 and sys.argv[1] == '-csv':
        with open(sys.argv[2], 'rb') as csvfile: 
            csvreader = csv.reader(csvfile)
            csvarray = []
            for row in csvreader:
                csvarray.append(row)
            for row in csvarray:
                for song in row:
                    googsearch = pygoogle(song + ' site:youtube.com/watch')
                    googsearch.pages = 1
                    ytlink = googsearch.get_urls()[0]
                    urls.append(ytlink)
            if len(sys.argv) > 2:
                scrape(urls, sys.argv[2])
            else:
                scrape(urls)
    elif len(sys.argv) > 1 and (sys.argv[1] == '-h' or sys.argv[1] == '-help'):
        print '''Youtube Song Downloader
        Usage examples:
        
        OPEN GUI
        python pysonggui.py
        
        DOWNLOAD FROM CSV FILE
        python pysonggui.py -csv <csv filename> [download directory]
        
        DISPLAY HELP
        python pysonggui.py -h'''
    else:
        Root = Tk()
        Pmw.initialise(Root)
        import Tkinter
        del Tkinter
        App = pysonggui(Root)
        App.pack(expand='yes',fill='both')
        Root.geometry('1000x480+10+10')
        Root.title('Python Youtube Downloader')
        Root.mainloop()

        

    #Adjust sys.path so we can find other modules of this project
import sys
if '.' not in sys.path:
    sys.path.append('.')
#Put lines to import other modules of this project here
    
if __name__ == '__main__':
    main()
    #--------------------------------------------------------------------------#
    # User code should go above this comment.                                  #
    #--------------------------------------------------------------------------#
