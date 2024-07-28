# import sys
# import cv2
# from PIL import Image
# import numpy as np
# import pandas as pd
# import re
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog, QTextEdit
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtCore import Qt
# from tensorflow.keras.models import load_model  # Ensure the correct import
# import tensorflow as tf
# from ResultsWindow import ResultsWindow, DetailedRecipeWindow


# class FoodRecommendationApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         # Load the model using load_model
#         print("Loading model...")
#         self.model = load_model(r'C:\Users\niqan\OneDrive\Documents\Semester 4\Proyek 2\TUBES\Coba\model')
#         print("Model loaded successfully")

#     def initUI(self):
#         self.setWindowTitle('Food Recommendation System')
#         self.setGeometry(100, 100, 1000, 600)
        
#         self.main_widget = QWidget(self)
#         self.setCentralWidget(self.main_widget)
        
#         self.main_layout = QHBoxLayout(self.main_widget)

#         # Left layout
#         self.left_layout = QVBoxLayout()
        
#         self.ingredients_input = QTextEdit(self)
#         self.ingredients_input.setPlaceholderText("Enter at least four ingredients, separated by commas.")
#         self.left_layout.addWidget(self.ingredients_input)
        
#         self.search_button = QPushButton('Search Recipes', self)
#         self.search_button.clicked.connect(self.search_recipes)
#         self.left_layout.addWidget(self.search_button)
        
#         self.result_display = QLabel(self)
#         self.result_display.setAlignment(Qt.AlignLeft)
#         self.left_layout.addWidget(self.result_display)

#         self.main_layout.addLayout(self.left_layout)

#         # Right layout
#         self.right_layout = QVBoxLayout()
        
#         self.upload_button = QPushButton('Upload Image', self)
#         self.upload_button.clicked.connect(self.upload_image)
#         self.right_layout.addWidget(self.upload_button)
        
#         self.webcam_button = QPushButton('Capture Image from Webcam', self)
#         self.webcam_button.clicked.connect(self.capture_image)
#         self.right_layout.addWidget(self.webcam_button)
        
#         self.image_label = QLabel(self)
#         self.image_label.setAlignment(Qt.AlignCenter)
#         self.right_layout.addWidget(self.image_label)
        
#         self.result_label = QLabel('Prediction: ', self)
#         self.result_label.setAlignment(Qt.AlignCenter)
#         self.right_layout.addWidget(self.result_label)
        
#         self.main_layout.addLayout(self.right_layout)
    
#     def preprocess_image(self, file_path):
#         print("Preprocessing image...")
#         image = Image.open(file_path)
#         image = image.resize((224, 224))
#         image_array = np.array(image) / 255.0
#         image_array = np.expand_dims(image_array, axis=0)
#         return image_array
    
#     def upload_image(self):
#         options = QFileDialog.Options()
#         file_name, _ = QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Images (*.png *.xpm *.jpg)', options=options)
#         if file_name:
#             self.image_path = file_name
#             self.display_image(file_name)
#             self.classify_image(file_name)
    
#     def capture_image(self):
#         cap = cv2.VideoCapture(0)
#         ret, frame = cap.read()
#         cap.release()
#         if ret:
#             cv2.imwrite('captured_image.jpg', frame)
#             self.image_path = 'captured_image.jpg'
#             self.display_image('captured_image.jpg')
#             self.classify_image('captured_image.jpg')
    
#     def display_image(self, file_path):
#         pixmap = QPixmap(file_path)
#         self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))
    
#     def classify_image(self, file_path):
#         image_array = self.preprocess_image(file_path)
        
#         # Debug: Print the processed image array
#         print("Image array:", image_array)
        
#         prediction = self.model.predict(image_array)
        
#         # Debug: Print the prediction
#         print("Prediction:", prediction)
        
#         label = self.get_label(prediction)
#         self.result_label.setText(f'Prediction: {label}')
#         self.predicted_label = label
    
#     def get_label(self, prediction):
#         labels = ['Ayam', 'Ikan', 'Kambing', 'Sapi', 'Tahu', 'Telur', 'Udang']
#         predicted_index = np.argmax(prediction)
#         print("Predicted class index:", predicted_index)  # Debug statement
#         return labels[predicted_index]
    
#     def search_recipes(self):
#         # Get the ingredients entered by the user
#         user_ingredients = self.ingredients_input.toPlainText().split(',')
#         user_ingredients = [ingredient.strip().lower() for ingredient in user_ingredients if ingredient.strip()]

#         if not user_ingredients or len(user_ingredients) < 4:
#             self.result_display.setText("Please enter at least four ingredients.")
#             return

#         # Tokenize the user ingredients
#         user_ingredient_tokens = set(token for ingredient in user_ingredients for token in re.split(r'\W+', ingredient) if token)

#         print("User Ingredient Tokens:", user_ingredient_tokens)  # Debug statement

#         # Read the corresponding CSV file based on the prediction
#         csv_path = f'C:/Users/niqan/OneDrive/Documents/Semester 4/Proyek 2/TUBES/Coba/{self.predicted_label}.csv'
#         try:
#             recipes_df = pd.read_csv(csv_path, delimiter=';')  # Specify semicolon as the delimiter
#             recipes_df.columns = recipes_df.columns.str.strip()  # Strip whitespace from column names
            
#             # Debug statement
#             print("Columns in the DataFrame:", recipes_df.columns)
#         except FileNotFoundError:
#             self.result_display.setText(f"CSV file for {self.predicted_label} not found.")
#             return
#         except pd.errors.EmptyDataError:
#             self.result_display.setText(f"CSV file for {self.predicted_label} is empty.")
#             return
#         except pd.errors.ParserError:
#             self.result_display.setText(f"CSV file for {self.predicted_label} is malformed.")
#             return
#         except Exception as e:
#             self.result_display.setText(f"An error occurred: {e}")
#             return

#         # Ensure the 'Ingredients' column exists
#         if 'Ingredients' not in recipes_df.columns:
#             self.result_display.setText("The 'Ingredients' column is missing in the CSV file.")
#             return

#         # Convert all values in the 'Ingredients' column to strings
#         recipes_df['Ingredients'] = recipes_df['Ingredients'].astype(str).str.lower().str.split('--')

#         print("Tokenized Ingredients from CSV:")  # Debug statement
#         print(recipes_df['Ingredients'])  # Debug statement

#         # Tokenize the ingredients in the recipes
#         recipes_df['ingredient_tokens'] = recipes_df['Ingredients'].apply(
#             lambda ingredients: set(token for ingredient in ingredients for token in re.split(r'\W+', ingredient) if token)
#         )

#         print("Ingredient Tokens from Recipes:")  # Debug statement
#         print(recipes_df['ingredient_tokens'])  # Debug statement

#         # Calculate the match count for each recipe
#         recipes_df['match_count'] = recipes_df['ingredient_tokens'].apply(lambda tokens: len(user_ingredient_tokens & tokens))

#         print("Match Counts:")  # Debug statement
#         print(recipes_df[['Title', 'match_count']])  # Debug statement

#         # Sort recipes based on the number of matching ingredients
#         sorted_recipes = recipes_df.sort_values(by='match_count', ascending=False)

#         if not sorted_recipes[sorted_recipes['match_count'] > 0].empty:
#             # Open the results window and display the matched recipes
#             self.results_window = ResultsWindow(sorted_recipes)
#             self.results_window.show()
#         else:
#             self.result_display.setText("No recipes matched the ingredients.")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = FoodRecommendationApp()
#     ex.show()
#     sys.exit(app.exec_())

import sys
import cv2
from PIL import Image
import numpy as np
import pandas as pd
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog, QTextEdit, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from tensorflow.keras.models import load_model
from ResultsWindow import ResultsWindow


class RecipeListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        print("Loading model...")
        self.model = load_model(r'C:\Users\niqan\OneDrive\Documents\Semester 4\Proyek 2\TUBES\Coba\model')
        print("Model loaded successfully")

    def initUI(self):
        self.setWindowTitle('Sistem Menampilkan List Resep')
        self.setGeometry(100, 100, 1000, 600)
        
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        
        self.main_layout = QHBoxLayout(self.main_widget)

        # Left layout
        self.left_layout = QVBoxLayout()
        
        self.ingredients_input = QTextEdit(self)
        self.ingredients_input.setPlaceholderText("Enter at least four ingredients, separated by commas.")
        self.left_layout.addWidget(self.ingredients_input)
        
        self.search_button = QPushButton('Search Recipes', self)
        self.search_button.clicked.connect(self.search_recipes)
        self.left_layout.addWidget(self.search_button)
        
        self.result_display = QLabel(self)
        self.result_display.setAlignment(Qt.AlignLeft)
        self.left_layout.addWidget(self.result_display)

        self.left_widget = QWidget()
        self.left_widget.setLayout(self.left_layout)
        self.main_layout.addWidget(self.left_widget)

        # Right layout
        self.right_layout = QVBoxLayout()
        
        self.button_layout = QHBoxLayout()
        self.upload_button = QPushButton('Upload Image', self)
        self.upload_button.clicked.connect(self.upload_image)
        self.button_layout.addWidget(self.upload_button)
        
        self.webcam_button = QPushButton('Capture Image from Webcam', self)
        self.webcam_button.clicked.connect(self.capture_image)
        self.button_layout.addWidget(self.webcam_button)

        self.right_layout.addLayout(self.button_layout)
        
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.right_layout.addWidget(self.image_label)
        
        self.result_label = QLabel('Prediction: ', self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.right_layout.addWidget(self.result_label)

        self.right_widget = QWidget()
        self.right_widget.setLayout(self.right_layout)
        self.main_layout.addWidget(self.right_widget)

        # Set equal size policies for the left and right widgets
        self.left_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.right_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    
    def preprocess_image(self, file_path):
        print("Preprocessing image...")
        image = Image.open(file_path)
        image = image.resize((224, 224))
        image_array = np.array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)
        return image_array
    
    def upload_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Images (*.png *.xpm *.jpg)', options=options)
        if file_name:
            self.image_path = file_name
            self.display_image(file_name)
            self.classify_image(file_name)
    
    def capture_image(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        if ret:
            cv2.imwrite('captured_image.jpg', frame)
            self.image_path = 'captured_image.jpg'
            self.display_image('captured_image.jpg')
            self.classify_image('captured_image.jpg')
    
    def display_image(self, file_path):
        pixmap = QPixmap(file_path)
        self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))
    
    def classify_image(self, file_path):
        image_array = self.preprocess_image(file_path)
        print("Image array:", image_array)
        prediction = self.model.predict(image_array)
        print("Prediction:", prediction)
        label = self.get_label(prediction)
        self.result_label.setText(f'Prediction: {label}')
        self.predicted_label = label
    
    def get_label(self, prediction):
        labels = ['Ayam', 'Ikan', 'Kambing', 'Sapi', 'Tahu', 'Telur', 'Udang']
        predicted_index = np.argmax(prediction)
        print("Predicted class index:", predicted_index)
        return labels[predicted_index]
    
    def search_recipes(self):
        user_ingredients = self.ingredients_input.toPlainText().split(',')
        user_ingredients = [ingredient.strip().lower() for ingredient in user_ingredients if ingredient.strip()]

        if not user_ingredients or len(user_ingredients) < 4:
            self.result_display.setText("Please enter at least four ingredients.")
            return

        user_ingredient_tokens = set(token for ingredient in user_ingredients for token in re.split(r'\W+', ingredient) if token)
        print("User Ingredient Tokens:", user_ingredient_tokens)

        csv_path = f'C:/Users/niqan/OneDrive/Documents/Semester 4/Proyek 2/TUBES/Coba/{self.predicted_label}.csv'
        try:
            recipes_df = pd.read_csv(csv_path, delimiter=';')
            recipes_df.columns = recipes_df.columns.str.strip()
            print("Columns in the DataFrame:", recipes_df.columns)
        except FileNotFoundError:
            self.result_display.setText(f"CSV file for {self.predicted_label} not found.")
            return
        except pd.errors.EmptyDataError:
            self.result_display.setText(f"CSV file for {self.predicted_label} is empty.")
            return
        except pd.errors.ParserError:
            self.result_display.setText(f"CSV file for {self.predicted_label} is malformed.")
            return
        except Exception as e:
            self.result_display.setText(f"An error occurred: {e}")
            return

        if 'Ingredients' not in recipes_df.columns:
            self.result_display.setText("The 'Ingredients' column is missing in the CSV file.")
            return

        recipes_df['Ingredients'] = recipes_df['Ingredients'].astype(str).str.lower().str.split('--')
        print("Tokenized Ingredients from CSV:")
        print(recipes_df['Ingredients'])

        recipes_df['ingredient_tokens'] = recipes_df['Ingredients'].apply(
            lambda ingredients: set(token for ingredient in ingredients for token in re.split(r'\W+', ingredient) if token)
        )

        print("Ingredient Tokens from Recipes:")
        print(recipes_df['ingredient_tokens'])

        recipes_df['match_count'] = recipes_df['ingredient_tokens'].apply(lambda tokens: len(user_ingredient_tokens & tokens))
        print("Match Counts:")
        print(recipes_df[['Title', 'match_count']])

        sorted_recipes = recipes_df.sort_values(by='match_count', ascending=False)

        if not sorted_recipes[sorted_recipes['match_count'] > 0].empty:
            self.results_window = ResultsWindow(sorted_recipes)
            self.results_window.show()
        else:
            self.result_display.setText("No recipes matched the ingredients.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RecipeListApp()
    ex.show()
    sys.exit(app.exec_())
