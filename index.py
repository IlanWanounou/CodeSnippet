"""Main file for the program."""

import threading
from src import listener
from src import window_manager

listener_thread = threading.Thread(target=listener.start_listener)
window_manager_thread = threading.Thread(target=window_manager.create_window)

listener_thread.start()
window_manager_thread.start()

listener_thread.join()
window_manager_thread.join()
