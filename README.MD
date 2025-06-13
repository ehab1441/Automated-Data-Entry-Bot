# 📝 Automated Data Entry Bot for Notepad

This Python project automates data entry into the Windows Notepad application using **BotCity** and **PyAutoGUI**. It fetches blog posts from the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/guide/) and saves them as `.txt` files on the desktop.

## 🚀 Features

- Opens Notepad automatically.
- Fetches and types 10 blog posts (title + body).
- Saves each post as `post 1.txt`, `post 2.txt`, etc., inside a `posts/` folder.
- Handles errors during app launching or API failure.
- Falls back to PyAutoGUI if BotCity is unavailable.

## 🛠️ Requirements

- Python 3.x
- Notepad (pre-installed on Windows)
- Python packages:
  - `pyautogui`
  - `requests`
  - `botcity-core`

## 📦 Installation

```bash
git clone https://github.com/yourusername/tjm-project.git
cd tjm-project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
````

If you're using **BotCity**, create a folder named `resources` inside the project and place a screenshot of the Notepad icon as `notepad_icon.png`.

## 📁 Project Structure

```
tjm-project/
│
├── main.py                   # Main automation script
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── resources/                # Assets for BotCity (if used)
│   └── notepad_icon.png      # Screenshot for visual automation
└── posts/                    # Output folder for saved blog posts (created at runtime)
    ├── post 1.txt
    ├── post 2.txt
    └── ...
```

> 📝 The `posts/` folder is automatically created in the `tjm-project` directory when you run the script.

## 📜 Usage

```bash
python main.py
```

* Move your mouse away once the automation starts.
* The script will open Notepad, type content, and save files automatically.

## 🧠 Technical Notes

* Uses BotCity for visual recognition of Notepad icon. Falls back to `Win + R` launch if not found.

* Types each blog post with the following structure:

  ```
  Title: <post title>

  Body:
  <post body>
  ```

* Saves all text files in `tjm-project/posts` with filenames based on the post ID.

## ⚠️ Disclaimer

* Works only on **Windows OS**.
* Make sure **Notepad is closed** before starting the script.
* If you're using BotCity, ensure proper screenshots and resolution compatibility.

---
