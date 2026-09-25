# gitCheetSheet
হ্যাঁ, **এই Python code-টা চালালে আসলে একটি `.html` file তৈরি হবে**। তোমার Windows PC-তে করার সবচেয়ে সহজ পদ্ধতি নিচে দিলাম।

তবে একটা বিষয়: তোমার দেওয়া code-এ শেষে কিছু জায়গায় copy/paste-এর কারণে `)`/quote বা HTML অংশের formatting সমস্যা হতে পারে। তাই **Python দিয়ে চালানোর আগে code-টা `.py` file হিসেবে ঠিকভাবে save করতে হবে**।

### 1. একটি Python file বানাও

ধরো:

```text
D:\Git-Cheat-Sheet\generate.py
```

Notepad/VS Code/IntelliJ-তে `generate.py` নামে save করো।

তারপর তোমার পুরো Python code:

```python
from pathlib import Path

html = r'''<!DOCTYPE html>
<html lang="bn">
...
</html>
'''

path = Path("git-github-powershell-cheat-sheet.html")
path.write_text(html, encoding="utf-8")

print(f"Created: {path}")
```

এভাবে থাকবে।

**গুরুত্বপূর্ণ:** আমি এখানে পুরো HTML আবার paste করছি না—তোমার দেওয়া বড় `html = r''' ... '''` অংশটাই ওই জায়গায় থাকবে।

---

### 2. PowerShell থেকে folder-এ যাও

```powershell
cd "D:\Git-Cheat-Sheet"
```

Check করো:

```powershell
dir
```

দেখাবে:

```text
generate.py
```

---

### 3. Python install আছে কিনা দেখো

```powershell
python --version
```

যেমন:

```text
Python 3.13.5
```

হলে ঠিক আছে।

যদি `python is not recognized` আসে, তাহলে Python install করতে হবে।

---

### 4. Python code execute করো

```powershell
python generate.py
```

যদি সব ঠিক থাকে, output:

```text
Created: git-github-powershell-cheat-sheet.html
```

তারপর:

```powershell
dir
```

দেখবে:

```text
generate.py
git-github-powershell-cheat-sheet.html
```

---

### 5. HTML browser-এ খুলবে

PowerShell থেকে:

```powershell
start .\git-github-powershell-cheat-sheet.html
```

অথবা File Explorer থেকে:

```text
git-github-powershell-cheat-sheet.html
```

-এ double click করো।

তাহলেই তোমার সুন্দর Git/GitHub Cheat Sheet browser-এ খুলবে।

---

## ⭐ সবচেয়ে গুরুত্বপূর্ণ ব্যাপার

তোমার workflow হবে:

```text
generate.py
     ↓
python generate.py
     ↓
git-github-powershell-cheat-sheet.html
     ↓
Browser
```

এর সুবিধা হলো, ভবিষ্যতে HTML-এর content পরিবর্তন করতে চাইলে শুধু Python file-এর:

```python
html = r'''
...
'''
```

এর ভিতরের HTML/CSS/JS পরিবর্তন করবে।

তারপর আবার:

```powershell
python generate.py
```

দিলেই নতুন HTML তৈরি হবে।

---

### কিন্তু আরও সহজ একটা উপায় আছে

তোমার ক্ষেত্রে **Python ব্যবহার করার কোনো বাস্তব প্রয়োজন নেই**।

কারণ তোমার final product হচ্ছে HTML। তাই সরাসরি:

```text
git-github-powershell-cheat-sheet.html
```

বানিয়ে HTML/CSS/JS রাখাই cleaner approach।

আর যদি তুমি চাও **একটা proper editable project** হিসেবে রাখতে:

```text
git-github-cheatsheet/
│
├── index.html
├── style.css
├── script.js
└── README.md
```

এটাই আমি তোমার জন্য recommend করব। এতে পরে GitHub-এ push করে **GitHub Pages-এ সরাসরি deploy** করাও সহজ হবে।
