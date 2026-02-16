import os
import requests
import threading
import time


# ==========================
# CONFIGURATION
# ==========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_FILE = os.path.join(BASE_DIR, "images", "images.txt")
DOWNLOAD_FOLDER = os.path.join(BASE_DIR, "images")


# ==========================
# PART A – Download Function
# ==========================

def download_image(url):
    """
    Downloads a single image from a given URL
    and saves it inside the images folder.
    """

    try:
        response = requests.get(url)
        response.raise_for_status()

        # Extract file name from URL
        file_name = url.split("/")[-1]

        # Add extension if missing
        if "." not in file_name:
            file_name += ".jpg"

        file_path = os.path.join(DOWNLOAD_FOLDER, file_name)

        # Write file as bytes
        with open(file_path, "wb") as file:
            file.write(response.content)

        print(f"Downloaded: {file_name}")

    except Exception as e:
        print(f"Error downloading {url}: {e}")


# ==========================
# Utility Function
# ==========================

def load_urls():
    with open(IMAGES_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]


# ==========================
# PART B – Sequential Download
# ==========================

def sequential_download(urls):
    print("\nStarting Sequential Download...\n")
    start_time = time.perf_counter()

    for url in urls:
        download_image(url)

    end_time = time.perf_counter()
    elapsed = end_time - start_time

    print(f"\nSequential Download Time: {elapsed:.2f} seconds\n")
    return elapsed


# ==========================
# PART C – Threaded Download
# ==========================

def threaded_download(urls):
    print("\nStarting Threaded Download...\n")
    start_time = time.perf_counter()

    threads = []

    for url in urls:
        thread = threading.Thread(target=download_image, args=(url,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    end_time = time.perf_counter()
    elapsed = end_time - start_time

    print(f"\nThreaded Download Time: {elapsed:.2f} seconds\n")
    return elapsed


# ==========================
# MAIN
# ==========================

def main():
    urls = load_urls()

    seq_time = sequential_download(urls)
    thread_time = threaded_download(urls)

    print("========== FINAL RESULT ==========")
    print(f"Sequential Time: {seq_time:.2f} seconds")
    print(f"Threaded Time:   {thread_time:.2f} seconds")

    if thread_time < seq_time:
        print("Threads are faster ✅")
    else:
        print("Sequential is faster ❌")


if __name__ == "__main__":
    main()
