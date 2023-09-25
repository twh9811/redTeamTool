Preqrequisites
=============
- python3 must be installed on the machine
- A sudoer or root account must be used to run the script

DEPENDENCIES
=============
- The script only uses standard libraries so nothing else needs to be installed
- Permissions of the file may need to be changed depending on the system configuration/setup 

How to run?
=============
python TrafficClassifier.py &

- Using & will let the process run in the background and not require the terminal to stay open and is recommended

- For testing purposes you can reduce the wait time to something shorter.

- You can prevent disabling core services (if you want) by putting them in the DONT_TOUCH list before running the script.