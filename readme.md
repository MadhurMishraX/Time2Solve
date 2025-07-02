# ⏳ Time2Solve

A smart, terminal-based **weekly study planner** that helps you allocate your time efficiently across **Physics, Chemistry, and Math**, based on:

- 🧠 Number of questions  
- ⚖️ Subject difficulty  
- ⏰ Actual time available per day

Ideal for JEE aspirants, Olympiad learners, or anyone looking to beat procrastination with a precision-engineered plan.

---

## ✨ Features

✅ Smart time-weighted workload distribution  
✅ Handles uneven daily schedules  
✅ Outputs total subject-wise time (in hours & minutes)  
✅ Shows time per question (in mm:ss format)

⚠️ **Coming Soon**:
- 📅 Daily question distribution (per subject per day)

---

## 🛠️ How It Works

You input:
1. Number of questions in each subject  
2. Relative difficulty (e.g., 1.0 = normal, 1.5 = tough)  
3. Study hours available for each day of the week

The script calculates:
- Total time each subject deserves based on difficulty × quantity  
- Average time allowed per question  
- Clean breakdowns in human-friendly formats

---

## ▶️ Sample Run

### **Input**:
```text
Enter the number of questions in each subject separated by spaces: 140 105 175
Enter the difficulty of each subject separated by spaces: 1.2 1.0 1.5
Enter the total study time in hours you have for each day separated by spaces: 3 3 4 3 5 2 3
```
### 📤 Output:
```text
============== 📊 Weekly Study Plan Breakdown ==============
📘 Physics   : 6 hr 25 min
🧪 Chemistry : 4 hr 46 min
📐 Math      : 8 hr 48 min

----- ⏱ Average Time Per Question -----
Physics   : 2 min 12 sec
Chemistry : 2 min 43 sec
Math      : 1 min 30 sec
=============================================================
