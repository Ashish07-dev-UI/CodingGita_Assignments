## Assignment 3 – `.gitignore` + `git rm --cached`

**Goal:** Properly ignore sensitive files and practice stopping Git from tracking a file using `git rm --cached`.

1. Create a file named `config.env` with sample secret data:
```env
DB_PASSWORD=SuperSecretPass999
API_KEY=sk-test-abc123xyz789
```

2. **Intentionally** add and commit it (to practice the fix):
```bash
git add config.env
git commit -m "Accidentally commit config.env"
```

3. Create a folder named `vendor` and put any dummy file inside it.

4. Create a `.gitignore` file and add:
```gitignore
vendor/
config.env
```

5. Stop tracking `config.env` but **keep the file on your computer**:
```bash
git rm --cached config.env
```

6. Run `git status` and observe that `config.env` is staged for removal from Git (but the file still exists locally).

7. Commit the fix:
```bash
git add .gitignore
git commit -m "Stop tracking config.env and add .gitignore"
git push origin main
```

8. Confirm on GitHub that `config.env` is **no longer visible** in the repository, while the file still exists on your local machine.

9. Create a file named `why-gitignore.txt` and answer:
- Why should we ignore folders like `vendor` or `node_modules`?
- Why should we ignore files like `config.env` or `.env`?
- What does `git rm --cached` do?
- Why should we **not** add `.gitignore` inside `.gitignore`?

---
---

**Answers:**

---
---

**Screenshot of `git status` after using `git rm --cached`**

<img width="1017" height="261" alt="Screenshot 2026-09-08 122721" src="https://github.com/user-attachments/assets/a86cad50-1149-4bc5-8135-969d4f64b446" />

---

**Screenshot showing that `config.env` is ignored / removed from GitHub**

<img width="1920" height="1080" alt="Screenshot 2026-09-08 123412" src="https://github.com/user-attachments/assets/cf8076bb-d995-4699-93fb-a86691020356" />

---

**Content of `why-gitignore.txt`**

<img width="1860" height="439" alt="Screenshot 2026-09-08 123653" src="https://github.com/user-attachments/assets/6157c6b2-8703-42a8-bc98-7518f6c7440d" />

---

**Repository link** --> https://github.com/Ashish07-dev-UI/Git-restore-rm-gitignore-practice-3

---
