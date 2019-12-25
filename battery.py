import psutil # for getting bettary info
import datetime # for converting seconds to hours, with timedate.timedelta
import os # for getting beep file from the os
import winsound # for beep or sound in the program
# function and setting for the sound from the sound folder
from sound import Sound 




class MyBattery:
    """
    Class MyBattery
    :author: Umer khan <https://github.com/umerk4466>
    :description:

    Allows you to get your device 
    battery status also provided some
    functions from Sound Class.
    """
        # get betterty percentage
    def get_battery_percentage(self):
        # battary obj from the module psutil
        battery = psutil.sensors_battery() 
        percent = battery.percent
        return(percent)

    # get betterty plugged status
    def get_plugged_status(self):
        # battary obj from the module psutil
        battery = psutil.sensors_battery() 
        plugged = battery.power_plugged
        return(plugged)

        # get remaining time
    def get_battery_time_left(self):
        # battary obj from the module psutil
        battery = psutil.sensors_battery() 
        hours = datetime.timedelta(seconds= battery.secsleft)
        return(hours)

        # make sound with the specified file name
    def make_sound(self):
        # befor beep increase the volume to the end
        Sound.volume_max()
        # in the current directory ther is the file name sound.wav to play
        return winsound.PlaySound(os.path.abspath("custom_beep.wav"), winsound.SND_FILENAME | winsound.SND_ALIAS)

        # make beep sound
    def make_beep_sound(self):
        # befor beep increase the volume to the end
        Sound.volume_max()
        return winsound.Beep(2700, 1000)

