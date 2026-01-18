from winotify import Notification

from time import sleep

def send_notification(title, message, sound=False):
    toast = Notification(
        app_id="Eye Care Reminder",
        title=title,
        msg=message,
        duration="short",
    )
    if sound:
        toast.set_audio("ms-winsoundevent:Notification.Reminder", loop=False)
    toast.show()
    
if __name__ == "__main__":
    send_notification("Hi!", "Eye Care Reminder is running!")
    while True:
        sleep(1200)
        send_notification("20 minutes 20 seconds", "Look into the distance for 20 seconds", sound=True)
        sleep(20)
