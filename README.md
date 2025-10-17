# 📚 Book Tracking Library

A lightweight, elegant book tracking web application built with Python Flask and SQLite. Keep track of your personal library, manage your reading progress, and organize your book collection all in one place.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0+-green.svg)
![SQLite](https://img.shields.io/badge/sqlite-3-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

- **📖 Book Management**: Add, edit, and delete books from your personal library
- **⭐ Ratings & Reviews**: Rate your books and add personal notes
- **💾 Persistent Storage**: All data stored securely in a local SQLite database
- **🎨 Clean Interface**: Simple, intuitive UI for easy navigation
- **📱 Responsive Design**: Works seamlessly on desktop and mobile devices

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/lazy-blake/Book-Tracking-Library.git
   cd Book-Tracking-Library
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (optional)

   ```bash
   # Create a .env file
   echo "DATABASE_URL=sqlite:///library.db" > .env
   echo "SECRET_KEY=your-secret-key-here" >> .env
   ```

5. **Initialize the database**

   ```bash
   python init_db.py
   # or
   flask db init
   ```

6. **Run the application**

   ```bash
   python app.py
   # or
   flask run
   ```

7. **Open your browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
Book-Tracking-Library/
├── app.py                  # Main Flask application
├── models.py              # Database models
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── .gitignore            # Git ignore rules
├── static/               # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── add_book.html
│   └── book_detail.html
└── instance/             # Instance folder (SQLite database)
    └── library.db
```

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite (lightweight database)
- **ORM**: Flask-SQLAlchemy (database abstraction)
- **Frontend**: HTML, CSS, JavaScript
- **Templating**: Jinja2

## 📖 Usage

### Adding a Book

1. Click on "Add Book" button
2. Fill in book details:
   - Title
   - Author
   - ISBN (optional)
   - Publication year
3. Click "Save" to add to your library

### Managing Books

- **View Details**: Click on any book to see full information
- **Edit**: Update book information anytime
- **Delete**: Remove books from your library

## 🔧 Configuration

Create a `.env` file in the root directory:

```env
# Database Configuration
DATABASE_URL=sqlite:///library.db

# Flask Configuration
SECRET_KEY=your-super-secret-key-change-this
FLASK_ENV=development
DEBUG=True

# Optional: Change default port
FLASK_RUN_PORT=5000
```

## 📦 Dependencies

Core dependencies (install via `requirements.txt`):

```
Flask>=3.0.0
Flask-SQLAlchemy>=3.0.0
python-dotenv>=1.0.0
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

## 🐛 Bug Reports & Feature Requests

Found a bug or have a feature idea? Please open an issue on GitHub with:

- Clear description of the bug/feature
- Steps to reproduce (for bugs)
- Expected behavior
- Screenshots (if applicable)

## 📝 To-Do List

- [ ] Add user authentication system
- [ ] Implement book cover upload
- [ ] Add reading statistics dashboard
- [ ] Export library to CSV/PDF
- [ ] Reading goals and challenges

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**lazy-blake**

- GitHub: [@lazy-blake](https://github.com/lazy-blake)

## 🙏 Acknowledgments

- Flask documentation and community
- SQLAlchemy for excellent ORM functionality
- All contributors who help improve this project

## 📸 Screenshots

_Add screenshots of your application here to showcase the UI_

---

### 💡 Tips for Users

- **Backup your database**: Regularly backup the `instance/library.db` file
- **Book data**: Consider adding ISBNs to enable future API integrations
- **Performance**: For large libraries (1000+ books), consider PostgreSQL instead of SQLite

### 🆘 Troubleshooting

**Database not found error?**

```bash
# Make sure to initialize the database first
python init_db.py
```

**Port already in use?**

```bash
# Change the port in .env file or run with:
flask run --port 5001
```

**Module not found error?**

```bash
# Ensure all dependencies are installed
pip install -r requirements.txt
```

---

⭐ If you find this project helpful, please consider giving it a star on GitHub!
