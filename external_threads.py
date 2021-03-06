import queue
import blueP


blueClass = blueP.Blue()

def get_headsets_devices(queue, event):
    if event.is_set() == True:
        blueClass.get_bluetooth_devices()
        queue.put("OK")
        event.clear()

def get_battery_level(queue, event, selected_device):
    if event.is_set() == True:
        battery_level = blueClass.get_battery_level(selected_device)
        queue.put(battery_level)
        event.clear()