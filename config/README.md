# 💰 Bill Splitting App

A Django-based web application that helps users split shared expenses fairly among members of a group. The app automatically calculates how much each member should pay or receive, making it easier to manage shared bills without disputes.

---

## 📌 Problem Statement

Shared costs among friends, roommates, families, and colleagues often lead to disagreements because it is difficult to keep track of who paid and how much each person owes.

This application solves that problem by allowing users to record expenses and automatically calculate each member's balance.

---

## 🚀 Features

- 👥 Add Members
- 💰 Add Expenses
- ✏️ Edit Expenses
- 🗑️ Delete Expenses
- 📊 Dashboard
- 📈 Total Members
- 💵 Total Expenses
- 🧾 Number of Expenses
- ⚖️ Settlement Summary
- 🕒 Recent Activity
- 💸 Currency formatting with commas
- 🎨 Modern and responsive interface

---

## 🛠️ Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- Git
- GitHub

---

## 📂 Project Structure

```text
config/
│
├── bills/
│   ├── static/
│   ├── templates/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/zarryolly-code/bill-splitting-app.git
```

### Navigate into the project

```bash
cd config
```

### Install Django

```bash
pip install django
```

```bash
cd bill-splitting-app/config
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

### Run migrations

```bash
python manage.py migrate
```

### Start the server

```bash
python manage.py runserver
```

### Open in your browser

```
http://127.0.0.1:8000/
```

---

## 🇳🇬 Problem Being Solved

In Nigeria, friends, families, colleagues, and roommates often contribute money for rent, food, transport, events, and other shared expenses. Keeping track of who paid and who owes money can be difficult and may lead to misunderstandings.

This Bill Splitting App helps users record expenses, calculate balances automatically, and clearly show how much each member should pay or receive.

---

## 📸 Screenshots

Add screenshots here before submission:

- Home Page
- Dashboard
- Add Member
- Add Expense
- Settlement Summary
- Recent Activity

---

## 🌐 Live Demo

Deployment Link:

> Coming Soon

---

## 🎥 Demo Video

A 2–3 minute demonstration video showing:

- Adding members
- Adding expenses
- Editing expenses
- Deleting expenses
- Settlement calculation
- Dashboard
- Recent activity

---

## 👩‍💻 Author

**Olatunji Zainab**

Software Development NextGen Cohort

**Fellow ID:** FE/23/36903732

**Provider:** Ibadan Digital Academy

**State:** Oyo

**Email:** zarryolly@gmail.com

---

## 📄 License

This project was developed for educational purposes as part of the **3MTT Software Development NextGen Cohort**.