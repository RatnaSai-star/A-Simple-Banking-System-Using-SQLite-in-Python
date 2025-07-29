👨‍💻 Author
Ratnasai Peddireddy
Full Stack Developer
Portfolio Website | LinkedIn | GitHub

# 🏦 BOB Bank CLI System

A simple command-line banking system built in Python using SQLite for data persistence. This project simulates core banking functionalities like account creation, PIN generation, balance check, deposit, withdrawal, and account-to-account transfer.

---

## 📂 Project Structure

- **Bank.db** – SQLite database to store account information.
- **main.py** – Main Python file to execute banking operations.

---

## ⚙️ Features

✔ Account Creation  
✔ PIN Generation  
✔ Balance Inquiry  
✔ Withdrawal  
✔ Deposit  
✔ Account Transfer  

---

## 🧱 Database Schema

The table `ACCOUNTS` includes:

| Column      | Type          | Description                   |
|-------------|---------------|-------------------------------|
| acc_number  | number(16)    | Primary Key (Auto Increment) |
| name        | varchar(32)   | Customer Name (Required)     |
| phone       | number(10)    | Unique Phone Number          |
| email       | varchar(256)  | Unique Email ID              |
| balance     | number(8,2)   | Defaults to ₹1000            |
| pin         | number(4)     | Security PIN (Defaults to 0) |
| address     | varchar(256)  | Address of the User          |

---

## 🛠️ Setup Instructions

1. Clone this repository:

```bash
git clone https://github.com/<your-username>/BOB-Bank-System.git
cd BOB-Bank-System
