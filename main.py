from plyer import notification
from time import sleep
import ctypes

# Constants for Windows API
user32 = ctypes.windll.User32
DESKTOP_SWITCHDESKTOP = 0x0100

class Pc:
    def __init__(self):
        self.__status = "ON"
    
    def get_status(self):
        if self.is_workstation_locked():
            self.__status = "OFF"
            
        return self.__status
    
    @staticmethod
    def is_workstation_locked():
        if (user32.GetForegroundWindow() % 10 == 0):
            return True
        return False
        

class User:
    def __init__(self):
        self.__active = True
    
    def is_active(self):
        self.update_activity()
        return self.__active
    
    def update_activity(self):
        pc = Pc()
        if pc.get_status() == "OFF":
            self.__active = False
        else:
            self.__active = True
        return self.__active

class NotificationManager:
    def __init__(self, title, message):
        self.title = title
        self.message = message
        self.__app_name = "Eye Care Reminder"
        self.__timeout = 20

    def send_notification(self):
        notification.notify(
            title=self.title,
            message=self.message,
            app_name=self.__app_name,
            timeout=self.__timeout
        )
  
    
if __name__ == "__main__":
    user = User()
    notifier = NotificationManager("20 Minutes 20 Seconds", "Time to look away for 20 seconds!")
    
    while True:
        i = 0
        time_for_reset = 20
        while i < 600:
            time_for_reset = 20
            print(i, end="\r")
            sleep(2)
            print("\n", user.is_active())
            
            while not user.is_active():
                sleep(2)
                time_for_reset -= 2
                print("Waiting for user to be active again...", time_for_reset)
                if time_for_reset <= 0:
                    i = 0
            if time_for_reset < 20:
                i += 20 - time_for_reset // 2
            
            i += 1
        notifier.send_notification()
