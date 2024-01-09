import random
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSpinBox, QWidget, QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Ajoutez une QSpinBox pour déterminer le nombre de QComboBox
        self.spin_box = QSpinBox(self)
        self.spin_box.setMinimum(1)
        self.spin_box.setMaximum(10)
        self.spin_box.valueChanged.connect(self.update_comboboxes)
        self.layout.addWidget(self.spin_box)

        # Initialisation avec un QComboBox
        self.comboboxes = [QComboBox(self) for _ in range(self.spin_box.value())]
        self.update_comboboxes()

    def update_comboboxes(self):
        # Mettez à jour le nombre de QComboBox en fonction de la valeur de la QSpinBox
        new_value = self.spin_box.value()

        # Supprimez les QComboBox actuelles du layout
        for combo_box in self.comboboxes:
            combo_box.setParent(None)

        # Créez de nouveaux QComboBox en fonction de la nouvelle valeur de la QSpinBox
        self.comboboxes = [QComboBox(self) for _ in range(new_value)]

        # Ajoutez les nouveaux QComboBox au layout et remplissez-les avec des nombres aléatoires
        for combo_box in self.comboboxes:
            self.layout.addWidget(combo_box)
            self.fill_combobox_with_random_numbers(combo_box)

    def fill_combobox_with_random_numbers(self, combo_box):
        # Remplissez un QComboBox avec des nombres aléatoires
        combo_box.clear()
        for _ in range(5):  # Changez 5 selon le nombre d'éléments aléatoires que vous souhaitez dans chaque QComboBox
            combo_box.addItem(str(random.randint(1, 100)))

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
