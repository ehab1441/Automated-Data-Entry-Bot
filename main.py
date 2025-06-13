import requests
import pyautogui
import time
import os

try:
    from botcity.core import DesktopBot
    bot = DesktopBot()
except ImportError:
    bot = None
    print("BotCity not available, using PyAutoGUI for automation.")

# Fetch the first 10 posts from the API
def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()[:10]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")
        return []

# Open Notepad using BotCity or fallback to PyAutoGUI
def open_notepad():
    print("Opening Notepad...")
    if bot:
        try:
            bot.find_path = "resources"
            bot.find("notepad_icon", matching=0.95, waiting_time=10000)
            bot.click()
            time.sleep(1.5)
            return
        except Exception as e:
            print(f"BotCity: Notepad icon not found or error: {e}. Falling back to PyAutoGUI.")
    
    pyautogui.hotkey("win", "r")
    time.sleep(1)
    pyautogui.typewrite("notepad\n", interval=0.1)
    time.sleep(1.5)

# Type the blog post content into Notepad
def type_post(post):
    title = post["title"]
    body = post["body"]
    content = f"Title: {title}\n\nBody:\n{body}"
    pyautogui.typewrite(content, interval=0.05)

# Save the Notepad file with post ID as the filename
def save_file(post_id):
    print(f"Saving post {post_id}...")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "s")
    time.sleep(1)

    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    project_folder = os.path.join(desktop, "tjm-project", "posts")
    os.makedirs(project_folder, exist_ok=True)

    filepath = os.path.join(project_folder, f"post {post_id}.txt")
    pyautogui.typewrite(filepath, interval=0.05)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('y')  # Confirm overwrite if needed

# Close Notepad
def close_notepad():
    pyautogui.hotkey("ctrl", "w")
    time.sleep(1)
    pyautogui.press('n')  # Don't save again

# Main automation logic
if __name__ == "__main__":
    posts = fetch_posts()
    if not posts:
        print("No posts fetched.")
        exit()

    print("Starting automation in 3 seconds... move your mouse away.")
    time.sleep(3)

    for post in posts:
        try:
            open_notepad()
            type_post(post)
            save_file(post["id"])
            close_notepad()
        except Exception as e:
            print(f"Error processing post {post['id']}: {e}")
