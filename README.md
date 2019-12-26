# BatteryNotifier
This Program will remind you when to plug in or plug off the charger of your laptop to maintain healthy battery.
After executing program, this will run in the background and will keep checking given below conditions after every 20 minutes:
* Battery is less then 45% and charger is not plugged in.
* Battery is more than 80% and charger is plugged in.

if any of the above condition is true then program will send you reminder window with beep.

## Getting Started

#### Prerequisites
To run in this program you need to have installed:
* **Python version:** Python >= v3.5 [Install Python](https://www.python.org/downloads/)
* **Python module:** psutil
```
pip install psutil
```
### How to Run this program in Windows
Open cmd and go to the directory of this program and run
```
C:\Users\USERNAME\PROGRAM_DIR>main.py
```
## From where to get full Executable(.exe) of this program?
It is in the releases of this repository [Download full executable(.exe) here](https://github.com/umerk4466/BatteryNotifier/releases)

## Specifications
* **Tested on:** Windows 10

## Authors

* **Umer Khan** - *Initial work* - [umerk4466](https://github.com/umerk4466)

## License

This project is licensed under the MIT License - see the **LICENSE.md** file for details

## Links

* [Windows sound class Credit](https://github.com/Paradoxis)
