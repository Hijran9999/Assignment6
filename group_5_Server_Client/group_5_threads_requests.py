# Import operating system utilities (for file paths)
import os

# Import requests library to download files from the internet
import requests

# Import threading module to run downloads in parallel
import threading

# Import time module to measure execution time
import time


# ==========================
# CONFIGURATION SECTION
# ==========================

# Get the absolute path of the current Python file directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build full path to images.txt file inside images folder
IMAGES_FILE = os.path.join(BASE_DIR, "images", "images.txt")

# Define the folder where downloaded images will be saved
DOWNLOAD_FOLDER = os.path.join(BASE_DIR, "images")


# ==========================
# PART A – DOWNLOAD FUNCTION
# ==========================

def download_image(url):
    """
    This function downloads a single image from a URL
    and saves it into the images folder.
    """

    try:
        # Send HTTP GET request to download the image content
        response = requests.get(url)

        # Raise error if request failed (e.g., 404, 500)
        response.raise_for_status()

        # Extract the last part of URL to use as file name
        file_name = url.split("/")[-1]

        # If URL has no file extension, add .jpg by default
        if "." not in file_name:
            file_name += ".jpg"

        # Create full path for saving the file
        file_path = os.path.join(DOWNLOAD_FOLDER, file_name)

        # Open file in binary write mode
        with open(file_path, "wb") as file:
            # Write downloaded bytes into file
            file.write(response.content)

        # Print confirmation message
        print(f"Downloaded: {file_name}")

    except Exception as e:
        # Print error message if something goes wrong
        print(f"Error downloading {url}: {e}")


# ==========================
# UTILITY FUNCTION
# ==========================

def load_urls():
    # Open the images.txt file in read mode
    with open(IMAGES_FILE, "r") as f:
        # Read each line, remove spaces/newlines, ignore empty lines
        return [line.strip() for line in f if line.strip()]


# ==========================
# PART B – SEQUENTIAL DOWNLOAD
# ==========================

def sequential_download(urls):
    # Print start message
    print("\nStarting Sequential Download...\n")

    # Record starting time
    start_time = time.perf_counter()

    # Loop through URLs one by one
    for url in urls:
        # Download each image sequentially
        download_image(url)

    # Record ending time
    end_time = time.perf_counter()

    # Calculate total elapsed time
    elapsed = end_time - start_time

    # Print total time taken
    print(f"\nSequential Download Time: {elapsed:.2f} seconds\n")

    # Return elapsed time for comparison
    return elapsed


# ==========================
# PART C – THREADED DOWNLOAD
# ==========================

def threaded_download(urls):
    # Print start message
    print("\nStarting Threaded Download...\n")

    # Record starting time
    start_time = time.perf_counter()

    # Create empty list to store threads
    threads = []

    # Loop through each URL
    for url in urls:
        # Create a new thread that runs download_image function
        thread = threading.Thread(target=download_image, args=(url,))

        # Start the thread
        thread.start()

        # Add thread to list
        threads.append(thread)

    # Wait for all threads to complete before continuing
    for thread in threads:
        thread.join()

    # Record ending time
    end_time = time.perf_counter()

    # Calculate total elapsed time
    elapsed = end_time - start_time

    # Print total time taken
    print(f"\nThreaded Download Time: {elapsed:.2f} seconds\n")

    # Return elapsed time for comparison
    return elapsed


# ==========================
# MAIN FUNCTION
# ==========================

def main():
    # Load all image URLs from file
    urls = load_urls()

    # Run sequential download and store time
    seq_time = sequential_download(urls)

    # Run threaded download and store time
    thread_time = threaded_download(urls)

    # Print comparison results
    print("========== FINAL RESULT ==========")
    print(f"Sequential Time: {seq_time:.2f} seconds")
    print(f"Threaded Time:   {thread_time:.2f} seconds")

    # Check which method is faster
    if thread_time < seq_time:
        print("Threads are faster ✅")
    else:
        print("Sequential is faster ❌")


# Run main function only if this file is executed directly
if __name__ == "__main__":
    main()
