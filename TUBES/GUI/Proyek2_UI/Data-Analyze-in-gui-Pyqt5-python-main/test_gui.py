# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QSpinBox
# from PyQt5.uic import loadUiType
# import pandas as pd

# # Define a basic UI for testing
# class MainWindow(QWidget):
#     def __init__(self):
#         super(MainWindow, self).__init__()

#         # Basic UI layout for testing
#         self.layout = QVBoxLayout(self)
        
#         self.ButtonOpen = QPushButton('Open CSV', self)
#         self.BtnDescribe = QPushButton('Describe Data', self)
#         self.spinBox = QSpinBox(self)
#         self.tableWidget = QTableWidget(self)
        
#         self.layout.addWidget(self.ButtonOpen)
#         self.layout.addWidget(self.BtnDescribe)
#         self.layout.addWidget(self.spinBox)
#         self.layout.addWidget(self.tableWidget)
        
#         self.ButtonOpen.clicked.connect(self.loadCsv)
#         self.BtnDescribe.clicked.connect(self.dataHead)
#         self.all_data = pd.DataFrame()  # Initialize as an empty DataFrame

#     def loadCsv(self):
#         try:
#             fileName, _ = QFileDialog.getOpenFileName(self, 'Open CSV', '', 'CSV(*.csv)')
#             if fileName:
#                 print(f"Selected file: {fileName}")
#                 self.all_data = pd.read_csv(fileName)
#                 print("CSV loaded successfully")
#                 print(self.all_data.head())
                
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

# 1

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QSpinBox
# import pandas as pd

# class MainWindow(QWidget):
#     def __init__(self):
#         super(MainWindow, self).__init__()

#         # Basic UI layout for testing
#         self.layout = QVBoxLayout(self)
        
#         self.ButtonOpen = QPushButton('Open CSV', self)
#         self.BtnDescribe = QPushButton('Describe Data', self)
#         self.spinBox = QSpinBox(self)
#         self.tableWidget = QTableWidget(self)
        
#         self.layout.addWidget(self.ButtonOpen)
#         self.layout.addWidget(self.BtnDescribe)
#         self.layout.addWidget(self.spinBox)
#         self.layout.addWidget(self.tableWidget)
        
#         self.ButtonOpen.clicked.connect(self.loadCsv)
#         self.BtnDescribe.clicked.connect(self.dataHead)
#         self.all_data = pd.DataFrame()  # Initialize as an empty DataFrame

#     def loadCsv(self):
#         try:
#             # Open a file dialog to select the CSV file
#             fileName, _ = QFileDialog.getOpenFileName(self, 'Open CSV', '', 'CSV(*.csv)')
#             if fileName:
#                 print(f"Selected file: {fileName}")
#                 # Try reading the CSV file with a different encoding
#                 try:
#                     self.all_data = pd.read_csv(fileName, encoding='latin1')
#                 except Exception as e:
#                     print(f"Error with latin1 encoding: {e}")
#                     # Attempt with another encoding
#                     self.all_data = pd.read_csv(fileName, encoding='iso-8859-1')

#                 print("CSV loaded successfully")
#                 print(self.all_data.head())
                
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

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QSpinBox
import pandas as pd

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Basic UI layout for testing
        self.layout = QVBoxLayout(self)
        
        self.ButtonOpen = QPushButton('Open CSV', self)
        self.BtnDescribe = QPushButton('Describe Data', self)
        self.spinBox = QSpinBox(self)
        self.tableWidget = QTableWidget(self)
        
        self.layout.addWidget(self.ButtonOpen)
        self.layout.addWidget(self.BtnDescribe)
        self.layout.addWidget(self.spinBox)
        self.layout.addWidget(self.tableWidget)
        
        self.ButtonOpen.clicked.connect(self.loadCsv)
        self.BtnDescribe.clicked.connect(self.dataHead)
        self.all_data = pd.DataFrame()  # Initialize as an empty DataFrame

    def loadCsv(self):
        try:
            # Open a file dialog to select the CSV file
            fileName, _ = QFileDialog.getOpenFileName(self, 'Open CSV', '', 'CSV(*.csv)')
            if fileName:
                print(f"Selected file: {fileName}")
                # Try reading the cleaned CSV file
                self.all_data = pd.read_csv(fileName, delimiter=';', encoding='latin1', on_bad_lines='skip')

                print("CSV loaded successfully")
                print(self.all_data.head())
                
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
