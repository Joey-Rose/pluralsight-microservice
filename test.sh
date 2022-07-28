#!/bin/bash

echo "Test API"

echo -e "\nCreate Account\n"
curl http://localhost:5555/api/CustomerAccount/OpenCustomerAccount -d '{"firstname": "First Name","lastname": "Last Name" }' -H "Content-Type: application/json" -X POST

echo -e "\nView Account Details\n"
curl http://localhost:5555/api/CustomerAccount/GetCustomerAccountByAccountNumber?accountNumber=1111 -X GET


echo -e "\nDelete Account\n"
curl http://localhost:5555/api/CustomerAccount/CloseCustomerAccount?accountNumber=1111 -X POST
