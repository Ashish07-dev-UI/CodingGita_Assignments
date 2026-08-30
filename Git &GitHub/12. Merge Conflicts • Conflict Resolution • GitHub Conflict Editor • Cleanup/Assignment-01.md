### Assignment 1 – Create and Resolve a Merge Conflict on GitHub (Mandatory)

**Goal:** Create a real conflict with two feature branches and resolve it using the GitHub browser editor.

1. Create/clone a repository and on `main` create `tasks.txt`:

```text
My Tasks
1. Study Git
2. Complete assignment
3. Review notes
```

2. Commit and push to `main`.
3. Create branch `feature/tasks-A` → change line 3 to `Practice merge conflicts` → commit → push → open PR (do **not** merge yet).
4. Switch back to `main`, create branch `feature/tasks-B` → change line 3 to `Watch Git tutorial` → commit → push → open second PR.
5. Merge the first PR successfully.
6. Merge the second PR → conflict appears.
7. Resolve the conflict on GitHub:
   - Understand Current vs Incoming
   - Decide final text (keep one, both, or write your own)
   - Remove all conflict markers
   - Mark as resolved → Commit merge → Merge the PR
8. Delete both remote feature branches.
9. Update local main and delete local branches:
   ```bash
   git checkout main
   git pull origin main
   git branch -D feature/tasks-A
   git branch -D feature/tasks-B
   ```

**Submit:**
- Repository link
- Screenshot of the conflict editor (showing markers)
- Screenshot of the successfully merged second PR
- Screenshot of `git log --oneline` after pull

---

**Answers**

---

<img width="1840" height="946" alt="Screenshot 2026-08-27 093251" src="https://github.com/user-attachments/assets/e59ddd32-efc2-4540-bf8a-ac57f8b23008" />

---

<img width="1837" height="937" alt="Screenshot 2026-08-27 094149" src="https://github.com/user-attachments/assets/c2a05ca5-d79c-4d91-86ad-79800e3806f0" />

---


<img width="1255" height="393" alt="Screenshot 2026-08-27 094640" src="https://github.com/user-attachments/assets/9326d02d-90f5-4343-8d86-177203a1763a" />
