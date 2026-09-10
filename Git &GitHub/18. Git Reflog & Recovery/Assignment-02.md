## 📋 Part 2: Reworking Old Commit (5 Points)

### Task
1. Create a new repository called `reflog-practice-part2`
2. Create 3 commits:
   - **C0:** `README.md` with just title
   - **C1:** `app.js` with basic function
   - **C2:** `utils.js` with helper functions
3. Realize you need to add description to README (C0) without losing C1 and C2
4. Create a branch at C0: `git switch -c rework/readme-update <C0-hash>`
5. Update README.md with description, commit
6. Merge the branch back to main
7. Verify C0, C1, and C2 are all preserved
---

**Answers:**

---

**Screenshot of: git log --oneline BEFORE creating branch**

<img width="900" height="165" alt="Screenshot 2026-09-10 110833" src="https://github.com/user-attachments/assets/15fe6f2e-776d-4776-a9c9-c44b19290adb" />

---

**Screenshot of: git branch output (showing both branches)**

<img width="947" height="143" alt="Screenshot 2026-09-10 111000" src="https://github.com/user-attachments/assets/81d553b1-36dd-403b-9c2d-d781c778dd83" />

---

**Screenshot of: git log --oneline --graph (showing merge)**

<img width="902" height="242" alt="Screenshot 2026-09-10 111956" src="https://github.com/user-attachments/assets/dc0ba730-927e-4320-a8ae-c8a4bea87e94" />

---

**Screenshot of: Final README.md content**

<img width="1176" height="918" alt="Screenshot 2026-09-10 112040" src="https://github.com/user-attachments/assets/2237c24b-f66b-4c04-877e-4cafbc01f0d7" />
