import sys
from PySide6.QtWidgets import *
from WidgetFileList import WidgetFileList
import numpy as np
import matplotlib.pyplot as plt


class DisplayGcode:

    def __init__(self, srcfile, color='r', stock_x=305, stock_y=305):
        self.src_file_path = srcfile
        self.stock_x = stock_x
        self.stock_y = stock_y

        # Colors in matplotlib: https://matplotlib.org/stable/users/explain/colors/colors.html
        self.color = color

    def show(self):
        # Display stock on the diagram
        plt.plot([0, self.stock_x*100, self.stock_x*100, 0, 0], [0, 0, self.stock_y*100, self.stock_y*100, 0], '--', label='brut')

        file = open(self.src_file_path, "r")
        # title = self.src_file_path.split('/')[-1].split('.')[0]

        vect_x = np.array([])
        vect_y = np.array([])
        vect_z = np.array([])

        previous_z = 0

        for line in file:
            instruction_list = line.split(";")

            for instruction in instruction_list:
                # Check that line is not empty or a return carriage
                if len(instruction) != 0 and instruction != "\n":
                    # Instruction moves start with a "Z"
                    if instruction[0] == "Z":
                        # Extract X, Y and Z coordinates from the instruction line
                        coord = instruction.replace("Z", "").split(",")

                        x = float(coord[0])
                        y = float(coord[1])
                        z = float(coord[2])

                        # Display lines differently if they are cut moves or just jump moves
                        if z != previous_z:
                            if previous_z < 0:
                                plt.plot(vect_x, vect_y, color=self.color)

                            if previous_z > 0:
                                plt.plot(vect_x, vect_y, color='0.8')

                            # Start a new vector
                            vect_x = np.array([])
                            vect_y = np.array([])
                            vect_z = np.array([])

                        # Append x, y, z coordinates to each vector
                        vect_x = np.append(vect_x, [x])
                        vect_y = np.append(vect_y, [y])
                        vect_z = np.append(vect_z, [z])

                        previous_z = z

        file.close()

        # Plot setup
        display_margin = 500
        ax = plt.gca()  # Figure axes
        ax.set_xlim(-display_margin, self.stock_x + display_margin)
        ax.set_ylim(-display_margin, self.stock_y + display_margin)

        plt.axis('scaled')  # In order not to get any deformations

        plt.grid(True)
        plt.xlabel("x [1/100 mm]")
        plt.ylabel("y [1/100 mm]")

        plt.show()


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Display parts")

        # Add widgets, the first one being the file list widget given for the exercise
        self.file_selection = WidgetFileList()
        self.button_start = QPushButton("Show parts")

        layout = QVBoxLayout()
        layout.addWidget(self.file_selection)
        layout.addWidget(self.button_start)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Launch function when button is clicked
        self.button_start.clicked.connect(self.show_files)

    def show_files(self):
        color_array = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']
        i = 0

        for file in self.file_selection.list_files():
            part = DisplayGcode(file, color_array[i%10])
            part.show()

            i += 1


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
