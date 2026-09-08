## Assignment 1 – Understanding HEAD and Basic Reset (Easy)

**Goal:** Practice viewing history and using a simple mixed reset. 

1. Create or open your practice repository.
2. Make three simple commits (you can create/edit a file called `notes.txt`):
   - Commit 1: Add some text → commit message `"First note"`
   - Commit 2: Add more text → commit message `"Second note"`
   - Commit 3: Add more text → commit message `"Third note"`
3. Run:
   ```bash
   git log --oneline
   ```
4. Reset to the previous commit using:
   ```bash
   git reset HEAD~1
   ```
5. Run `git log --oneline` and `git status` again.
6. Observe what happened to the latest commit and the file changes.
---
---

**Answers:**

---
---

**Screenshot of `git log --oneline` "before" reset**

<img width="936" height="143" alt="Screenshot 2026-09-08 130000" src="https://github.com/user-attachments/assets/79c5ebdd-2963-47e7-a263-9d24b8b1b771" />

---

**Screenshot of `git log --oneline` and `git status` "after" reset**

<img width="946" height="421" alt="Screenshot 2026-09-08 130106" src="https://github.com/user-attachments/assets/859d4282-bb0c-400b-b522-dccde0e8073b" />

---

**Repository link** --> https://github.com/Ashish07-dev-UI/Git-reset-revert-commands-1

---
