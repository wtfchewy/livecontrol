<a target="_blank"> <img src="https://i.ibb.co/Hrph97t/github-1.png" alt="Banner"/></a>

# liveControl - WORK IN PROGRESS
Was in need of a way to control my Ableton LIVE from my phone in a way similar to Reapers solution. I came across a few solutions to this but in discovering of these options I thought to myself, "these fucking blow" and here we are.


# Local Development

### Install AbletonOSC
- [Download a zip of AbletonOSC](https://github.com/ideoforms/AbletonOSC/archive/refs/heads/master.zip), unzip its contents, and rename `AbletonOSC-master` to `AbletonOSC`
- Install it following the instructions on
  Ableton's [Installing third-party remote scripts](https://help.ableton.com/hc/en-us/articles/209072009-Installing-third-party-remote-scripts)
  doc, by copying the `AbletonOSC` folder to:
    - **Windows**: `\Users\[username]\Documents\Ableton\User Library\Remote Scripts`
    - **macOS**: `Macintosh HD/Users/[username]/Music/Ableton/User Library/Remote Scripts`
- Restart Live
- In `Preferences > Link / Tempo / MIDI`, under the Control Surface dropdown, select the new "AbletonOSC" option. Live should display a message
  saying "AbletonOSC: Listening for OSC on port 11000"

```console
# Install Depends
$ pip install -r requirements.txt

# Run the Flask Webserver
$ python3 index.py

```

# Preview
<a target="_blank"> <img src="https://i.ibb.co/yhn1SmW/127-0-0-1-8080.jpg" alt="Preview"/></a>
