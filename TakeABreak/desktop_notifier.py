import time
import notify2

notify2.init("Break Notifier")
notification = notify2.Notification(summary="Take a Break", message="I am going to sleep in 10 seconds")
notification.set_urgency(notify2.URGENCY_NORMAL)
notification.set_timeout(500)
notification.show()