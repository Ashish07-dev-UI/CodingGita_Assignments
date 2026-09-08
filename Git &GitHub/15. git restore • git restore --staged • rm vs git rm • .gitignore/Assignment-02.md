## Assignment 2 – `rm` vs `git rm`

**Goal:** Understand the difference between normal delete and Git delete.

1. Make sure `profile.txt` is committed on `main`.
2. Delete the file using normal system command:
```bash
rm profile.txt
```
3. Run `git status` and observe the output.
4. Recover the file using:
```bash
git restore profile.txt
```
5. Now delete it properly with Git:
```bash
git rm profile.txt
```
6. Run `git status` again and observe the difference.
7. Commit the deletion:
```bash
git commit -m "Remove profile.txt using git rm"
```
8. Create a short file named `delete-difference.txt` and write in your own words:
- What is the difference between `rm` and `git rm`?
- When should you use `git rm`?

---
---

**Answers:**

---
---

**Screenshots of `git status` after `rm` and after `git rm`**

---

<img width="1028" height="277" alt="Screenshot 2026-09-08 114313" src="https://github.com/user-attachments/assets/1518c20f-1931-4f97-8c17-9240b52cb43b" />

---

<img width="1022" height="222" alt="Screenshot 2026-09-08 114430" src="https://github.com/user-attachments/assets/356d2386-07a8-4182-8bdf-134497f2e1ce" />

---

**Content of `delete-difference.txt`**

---

<img width="1806" height="912" alt="Screenshot 2026-09-08 115545" src="https://github.com/user-attachments/assets/709085da-55a8-4d70-b239-efb696f6a0cf" />

---

**Repository link** --> https://github.com/Ashish07-dev-UI/Git-restore-rm-gitignore-practice--2

---
