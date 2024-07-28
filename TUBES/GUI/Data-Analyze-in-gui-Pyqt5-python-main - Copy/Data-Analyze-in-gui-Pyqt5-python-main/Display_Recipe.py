import sys
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QLineEdit, QPushButton, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt

class CSVViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("CSV Viewer with Token Calculation")
        self.setGeometry(100, 100, 800, 600)
        
        # Main layout
        main_layout = QVBoxLayout()
        
        # Input layout for the token value
        input_layout = QHBoxLayout()
        self.token_input = QLineEdit(self)
        self.token_input.setPlaceholderText("Enter token value")
        self.calculate_button = QPushButton("Calculate", self)
        self.calculate_button.clicked.connect(self.calculate_tokens)
        input_layout.addWidget(QLabel("Token Input: "))
        input_layout.addWidget(self.token_input)
        input_layout.addWidget(self.calculate_button)
        
        main_layout.addLayout(input_layout)
        
        # Tables layout
        tables_layout = QHBoxLayout()
        
        # CSV Table
        self.csv_table = QTableWidget(self)
        tables_layout.addWidget(self.csv_table)
        
        # Tokens Table
        self.tokens_table = QTableWidget(self)
        self.tokens_table.setColumnCount(1)
        self.tokens_table.setHorizontalHeaderLabels(['Token Difference'])
        tables_layout.addWidget(self.tokens_table)
        
        main_layout.addLayout(tables_layout)
        
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)
    
    def load_csv(self, file_path):
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
        
        if data:
            self.csv_table.setRowCount(len(data))
            self.csv_table.setColumnCount(len(data[0]))
            self.csv_table.setHorizontalHeaderLabels(data[0])
            
            for row_idx, row_data in enumerate(data[1:], start=1):
                for col_idx, cell_data in enumerate(row_data):
                    self.csv_table.setItem(row_idx - 1, col_idx, QTableWidgetItem(cell_data))
    
    def calculate_tokens(self):
        token_value = self.token_input.text()
        if not token_value.isdigit():
            return
        
        token_value = int(token_value)
        self.tokens_table.setRowCount(self.csv_table.rowCount())
        
        for row in range(self.csv_table.rowCount()):
            second_column_value = self.csv_table.item(row, 1).text()
            token_count = len(second_column_value.split())
            token_difference = token_count - token_value
            self.tokens_table.setItem(row, 0, QTableWidgetItem(str(token_difference)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = CSVViewer()
    viewer.load_csv('C:/Users/niqan/OneDrive/Documents/Semester 4/Proyek 2/TUBES/GUI/Data-Analyze-in-gui-Pyqt5-python-main - Copy/Data-Analyze-in-gui-Pyqt5-python-main/Ayam.csv')  # Replace with your CSV file path
    viewer.show()
    sys.exit(app.exec_())
