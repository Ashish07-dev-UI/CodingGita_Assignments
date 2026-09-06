### Assignment 1  
**Conflict during `git pull`**

**Goal:** Face and resolve a conflict that appears when you run `git pull origin main`.

1. On GitHub (remote `main`), create a file `welcome.txt` with the content:  
   `Welcome to Git class`
2. Commit it directly on GitHub.
3. On your **local main**, create the same file `welcome.txt` with different content:  
   `Welcome to Day 13`
4. Run:
   ```bash
   git add welcome.txt
   git commit -m "Add welcome.txt locally"
   git pull origin main
   ```
5. A conflict will appear. Resolve it by keeping **both** lines (or any final version you prefer).
6. Remove all conflict markers, then:
   ```bash
   git add welcome.txt
   git commit -m "Resolve pull conflict in welcome.txt"
   git push origin main
   ```

**Submit:**
- Screenshot of the conflict markers
- Screenshot of the final resolved file on GitHub
- Repository link

---

**Answers**

---

<img width="1267" height="1009" alt="Screenshot 2026-09-06 163635" src="https://github.com/user-attachments/assets/d22ddf7a-cd7e-44e4-b0c3-024a1676504b" />


---

<img width="1843" height="949" alt="Screenshot 2026-09-06 165226" src="https://github.com/user-attachments/assets/2ee5107d-979f-4a30-abdd-ad58f314be0c" />


---

https://github.com/Ashish07-dev-UI/Modify-Delete-Conflict-Practice-1/tree/main
