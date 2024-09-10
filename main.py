import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from ui import  Ui


def main():
    # app = QApplication(sys.argv)
    # window = Ui_ShangYi()
    # window.show()
    # sys.exit(app.exec_())

    app = QApplication(sys.argv)
    # MainWindow = QMainWindow()
    ui = Ui()
    ui.btn_bind_func()

    ui.show()
    sys.exit(app.exec_())

# if __name__ == "__main__":



if __name__ == "__main__":
    main()
