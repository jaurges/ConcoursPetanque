from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QApplication
from PySide6.QtCore import Signal, Slot

class SecondTab(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)
        self.setLayout(layout)
        
    @Slot(str)
    def add_item(self, item_text):
        self.list_widget.addItem(item_text)

class FirstTab(QWidget):
    #value_added = Signal(str)  # Signal émis lorsque la valeur doit être ajoutée
    
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.push_button = QPushButton("Ajouter valeur")
        layout.addWidget(self.push_button)
        self.setLayout(layout)
        
        self.push_button.clicked.connect(self.add_value)
        
    def add_value(self):
        value = "Nouvelle valeur"
        self.value_added.emit(value)

if __name__ == "__main__":
    app = QApplication([])
    first_tab = FirstTab()
    second_tab = SecondTab()

    first_tab.value_added.connect(second_tab.add_item)  # Connexion du signal au slot

    first_tab.show()
    second_tab.show()
    
    app.exec()
