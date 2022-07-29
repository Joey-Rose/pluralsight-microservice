from flask import Flask
from flask_restful import Api
from controllers.AccountController import OpenCustomerAccount, CloseCustomerAccount,ViewAccountDetails,Customers
from controllers.TransactionController import HandleTransaction
from os import getenv

def main():
    app = Flask(__name__)
    api = Api(app)

    serverPort = getenv("APP_PORT","5555")

    # Customers
    api.add_resource(Customers,"/api/Customers")

    # Bank Account
    api.add_resource(OpenCustomerAccount,"/api/CustomerAccount/OpenCustomerAccount")
    api.add_resource(CloseCustomerAccount,"/api/CustomerAccount/CloseCustomerAccount")
    api.add_resource(ViewAccountDetails,"/api/CustomerAccount/GetCustomerAccountByAccountNumber")

    # Account Transactions
    api.add_resource(HandleTransaction,"/api/CustomerAccount/ApplyTransactionToCustomerAccountAsync")

    app.run(host="0.0.0.0",port=int(serverPort),debug=True)


if __name__ == "__main__":
    main()