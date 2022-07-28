from flask import request
from flask_restful import Resource, reqparse


class ViewAccountDetails(Resource):

    def get(self):
        response = {}

        args = request.args
        accountNumber = args["accountNumber"]

        print(f"LOGGING: {accountNumber}")

        # TODO: get `accountId`, `firstname`, `lastname`, `balance`  from the database using accountNumber

        accountId = 1
        firstName = ""
        lastName = ""


        response["value"] = dict(
            id=accountId,
            firstname=firstName,
            lastname=lastName,
            account=dict(
                id=accountId,
                accountNumber=accountNumber,
                balance=0,
                status=0
            ),
            accountId=accountId
        )

        response["formatters"] = []
        response["contentTypes"] = []
        response["declaredType"] = None
        response["statusCode"] = 200

        return response


class OpenCustomerAccount(Resource):

    def post(self):
        response = {}

        account = request.get_json()

        print(f"LOGGING: {account}")

        generatedAccountNumber = "11112"
        accountId = 1

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


        # TODO: Save to database.


        return response



class CloseCustomerAccount(Resource):

    def post(self):
        response = {}

        args = request.args

        accountNumber = args["accountNumber"]

        print(f"LOGGING: Account Number: {accountNumber}")


        # TODO: from the database retrieve `firstname`, `lastname`, `id`, `balance` using the accountNumber sent.
        firstname = ""
        lastname = ""
        balance = 0
        accountId = 1

        response["value"] = dict(
            id=accountId,
            firstname=firstname,
            lastname=lastname,
            account=dict(
                id=accountId,
                accountNumber=accountNumber,
                balance=balance,
                status=1,
            ),
            accountId=accountId
        )

        response["formatters"] = []
        response["contentTypes"] = []
        response["declaredType"] = None
        response["statusCode"] = 200

        return response