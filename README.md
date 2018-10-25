# midiMusicGenerator
A MIDI Music generator based on python-rtmidi implementaton.

### requirements
You will need python3 for this. also preferred is virtualenv and latest version of pip installed.

### setup

1. clone this repo
2. create a python virtual env for python3, and activate it:

```shell
virtualenv -p $(which python3) <repo location>
source <repo location>/bin/activate
```

3. install all of the requirements:

```shell
pip install -r /path/to/repo/requirements.txt
```

4. find the list of available midi devices on your machine via the provided method, and take note of the one you wish to send output to:

```shell
cd src
python listmidiports.py
```

5. set the `MIDI_PORT` environment variable to whatever device you wish to send output to:

```shell
export MIDI_PORT='name of midi port device form step 4'
```

this step is not strictly necessary. If the port is left empty, the output will be sent omni (to all exposed midi devices taking output).

6. run the test to ensure everything is working. your MID output device should be sent a scale as well as some random notes:

```shell
cd src
python test.py
```

### contributing

please feel free to contribute in any way you see fit.
