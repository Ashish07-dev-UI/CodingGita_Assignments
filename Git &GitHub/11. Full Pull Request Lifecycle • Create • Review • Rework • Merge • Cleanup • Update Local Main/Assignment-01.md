### Assignment 1 – Complete PR Lifecycle with `feature/contact-form` (Mandatory)

**Goal:** Practice the full cycle: branch → file → commit → push → PR → merge → cleanup.

1. Update main:  
   `git checkout main && git pull origin main`
2. Create branch:  
   `git checkout -b feature/contact-form`
3. Create file `contact.html` with a simple heading and a short paragraph about a contact form.
4. Stage, commit and push:  
   ```bash
   git add contact.html
   git commit -m "Add contact form page"
   git push -u origin feature/contact-form
   ```
5. On GitHub: Open a Pull Request (base = `main`, compare = `feature/contact-form`). Write a clear title and description.
6. Merge the Pull Request using **“Create a merge commit”**.
7. Delete the remote branch (GitHub “Delete branch” button or `git push origin --delete feature/contact-form`).
8. Update local main using the two-command method:  
   ```bash
   git checkout main
   git fetch origin main
   git merge origin/main
   ```
9. Delete local branch:  
   `git branch -d feature/contact-form`
10. Take screenshots of:  
    (a) the merged PR  
    (b) terminal after fetch + merge  
    (c) `git branch` showing the branch is gone

**Submit:** Merged PR link + the 3 screenshots listed above.

---

**Answers**

---

<img width="1840" height="946" alt="Screenshot 2026-08-27 093251" src="https://github.com/user-attachments/assets/35e65316-fa00-42a8-bbff-e00d18a6606e" />

---

<img width="1837" height="937" alt="Screenshot 2026-08-27 094149" src="https://github.com/user-attachments/assets/f06ffd7e-1408-49af-b8f1-87b024efff7e" />

---

<img width="1255" height="393" alt="Screenshot 2026-08-27 094640" src="https://github.com/user-attachments/assets/ef3e2c78-7c67-463a-a8c3-f7369c1f5371" />
