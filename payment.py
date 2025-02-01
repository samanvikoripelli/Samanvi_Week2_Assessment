class payment:
    def process_payment(self):
        print("processing the payment")
class creditcardpayment(payment):
    def process_payment(self):
        print("processing the credit card payment")
class paypalpayment(payment):
    def process_payment(self):
        print("processing the paypal payment")
class bitcoinpayment(payment):
    def process_payment(self):
        print("processing the bitcoin payment")
payments = [creditcardpayment(),paypalpayment(),bitcoinpayment()]
for payment in payments:
    payment.process_payment()

