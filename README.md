# Layout and OCR Shootout

Initial setup is complicated by upstream package issues, but this (or something like it) should work for creating a clean environment and installing the necessary libraries:

```
python3 -m venv local
source local/bin/activate
pip install pip==23.0.1
pip install torch
pip install -r requirements.txt
pip install git+https://github.com/nikhilweee/iopath
```

It may take a while (tens of minutes?) to compile and install all the necessities.  You can then run all experiments with:

```
scons -Q
```
