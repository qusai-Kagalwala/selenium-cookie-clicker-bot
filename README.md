# 🍪 Selenium Cookie Clicker Bot

An automated Cookie Clicker bot built with Python and Selenium that continuously clicks the cookie, analyzes the store in real-time, and purchases the most optimal (most expensive affordable) upgrade every 5 seconds.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?logo=selenium&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📖 About

This project automates gameplay on [Cookie Clicker](https://ozh.github.io/cookieclicker/) using Selenium WebDriver. The bot handles everything — language selection on startup, continuous cookie clicking, real-time cookie count parsing, and intelligent store purchasing — all without any human input. It runs for a configurable duration (default: 5 minutes) and logs every purchase to the console.

The repo also includes two supplementary Selenium scripts (`main.py` and `interaction.py`) that demonstrate core browser automation concepts like element location, scraping, and keyboard simulation on Python.org and Wikipedia.

---

## ✨ Features

- 🖱️ **Continuous auto-clicking** — clicks the big cookie as fast as the loop allows
- 🏪 **Greedy purchase strategy** — every 5 seconds, buys the most expensive item the current cookie count can afford (product0–product17)
- 🌐 **Auto language selection** — detects and clicks the English language button on startup
- 📊 **Real-time cookie parsing** — reads and parses the live cookie count (handles comma-formatted numbers)
- ⏱️ **Timed execution** — stops automatically after 5 minutes and prints the final cookie score
- 🛡️ **Graceful error handling** — catches `NoSuchElementException` and `ValueError` without crashing

---

## 📁 Project Structure

```
selenium-cookie-clicker-bot/
│
├── cookie.py          # Main bot — Cookie Clicker automation
├── main.py            # Demo script — Python.org event scraper
├── interaction.py     # Demo script — Wikipedia search automation
└── README.md
```

| File | Description |
|------|-------------|
| `cookie.py` | Core bot logic: launches Cookie Clicker, clicks, and buys upgrades |
| `main.py` | Scrapes upcoming events from python.org using CSS selectors |
| `interaction.py` | Demonstrates form interaction, link navigation, and keyboard input on Wikipedia |

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Selenium WebDriver** — browser automation
- **ChromeDriver** — Chrome browser control
- **`time` module** — loop timing and session duration

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.x installed
- Google Chrome installed
- ChromeDriver matching your Chrome version ([download here](https://chromedriver.chromium.org/downloads))

### 1. Clone the repository

```bash
git clone https://github.com/qusai-Kagalwala/selenium-cookie-clicker-bot.git
cd selenium-cookie-clicker-bot
```

### 2. Install dependencies

```bash
pip install selenium
```

### 3. Run the bot

```bash
python cookie.py
```

Chrome will open automatically, navigate to Cookie Clicker, and the bot will begin.

---

## 🤖 How It Works

```
Start
  └── Launch Chrome & open Cookie Clicker
        └── Click English language button
              └── Locate #bigCookie element
                    └── LOOP (5 minutes):
                          ├── Click cookie (every iteration)
                          └── Every 5 seconds:
                                ├── Read current cookie count
                                ├── Scan store (product0 → product17)
                                ├── Find most expensive "enabled" item
                                └── Purchase it → reset timer
  └── Print final cookie count & exit
```

**Purchase Strategy:** The bot iterates through the store in reverse order (most expensive → cheapest) and buys the first item whose class includes `"enabled"` — meaning the player can currently afford it. This greedy approach prioritizes higher-value buildings over cheaper ones.

---

## 📋 Configuration

Inside `cookie.py`, you can tweak these constants:

| Variable | Default | Description |
|----------|---------|-------------|
| `wait_time` | `5` | Seconds between each store purchase check |
| `five_min` | `time() + 60 * 5` | Total bot runtime (currently 5 minutes) |

To run the bot for 10 minutes, change:
```python
five_min = time() + 60 * 10
```

---

## 📌 Notes

- The `detach=True` Chrome option keeps the browser open after the script ends so you can inspect the final game state.
- `main.py` and `interaction.py` are standalone learning scripts and do not depend on `cookie.py`.
- ChromeDriver must match your installed version of Chrome. If you get a session error, update ChromeDriver.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Qusai Kagalwala**  
[![GitHub](https://img.shields.io/badge/GitHub-qusai--Kagalwala-181717?logo=github)](https://github.com/qusai-Kagalwala)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-qusai--kagalwala-0A66C2?logo=linkedin)](https://www.linkedin.com/in/qusai-kagalwala/)
[![DevVault](https://img.shields.io/badge/Portfolio-DevVault-blueviolet?logo=github)](https://github.com/qusai-Kagal/DevVault)
