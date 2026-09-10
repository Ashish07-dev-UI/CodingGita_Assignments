## 📋 Part 1: Recovery After `git reset --hard` (5 Points)

### Task
1. Create a new repository called `reflog-practice-part1`
2. Create 3 commits:
   - **C0:** `README.md` with project title
   - **C1:** `index.html` with `<h1>Welcome</h1>`
   - **C2:** `style.css` with basic styling
3. Accidentally delete C1 and C2 using `git reset --hard <C0-commit-hash>`
4. Use `git reflog` to find the lost C2 commit
5. Recover C2 (and C1) using detached HEAD + branch + merge
6. Verify all commits are restored
---

**Answers**

---

**Screenshot of: git log --oneline BEFORE reset**

<img width="911" height="136" alt="Screenshot 2026-09-10 095643" src="https://github.com/user-attachments/assets/c5d9fe9c-fc06-440f-a304-c7510fec07f4" />

---

**Screenshot of: git log --oneline AFTER reset (showing lost commits)**

<img width="881" height="92" alt="Screenshot 2026-09-10 100014" src="https://github.com/user-attachments/assets/96f805b4-089b-4a5e-aa9b-cb10cf52923d" />

---

**Screenshot of: git reflog output (highlighting the commit you recovered)**

<img width="1096" height="238" alt="Screenshot 2026-09-10 100353" src="https://github.com/user-attachments/assets/b2b5d8eb-b219-4f56-b14a-75fa4ce14485" />

---

**Screenshot of: git log --oneline AFTER recovery (showing all commits restored)**

<img width="882" height="141" alt="Screenshot 2026-09-10 102746" src="https://github.com/user-attachments/assets/30d4455a-2155-4a47-a7c8-f9890377c7b7" />
