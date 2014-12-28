youtubesongscraper
by Jason Giancono jasongi.com/
==================

Tool (with GUI or import from CSV) for easy downloading youtube songs in bulk

##Installation Instructions
You need have python (2.x.x) unless you are using the cx_freeze version. The cx_freeze version should work on windows.

##How it works
youtubesongscraper uses pafy and pygoogle to simplify downloading multiple youtube video audio (eg when you want to download a custom playlist. It does a google search for the terms you write in edit box and then you can select the youtube video to download.

Because it uses an old google API, the amount of queries is limited and do too many you may be blocked from the api.

##Using the program
1. Open pysonggui

2. Choose the directory to download things to (if the directory does not exist it will be created

3. Write a list of the songs you wish to download in the text box in the left. The most effective method is to use a method of *<artist> -- <song title*>*

4. Press the refresh button. This does a google search for each item and populates the **Select Song** and **Select Youtube Search Match** box.

5. If Google Quick Mode is selected, only the title of the first hit for each song will be displayed. You can fetch other titles by clicking on the youtube like and pressing **Resolve Title**. This is so it loads quicker.

6. If you want to visit the page to listen to the song, press **Visit URL**

7. Go through each song on the **Select Song** list, pick a youtube video from the **Select Youtube Search Match** box for each one and then you can download them by pressing **Download All**

8. If none of the 4 retrieved links are the song, you can widen the search by changing the **Pages to Download** number.

9. Alternatively, if you have you song list in a csv file, and are 'Feeling Lucky', you can YOLO download the first hit for each of the entries in the csv file via the command line

See usage below

#Open GUI
```bash
python pysonggui.py
```

#Download from CSV
```bash
python pysonggui.py -csv <csv filename> [download directory]
```

#Display Help
```bash
python pysonggui.py -h
```
