from battery import MyBattery
import sched, time # run program again and again
import ctypes # starting messagebox
import sys
import psutil # to get info about procssor apps


# ctypes messageBox numbers
MB_OK = 0
MB_OKCANCEL = 1
MB_YESNOCANCEL = 3
MB_YESNO = 4

IDOK = 1
IDCANCEL = 2
IDABORT = 3
IDYES = 6
IDNO = 7


# check if the app is runing in the background(prcessor)
is_app_running = [proc for proc in psutil.process_iter() if 'batterynotifier.exe' in proc.name()]

# if the program is already runnig then show message and let user choose to close app
if len(is_app_running) > 1:
	start_program_window = ctypes.windll.user32.MessageBoxW(None, 'batterynotifier.exe is already working in the background. \n\n Do you want to close BatteryNotifier?', 'Battery Notifier', MB_YESNO)
	if start_program_window == IDYES:
			# find program in the processor and kill the program
			for processor in psutil.process_iter(attrs=['pid','name']):
				if 'batterynotifier.exe' in processor.info['name']:
					processor.kill()
					ctypes.windll.user32.MessageBoxW(None, 'Battery Notifier is Closed now :(', 'Battery Notifier', MB_OK)
	elif start_program_window == IDNO:
			sys.exit()			
			
# if app is not running in the background
else:
	# program started Notification window
	ctypes.windll.user32.MessageBoxW(None, 'Battery Notifier is started successfully in the background! :) \n\nTo close this program, Execute BatteryNotifier again.', 'Battery Notifier', MB_OK)

	# default seconds(0) for program sleep
	seconds = int()

	# set seconds of the program for sleep time
	def set_seconds(sec):
		global seconds 
		seconds = sec


	# main function
	def start():
		obj = MyBattery()
		battery_percentage = obj.get_battery_percentage()
		plugged = obj.get_plugged_status()

		if battery_percentage <= 45 and plugged == False or battery_percentage >= 80 and plugged == True:
			obj.make_sound()

			# set seconds according to ctypes window input
			message = "Warning!!! Your Battery in at "+str(battery_percentage)+"%. \nIt is good practice to have battery between 40% to 80%. \n\nRemind me in 2 minutes?"
			MessageBox = ctypes.windll.user32.MessageBoxW(None, message, 'Battery Reminder', MB_YESNO)
			if MessageBox == IDYES:
				set_seconds(200)
			elif MessageBox == IDNO:
				set_seconds(1200)
		else:
			# set 20min(seconds)
			set_seconds(1200)




	if __name__ == '__main__':
		while True:
			program = sched.scheduler(time.time, time.sleep)
			program.enter(seconds, 1, start)
			program.run()





