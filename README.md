# 💬 Real-Time Chat Application

A full-stack real-time chat application built using Django and Django Channels, enabling seamless and instant communication between multiple users using WebSockets.

---

## 🚀 Live Features

✨ Real-time messaging (no refresh required)  
👥 Multi-user communication in a shared chat room  
💾 Persistent message storage (database-backed)  
🔄 Automatic chat history loading on refresh  
🧹 Admin panel for message management  
🎨 Clean and user-friendly chat interface  

---

## 🧠 Project Overview

This application demonstrates how to build a scalable real-time communication system using Django and WebSockets. Unlike traditional HTTP-based apps, this project uses Django Channels to maintain a persistent connection between client and server, allowing instant data exchange.

---

## ⚙️ Tech Stack

| Layer        | Technology |
|-------------|-----------|
| Backend     | Django |
| Real-time   | Django Channels (WebSocket) |
| Frontend    | HTML, CSS, JavaScript |
| Database    | SQLite |
| Server      | Daphne (ASGI) |

---

## 🔄 Application Flow

1. User enters a message in the chat interface  
2. Message is sent via WebSocket connection  
3. Django Channels Consumer receives the message  
4. Message is saved to the database  
5. Message is broadcast to all connected users  
6. UI updates instantly without page reload  

---

## 📂 Project Structure
chatproject/
│
├── chat/
│ ├── models.py # Database model for messages
│ ├── views.py # Handles HTTP requests
│ ├── consumers.py # Handles WebSocket connections
│ ├── routing.py # WebSocket URL routing
│ ├── admin.py # Admin configuration
│
├── chatproject/
│ ├── settings.py # Project configuration
│ ├── asgi.py # ASGI entry point for Channels
│ ├── urls.py # URL routing
│
├── templates/
│ └── home.html # Frontend UI
│
├── db.sqlite3 # Database
└── manage.py


---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

git clone https://github.com/ShravaniShinde-0808/django-chat-app.git

cd django-chat-app


### 2️⃣ Install dependencies

pip install django channels daphne


### 3️⃣ Run the server

daphne chatproject.asgi:application


### 4️⃣ Open in browser

http://127.0.0.1:8000/


---

## 🔐 Admin Panel Access

- URL: http://127.0.0.1:8000/admin/  
- Create superuser:

python manage.py createsuperuser


- Manage chat messages (view/delete)

---

## 📈 Key Learnings

- Implemented real-time communication using WebSockets  
- Understood Django Channels architecture  
- Managed asynchronous message handling  
- Integrated backend with dynamic frontend updates  
- Worked with database persistence  

---

## 🚀 Future Enhancements

- 🔐 User authentication (Login/Signup)  
- 💬 Multiple chat rooms  
- ⏰ Message timestamps in UI  
- 🎨 Advanced UI (WhatsApp-like design)  
- 📱 Mobile responsiveness  

---

## 👩‍💻 Author

**Shravani Shinde**

---

## ⭐ Show Your Support

If you found this project helpful, consider giving it a ⭐ on GitHub!
