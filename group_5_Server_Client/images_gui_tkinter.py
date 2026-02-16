# Import tkinter module for building GUI
import tkinter as tk

# Import required functions from your main threads file
from group_5_threads_requests import load_urls, threaded_download


# Function that will run when button is clicked
def start_download():
    # Load image URLs from images.txt
    urls = load_urls()

    # Start threaded download process
    threaded_download(urls)


# Create main application window
root = tk.Tk()

# Set window title
root.title("Image Downloader")

# Create a button widget
btn = tk.Button(
    root,                               # Parent window
    text="Download Images (Threaded)",  # Button label
    command=start_download               # Function executed when clicked
)

# Add button to window with padding
btn.pack(padx=20, pady=20)

# Start the GUI event loop (keeps window open)
root.mainloop()
