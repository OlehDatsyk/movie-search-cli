# 📘 Movie Search CLI - Complete Beginner's Instruction Guide

This guide assumes you have **never** used Python, Git, a terminal, Visual
Studio Code, or an API before. Every step is spelled out. Just follow the
guide from top to bottom, in order, and don't skip anything.

> ⏱️ **Time required:** ~20-30 minutes for a first-time setup.

---

## Table of Contents

1. [What This App Does](#1-what-this-app-does)
2. [Install Python](#2-install-python)
3. [Install Git](#3-install-git)
4. [Install Visual Studio Code](#4-install-visual-studio-code)
5. [Install the Recommended VS Code Extensions](#5-install-the-recommended-vs-code-extensions)
6. [Open the Project in VS Code](#6-open-the-project-in-vs-code)
7. [Create a Virtual Environment](#7-create-a-virtual-environment)
8. [Activate the Virtual Environment](#8-activate-the-virtual-environment)
9. [Install the Project's Dependencies](#9-install-the-projects-dependencies)
10. [Get a Free OMDb API Key](#10-get-a-free-omdb-api-key)
11. [Create Your .env File](#11-create-your-env-file)
12. [Run the Application](#12-run-the-application)
13. [Using Every Feature](#13-using-every-feature)
14. [Testing the Application](#14-testing-the-application)
15. [Troubleshooting](#15-troubleshooting)
16. [FAQ](#16-faq)
17. [Common Mistakes](#17-common-mistakes)
18. [Security Recommendations](#18-security-recommendations)
19. [Next Learning Steps](#19-next-learning-steps)

---

## 1. What This App Does

Movie Search CLI is a program that runs in a terminal (a text-based window
on your computer). You type a movie title, and it fetches details about
that movie - release year, runtime, genre, director, actors, IMDb rating,
plot, poster link, country, language, and awards - from the free **OMDb
API** (Open Movie Database) and displays it neatly in your terminal.

"CLI" stands for **Command Line Interface** - meaning you interact with it
by typing commands instead of clicking buttons.

---

## 2. Install Python

Python is the programming language this app is written in. Your computer
needs it installed to run the app.

1. Open your web browser and go to **https://www.python.org/downloads/**
2. Click the big **"Download Python 3.x.x"** button (any version 3.9 or
   newer is fine; 3.11 or 3.12 is recommended).
3. Run the installer:
   - **Windows:** ✅ Check the box **"Add python.exe to PATH"** at the
     bottom of the very first installer screen. This is the single most
     common mistake beginners make - if you miss it, nothing else will
     work. Then click **Install Now**.
   - **macOS:** Open the downloaded `.pkg` file and click through
     Continue -> Continue -> Install, then enter your Mac password if asked.
   - **Linux:** Most distributions already include Python. Open a
     terminal and run `python3 --version` to check.
4. Verify the installation by opening a terminal (see Step 6 for how to
   open one inside VS Code) and typing:

   ```bash
   python --version
   ```

   If you see something like `Python 3.11.4`, it worked. If you get an
   error, try `python3 --version` instead (common on macOS/Linux).

---

## 3. Install Git

Git is a tool for downloading and managing code projects. You don't
strictly need it if you already have the project folder on your computer,
but it's recommended for future projects.

1. Go to **https://git-scm.com/downloads**
2. Download the installer for your operating system.
3. Run the installer and click "Next" through the default options - the
   defaults are fine for beginners.
4. Verify it worked by opening a terminal and running:

   ```bash
   git --version
   ```

   You should see something like `git version 2.44.0`.

---

## 4. Install Visual Studio Code

Visual Studio Code (VS Code) is the code editor you'll use to open, edit,
and run this project.

1. Go to **https://code.visualstudio.com/**
2. Click **Download** for your operating system.
3. Run the installer with default settings.
4. Launch VS Code once installation finishes.

---

## 5. Install the Recommended VS Code Extensions

Extensions add extra features to VS Code. Install these two:

1. Click the **Extensions** icon in the left sidebar (it looks like four
   squares, one detached).
2. Search for **"Python"** (published by Microsoft) and click **Install**.
   This gives VS Code the ability to understand and run Python files.
3. Search for **"Pylance"** (also by Microsoft) and click **Install**
   (this is often installed automatically with the Python extension). It
   gives you better auto-complete and error checking.

That's all you need - no FastAPI or web-framework extensions are required
for this project, since it's a terminal application, not a web app.

---

## 6. Open the Project in VS Code

1. Open VS Code.
2. Click **File -> Open Folder...**
3. Browse to the `movie-search-cli` folder (the folder containing
   `main.py`, `config.py`, etc.) and select it.
4. Open the built-in terminal: **Terminal -> New Terminal** in the top
   menu, or press `` Ctrl+` `` (Windows/Linux) or `` Cmd+` `` (macOS).
   A terminal panel will appear at the bottom of the window - this is
   where you'll type all the commands in this guide.

---

## 7. Create a Virtual Environment

A **virtual environment** is an isolated, self-contained folder that
holds Python packages just for this project, so they don't interfere with
other projects or your system's Python installation. Think of it as a
clean, private toolbox for this app only.

In the VS Code terminal, run:

```bash
python -m venv venv
```

(If `python` doesn't work, try `python3 -m venv venv`.)

This creates a new folder called `venv` inside your project. You only need
to do this **once**.

---

## 8. Activate the Virtual Environment

Activating tells your terminal "use the tools inside `venv`, not the
system-wide Python." You must do this **every time** you open a new
terminal to work on this project.

- **Windows (Command Prompt / PowerShell):**

  ```bash
  venv\Scripts\activate
  ```

- **macOS / Linux:**

  ```bash
  source venv/bin/activate
  ```

You'll know it worked when you see `(venv)` appear at the start of your
terminal line.

> 💡 If Windows PowerShell blocks the activation with a "running scripts
> is disabled" error, see the [Troubleshooting](#15-troubleshooting)
> section below.

---

## 9. Install the Project's Dependencies

Dependencies are external packages the app relies on (listed in
`requirements.txt`: `requests`, `rich`, and `python-dotenv`). With your
virtual environment activated, run:

```bash
pip install -r requirements.txt
```

This downloads and installs everything the app needs. You'll see progress
messages; wait for the terminal prompt to return.

---

## 10. Get a Free OMDb API Key

An **API key** is a personal password that lets this app fetch movie data
from OMDb's servers on your behalf.

1. Go to **https://www.omdbapi.com/apikey.aspx**
2. Choose the **FREE** tier (1,000 daily requests - plenty for personal
   use).
3. Enter your email address and submit the form.
4. Check your email inbox - OMDb will send you a key (a short string of
   letters and numbers). You may need to click an activation link in that
   email first.
5. Copy that key somewhere safe; you'll paste it in the next step.

---

## 11. Create Your .env File

The `.env` file stores your personal API key **locally** - it is never
uploaded anywhere and is excluded from Git by `.gitignore`.

1. In VS Code's file explorer, find the file named `.env.example`.
2. Make a copy of it and rename the copy to exactly `.env` (no other
   text - just a dot followed by "env").
   - Easiest way: right-click `.env.example` -> Copy, then right-click the
     folder -> Paste, then rename the new file to `.env`.
3. Open `.env` and replace the placeholder with your real key:

   ```
   OMDB_API_KEY=your_actual_api_key_here
   ```

4. Save the file (`Ctrl+S` / `Cmd+S`).

Leave the other two lines (`OMDB_BASE_URL` and `REQUEST_TIMEOUT`) as they
are - they're optional advanced settings.

---

## 12. Run the Application

With your virtual environment still activated, run:

```bash
python main.py
```

You should see a colorful welcome banner, followed by a prompt asking you
to type a movie title. That means it's working! 🎉

You can also skip the interactive menu and search directly:

```bash
python main.py "Inception"
python main.py "Inception" --year 2010
python main.py "Batman" --search
```

- The double-click startup scripts described below (`Start App.bat` for
  Windows and `Start App (Mac).command` for macOS) do steps 7-9 and 12
  automatically for you after the very first manual setup.

---

## 13. Using Every Feature

| Feature | How to Use It |
|---|---|
| **Interactive mode** | Run `python main.py` with no arguments. Type a title, optionally a year, and press Enter. Type `exit`, `quit`, or `q` to leave. |
| **Direct single search** | `python main.py "Movie Title"` - shows full details for the best match. |
| **Search with a release year** | `python main.py "Movie Title" --year 2010` (or `-y 2010`) - helps disambiguate movies with the same name released in different years. |
| **Search for multiple matches** | `python main.py "Movie Title" --search` (or `-s`) - shows a table of all matching titles instead of one detailed result. |
| **Help / list of options** | `python main.py --help` |

Every detailed result includes: title, release year, runtime, genres,
director, actors, IMDb rating, country, language, awards, poster image
URL, and full plot summary.

---

## 14. Testing the Application

This project doesn't currently ship an automated test suite (see
`PROJECT_REVIEW.md` for details), so "testing" here means manually
verifying it works:

1. Run `python main.py "Inception" --year 2010` - you should see a full
   details panel.
2. Run `python main.py "asdkfjqwer"` (a nonsense title) - you should see
   a friendly yellow "no movie found" warning, not a crash.
3. Temporarily rename your `.env` file and run `python main.py` again -
   you should see a clear red error message telling you the API key is
   missing, not a raw Python error. Rename `.env` back afterward.
4. Turn off your Wi-Fi/internet and try a search - you should see a
   friendly network-error message, not a crash.

If all four behave as described, the app is working correctly.

---

## 15. Troubleshooting

**"python is not recognized as an internal or external command" (Windows)**
Python wasn't added to PATH during installation. Re-run the Python
installer, choose "Modify," and make sure "Add python.exe to PATH" is
checked. Alternatively, try `py` instead of `python`.

**"command not found: python" (macOS/Linux)**
Use `python3` instead of `python` for every command in this guide.

**PowerShell says "running scripts is disabled on this system"**
Run this once in PowerShell (as Administrator is not required):

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then try activating the virtual environment again.

**"No module named 'rich'" (or 'requests', or 'dotenv')**
Your virtual environment either isn't activated or dependencies weren't
installed. Re-run Steps 8 and 9.

**Red error box: "Missing OMDb API key"**
Your `.env` file is missing, misnamed, or empty. Re-check Step 11 - the
file must be named exactly `.env`, in the project's root folder, sitting
next to `main.py`.

**Yellow warning: "No movie found matching '...'"**
The title may be misspelled, or that movie simply isn't in OMDb's
database. Try a simpler or shorter title, or drop the `--year` flag.

**Red error box: "The configured OMDb API key is invalid"**
Double-check you copied the entire key from OMDb's email with no extra
spaces or line breaks, and that you clicked any activation link OMDb sent
you.

**Nothing happens when I double-click `Start App.bat` / `Start App (Mac).command`**
See the comments inside those files - they open a terminal window so you
can read any error messages. If the window flashes and closes instantly,
right-click the file and choose "Edit" to review it, or run it from
inside a terminal instead so the output stays visible.

---

## 16. FAQ

**Do I need to be online to use this app?**
Yes - it fetches live data from the OMDb API every time you search.

**Is the OMDb API key free forever?**
The free tier allows 1,000 requests per day, which resets daily. That's
far more than casual personal use requires.

**Can I search for TV shows?**
Not with this version - searches are currently restricted to movies only
(see `PROJECT_REVIEW.md` for details on this limitation).

**Do I need to activate the virtual environment every time?**
Yes, every time you open a new terminal window to work on or run this
project, run the activation command from Step 8 again.

**Can I run this on a phone or tablet?**
No - this is a desktop command-line application requiring Python.

**Where is my API key stored?**
Only in your local `.env` file, on your own computer. It is never sent
anywhere except directly to OMDb's servers as part of each request.

---

## 17. Common Mistakes

- ❌ Forgetting to check "Add python.exe to PATH" during Python
  installation on Windows.
- ❌ Naming the environment file `.env.txt` or `env` instead of exactly
  `.env`.
- ❌ Forgetting to activate the virtual environment before installing
  dependencies or running the app.
- ❌ Committing the real `.env` file to Git/GitHub (it contains your
  private API key - `.gitignore` is already set up to prevent this, but
  don't override it).
- ❌ Pasting the API key with extra spaces or quotation marks around it.
- ❌ Running `pip install` outside the activated virtual environment,
  which installs packages system-wide instead.

---

## 18. Security Recommendations

- **Never** share your `.env` file or commit it to GitHub. It contains
  your private OMDb API key.
- If you ever accidentally commit your API key, treat it as compromised:
  generate a new one from OMDb and update your local `.env`.
- Don't paste your API key into chat messages, screenshots, or public
  forums when asking for help - redact it first.
- Keep your dependencies reasonably current (`pip list --outdated`) so
  you receive security patches from `requests`, `rich`, and
  `python-dotenv`.
- This app only ever makes outbound GET requests to the OMDb API - it
  does not open any network ports or accept incoming connections, so it
  carries minimal attack surface.

---

## 19. Next Learning Steps

Once you're comfortable running this app, here are good next steps:

1. **Learn basic Python syntax** - freeCodeCamp and the official Python
   tutorial (docs.python.org/3/tutorial) are great free starting points.
2. **Read through `main.py`, `config.py`, `movie_service.py`, and
   `utils.py`** in this project, top to bottom, with comments - this is
   a realistic example of a small, well-organized Python project.
3. **Learn about virtual environments and `pip`** in more depth, since
   you'll use both in almost every Python project.
4. **Try adding a small feature yourself**, such as a `--type series`
   flag to search TV shows instead of movies (OMDb's API already
   supports this - see `movie_service.py`).
5. **Learn Git and GitHub properly** so you can save versions of your
   own projects and share them with others.
6. **Learn about automated testing** with `pytest`, and try writing a
   few tests for `utils.clean_value()` as practice - it's a small, pure
   function that's easy to test.

Good luck, and enjoy exploring! 🎬
