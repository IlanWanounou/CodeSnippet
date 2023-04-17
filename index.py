from src import listener
from src import window_manager
import threading

listener_thread = threading.Thread(target=listener.start_listener)
window_manager_thread = threading.Thread(target=window_manager.createWindow)

listener_thread.start()
window_manager_thread.start()

listener_thread.join()
window_manager_thread.join()