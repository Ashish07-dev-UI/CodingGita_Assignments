## Assignment 2 – Modify/Delete Conflict during Revert

**Goal:** Face and resolve a Modify/Delete conflict while reverting.

1. Create a commit that **adds a new file**.
2. Make one more commit after that.
3. Try to revert the commit that added the file.
4. A Modify/Delete conflict should appear.
5. Resolve it (either delete the file or keep it with required content).
6. Use:
   ```bash
   git add .
   git revert --continue
   ```
---
---

**Answers:**

---
---

**Screenshot of the conflict (VS Code or terminal)**

<img width="1377" height="280" alt="Screenshot 2026-09-09 191302" src="https://github.com/user-attachments/assets/a596802f-19df-45e4-89e5-a62063a5ec7b" />

---

**Screenshot after successful `git revert --continue`**

<img width="1033" height="151" alt="image" src="https://github.com/user-attachments/assets/1c4230d5-c723-41f8-8869-de5dd580bc3f" />

---

**Repository link** --> https://github.com/Ashish07-dev-UI/Git-reset-revert-restore-2

---
