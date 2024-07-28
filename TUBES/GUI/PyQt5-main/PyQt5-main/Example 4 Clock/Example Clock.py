# from PyQt5.QtCore import QTime, QTimer
# from PyQt5 import QtWidgets, uic

# # Corrected file path
# ui_file_path = r"C:\Users\niqan\OneDrive\Documents\Semester 4\Proyek 2\TUBES\GUI\PyQt5-main\PyQt5-main\Example 4 Clock\Example 4 Clock.ui"

# app = QtWidgets.QApplication([])
# ui = uic.loadUi(ui_file_path)

# def clock():
#     currentTime = QTime.currentTime()           # Get current time
#     currentTimeText = currentTime.toString('hh:mm:ss')  # Convert to string
#     ui.lcdClock.display(currentTimeText)        # Display on LCD

# timer = QTimer()               # Create timer
# timer.timeout.connect(clock)    # Connect to clock function
# timer.start(1000)               # Start timer, update every second

# ui.show()   # Show UI
# app.exec()  # Run app
