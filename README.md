# gitCheetSheet
1. একটি Python file বানাও

ধরো:

D:\Git-Cheat-Sheet\generate.py

Notepad/VS Code/IntelliJ-তে generate.py নামে save করো।

তারপর তোমার পুরো Python code:

from pathlib import Path

html = r'''<!DOCTYPE html>
<html lang="bn">
...
</html>
'''

path = Path("git-github-powershell-cheat-sheet.html")
path.write_text(html, encoding="utf-8")

print(f"Created: {path}")

এভাবে থাকবে।

গুরুত্বপূর্ণ: আমি এখানে পুরো HTML আবার paste করছি না—তোমার দেওয়া বড় html = r''' ... ''' অংশটাই ওই জায়গায় থাকবে।

2. PowerShell থেকে folder-এ যাও
cd "D:\Git-Cheat-Sheet"

Check করো:

dir

দেখাবে:

generate.py
3. Python install আছে কিনা দেখো
python --version

যেমন:

Python 3.13.5

হলে ঠিক আছে।

যদি python is not recognized আসে, তাহলে Python install করতে হবে।

4. Python code execute করো
python generate.py

যদি সব ঠিক থাকে, output:

Created: git-github-powershell-cheat-sheet.html

তারপর:

dir

দেখবে:

generate.py
git-github-powershell-cheat-sheet.html
5. HTML browser-এ খুলবে

PowerShell থেকে:

start .\git-github-powershell-cheat-sheet.html

অথবা File Explorer থেকে:

git-github-powershell-cheat-sheet.html

-এ double click করো।

তাহলেই তোমার সুন্দর Git/GitHub Cheat Sheet browser-এ খুলবে।

তোমার workflow হবে:

generate.py
     ↓
python generate.py
     ↓
git-github-powershell-cheat-sheet.html
     ↓
Browser

এর সুবিধা হলো, ভবিষ্যতে HTML-এর content পরিবর্তন করতে চাইলে শুধু Python file-এর:

html = r'''
...
'''

এর ভিতরের HTML/CSS/JS পরিবর্তন করবে।

তারপর আবার:

python generate.py

দিলেই নতুন HTML তৈরি হবে।
