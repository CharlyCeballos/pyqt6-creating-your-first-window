# Only needed for access to command line arguments
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("My App")

    self.label = QLabel()

    self.input = QLineEdit()
    self.input.textChanged.connect(self.label.setText)

    layout = QVBoxLayout()
    layout.addWidget(self.input)
    layout.addWidget(self.label)

    container = QWidget()
    container.setLayout(layout)

    # Set the central widget of the Window.
    self.setCentralWidget(container)

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event loop has stopped.
