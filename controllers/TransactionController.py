from flask import request, jsonify
from flask_restful import Resource
from .db.config import dbconfig
from mysql.connector import connect

class HandleTransaction(Resource):

    # JSON must include the field `transactionType` set to 0 or 1.
    # Debit = 0, Credit = 1
    def post(self):
        response = {}

        data = request.get_json()
        print(f"LOGGING: {data}")

        accountNumber = data.get("accountNumber")
        depositAmount = float(data.get("amount"))
        transactionType = int(data.get("transactionType"))

        try:
            db = connect(**dbconfig)
            cursor = db.cursor(dictionary=True)

            sql = "select * from accounts  inner join customers on accounts.id = customers.id where accountNumber like \"%s\"" % accountNumber
            cursor.execute(sql)

            record = cursor.fetchone()

            transactionQuery = "INSERT INTO transactions(accountID,amount,transactionType) VALUES (%d,%.2f,%d)" % (record.get("id"),depositAmount,transactionType)
            cursor.execute(transactionQuery)
            db.commit()

            if transactionType and depositAmount>=0 and not int(record.get("accountStatus")):
                # Credit transaction
                newBalance = float(record.get("balance")) + depositAmount

                updateQuery = "UPDATE accounts SET balance = %.2f WHERE id LIKE %d" %(newBalance,record.get("id"))

                print(f"LOGGING: {updateQuery}")

                cursor.execute(updateQuery)
                db.commit()

            else:
                # Debit transaction
                newBalance = float(record.get("balance")) + depositAmount

                updateQuery = "UPDATE accounts SET balance = %.2f WHERE id LIKE %d" %(newBalance,record.get("id"))

                print(f"LOGGING: {updateQuery}")

                cursor.execute(updateQuery)
                db.commit()

            response["value"] = dict(
                id=record.get("id"),
                firstName=record.get("firstName"),
                lastName=record.get("lastName"),
                account=dict(
                    id=record.get("id"),
                    accountNumber=record.get("accountNumber"),
                    balance=newBalance,
                    status=record.get("accountStatus")
                ),
                accountId=record.get("id")
            )

            response["formatters"] = []
            response["contentTypes"] = []
            response["declaredType"] = None
            response["statusCode"] = 200

            db.close()
            return jsonify(response)

        except Exception as err:
            return dict(message="account number does not exist.")
