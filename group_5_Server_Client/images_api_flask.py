from flask import Flask, jsonify
from group_5_threads_requests import load_urls, threaded_download

app = Flask(__name__)

@app.route("/download")
def download():
    urls = load_urls()
    time_taken = threaded_download(urls)
    return jsonify({
        "message": "Download completed",
        "time_taken": time_taken
    })

if __name__ == "__main__":
    app.run(debug=True)
