import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from app.logic import Pump, Radiator, Fan
from ui.main_page import Ui_MainWindow


class ExpenseTracker(QMainWindow):
    line_edits = []
    float_data = {}

    def __init__(self, parent=None):
        super(ExpenseTracker, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.line_edits = [self.ui.Q_engine_to_radiator, self.ui.C_water, self.ui.Ro_water, self.ui.H_water,
                           self.ui.n, self.ui.T_air, self.ui.T_average_air]
        self.float_data = {}
        self.ui.result_button.clicked.connect(self.result)

    def validate_data(self):
        for line_edit in self.line_edits:
            input_text = line_edit.text()
            if not input_text:
                QMessageBox.critical(self, 'Ошибка',
                                     f'Пожалуйста, заполните строку: {line_edit.text()}')
                return False
            try:
                float_value = float(input_text)
                self.float_data[f'{line_edit.objectName()}'] = float_value
            except ValueError:
                QMessageBox.critical(self, 'Ошибка',
                                     f'Пожалуйста, введите числовое значение в строку: {line_edit.text()}')
                return False
        return self.float_data

    def result(self):
        if self.validate_data():
            pump = Pump(Q_engine_to_radiator=self.float_data['Q_engine_to_radiator'],
                        C_water=self.float_data['C_water'],
                        Ro_water=self.float_data['Ro_water'],
                        H_water=self.float_data['H_water'],
                        n=self.float_data['n'])
            radiator = Radiator(Q_engine_to_radiator=self.float_data['Q_engine_to_radiator'],
                                G_water=pump.G_water(),
                                Ro_water=self.float_data['Ro_water'],
                                T_water=pump.T)
            fan = Fan(G_air=radiator.G_air(),
                      T_average_air=radiator.T_average_air)

            self.ui.N_result.setText(str(pump.N()))
            self.ui.F_result.setText(str(radiator.F()))
            self.ui.N_fan_result.setText(str(fan.N_fan()))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())
