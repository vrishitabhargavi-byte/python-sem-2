class payment:
    def pay(self):
        print("Payment method is not specified")
class credit_card(payment):
    def pay(self):
        print("Payment method is credit card")
class debit_card(payment):
    def pay(self):
        print("Payment method is debit card")
class cash(payment):
    def pay(self):
        print("Payment method is cash")
def process_payment(payment_method):
    payment_method.pay()
payment1=credit_card()
payment2=debit_card()
payment3=cash()
process_payment(payment1)
process_payment(payment2)
process_payment(payment3)