## Assignment 1 – Practice `git restore` and `git restore --staged`

**Goal:** Understand how staging and unstaging works with `git restore`.

1. Create a new file named `profile.txt` and write 3–4 lines about your favorite programming topic.
2. Run `git status` and note that the file is **untracked**.
3. Try the command:
```bash
git restore profile.txt
```
Observe that it does **not** work (because the file is untracked).
4. Stage the file:
```bash
git add profile.txt
```
5. Unstage it using:
```bash
git restore --staged profile.txt
```
6. Run `git status` again and confirm the file is back to untracked / unstaged.
7. Now stage and commit the file properly:
```bash
git add profile.txt
git commit -m "Add profile.txt"
```
**Submit:**

---
---

**Answers**

---
---

**Screenshot of `git status` when the file was untracked**

<img width="1250" height="245" alt="Screenshot 2026-09-08 111817" src="https://github.com/user-attachments/assets/66ffff7d-2bd4-4169-b703-e6ea6419e28b" />

---

**Screenshot after using `git restore --staged`**

<img width="1498" height="917" alt="Screenshot 2026-09-08 111932" src="https://github.com/user-attachments/assets/94102248-51ae-409b-95b8-8373a408c598" />

---

**Repository link** --> https://github.com/Ashish07-dev-UI/git-restore-git-restore---staged-rm-vs-git-rm-.gitignore


