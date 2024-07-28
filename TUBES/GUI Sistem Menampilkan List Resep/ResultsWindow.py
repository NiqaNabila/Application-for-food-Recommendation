
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QVBoxLayout, QWidget
# import pandas as pd
# import re

# class ResultsWindow(QMainWindow):
#     def __init__(self, matched_recipes):
#         super().__init__()

#         self.setWindowTitle("Matched Recipes")
#         self.setGeometry(100, 100, 600, 400)

#         # Create a layout for the central widget
#         layout = QVBoxLayout()
        
#         # Add a label to display the matched recipes
#         self.results_label = QLabel()
#         self.results_label.setText(matched_recipes)
#         self.results_label.setWordWrap(True)  # Enable word wrap for long text
        
#         # Add the label to the layout
#         layout.addWidget(self.results_label)
        
#         # Create a central widget and set the layout
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)
# results_window.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QVBoxLayout, QWidget, QScrollArea

class DetailedRecipeWindow(QMainWindow):
    def __init__(self, recipe):
        super().__init__()

        self.setWindowTitle(recipe['Title'])
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()
        self.title_label = QLabel(f"Title: {recipe['Title']}")
        layout.addWidget(self.title_label)

        self.ingredients_label = QLabel(f"Ingredients: {', '.join(recipe['Ingredients'])}")
        self.ingredients_label.setWordWrap(True)
        layout.addWidget(self.ingredients_label)

        self.steps_label = QLabel(f"Steps: {recipe['Steps']}")
        self.steps_label.setWordWrap(True)
        layout.addWidget(self.steps_label)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.close)
        layout.addWidget(self.back_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

class ResultsWindow(QMainWindow):
    def __init__(self, recipes_df):
        super().__init__()

        self.setWindowTitle("Matched Recipes")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout()

        for index, row in recipes_df.head(10).iterrows():
            button = QPushButton(f"Recipe: {row['Title']} (Match Count: {row['match_count']})")
            button.clicked.connect(lambda checked, r=row: self.show_recipe_details(r))
            scroll_layout.addWidget(button)

        scroll_widget.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_widget)
        layout.addWidget(scroll_area)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_recipe_details(self, recipe):
        self.detailed_recipe_window = DetailedRecipeWindow(recipe)
        self.detailed_recipe_window.show()
