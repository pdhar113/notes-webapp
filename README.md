# NotesApp - Personal Note-Taking Application

NotesApp is a professional, clean, and minimalist web application built with Flask. It allows users to securely create an account, log in, and manage their personal notes with timestamps.

## 🚀 Features

- **User Authentication**: Secure Sign-up, Login, and Logout functionality powered by Flask-Login.
- **Personal Notes**: Create and delete notes that are privately stored and linked to your account.
- **Modern Design**: A polished, responsive UI built with Vanilla CSS and modern typography (Inter font).
- **Auto-dismiss Alerts**: Professional flash messages that automatically disappear after a short delay.
- **Secure Handling**: Backend protection for note deletion and custom error pages (404/500).

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Database**: SQLite (SQLAlchemy ORM)
- **Frontend**: HTML5, Vanilla CSS, JavaScript, Bootstrap 4 (for layout)
- **Security**: Werkzeug password hashing, Flask-Login authentication

## 📋 Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python main.py
   ```
   The app will be available at `http://127.0.0.1:5000`.

## 📂 Project Structure

- `main.py`: Entry point for the application.
- `website/`: Main package directory.
  - `__init__.py`: App factory and configuration.
  - `auth.py`: Authentication routes (Login/Signup).
  - `views.py`: Main application routes (Notes).
  - `model.py`: Database schemas for User and Note.
  - `templates/`: Jinja2 HTML templates.
  - `static/`: CSS and JavaScript assets.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
