import tkinter as tk
from tkinter import messagebox
import lyricsgenius

genius = lyricsgenius.Genius("your_access_token")


def get_lyrics():
    artist = label1.get()
    song = label2.get()
    try:
        song1 = genius.search_song(song, artist)
        lyrics.delete(1.0, tk.END)
        lyrics.insert(tk.END, song1.lyrics)
    except:
        messagebox.showerror("Error", f"Could not fetch lyrics: {e}")


root = tk.Tk()
root.title("Lyrics Finder")


label1=tk.Label(root, text="Artist Name:",font=("ROG Fonts",15)).grid(row=0, column=0, padx=10, pady=10)
label1= tk.Entry(root, width=40)
label1.grid(row=0, column=1, padx=10, pady=10)

label2=tk.Label(root, text="Song Title:",font=("ROG Fonts",15)).grid(row=1, column=0, padx=10, pady=10)
label2= tk.Entry(root, width=40)
label2.grid(row=1, column=1, padx=10, pady=10)

label3 = tk.Button(root, text="Get Lyrics",font=("ROG Fonts",15), command=get_lyrics,bg='blue',fg='white')
label3.grid(row=2, column=0, columnspan=2, pady=10)

lyrics = tk.Text(root, wrap='word', width=60, height=20)
lyrics.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
