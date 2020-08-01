from pytube import *
from tkinter import *
from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *

# File size variable
file_size = 0

# Download progress function


def downloadingProgress(stream=None, chunk=None, remaining=None):
    # Getting percentage download file
    file_downloaded = (file_size - remaining)
    per = (file_downloaded / file_size) * 100
    dBtn.config(text="{:00.0f} % Downloaded".format(per))


def startDownloading():
    global file_size
    try:
        url = urlField.get()
        dBtn.config(text='Please wait..')
        dBtn.config(state=DISABLED)
        save_place = askdirectory()
        if save_place is None:
            return
        # Youtube object with url parameter
        ob = YouTube(url, on_progress_callback=downloadingProgress)
        strms = ob.streams.get_by_itag('22')
        file_size = strms.filesize
        videoTitle.config(text=strms.title)
        videoTitle.pack(side=TOP)
        # Video downloadng
        strms.download(save_place)
        dBtn.config(state=NORMAL)
        dBtn.config(text='Start Downloading')
        urlField.delete(0, END)
        videoTitle.pack_forget()
        showinfo("Success", "Video Downloaded")

    except Exception as e:
        print(e)
        print("Error!")

# Download Thread


def startDownloadThread():
    thread = Thread(target=startDownloading)
    thread.start()


# GUI design code start
main = Tk()

main.title('TubeDownloader')
main.iconbitmap('icon.ico')
main.geometry("1000x300")
file = PhotoImage(file='logo.png')
headingIcon = Label(main, image=file)
headingIcon.pack(side=TOP, pady=10)
urlField = Entry(main)
urlField.pack(side=TOP, fill=X, pady=10)
dBtn = Button(main, text="Start Downloading!",
              font=("verdana", 15), relief='ridge', command=startDownloadThread)
dBtn.pack(side=TOP, pady=10)
videoTitle = Label(main, text="Video Title", font=("verdana", 18))
# videoTitle.pack(side=TOP)
author = Label(main, text="Moiz Sharif", font=(
    "verdana", 12))
author.pack(side=BOTTOM)
main.mainloop()
# GUI design code end
