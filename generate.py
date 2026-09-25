from pathlib import Path

html = r'''<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Git & GitHub PowerShell Cheat Sheet — A to Z</title>
<style>
:root{
  --bg:#f5f7fb;--card:#fff;--text:#172033;--muted:#667085;--primary:#2563eb;
  --primary2:#1d4ed8;--border:#dfe4ec;--code:#101828;--codeText:#e6edf7;
  --green:#087443;--red:#b42318;--yellow:#9a6700;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:system-ui,-apple-system,"Segoe UI","Noto Sans Bengali",sans-serif;background:var(--bg);color:var(--text);line-height:1.65}
header{background:linear-gradient(135deg,#0f172a,#1e3a8a);color:#fff;padding:48px 20px 38px}
.hero{max-width:1180px;margin:auto}
h1{font-size:clamp(30px,5vw,52px);line-height:1.1;margin:0 0 12px}
.hero p{max-width:820px;color:#dbeafe;font-size:17px}
.badges span{display:inline-block;border:1px solid #ffffff44;border-radius:999px;padding:5px 11px;margin:4px;font-size:13px}
.layout{max-width:1180px;margin:auto;display:grid;grid-template-columns:260px 1fr;gap:24px;padding:24px 16px}
nav{position:sticky;top:15px;align-self:start;background:var(--card);border:1px solid var(--border);border-radius:14px;padding:15px;max-height:calc(100vh - 30px);overflow:auto}
nav b{display:block;margin:4px 0 8px}
nav a{display:block;color:#344054;text-decoration:none;padding:7px 8px;border-radius:8px;font-size:14px}
nav a:hover{background:#eff6ff;color:var(--primary)}
main{min-width:0}
section,.tip,.warning,.success{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:24px;margin-bottom:20px;box-shadow:0 3px 12px #10182808}
h2{font-size:27px;margin:0 0 12px;border-bottom:1px solid var(--border);padding-bottom:9px}
h3{margin-top:25px;font-size:20px}
h4{margin-bottom:7px}
p{margin:8px 0 13px}
code.inline{background:#eef2f7;padding:2px 6px;border-radius:5px;font-size:.92em}
pre{position:relative;background:var(--code);color:var(--codeText);padding:17px;border-radius:10px;overflow:auto;margin:10px 0 17px}
pre code{font-family:Consolas,"Cascadia Code",monospace;font-size:13px;white-space:pre}
.copy{position:absolute;right:9px;top:8px;border:0;background:#344054;color:#fff;border-radius:6px;padding:5px 9px;cursor:pointer;font-size:12px}
.copy:hover{background:#475467}
.tip{border-left:5px solid var(--primary)}
.warning{border-left:5px solid #f59e0b}
.success{border-left:5px solid #12b76a}
table{width:100%;border-collapse:collapse;margin:12px 0 18px;font-size:14px}
th,td{border:1px solid var(--border);padding:9px;text-align:left;vertical-align:top}
th{background:#f1f5f9}
.bad{color:var(--red);font-weight:700}.good{color:var(--green);font-weight:700}
.search{width:100%;padding:11px 13px;border:1px solid var(--border);border-radius:9px;margin-bottom:12px;font:inherit}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.card{border:1px solid var(--border);border-radius:10px;padding:14px}
.flow{font-weight:700;background:#eff6ff;border-radius:10px;padding:14px;overflow:auto}
kbd{background:#111827;color:#fff;border-radius:4px;padding:2px 6px;font-size:12px}
footer{max-width:1180px;margin:0 auto;padding:15px 20px 50px;color:var(--muted);text-align:center}
@media(max-width:850px){.layout{grid-template-columns:1fr}nav{position:relative;top:auto;max-height:none}.layout{padding-top:14px}}
@media print{nav,.copy,.search{display:none!important}header{background:#fff;color:#000;border-bottom:2px solid #000}.hero p,.badges span{color:#000}.layout{display:block}.section,.tip,.warning,.success{box-shadow:none}}
</style>
</head>
<body>
<header>
<div class="hero">
<h1>Git & GitHub PowerShell Cheat Sheet</h1>
<p>Windows PowerShell থেকে Git repository তৈরি, connect, commit, push, pull, branch, merge, conflict fix, undo, tag, stash এবং GitHub Pages deployment—এক জায়গায় A to Z। প্রতিটি command-এর পাশে সহজ বাংলা ব্যাখ্যা ও common problem-এর solution দেওয়া আছে।</p>
<div class="badges"><span>Windows PowerShell</span><span>Git</span><span>GitHub</span><span>React / Vite</span><span>Copy-friendly</span></div>
</div>
</header>

<div class="layout">
<nav>
<b>Quick Navigation</b>
<input class="search" id="search" placeholder="Search topic...">
<div id="navlinks">
<a href="#mental">0. Git বুঝে নাও</a>
<a href="#setup">1. Setup</a>
<a href="#newrepo">2. New Project → GitHub</a>
<a href="#existing">3. Existing GitHub Repo → PC</a>
<a href="#daily">4. Daily Workflow</a>
<a href="#remote">5. Remote</a>
<a href="#branch">6. Branch</a>
<a href="#merge">7. Merge</a>
<a href="#pull">8. Pull / Rebase</a>
<a href="#conflict">9. Conflict</a>
<a href="#undo">10. Undo / Recovery</a>
<a href="#stash">11. Stash</a>
<a href="#history">12. History / Diff</a>
<a href="#tag">13. Tag / Release</a>
<a href="#github">14. GitHub CLI basics</a>
<a href="#deploy">15. GitHub Pages Deploy</a>
<a href="#errors">16. Common Errors</a>
<a href="#commands">17. Command Table</a>
<a href="#rules">18. Golden Rules</a>
</div>
</nav>

<main>
<section id="mental">
<h2>0. আগে Git-এর পুরো flow বুঝে নাও</h2>
<div class="flow">Working Folder → git add → Staging Area → git commit → Local Repository → git push → GitHub<br>GitHub → git pull → Local Repository / Working Folder</div>
<p><b>Git</b> হলো version control system। <b>GitHub</b> হলো online hosting/collaboration platform।</p>
<table><tr><th>Command</th><th>কাজ</th></tr>
<tr><td><code class="inline">git add</code></td><td>পরিবর্তন staging-এ নেয়</td></tr>
<tr><td><code class="inline">git commit</code></td><td>local history-তে snapshot তৈরি করে</td></tr>
<tr><td><code class="inline">git push</code></td><td>local commit GitHub-এ পাঠায়</td></tr>
<tr><td><code class="inline">git pull</code></td><td>remote changes এনে integrate করে</td></tr>
<tr><td><code class="inline">git fetch</code></td><td>remote changes আনে, কিন্তু working branch-এ নিজে থেকে merge করে না</td></tr>
<tr><td><code class="inline">git merge</code></td><td>দুই branch-এর history একত্র করে</td></tr>
</table>
</section>

<section id="setup">
<h2>1. প্রথমবার Git setup</h2>
<h3>Git install আছে কি না</h3>
<pre><code>git --version</code></pre>
<h3>User name / email</h3>
<pre><code>git config --global user.name "Julkar Nain"
git config --global user.email "your-email@example.com"</code></pre>
<p>যা set হয়েছে:</p>
<pre><code>git config --global --list
git config user.name
git config user.email</code></pre>
<div class="tip"><b>Note:</b> Commit author হিসেবে কোন name/email ব্যবহার হবে সেটা এই configuration থেকে আসে।</div>
</section>

<section id="newrepo">
<h2>2. Local project → নতুন GitHub repository</h2>
<h3>Step 1: Project folder-এ যাও</h3>
<pre><code>cd "E:\programingHeroAI -14\fitlog"</code></pre>
<h3>Step 2: Git initialize</h3>
<pre><code>git init</code></pre>
<h3>Step 3: Files দেখো</h3>
<pre><code>git status</code></pre>
<h3>Step 4: .gitignore বানাও</h3>
<p>Node/React project হলে অন্তত:</p>
<pre><code>node_modules/
dist/
.env
.env.*
!.env.example</code></pre>
<h3>Step 5: Add → Commit</h3>
<pre><code>git add .
git commit -m "Initial commit"</code></pre>
<h3>Step 6: Main branch</h3>
<pre><code>git branch -M main</code></pre>
<h3>Step 7: GitHub remote connect</h3>
<pre><code>git remote add origin https://github.com/USERNAME/REPOSITORY.git
git remote -v</code></pre>
<h3>Step 8: Push</h3>
<pre><code>git push -u origin main</code></pre>
<div class="success"><b>পরেরবার:</b> <code>git push</code> দিলেই হবে, কারণ <code>-u</code> upstream সেট করে দেয়।</div>
</section>

<section id="existing">
<h2>3. GitHub repository → PC (clone)</h2>
<pre><code>cd "E:\programingHeroAI -14"
git clone https://github.com/USERNAME/REPOSITORY.git
cd REPOSITORY
git status</code></pre>
<p>Existing remote repository copy করার সবচেয়ে সহজ উপায় <code>git clone</code>।</p>
</section>

<section id="daily">
<h2>4. প্রতিদিনের কাজের standard workflow</h2>
<pre><code># 1. Remote changes আগে আনো
git pull --rebase origin main

# 2. নিজের code check
git status

# 3. Changes দেখো
git diff

# 4. Stage
git add .

# 5. Commit
git commit -m "Describe what changed"

# 6. Push
git push</code></pre>
<div class="tip"><b>Professional habit:</b> বড় কাজের আগে <code>git status</code>, commit-এর আগে <code>git diff</code>, push-এর আগে branch check করা ভালো।</div>
</section>

<section id="remote">
<h2>5. Remote repository manage</h2>
<pre><code>git remote -v
git remote get-url origin
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git
git remote remove origin
git remote add origin https://github.com/USERNAME/REPOSITORY.git</code></pre>
<p><b>তোমার আগের মতো:</b></p>
<pre><code>git remote -v</code></pre>
<p>এতে fetch এবং push URL দেখা যাবে।</p>
</section>

<section id="branch">
<h2>6. Branch</h2>
<pre><code># সব local branch
git branch

# remote সহ সব branch
git branch -a

# নতুন branch
git branch feature/login

# নতুন branch তৈরি + switch
git switch -c feature/login

# branch change
git switch main

# পুরোনো syntax
git checkout feature/login

# branch delete
git branch -d feature/login

# remote branch delete
git push origin --delete feature/login</code></pre>
<h3>Feature workflow</h3>
<pre><code>git switch main
git pull --rebase origin main
git switch -c feature/navbar

# কাজ...
git add .
git commit -m "Add responsive navbar"
git push -u origin feature/navbar</code></pre>
</section>

<section id="merge">
<h2>7. Merge</h2>
<p>Feature branch-এর কাজ <code>main</code>-এ আনার একটি উপায় হলো merge।</p>
<pre><code>git switch main
git pull origin main
git merge feature/navbar
git push origin main</code></pre>
<p>যদি fast-forward হয়, Git সরাসরি pointer এগিয়ে দিতে পারে। Conflict হলে conflict section দেখো।</p>
<h3>Merge cancel</h3>
<pre><code>git merge --abort</code></pre>
</section>

<section id="pull">
<h2>8. Pull, Fetch এবং Rebase</h2>
<h3>git pull</h3>
<pre><code>git pull origin main</code></pre>
<p>Remote changes এনে current branch-এর সাথে integrate করে।</p>
<h3>git fetch</h3>
<pre><code>git fetch origin
git status
git log --oneline --decorate --graph --all</code></pre>
<p>শুধু remote information update করতে চাইলে useful।</p>
<h3>Pull with rebase</h3>
<pre><code>git pull --rebase origin main</code></pre>
<p>Local unpushed commits থাকলে remote-এর নতুন commits-এর পরে তোমার commits replay করতে পারে। এতে অনেক ক্ষেত্রে linear history পাওয়া যায়।</p>
<div class="warning"><b>সতর্কতা:</b> Rebase করে already-shared/public commits rewrite করা উচিত নয় যদি team policy না থাকে।</div>
</section>

<section id="conflict">
<h2>9. Merge / Pull conflict হলে কী করবে</h2>
<p>ধরো Git বলল:</p>
<pre><code>CONFLICT (content): Merge conflict in src/App.tsx</code></pre>
<p>প্রথমে:</p>
<pre><code>git status</code></pre>
<p>File খুলে এই markers খুঁজে বের করো:</p>
<pre><code>&lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD
তোমার/current branch-এর code
=======
অন্য branch-এর code
&gt;&gt;&gt;&gt;&gt;&gt;&gt; feature/login</code></pre>
<p>যেটা দরকার রেখে markers মুছে save করো। তারপর:</p>
<pre><code>git add src/App.tsx
git commit -m "Resolve merge conflict"
git push</code></pre>
<h3>Conflict থেকে পুরো merge বাতিল</h3>
<pre><code>git merge --abort</code></pre>
<h3>Rebase conflict হলে</h3>
<pre><code># conflict resolve করে
git add .
git rebase --continue

# সব rebase বাতিল
git rebase --abort</code></pre>
</section>

<section id="undo">
<h2>10. Undo / ভুল ঠিক করা</h2>
<h3>Unstaged change বাতিল</h3>
<pre><code>git restore filename
git restore .</code></pre>
<p><span class="bad">সতর্ক:</span> এই changes হারিয়ে যেতে পারে।</p>

<h3>Staging থেকে file নামানো</h3>
<pre><code>git restore --staged filename
git restore --staged .</code></pre>

<h3>শেষ commit-এর message পরিবর্তন</h3>
<pre><code>git commit --amend -m "Correct commit message"</code></pre>

<h3>শেষ commit undo, changes রেখে</h3>
<pre><code>git reset --soft HEAD~1</code></pre>

<h3>শেষ commit undo, changes unstaged রেখে</h3>
<pre><code>git reset HEAD~1</code></pre>

<h3>শেষ commit + changes discard</h3>
<pre><code>git reset --hard HEAD~1</code></pre>

<div class="warning"><b>Danger:</b> <code>git reset --hard</code> uncommitted work মুছে দিতে পারে। Shared branch-এ reset/force push করার আগে নিশ্চিত হও।</div>
</section>

<section id="stash">
<h2>11. Stash — কাজ temporarily সরিয়ে রাখা</h2>
<pre><code># current changes stash
git stash

# message সহ
git stash push -m "WIP navbar"

# stash list
git stash list

# latest stash apply, stash রেখে দেয়
git stash apply

# latest stash apply + remove
git stash pop

# stash delete
git stash drop

# সব stash delete
git stash clear</code></pre>
<p>Example: feature কাজ অসম্পূর্ণ, কিন্তু জরুরি কারণে <code>main</code>-এ যেতে হবে → stash → switch main → কাজ → আবার feature-এ গিয়ে stash pop।</p>
</section>

<section id="history">
<h2>12. History, Diff, Log</h2>
<pre><code>git status
git diff
git diff --staged
git log
git log --oneline
git log --oneline --graph --decorate --all
git show HEAD
git show COMMIT_ID</code></pre>
<p>কোন commit কী পরিবর্তন করেছে দেখতে <code>git show</code> useful।</p>
</section>

<section id="tag">
<h2>13. Tag / Release</h2>
<pre><code># lightweight tag
git tag v1.0.0

# annotated tag
git tag -a v1.0.0 -m "First stable release"

# tags
git tag

# push one tag
git push origin v1.0.0

# all tags
git push origin --tags

# tag delete local
git tag -d v1.0.0

# tag delete remote
git push origin --delete v1.0.0</code></pre>
</section>

<section id="github">
<h2>14. GitHub authentication / CLI basics</h2>
<p>GitHub password দিয়ে HTTPS Git authentication সাধারণত করা হয় না; credential manager, token বা SSH-এর মতো supported authentication ব্যবহার করা যায়।</p>
<h3>SSH check</h3>
<pre><code>ssh -T git@github.com</code></pre>
<h3>Remote-কে SSH URL করা</h3>
<pre><code>git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
git remote -v</code></pre>
<p>যদি GitHub CLI (<code>gh</code>) install করা থাকে:</p>
<pre><code>gh auth login
gh repo view
gh repo clone USERNAME/REPOSITORY</code></pre>
</section>

<section id="deploy">
<h2>15. GitHub Pages Deploy — React + Vite</h2>
<p>তোমার <b>React + Vite + TypeScript</b> project-এর জন্য একটি common GitHub Pages approach হলো <code>gh-pages</code> package ব্যবহার করা।</p>
<h3>1. Install</h3>
<pre><code>npm install --save-dev gh-pages</code></pre>
<h3>2. package.json</h3>
<pre><code>"scripts": {
  "dev": "vite",
  "build": "tsc -b &amp;&amp; vite build",
  "lint": "eslint .",
  "preview": "vite preview",
  "predeploy": "npm run build",
  "deploy": "gh-pages -d dist"
}</code></pre>
<h3>3. vite.config.ts</h3>
<p>Repository যদি <code>assignment_5</code> হয়:</p>
<pre><code>import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  base: '/assignment_5/',
})</code></pre>
<h3>4. Build test</h3>
<pre><code>npm run build</code></pre>
<h3>5. Deploy</h3>
<pre><code>npm run deploy</code></pre>
<h3>6. GitHub Pages</h3>
<p>Repository → <b>Settings → Pages → Deploy from a branch → gh-pages → / (root)</b> নির্বাচন করো।</p>
<p>Project URL সাধারণত হবে:</p>
<pre><code>https://USERNAME.github.io/REPOSITORY/</code></pre>
<h3>Public assets / logo</h3>
<p>যদি <code>public/logo.png</code> থাকে এবং Vite base path ব্যবহার করো, React code-এ:</p>
<pre><code>&lt;img src={`${import.meta.env.BASE_URL}logo.png`} alt="Logo" /&gt;</code></pre>
<div class="tip"><b>Common reason logo missing:</b> GitHub Pages project URL-এর জন্য root-relative <code>/logo.png</code> path অনেক সময় ভুল location-এ point করে। <code>import.meta.env.BASE_URL</code> ব্যবহার করলে base path অনুযায়ী URL তৈরি করা যায়।</div>
</section>

<section id="errors">
<h2>16. Common Git Errors → Problem → Solution</h2>

<h3>❌ rejected — fetch first</h3>
<pre><code>! [rejected] main -&gt; main (fetch first)
error: failed to push some refs</code></pre>
<p><b>কারণ:</b> Remote <code>main</code>-এ local-এর চেয়ে নতুন commit আছে।</p>
<pre><code>git pull --rebase origin main
git push origin main</code></pre>
<p>Conflict হলে conflict section follow করো।</p>

<h3>❌ no tracking information</h3>
<pre><code>There is no tracking information for the current branch.</code></pre>
<pre><code>git push -u origin main</code></pre>
<p>তারপর ভবিষ্যতে শুধু <code>git push</code>।</p>

<h3>❌ remote origin already exists</h3>
<pre><code>error: remote origin already exists.</code></pre>
<pre><code>git remote -v
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git</code></pre>

<h3>❌ not a git repository</h3>
<pre><code>fatal: not a git repository</code></pre>
<p>ভুল folder-এ আছো।</p>
<pre><code>pwd
cd "YOUR_PROJECT_FOLDER"
git status</code></pre>

<h3>❌ Nothing to commit</h3>
<pre><code>nothing to commit, working tree clean</code></pre>
<p>এটা error নয়। Local working tree-তে নতুন uncommitted change নেই।</p>

<h3>❌ src refspec main does not match</h3>
<p>সাধারণত local <code>main</code> branch/commit নেই।</p>
<pre><code>git branch
git status
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main</code></pre>

<h3>❌ LF will be replaced by CRLF</h3>
<p>Windows line-ending warning। সাধারণত fatal error নয়। Team project হলে consistent line-ending policy রাখা ভালো।</p>
<pre><code>git config --global core.autocrlf true</code></pre>

<h3>❌ non-fast-forward</h3>
<pre><code>git pull --rebase origin main
git push origin main</code></pre>
<p>যদি remote history overwrite করাই উদ্দেশ্য হয়, force push-এর আগে নিশ্চিত হও।</p>

<h3>❌ accidentally committed .env</h3>
<p>Secret/API key কখনো GitHub-এ publish করা উচিত নয়। Secret rotate/revoke করে repository history থেকে removal-এর জন্য appropriate history-rewrite procedure ব্যবহার করতে হবে। শুধু file delete করে commit করলেই পুরোনো history থেকে secret মুছে যায় না।</p>
</section>

<section id="commands">
<h2>17. Most-used command table</h2>
<table>
<tr><th>কাজ</th><th>Command</th></tr>
<tr><td>Status</td><td><code>git status</code></td></tr>
<tr><td>All changes stage</td><td><code>git add .</code></td></tr>
<tr><td>Commit</td><td><code>git commit -m "message"</code></td></tr>
<tr><td>Push</td><td><code>git push</code></td></tr>
<tr><td>First push</td><td><code>git push -u origin main</code></td></tr>
<tr><td>Pull</td><td><code>git pull origin main</code></td></tr>
<tr><td>Pull + rebase</td><td><code>git pull --rebase origin main</code></td></tr>
<tr><td>Fetch</td><td><code>git fetch origin</code></td></tr>
<tr><td>Branches</td><td><code>git branch -a</code></td></tr>
<tr><td>New branch</td><td><code>git switch -c feature/name</code></td></tr>
<tr><td>Switch</td><td><code>git switch main</code></td></tr>
<tr><td>Merge</td><td><code>git merge branch-name</code></td></tr>
<tr><td>Abort merge</td><td><code>git merge --abort</code></td></tr>
<tr><td>Stash</td><td><code>git stash</code></td></tr>
<tr><td>Stash back</td><td><code>git stash pop</code></td></tr>
<tr><td>History</td><td><code>git log --oneline --graph --all</code></td></tr>
<tr><td>Diff</td><td><code>git diff</code></td></tr>
<tr><td>Remote</td><td><code>git remote -v</code></td></tr>
<tr><td>Undo staged</td><td><code>git restore --staged .</code></td></tr>
<tr><td>Discard working changes</td><td><code>git restore .</code></td></tr>
</table>
</section>

<section id="rules">
<h2>18. Golden Rules — এগুলো মনে রাখো</h2>
<div class="grid">
<div class="card"><b>1. Push-এর আগে</b><p><code>git status</code> + <code>git branch</code></p></div>
<div class="card"><b>2. Team project</b><p>আগে <code>git pull --rebase</code>, তারপর কাজ/push—team policy অনুযায়ী।</p></div>
<div class="card"><b>3. Commit ছোট রাখো</b><p>এক commit-এ logically related change রাখো।</p></div>
<div class="card"><b>4. Meaningful message</b><p><code>Add login validation</code> > <code>update</code></p></div>
<div class="card"><b>5. Force push সাবধানে</b><p><code>--force</code> shared history overwrite করতে পারে।</p></div>
<div class="card"><b>6. Secrets নয়</b><p><code>.env</code>, password, API secret commit করো না।</p></div>
</div>

<h3>⭐ তোমার daily copy-paste flow</h3>
<pre><code>cd "YOUR_PROJECT_FOLDER"

git status
git pull --rebase origin main

git status
git add .
git commit -m "Describe your changes"
git push</code></pre>

<h3>⭐ নতুন project-এর complete flow</h3>
<pre><code>cd "YOUR_PROJECT_FOLDER"

git init
git add .
git commit -m "Initial commit"
git branch -M main

git remote add origin https://github.com/USERNAME/REPOSITORY.git
git remote -v

git push -u origin main</code></pre>

<h3>⭐ Push rejected হলে</h3>
<pre><code>git status
git pull --rebase origin main
# conflict হলে resolve → git add . → git rebase --continue
git push</code></pre>
</section>

<div class="tip">
<b>Quick decision:</b><br>
Local → GitHub = <code>add → commit → push</code><br>
GitHub → Local = <code>pull</code><br>
দুই branch এক করা = <code>merge</code><br>
Remote history আগে দেখে নেওয়া = <code>fetch</code><br>
Unfinished work temporarily সরানো = <code>stash</code><br>
React/Vite GitHub Pages = <code>build → gh-pages deploy → Pages enable</code>
</div>
</main>
</div>
<footer>Git & GitHub PowerShell Cheat Sheet • Personal learning reference • Update commands according to your team/repository policy.</footer>

<script>
document.querySelectorAll("pre").forEach(pre=>{
  const btn=document.createElement("button");
  btn.className="copy"; btn.textContent="Copy";
  btn.onclick=async()=>{
    const code=pre.querySelector("code").innerText;
    try{
      await navigator.clipboard.writeText(code);
      btn.textContent="Copied!";
      setTimeout(()=>btn.textContent="Copy",1200);
    }catch(e){
      btn.textContent="Select & copy";
      setTimeout(()=>btn.textContent="Copy",1200);
    }
  };
  pre.appendChild(btn);
});
const search=document.getElementById("search");
const links=[...document.querySelectorAll("#navlinks a")];
search.addEventListener("input",()=>{
  const q=search.value.toLowerCase().trim();
  links.forEach(a=>a.style.display=a.textContent.toLowerCase().includes(q)?"block":"none");
});
</script>
</body>
</html>
'''

path = Path("/mnt/data/git-github-powershell-cheat-sheet.html")
path.write_text(html, encoding="utf-8")
print(f"Created: {path}")
