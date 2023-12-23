from flask import Flask, render_template, redirect
import time
import requests
import live

# basic Flask config
config = {
    "DEBUG": True
}

# tell Flask to use the above defined config
app = Flask(__name__)
app.config.from_mapping(config)

# Index Page along with a Cache to keep the leaderboards updated
@app.route('/')
def index():

    set = live.Set()
    set.scan(scan_clip_names=True)
    app.tracks = set.tracks

    return render_template('index.html', 
        tracks=app.tracks
    )

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=8080)
