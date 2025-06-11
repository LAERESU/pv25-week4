import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

class POSApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui_mainwindow.ui", self)

        # Inisialisasi komponen
        self.cart = []
        self.product_prices = {"Roti": 10000, "Susu": 15000, "Telur": 12000}

        self.comboBoxProduct.addItems(self.product_prices.keys())
        self.comboBoxDiscount.addItems(["0%", "10%", "20%"])

        self.pushButtonAdd.clicked.connect(self.add_to_cart)
        self.pushButtonClear.clicked.connect(self.clear_form)

        self.labelidentity.setText("Yusril Ibtida Ramdhani | F1D022102")

    def add_to_cart(self):
        product = self.comboBoxProduct.currentText()
        quantity = self.spinBoxQuantity.value()
        discount_text = self.comboBoxDiscount.currentText()

        if quantity <= 0:
            QMessageBox.warning(self, "Input Error", "Jumlah harus lebih dari 0")
            return

        price = self.product_prices[product]
        subtotal = price * quantity

        discount = int(discount_text.replace("%", ""))
        discount_amount = subtotal * discount / 100
        total = subtotal - discount_amount

        self.cart.append((product, quantity, price, discount, total))

        self.update_cart_display()

    def update_cart_display(self):
        self.textBrowserCart.clear()
        total_payment = 0

        for item in self.cart:
            product, qty, price, disc, total = item
            self.textBrowserCart.append(
                f"{product} x{qty} @Rp{price} - {disc}% = Rp{total:,.0f}"
            )
            total_payment += total

        self.labelTotal.setText(f"Total: Rp{total_payment:,.0f}")

    def clear_form(self):
        self.spinBoxQuantity.setValue(1)
        self.comboBoxProduct.setCurrentIndex(0)
        self.comboBoxDiscount.setCurrentIndex(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = POSApp()
    window.setWindowTitle("POS App - Week 4")
    window.show()
    sys.exit(app.exec_())
