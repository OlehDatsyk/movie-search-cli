# 🎬 Movie Search CLI

A professional, production-ready command-line application for searching movies
and viewing detailed information - release year, runtime, genres, director,
actors, IMDb rating, plot, poster URL, country, language, and awards - powered
by the [OMDb API](https://www.omdbapi.com/) and beautifully rendered in your
terminal using [Rich](https://github.com/Textualize/rich).

This README is written for someone who has **zero prior experience** and has
only installed **Visual Studio Code**. Follow every step in order and you
will have the application running successfully.

---

## 📋 Table of Contents

1. [What You Need Before Starting](#-what-you-need-before-starting)
2. [Step 1: Install Python](#step-1-install-python)
3. [Step 2: Install Git (Optional but Recommended)](#step-2-install-git-optional-but-recommended)
4. [Step 3: Get the Project Files into VS Code](#step-3-get-the-project-files-into-vs-code)
5. [Step 4: Open the Project in VS Code](#step-4-open-the-project-in-vs-code)
6. [Step 5: Create a Virtual Environment](#step-5-create-a-virtual-environment)
7. [Step 6: Activate the Virtual Environment](#step-6-activate-the-virtual-environment)
8. [Step 7: Install Project Dependencies](#step-7-install-project-dependencies)
9. [Step 8: Get a Free OMDb API Key](#step-8-get-a-free-omdb-api-key)
10. [Step 9: Set Up the .env File](#step-9-set-up-the-env-file)
11. [Step 10: Run the Application](#step-10-run-the-application)
12. [Usage Examples](#-usage-examples)
13. [Project Folder Structure](#-project-folder-structure)
14. [Common Errors and Solutions](#-common-errors-and-solutions)
15. [Quick Reference: All Terminal Commands](#-quick-reference-all-terminal-commands)

---

## 🧰 What You Need Before Starting

- A Windows, macOS, or Linux computer
- [Visual Studio Code](https://code.visualstudio.com/) already installed
- An internet connection (to install software and to call the OMDb API)
- About 15–20 minutes

You do **not** need any prior programming experience. Every command below can
be typed directly into the VS Code terminal.

---

## Step 1: Install Python

The application is written in Python, so Python must be installed on your
computer first.

1. Go to the official Python website: **https://www.python.org/downloads/**
2. Click the yellow **"Download Python 3.x.x"** button (any version 3.9 or
   newer works fine - 3.11 or 3.12 is recommended).
3. Run the installer you downloaded.
   - **Windows users:** On the very first installer screen, make sure you
     check the box that says **"Add python.exe to PATH"** at the bottom
     before clicking "Install Now". This step is critical - if you skip it,
     Python commands will not work in the terminal.
   - **macOS users:** Run the downloaded `.pkg` file and follow the
     installation wizard (Continue -> Continue -> Install).
4. After installation finishes, verify it worked:
   - Open VS Code.
   - Open the built-in terminal: click **Terminal -> New Terminal** in the
     top menu (or press `` Ctrl+` `` on Windows/Linux, `` Cmd+` `` on macOS).
   - Type the following command and press Enter:

     ```bash
     python --version
     ```

     If that doesn't show a version number, try:

     ```bash
     python3 --version
     ```

   - You should see output similar to:

     ```
     Python 3.12.1
     ```

   If you see a version number, Python is installed correctly. ✅

5. **Install the VS Code Python extension** (strongly recommended):
   - Click the **Extensions** icon in the left sidebar of VS Code (it looks
     like four squares, one detached).
   - Search for **"Python"** (published by Microsoft).
   - Click **Install**.
   - This extension gives you syntax highlighting, IntelliSense, and lets VS
     Code automatically detect your virtual environment (set up in Step 5).

---

## Step 2: Install Git (Optional but Recommended)

Git is only needed if you plan to clone this project from a Git repository
(for example, GitHub). If you already have the project files as a ZIP folder
or a local folder, you can **skip this step** and go straight to
[Step 3](#step-3-get-the-project-files-into-vs-code).

1. Go to **https://git-scm.com/downloads**
2. Download and run the installer for your operating system.
3. Keep clicking "Next" using all default options - the defaults are fine
   for beginners.
4. Verify installation by opening a VS Code terminal and typing:

   ```bash
   git --version
   ```

   You should see something like:

   ```
   git version 2.44.0
   ```

---

## Step 3: Get the Project Files into VS Code

You have two options:

### Option A - You already have the project folder (e.g. downloaded as ZIP)

1. If the project is a `.zip` file, right-click it and choose
   **"Extract All..."** (Windows) or double-click it (macOS) to unzip it.
2. Make sure the extracted folder is named `movie-search-cli` and contains
   files like `main.py`, `requirements.txt`, etc.
3. Move this folder somewhere easy to find, such as your Desktop or
   Documents folder.

### Option B - Cloning from a Git repository

If this project lives in a Git repository, open a terminal (outside VS Code,
or use VS Code's terminal from any starting folder) and run:

```bash
git clone <repository-url>
cd movie-search-cli
```

Replace `<repository-url>` with the actual repository URL.

---

## Step 4: Open the Project in VS Code

1. Open Visual Studio Code.
2. Click **File -> Open Folder...** (macOS: **File -> Open...**).
3. Navigate to and select the `movie-search-cli` folder.
4. Click **Select Folder** (or **Open** on macOS).
5. You should now see the project files listed in the **Explorer** panel on
   the left side of VS Code:

   ```
   movie-search-cli/
   ├── .env.example
   ├── .gitignore
   ├── config.py
   ├── main.py
   ├── movie_service.py
   ├── README.md
   ├── requirements.txt
   └── utils.py
   ```

6. Open a terminal **inside this project folder**: go to
   **Terminal -> New Terminal** in the top menu. The terminal prompt should
   show you are inside the `movie-search-cli` directory.

---

## Step 5: Create a Virtual Environment

A virtual environment is an isolated, self-contained space where this
project's Python packages are installed - separate from other projects on
your computer. This avoids version conflicts and keeps your system clean.

In the VS Code terminal (make sure you are inside the `movie-search-cli`
folder), run:

```bash
python -m venv venv
```

(If `python` doesn't work, try `python3 -m venv venv` instead.)

This creates a new folder named `venv` inside your project. Nothing will
print on success - that's normal. You should now see a `venv/` folder appear
in the VS Code Explorer panel on the left.

---

## Step 6: Activate the Virtual Environment

You must "activate" the virtual environment every time you open a new
terminal to work on this project. Activation tells your terminal to use the
isolated Python and packages inside `venv` instead of your system-wide
Python.

Choose the command that matches your operating system and terminal type:

### Windows (PowerShell - this is the VS Code default terminal)

```powershell
.\venv\Scripts\Activate.ps1
```

> **If you get a "running scripts is disabled" error**, see the
> [Common Errors](#-common-errors-and-solutions) section below - it's a
> one-time fix.

### Windows (Command Prompt / cmd.exe)

```cmd
venv\Scripts\activate.bat
```

### macOS / Linux (bash, zsh)

```bash
source venv/bin/activate
```

### How to know it worked

Your terminal prompt should now show `(venv)` at the beginning of the line,
like this:

```
(venv) C:\Users\YourName\movie-search-cli>
```

or on macOS/Linux:

```
(venv) yourname@YourMac movie-search-cli %
```

If you see `(venv)`, the virtual environment is active. ✅ Keep it active for
every step below.

> 💡 **Tip:** VS Code often detects the `venv` folder automatically and asks
> "Select this environment as your workspace interpreter?" - click **Yes**.
> You can also select it manually: press `Ctrl+Shift+P` (or `Cmd+Shift+P` on
> macOS), type **"Python: Select Interpreter"**, and choose the one that
> mentions `./venv`.

---

## Step 7: Install Project Dependencies

With the virtual environment **activated** (you see `(venv)` in the prompt),
install all required Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

This installs:

| Package        | Purpose                                          |
|----------------|---------------------------------------------------|
| `requests`     | Makes HTTP calls to the OMDb API                  |
| `rich`         | Renders beautiful tables, panels, and colors in the terminal |
| `python-dotenv`| Loads your API key safely from a `.env` file      |

You should see output ending with something like:

```
Successfully installed requests-2.32.3 rich-13.9.4 python-dotenv-1.0.1
```

If you see "Successfully installed", the installation worked. ✅

---

## Step 8: Get a Free OMDb API Key

This application uses the OMDb API to fetch movie data. You need a free
personal API key.

1. Open your browser and go to: **https://www.omdbapi.com/apikey.aspx**
2. Select the **FREE (1,000 daily limit)** option.
3. Fill in your email address and accept the terms.
4. Click **Submit**.
5. Check your email inbox - OMDb will send you an activation link.
6. Click the activation link in the email. Your API key will be shown on the
   confirmation page and also included in the email (it looks like a short
   string of letters/numbers, e.g. `a1b2c3d4`).
7. Copy this API key - you'll need it in the next step.

> ⚠️ Keep your API key private. Don't share it publicly or commit it to
> GitHub. This project's `.gitignore` already prevents your `.env` file
> (where the key lives) from being committed.

---

## Step 9: Set Up the .env File

The application reads your API key from a file named `.env` (not
`.env.example`) in the project root.

1. In the VS Code Explorer panel, right-click on the `.env.example` file.
2. Click **Copy**, then right-click the `movie-search-cli` folder and click
   **Paste**. This creates a copy named `.env.example copy` or similar.
3. Rename the copied file to exactly: `.env`
   (Right-click the file -> **Rename**, then type `.env` and press Enter.)

   Alternatively, do it entirely from the terminal:

   **Windows (PowerShell):**
   ```powershell
   Copy-Item .env.example .env
   ```

   **macOS / Linux:**
   ```bash
   cp .env.example .env
   ```

4. Open the new `.env` file in VS Code (click it in the Explorer panel).
5. Replace `your_api_key_here` with the real API key you copied in Step 8:

   ```
   OMDB_API_KEY=a1b2c3d4
   ```

   (Use your actual key - the example above is just a placeholder.)

6. Save the file: **File -> Save** or `Ctrl+S` (`Cmd+S` on macOS).

Your `.env` file should now look like this (with your real key):

```
OMDB_API_KEY=a1b2c3d4
OMDB_BASE_URL=https://www.omdbapi.com/
REQUEST_TIMEOUT=10
```

---

## Step 10: Run the Application

Make sure:
- Your virtual environment is still activated (`(venv)` visible in the
  terminal prompt).
- Your `.env` file is saved with a valid API key.
- Your terminal is inside the `movie-search-cli` folder.

### Interactive mode (recommended for beginners)

Simply run:

```bash
python main.py
```

You will be prompted to type a movie title interactively. Type `exit` at
any time to quit.

### Direct search mode

Search for one specific movie directly:

```bash
python main.py "Inception"
```

Search with a specific release year to disambiguate remakes:

```bash
python main.py "The Lion King" --year 2019
```

List multiple matching results instead of a single movie:

```bash
python main.py "Batman" --search
```

---

## 💻 Usage Examples

### Example 1 - Interactive mode

**Command:**
```bash
python main.py
```

**Expected terminal output:**

```
╭──────────────────────────────────────────────────────────────╮
│ Movie Search CLI v1.0.0                                       │
│ Search for any movie and view detailed information powered by │
│ the OMDb API.                                                  │
╰──────────────────────────────────────────────────────────────╯
╭─────────────────────────────── Info ───────────────────────────────╮
│ Type a movie title to search, or type 'exit' at any time to quit.  │
╰──────────────────────────────────────────────────────────────────╯

Enter a movie title: Inception
Release year (optional, press Enter to skip):

╭─────────────────────── Inception (2010) ───────────────────────╮
│ Title          Inception                                        │
│ Release Year   2010                                              │
│ Runtime        148 min                                           │
│ Genres         Action, Adventure, Sci-Fi                         │
│ Director       Christopher Nolan                                 │
│ Actors         Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot... │
│ IMDb Rating    8.8 / 10                                          │
│ Country        United States, United Kingdom                    │
│ Language       English, Japanese, French                        │
│ Awards         Won 4 Oscars. 157 wins & 220 nominations total    │
│ Poster URL     https://m.media-amazon.com/images/...             │
│ Plot           A thief who steals corporate secrets through...   │
╰──────────────────────────────────────────────────────────────────╯
```

### Example 2 - Direct search with a year

**Command:**
```bash
python main.py "The Lion King" --year 2019
```

**Expected output:** a formatted panel with details for the 2019 remake
instead of the 1994 original.

### Example 3 - Listing multiple results

**Command:**
```bash
python main.py "Batman" --search
```

**Expected terminal output:**

```
                    Search Results
┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━━━━┓
┃ # ┃ Title                   ┃ Year ┃ IMDb ID   ┃
┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━━━━┩
│ 1 │ Batman Begins           │ 2005 │ tt0372784 │
│ 2 │ Batman                  │ 1989 │ tt0096895 │
│ 3 │ Batman Returns          │ 1992 │ tt0103776 │
└───┴─────────────────────────┴──────┴───────────┘
```

### Example 4 - Movie not found

**Command:**
```bash
python main.py "asdkjfhaskjdfh"
```

**Expected terminal output:**

```
╭────────────────────────────── Warning ──────────────────────────────╮
│ No movie found matching 'asdkjfhaskjdfh'.                            │
│                                                                       │
│ Tip: Double-check the spelling, or try searching without the release │
│ year.                                                                │
╰───────────────────────────────────────────────────────────────────────╯
```

---

## 📁 Project Folder Structure

```
movie-search-cli/
│
├── main.py              # CLI entry point: argument parsing, interactive
│                         # mode, and rendering results to the terminal
├── movie_service.py      # OMDb API client: HTTP requests, response
│                         # parsing, and custom error handling
├── config.py             # Loads and validates environment variables
│                         # (API key, base URL, timeout) from .env
├── utils.py               # Shared Rich Console instance + formatting
│                         # helpers (tables, panels, error/success messages)
├── requirements.txt      # Exact list of Python packages this project needs
├── .env.example           # Template showing which environment variables
│                         # are required (safe to commit to Git)
├── .env                   # Your real API key (created by you in Step 9,
│                         # NEVER committed to Git - see .gitignore)
├── .gitignore             # Tells Git which files/folders to ignore
│                         # (venv/, .env, __pycache__/, etc.)
└── README.md               # This file
```

---

## 🛠 Common Errors and Solutions

### ❌ `'python' is not recognized as an internal or external command`

**Cause:** Python isn't installed, or wasn't added to your system PATH.

**Solution:**
- Reinstall Python from https://www.python.org/downloads/ and make sure to
  check **"Add python.exe to PATH"** during installation (Windows).
- Close and reopen the VS Code terminal after installing.
- Try `python3` instead of `python`.

---

### ❌ `running scripts is disabled on this system` (PowerShell, Windows)

**Cause:** Windows PowerShell blocks running local scripts (like the venv
activation script) by default for security reasons.

**Solution:** Run this command once in your VS Code terminal (as a regular
user, not Administrator), then try activating again:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Type `Y` and press Enter if prompted. Then retry:

```powershell
.\venv\Scripts\Activate.ps1
```

---

### ❌ `ModuleNotFoundError: No module named 'rich'` (or `requests` / `dotenv`)

**Cause:** Either the virtual environment isn't activated, or dependencies
weren't installed.

**Solution:**
1. Confirm your terminal prompt shows `(venv)`. If not, repeat
   [Step 6](#step-6-activate-the-virtual-environment).
2. Re-run:
   ```bash
   pip install -r requirements.txt
   ```

---

### ❌ Missing OMDb API key error when running the app

**Cause:** The `.env` file is missing, misnamed, or doesn't contain a valid
key.

**Solution:**
- Confirm a file named exactly `.env` (not `.env.example` or `.env.txt`)
  exists in the project root.
- Open it and confirm it contains a line like:
  ```
  OMDB_API_KEY=your_real_key_here
  ```
- Make sure there are no extra quotes or spaces around the key.
- Save the file and re-run `python main.py`.

---

### ❌ `Invalid API key!` error when searching

**Cause:** The API key in `.env` is incorrect, not yet activated, or was
mistyped.

**Solution:**
- Double-check you clicked the activation link in the email OMDb sent you.
- Re-copy the key exactly from the OMDb confirmation email/page (no extra
  spaces).
- Update the `.env` file and save it again.

---

### ❌ `Could not connect to the OMDb API` / timeout errors

**Cause:** No internet connection, a firewall/VPN blocking the request, or
OMDb's servers are temporarily down.

**Solution:**
- Check your internet connection.
- Try opening https://www.omdbapi.com/ directly in your browser to confirm
  it's reachable.
- Temporarily disable any VPN or strict firewall and try again.

---

### ❌ VS Code terminal still shows the system Python, not the venv one

**Solution:**
- Press `Ctrl+Shift+P` (`Cmd+Shift+P` on macOS) -> type **"Python: Select
  Interpreter"** -> choose the interpreter path that includes `venv`
  (e.g. `./venv/bin/python` or `.\venv\Scripts\python.exe`).
- Close the terminal panel and open a new one (**Terminal -> New Terminal**)
  so it picks up the newly selected interpreter.

---

### ❌ Nothing happens / blank output after running `python main.py`

**Cause:** Usually means the terminal is waiting for input in interactive
mode.

**Solution:** Just type a movie title and press Enter - the prompt
`Enter a movie title:` should be visible just above your cursor.

---

## ⚡ Quick Reference: All Terminal Commands

Run these **in order**, inside the VS Code terminal, from the
`movie-search-cli` folder:

```bash
# 1. Check Python is installed
python --version

# 2. Create the virtual environment
python -m venv venv

# 3. Activate the virtual environment
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Windows cmd.exe:
venv\Scripts\activate.bat
# macOS / Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Set up your .env file (only once)
# Windows PowerShell:
Copy-Item .env.example .env
# macOS / Linux:
cp .env.example .env
# ...then edit .env and paste in your real OMDb API key

# 6. Run the app (interactive mode)
python main.py

# 6b. Or run a direct search
python main.py "Inception"
python main.py "The Lion King" --year 2019
python main.py "Batman" --search

# 7. When you're done, deactivate the virtual environment
deactivate
```

---

## ✅ You're All Set

If you followed every step above, you now have a fully working,
professional Movie Search CLI running locally in VS Code. Search for your
favorite movies and enjoy the beautifully formatted results right in your
terminal! 🍿

If something still isn't working after checking the
[Common Errors](#-common-errors-and-solutions) section, re-read Steps 5–9
carefully - the vast majority of issues come from either the virtual
environment not being activated or the `.env` file being missing/incorrect.
