# Python-LYRICS-Extractor
This project is a simple Tkinter-based application that allows users to search for and display song lyrics using the Genius API. Users can input the artist's name and song title, and the application retrieves the corresponding lyrics.

## Code Explanation

### Imports
```python
import tkinter as tk
from tkinter import messagebox
import lyricsgenius
```
- tkinter: This library is used for creating the graphical user interface (GUI).
- messagebox: This module is used to display error messages.
- lyricsgenius: This library interacts with the Genius API to fetch song lyrics.

###Genius API Setup
```python
genius = lyricsgenius.Genius("your_access_token")
```
- An instance of the Genius class is created using your access token. You need to replace "your_access_token" with a valid token obtained from the Genius API.

### Function to Fetch Lyrics
```python
def get_lyrics():
    artist = label1.get()
    song = label2.get()
    try:
        song1 = genius.search_song(song, artist)
        lyrics.delete(1.0, tk.END)
        lyrics.insert(tk.END, song1.lyrics)
    except Exception as e:
        messagebox.showerror("Error", f"Could not fetch lyrics: {e}")
```
- This function retrieves the artist and song title from the input fields.
- It calls genius.search_song() to find the lyrics.
- If successful, it clears any previous lyrics in the Text widget and displays the new lyrics.
- If an error occurs (e.g., if the song is not found), an error message is displayed.

### Creating the Main Window
```python
root = tk.Tk()
root.title("Lyrics Finder")
```
- A Tkinter window is created and titled "Lyrics Finder".

### Input Fields

#### Artist Name Input
```python
label1 = tk.Label(root, text="Artist Name:", font=("ROG Fonts", 15)).grid(row=0, column=0, padx=10, pady=10)
label1 = tk.Entry(root, width=40)
label1.grid(row=0, column=1, padx=10, pady=10)
```
- A label and an entry field are created for the artist name.

#### Song Title Input
```python
label2 = tk.Label(root, text="Song Title:", font=("ROG Fonts", 15)).grid(row=1, column=0, padx=10, pady=10)
label2 = tk.Entry(root, width=40)
label2.grid(row=1, column=1, padx=10, pady=10)
```
- A label and an entry field for the song title.

### Get Lyrics Button
```python
label3 = tk.Button(root, text="Get Lyrics", font=("ROG Fonts", 15), command=get_lyrics, bg='blue', fg='white')
label3.grid(row=2, column=0, columnspan=2, pady=10)
```
- A button is created to trigger the get_lyrics() function when clicked.

### Text Area for Lyrics Display
```python
lyrics = tk.Text(root, wrap='word', width=60, height=20)
lyrics.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
```
-A Text widget is created to display the fetched lyrics, with word wrapping and specified dimensions.

### Running the Application
```python
root.mainloop()
```
- This line starts the Tkinter event loop, allowing the application to respond to user actions.

## Conclusion
This Lyrics Finder application provides a user-friendly interface for accessing song lyrics through the Genius API. You can enhance this application by adding features like saving lyrics, searching by album, or improving error handling.

## Sample Output
<br>
<img src="https://github.com/user-attachments/assets/fb2adf74-da84-4e9e-8093-e34e40d86042" alt="ARDUINO UNO"  width="50%">
