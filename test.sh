#!/bin/bash

echo "Test API"

echo -e "\nCreate Account\n"
curl http://localhost:5555/api/CustomerAccount/OpenCustomerAccount -d '{"firstname": "First Name","lastname": "Last Name" }' -H "Content-Type: application/json" -X POST

echo -e "\n Get all enrolled customers\n"
curl http://localhost:5555/api/Customers

echo -e "\nView Account Details\n"
curl http://localhost:5555/api/CustomerAccount/GetCustomerAccountByAccountNumber?accountNumber=1111 -X GET


echo -e "\nDebit Deposit\n"
curl http://localhost:5555/api/CustomerAccount/ApplyTransactionToCustomerAccountAsync -d '{"accountNumber": "0000000472","amount": 500, "transactionType": 0 }' -H "Content-Type: application/json" -X POST


echo -e "\Credit Deposit\n"
curl http://localhost:5555/api/CustomerAccount/ApplyTransactionToCustomerAccountAsync -d '{"accountNumber": "0000000472","amount": 500, "transactionType": 1 }' -H "Content-Type: application/json" -X POST


echo -e "\Close Account\n"
curl http://localhost:5555/api/CustomerAccount/CloseCustomerAccount?accountNumber=1111 -X POST
