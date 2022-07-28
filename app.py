from flask import Flask
from flask_restful import Api

from controllers.AccountController import OpenCustomerAccount, CloseCustomerAccount,ViewAccountDetails
from controllers.TransactionController import CreditTransaction, DebitTransaction

app = Flask(__name__)

def main():
    api = Api(app)

    # Bank Account
    api.add_resource(OpenCustomerAccount,"/api/CustomerAccount/OpenCustomerAccount")
    api.add_resource(CloseCustomerAccount,"/api/CustomerAccount/CloseCustomerAccount")
    api.add_resource(ViewAccountDetails,"/api/CustomerAccount/GetCustomerAccountByAccountNumber")

    # Account Transactions
    # JSON must include the field `transactionType` set to 0 or 1.
    # Debit = 0, Credit = 1
    api.add_resource(CreditTransaction,"/api/CustomerAccount/ApplyTransactionToCustomerAccountAsync")
    api.add_resource(DebitTransaction,"/api/CustomerAccount/ApplyTransactionToCustomerAccountAsync")

    app.run(host="0.0.0.0",port=5555,debug=True)


if __name__ == "__main__":
    main()