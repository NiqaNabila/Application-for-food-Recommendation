# import os
# import sys
# from os.path import dirname, realpath, join, expanduser
# from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem
# from PyQt5.uic import loadUiType
# import pandas as pd


# scriptDir = dirname(realpath(__file__))
# From_Main, _ = loadUiType(join(dirname(__file__), "Main.ui"))

# class MainWindow(QWidget, From_Main):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         # QWidget.__init__(self)
#         self.setupUi(self)

#         self.ButtonOpen.clicked.connect(self.OpenFile)
#         self.BtnDescribe.clicked.connect(self.dataHead)
#         self.all_data = pd.DataFrame() # menggunakan panda
        
#     # def OpenFile(self):
#     #     try:
#     #         path = QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')[0]
#     #         self.all_data = pd.read_csv(path)
#     #     except:
#     #         print(path)

#     def OpenFile(self):
#         try:
#             # Use expanduser to get the user's home directory in a cross-platform manner
#             home_dir = r"C:\Users\niqan\OneDrive\Documents\Semester 4\Proyek 2\TUBES\GUI\Data-Analyze-in-gui-Pyqt5-python-main\Data-Analyze-in-gui-Pyqt5-python-main"
#             path, _ = QFileDialog.getOpenFileName(self, 'Open CSV', home_dir, 'CSV(*.csv)')
#             if path:
#                 print(f"Selected file path: {path}")  # Debugging line
#                 self.all_data = pd.read_csv(path)
#                 print("File loaded successfully")
#                 print(self.all_data.head())  # Print first few rows of the data for debugging
#             else:
#                 print("No file selected")
#         except Exception as e:
#             print(f"Error loading file: {e}")  # Improved error message

#     def dataHead(self):
#         try:
#             numColomn = self.spinBox.value()
#             if numColomn == 0:
#                 NumRows = len(self.all_data.index)
#             else:
#                 NumRows = numColomn
                
#             self.tableWidget.setColumnCount(len(self.all_data.columns))
#             self.tableWidget.setRowCount(NumRows)
#             self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

#             for i in range(NumRows):
#                 for j in range(len(self.all_data.columns)):
#                     self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

#             self.tableWidget.resizeColumnsToContents()
#             self.tableWidget.resizeRowsToContents()
#         except Exception as e:
#             print(f"Error displaying data: {e}")

# app = QApplication(sys.argv)
# sheet = MainWindow()
# sheet.show()
# sys.exit(app.exec_())

# 1

# import os
# import sys
# import csv
# from os.path import dirname, realpath, join, expanduser
# from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem
# from PyQt5.QtGui import QStandardItem
# from PyQt5.uic import loadUiType
# import pandas as pd


# scriptDir = dirname(realpath(__file__))
# From_Main, _ = loadUiType(join(dirname(__file__), "Main.ui"))

# class MainWindow(QWidget, From_Main):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         # QWidget.__init__(self)
#         self.setupUi(self)

#         self.ButtonOpen.clicked.connect(self.loadCsv)
#         self.BtnDescribe.clicked.connect(self.dataHead)
#         self.all_data = pd.DataFrame() # menggunakan panda
        
#     # def OpenFile(self):
#     #     try:
#     #         path = QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')[0]
#     #         self.all_data = pd.read_csv(path)
#     #     except:
#     #         print(path)

#     # def OpenFile(self):
#     #     try:
#     #         # Use expanduser to get the user's home directory in a cross-platform manner
#     #         home_dir = r"C:\Users\niqan\OneDrive\Documents\Semester 4\Proyek 2\TUBES\GUI\Data-Analyze-in-gui-Pyqt5-python-main\Data-Analyze-in-gui-Pyqt5-python-main"
#     #         path, _ = QFileDialog.getOpenFileName(self, 'Open CSV', home_dir, 'CSV(*.csv)')
#     #         if path:
#     #             print(f"Selected file path: {path}")  # Debugging line
#     #             self.all_data = pd.read_csv(path)
#     #             print("File loaded successfully")
#     #             print(self.all_data.head())  # Print first few rows of the data for debugging
#     #         else:
#     #             print("No file selected")
#     #     except Exception as e:
#     #         print(f"Error loading file: {e}")  # Improved error message

#     def loadCsv(self):
#         fileName = 'C:/Users/niqan/OneDrive/Documents/Semester 4/Proyek 2/TUBES/GUI/Data-Analyze-in-gui-Pyqt5-python-main/Data-Analyze-in-gui-Pyqt5-python-main/Ayam.csv'
#         with open(fileName, "r") as fileInput:
#             for row in csv.reader(fileInput):    
#                 items = [
#                     QtGui.QStandardItem(field)
#                     for field in row
#                 ]
#                 self.model.appendRow(items)


#     def dataHead(self):
#         try:
#             numColomn = self.spinBox.value()
#             if numColomn == 0:
#                 NumRows = len(self.all_data.index)
#             else:
#                 NumRows = numColomn
                
#             self.tableWidget.setColumnCount(len(self.all_data.columns))
#             self.tableWidget.setRowCount(NumRows)
#             self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

#             for i in range(NumRows):
#                 for j in range(len(self.all_data.columns)):
#                     self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

#             self.tableWidget.resizeColumnsToContents()
#             self.tableWidget.resizeRowsToContents()
#         except Exception as e:
#             print(f"Error displaying data: {e}")

# app = QApplication(sys.argv)
# sheet = MainWindow()
# sheet.show()
# sys.exit(app.exec_())

# 2
# import sys
# import csv
# from os.path import dirname, realpath, join
# from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
# from PyQt5.uic import loadUiType
# import pandas as pd


# scriptDir = dirname(realpath(__file__))
# From_Main, _ = loadUiType(join(dirname(__file__), "Main.ui"))

# class MainWindow(QWidget, From_Main):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setupUi(self)

#         self.ButtonOpen.clicked.connect(self.loadCsv)
#         self.BtnDescribe.clicked.connect(self.dataHead)
#         self.all_data = pd.DataFrame()  # using pandas

#     def loadCsv(self):
#         # fileName = "C:/Users/niqan/OneDrive/Documents/Semester 4/Proyek 2/TUBES/GUI/Data-Analyze-in-gui-Pyqt5-python-main/Data-Analyze-in-gui-Pyqt5-python-main/Ayam.csv"
#         try:
#             with open("C:/Users/niqan/OneDrive/Documents/Semester 4/Proyek 2/TUBES/GUI/Data-Analyze-in-gui-Pyqt5-python-main/Data-Analyze-in-gui-Pyqt5-python-main/Ayam.csv", "r") as fileInput:
#                 csv_reader = csv.reader(fileInput)
#                 headers = next(csv_reader)
                
#                 self.tableWidget.setColumnCount(len(headers))
#                 self.tableWidget.setHorizontalHeaderLabels(headers)

#                 self.tableWidget.setRowCount(0)
#                 for row_data in csv_reader:
#                     row = self.tableWidget.rowCount()
#                     self.tableWidget.insertRow(row)
#                     for column, data in enumerate(row_data):
#                         item = QTableWidgetItem(data)
#                         self.tableWidget.setItem(row, column, item)
#         except Exception as e:
#             print(f"Error loading CSV file: {e}")

#     def dataHead(self):
#         try:
#             numColomn = self.spinBox.value()
#             if numColomn == 0:
#                 NumRows = len(self.all_data.index)
#             else:
#                 NumRows = numColomn

#             self.tableWidget.setColumnCount(len(self.all_data.columns))
#             self.tableWidget.setRowCount(NumRows)
#             self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

#             for i in range(NumRows):
#                 for j in range(len(self.all_data.columns)):
#                     self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

#             self.tableWidget.resizeColumnsToContents()
#             self.tableWidget.resizeRowsToContents()
#         except Exception as e:
#             print(f"Error displaying data: {e}")

# app = QApplication(sys.argv)
# sheet = MainWindow()
# sheet.show()
# sys.exit(app.exec_())

# 3
# import sys
# import csv
# from os.path import dirname, realpath, join
# from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidgetItem
# from PyQt5.uic import loadUiType
# import pandas as pd

# scriptDir = dirname(realpath(__file__))
# From_Main, _ = loadUiType(join(dirname(__file__), "Main.ui"))

# class MainWindow(QWidget, From_Main):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setupUi(self)

#         self.ButtonOpen.clicked.connect(self.loadCsv)
#         self.BtnDescribe.clicked.connect(self.dataHead)
#         self.all_data = pd.DataFrame()  # using pandas

#     def loadCsv(self):
#         try:
#             # Open a file dialog to select the CSV file
#             fileName, _ = QFileDialog.getOpenFileName(self, 'Open CSV', '', 'CSV(*.csv)')
#             if fileName:
#                 # Read the CSV file using pandas
#                 self.all_data = pd.read_csv(fileName)
                
#                 # Display the data in the QTableWidget
#                 self.tableWidget.setColumnCount(len(self.all_data.columns))
#                 self.tableWidget.setRowCount(len(self.all_data.index))
#                 self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

#                 for i in range(len(self.all_data.index)):
#                     for j in range(len(self.all_data.columns)):
#                         self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))
                
#                 self.tableWidget.resizeColumnsToContents()
#                 self.tableWidget.resizeRowsToContents()
#             else:
#                 print("No file selected")
#         except Exception as e:
#             print(f"Error loading CSV file: {e}")

#     def dataHead(self):
#         try:
#             numColomn = self.spinBox.value()
#             if numColomn == 0:
#                 NumRows = len(self.all_data.index)
#             else:
#                 NumRows = numColomn

#             self.tableWidget.setColumnCount(len(self.all_data.columns))
#             self.tableWidget.setRowCount(NumRows)
#             self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

#             for i in range(NumRows):
#                 for j in range(len(self.all_data.columns)):
#                     self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

#             self.tableWidget.resizeColumnsToContents()
#             self.tableWidget.resizeRowsToContents()
#         except Exception as e:
#             print(f"Error displaying data: {e}")

# app = QApplication(sys.argv)
# sheet = MainWindow()
# sheet.show()
# sys.exit(app.exec_())

#4
import sys
from os.path import dirname, realpath, join
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidgetItem
from PyQt5.uic import loadUiType
import pandas as pd

# Load UI file
scriptDir = dirname(realpath(__file__))
From_Main, _ = loadUiType(join(scriptDir, "Main.ui"))

class MainWindow(QWidget, From_Main):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.ButtonOpen.clicked.connect(self.loadCsv)
        self.BtnDescribe.clicked.connect(self.dataHead)
        self.all_data = pd.DataFrame()  # Initialize as an empty DataFrame

    def loadCsv(self):
        try:
            # Open a file dialog to select the CSV file
            fileName, _ = QFileDialog.getOpenFileName(self, 'Open CSV', scriptDir, 'CSV(*.csv)')
            if fileName:
                print(f"Selected file: {fileName}")  # Debug statement
                # Read the CSV file using pandas
                self.all_data = pd.read_csv(fileName)
                print("CSV loaded successfully")  # Debug statement
                print(self.all_data.head())  # Print first few rows of the data for debugging
                
                # Display the data in the QTableWidget
                self.tableWidget.setColumnCount(len(self.all_data.columns))
                self.tableWidget.setRowCount(len(self.all_data.index))
                self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

                for i in range(len(self.all_data.index)):
                    for j in range(len(self.all_data.columns)):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))
                
                self.tableWidget.resizeColumnsToContents()
                self.tableWidget.resizeRowsToContents()
            else:
                print("No file selected")
        except Exception as e:
            print(f"Error loading CSV file: {e}")

    def dataHead(self):
        try:
            numColomn = self.spinBox.value()
            if numColomn == 0:
                NumRows = len(self.all_data.index)
            else:
                NumRows = numColomn

            self.tableWidget.setColumnCount(len(self.all_data.columns))
            self.tableWidget.setRowCount(NumRows)
            self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

            for i in range(NumRows):
                for j in range(len(self.all_data.columns)):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()
        except Exception as e:
            print(f"Error displaying data: {e}")

app = QApplication(sys.argv)
sheet = MainWindow()
sheet.show()
sys.exit(app.exec_())
