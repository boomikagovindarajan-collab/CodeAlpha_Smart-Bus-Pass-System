# 🚌 Smart Bus Pass System

## ☁️ Cloud-Based Bus Pass Booking & Management System

Smart Bus Pass System is a professional Flask web application designed to simplify bus pass booking and passenger travel management.

It allows users to register, log in, book bus passes, select travel date and time, choose seats, generate QR codes, and view booking history in one easy-to-use system.

---

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Backend programming language |
| 🌶️ Flask | Web application framework |
| 🗄️ SQLite | Local database management |
| 🎨 HTML | Website page structure |
| 🎨 CSS | User interface design and styling |
| 🔐 Flask Session | User login session management |
| 📱 QRCode Library | QR code generation for bus passes |
| ⚙️ Git & GitHub | Version control and project hosting |

---

## 📁 Project Structure

```text
Smart-Bus-Pass-System/
│
├── 📄 app.py
├── 📄 database.db
├── 📦 requirements.txt
│
├── 📁 static/
│   ├── 📁 css/
│   │   └── 🎨 style.css
│   └── 🖼️ QR code images
│
└── 📁 templates/
    ├── 🏠 index.html
    ├── 🔐 login.html
    ├── 📝 register.html
    ├── 📊 dashboard.html
    ├── 🚌 book_pass.html
    ├── 📋 history.html
    └── 👤 profile.html
```

---

## 🧩 Main Modules

### 🏠 Home Page
Provides an introduction to the Smart Bus Pass System and allows users to get started.

### 👤 User Registration and Login
Allows users to create an account, log in securely, and access their personal dashboard.

### 📊 User Dashboard
Displays welcome information, active passes, total savings, pass validity, and quick navigation options.

### 🚌 Bus Pass Booking
Allows users to enter source, destination, pass type, travel date, and travel time.

### 🪑 Seat Selection
Provides a bus-style seat layout where users can select available seats. Booked seats are displayed separately.

### 📱 QR Code Generation
Generates a QR code for each booked bus pass containing booking details such as pass ID, route, seat number, and travel information.

### 📋 Booking History
Shows previously booked bus passes with pass ID, source, destination, pass type, price, travel date, and seat number.

### 👤 Profile Management
Displays logged-in user details and account information.

### 🚪 Logout
Ends the user session securely and redirects the user to the home page.

---

## ✨ Key Features

- Secure user registration and login
- Session-based authentication
- Online bus pass booking
- Source and destination selection
- Travel date and time selection
- Interactive seat selection layout
- Available, booked, and selected seat status
- QR code generation for bus pass verification
- Booking confirmation page
- Booking history management
- User dashboard and profile page
- Responsive and modern user interface

---


## 👩‍💻 Author

**Boomika Govindarajan**  
🎓 B.Tech Information Technology Student
