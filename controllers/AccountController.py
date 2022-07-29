from flask import request, jsonify
from flask_restful import Resource, reqparse

from mysql.connector import connect
from .db.config import dbconfig

import random


class Customers(Resource):
    def get(self):
        db = connect(**dbconfig)

        cursor = db.cursor(dictionary=True)

        cursor.execute("select * from accounts")

        data = cursor.fetchall()

        return jsonify(data)


class ViewAccountDetails(Resource):

    def get(self):
        response = {}

        args = request.args
        accountNumber = args["accountNumber"]

        print(f"LOGGING: {accountNumber}")

        # Retrieve records from the database.
        db = connect(**dbconfig)
        cursor = db.cursor(dictionary=True)

        sql = "select * from accounts  inner join customers on accounts.id = customers.id where accountNumber like \"%s\"" % accountNumber
        cursor.execute(sql)

        data = cursor.fetchone()

        accountId = data.get("id")
        firstName = data.get("firstName")
        lastName = data.get('lastName')
        balance = float(data.get("balance"))
        accountStatus = data.get("accountStatus")

        response["value"] = dict(
            id=accountId,
            firstname=firstName,
            lastname=lastName,
            account=dict(
                id=accountId,
                accountNumber=accountNumber,
                balance=balance,
                status=accountStatus
            ),
            accountId=accountId
        )

        response["formatters"] = []
        response["contentTypes"] = []
        response["declaredType"] = None
        response["statusCode"] = 200

        return jsonify(response)


class OpenCustomerAccount(Resource):

    def post(self):
        response = {}

        account = request.get_json()

        print(f"LOGGING: {account}")

        mysql = connect(**dbconfig)

        if mysql.is_connected():

            accountId = int((random.randint(0,1000000000)))
            generatedAccountNumber = str(accountId).zfill(10)
            firstname = account.get("firstname")
            lastname = account.get("lastname")

            # Save to database
            cursor = mysql.cursor()
            cursor.execute("SET FOREIGN_KEY_CHECKS=0")

            print(f"LOGGING: {accountId}, {firstname}, {lastname}, {generatedAccountNumber}")

            # create customer
            sql = "INSERT INTO customers(firstname,lastname,accountID) VALUES (\"%s\",\"%s\",%d)" % (firstname,lastname,accountId)
            cursor.execute(sql)
            mysql.commit()

            # create account
            sql = "INSERT INTO accounts(accountNumber,balance,accountStatus) VALUES (\"%s\",%.2f,%d)" % (generatedAccountNumber,0.0,1)
            cursor.execute(sql)
            mysql.commit()

            response["value"] = dict(
                id=accountId,
                firstname=account.get("firstname"),
                lastname=account.get("lastname"),
                account=dict(
                    id=accountId,
                    accountNumber=generatedAccountNumber,
                    balance=0,
                    status=0
                ),
                accountId=accountId
            )

            response["formatters"] = []
            response["contentTypes"] = []
            response["declaredType"] = None
            response["statusCode"] = 200

            mysql.close()
        else:
            response["message"] = "can't connect to MYSQL Database."

        return jsonify(response)


class CloseCustomerAccount(Resource):

    def post(self):
        response = {}

        args = request.args

        accountNumber = args["accountNumber"]

        print(f"LOGGING: Account Number: {accountNumber}")

        # Retrieve records from the database.
        db = connect(**dbconfig)
        cursor = db.cursor(dictionary=True)

        sql = "select * from accounts  inner join customers on accounts.id = customers.id where accountNumber like \"%s\"" % accountNumber
        cursor.execute(sql)

        data = cursor.fetchone()

        firstname = data.get("firstName")
        lastname = data.get("lastName")
        balance = float(data.get("balance"))
        accountId = data.get("id")

        closedAccountStatus = 0

        # Update account
        sql = "UPDATE accounts SET accountStatus = %d WHERE id LIKE %d" % (closedAccountStatus,accountId)
        cursor.execute(sql)
        db.commit()

        response["value"] = dict(
            id=accountId,
            firstname=firstname,
            lastname=lastname,
            account=dict(
                id=accountId,
                accountNumber=accountNumber,
                balance=balance,
                status=closedAccountStatus
            ),
            accountId=accountId
        )

        response["formatters"] = []
        response["contentTypes"] = []
        response["declaredType"] = None
        response["statusCode"] = 200

        db.close()
        return jsonify(response)