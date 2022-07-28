-- Sources
-- https://github.com/KernelGamut32/working-with-cloud-public/blob/main/demos/RDS/DB%20Scripts/Product-Table.sql
-- https://www.sqlshack.com/understanding-sql-decimal-data-type/
-- https://www.w3schools.com/sql/sql_datatypes.asp

USE [launch-demo-db]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

-- 10 digit account number
-- Maximum 10 digits (XXXXXXXX.XX) for balance
-- OPEN => 1, CLOSED => 0
CREATE TABLE accounts (
    id INT AUTO_INCREMENT NOT NULL,
    accountNumber VARCHAR(10) UNIQUE NOT NULL,
    balance decimal(10,2) NOT NULL,
    accountStatus INT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE customers (
    id INT AUTO_INCREMENT NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    accountID INT UNIQUE NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (accountID) REFERENCES accounts (ID)
);

-- Credit Transactions => 0
--  Debit Transactions => 1
-- Maximum 10 digits (XXXXXXXX.XX) for amount
CREATE TABLE transactions (
    id INT AUTO_INCREMENT NOT NULL,
    amount decimal(10,2) NOT NULL,
    transactionType INT NOT NULL,
    accountID INT UNIQUE NOT NULL ,
    PRIMARY KEY (id),
    FOREIGN KEY (accountID) REFERENCES accounts (ID)
);

-- Dummy Data

INSERT INTO accounts (accountNumber, balance, accountStatus)
VALUES ('0000000001', '122.12', '1');

INSERT INTO customers (firstName, lastName, accountID)
VALUES ('John', 'Doe', '1');

INSERT INTO transactions (amount, transactionType, accountID)
VALUES ('1000.00', '0', '1');

-- #############################################################

INSERT INTO accounts (accountNumber, balance, accountStatus)
VALUES ('0000000002', '0.00', '1');

INSERT INTO customers (firstName, lastName, accountID)
VALUES ('Mary', 'Kate', '2');

INSERT INTO transactions (amount, transactionType, accountID)
VALUES ('4.00', '1', '2');

-- #############################################################

INSERT INTO accounts (accountNumber, balance, accountStatus)
VALUES ('0000000003', '5.34', '0');

INSERT INTO customers (firstName, lastName, accountID)
VALUES ('Peter', 'Heard', '3');

INSERT INTO transactions (amount, transactionType, accountID)
VALUES ('112.87', '0', '3');

-- #############################################################

INSERT INTO accounts (accountNumber, balance, accountStatus)
VALUES ('0000000004', '1769.00', '0');

INSERT INTO customers (firstName, lastName, accountID)
VALUES ('Rhea', 'Toll', '4');

INSERT INTO transactions (amount, transactionType, accountID)
VALUES ('18.98', '1', '4');

-- #############################################################

INSERT INTO accounts (accountNumber, balance, accountStatus)
VALUES ('0000000005', '19820.00', '0');

INSERT INTO customers (firstName, lastName, accountID)
VALUES ('Winston', 'Batch', '5');

INSERT INTO transactions (amount, transactionType, accountID)
VALUES ('0.01', '0', '5');
