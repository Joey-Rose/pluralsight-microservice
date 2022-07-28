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

-- 12 digit account number
-- Maximum 10 digits (XXXXXXXX.XX) for balance
-- OPEN => 1, CLOSED => 0
CREATE TABLE accounts (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    accountNumber VARCHAR(12) UNIQUE NOT NULL,
    balance decimal(10,2) NOT NULL,
    accountStatus INT NOT NULL
);

CREATE TABLE customers (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    accountID INT UNIQUE NOT NULL  REFERENCES accounts (ID)
);

-- Credit Transactions => 0
--  Debit Transactions => 1
-- Maximum 10 digits (XXXXXXXX.XX) for amount
CREATE TABLE transactions (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    amount decimal(10,2) NOT NULL,
    transactionType INT NOT NULL,
    accountID INT UNIQUE NOT NULL REFERENCES accounts (ID)
);

-- Inserting dummies values