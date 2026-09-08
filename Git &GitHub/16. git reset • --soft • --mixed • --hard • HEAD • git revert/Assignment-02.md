## Assignment 2 – Difference between --soft, --mixed and --hard (Medium)

**Goal:** Clearly see how the three reset modes behave differently.

1. Create a new file `demo.txt` and make **two commits** on it.
2. Perform the following one by one (create fresh commits each time if needed):

   **A. Soft Reset**
   ```bash
   git reset --soft HEAD~1
   git status
   ```

   **B. Mixed Reset**
   ```bash
   git reset --mixed HEAD~1
   git status
   ```

   **C. Hard Reset**
   ```bash
   git reset --hard HEAD~1
   git status
   ```

3. write the short answers in your own words in your notebook:
   - What is the difference between `--soft`, `--mixed`, and `--hard`?
   - Which one keeps changes staged?
   - Which one discards the changes completely?
   - When should you avoid `--hard`?
---
---

**Answers:**

---
---

**Screenshots of `git status` after each type of reset (`--soft`, `--mixed`, `--hard`)**

<img width="936" height="233" alt="Screenshot 2026-09-08 185258" src="https://github.com/user-attachments/assets/57042810-1b51-448b-9c5a-73abc900a634" />

---

<img width="968" height="277" alt="Screenshot 2026-09-08 190000" src="https://github.com/user-attachments/assets/0bcd1327-d43e-4ada-b067-72f920a8ad8f" />

---

<img width="949" height="177" alt="Screenshot 2026-09-08 190232" src="https://github.com/user-attachments/assets/81c26abc-c49c-4961-9f14-def8a6af33b1" />

---

**Photos of written answers.**

<img width="1600" height="1200" alt="WhatsApp Image 2026-09-08 at 7 07 08 PM" src="https://github.com/user-attachments/assets/c4d765c7-ad39-4a78-8b8e-00bf9aa9e165" />

---

**Repository link** --> https://github.com/Ashish07-dev-UI/Git-reset-revert-commands-2

---
