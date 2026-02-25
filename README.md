# libraries-spring2026

## Description
This repo is intended for DATA 4000, and is all about **libraries**

## For installing librarues with a vistual environment
1. create a repo on github
2. open VSC and connect to the repo, which creates a new folder on your computer
3. then create a vistual environment before trying to install packages as follows ( ** BUT YOU WILL NEED TO ADJUST THIS CODE TO YOUR DIRECTORY NAME - THIS WAS DONE ON MY COMPUTER** :

# Create a Virtual Environment Using Python 3.14 (macOS + VS Code)

## 1️⃣ Navigate to Your Project Folder

```bash
cd ~/Documents/DATA\ 4000/libraries-spring2026
```

---

## 2️⃣ Create a Virtual Environment (using Python 3.14)

```bash
python3.14 -m venv .venv
```

This creates a folder named `.venv` inside your project.

---

## 3️⃣ Activate the Virtual Environment

```bash
source .venv/bin/activate
```

You should now see something like:

```bash
(.venv) imowerman@DSBN323-C9522M %
```

---

## 4️⃣ Install Packages Inside the Virtual Environment

```bash
python -m pip install requests
```

⚠️ Always use `python -m pip install ...` instead of just `pip install`.

---

## 5️⃣ Verify the Correct Python Is Being Used

```bash
which python
```

It should return something like:

```bash
.../libraries-spring2026/.venv/bin/python
```

---

## 6️⃣ Tell VS Code to Use the Virtual Environment

1. Press **Cmd + Shift + P**
2. Select **Python: Select Interpreter**
3. Choose the interpreter that includes:

```
.venv/bin/python
```

---

✅ Now your environment is clean, isolated, and using Python 3.14 properly.
