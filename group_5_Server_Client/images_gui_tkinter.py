import tkinter as tk
from group_5_threads_requests import load_urls, threaded_download

def start_download():
    urls = load_urls()
    threaded_download(urls)

root = tk.Tk()
root.title("Image Downloader")

btn = tk.Button(root, text="Download Images (Threaded)", command=start_download)
btn.pack(padx=20, pady=20)

root.mainloop()
