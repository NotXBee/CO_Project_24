```markdown
# CO_Project_24 – Python-Based CPU Assembler & Simulator

A course-project for Introduction to Computer Organization & Architecture (Batch ’27), CO_Project_24 is a fully-featured, Python-implemented assembler and cycle-accurate CPU simulator. It lets you write simple assembly programs, translate them into machine code, and step through instruction execution—complete with pipeline stages, hazard detection, register/memory tracing, and automated test harnesses.

---

## 🔍 Project Overview

- **Assembler (`SimpleAssembler/`)**  
  - Parses a custom, RISC-style assembly language  
  - Encodes instructions into 16-bit machine-code words  
  - Supports labels, directives (e.g. `.data`, `.text`), pseudo-instructions, and immediate/addressing modes  
- **Simulator (`SimpleSimulator/`)**  
  - Models a 5-stage pipeline (Fetch, Decode, Execute, Memory, Write-back)  
  - Implements control- and data-hazard detection & stalling  
  - Maintains register file, data memory, and program counter state  
  - Provides single-step & full-run modes, with detailed cycle logs  
- **Automated Testing (`automatedTesting/`)**  
  - Suite of Python scripts that assemble, simulate, and verify dozens of small programs  
  - Compares simulated register/memory snapshots against golden-reference outputs  
  - Reports pass/fail with line-by-line diffs  

---

## ⚙️ Key Features

- **Modular, Readable Python Code**  
  Clear separation of parsing, encoding, pipeline stages, and logging—easy to extend with new instructions or pipeline optimizations.  
- **Cycle-Accurate Pipeline Simulation**  
  Models real-world pipeline behavior: hazards, forwarding, stalls, and branch penalties.  
- **Comprehensive Documentation & Manual**  
  - `CO_Project_2024_v8.pdf`: detailed design rationale, ISA spec, pipeline diagrams  
  - `Project_Manual.txt`: quick-start guide for assembling, simulating, and testing  
- **Extensible Test Harness**  
  Add your own `.asm` testcases; harness will automatically assemble, simulate, and compare results.  

---

## 🛠 Tech Stack & Dependencies

- **Language:** Python 3.8+  
- **Libraries:** only Python’s standard library (no external dependencies)  
- **Tools:**  
  - Git & GitHub for version control  
  - Any terminal or IDE for running `.py` scripts  

---

## 📂 Repository Structure

```

CO\_Project\_24/
├── SimpleAssembler/       # source & tests for the assembler
├── SimpleSimulator/       # pipeline simulator implementation
├── automatedTesting/      # end-to-end assemble+simulate+verify scripts
├── CO\_Project\_2024\_v8.pdf # design spec & pipeline diagrams
├── Project\_Manual.txt     # user guide & quick commands
├── IMPORTANT.txt          # project setup & naming conventions
└── members.txt            # team roster & GitHub handles

````

---

## 🚀 Getting Started

1. **Clone & Navigate**  
   ```bash
   git clone https://github.com/NotXBee/CO_Project_24.git
   cd CO_Project_24
````

2. **Assemble an Example**

   ```bash
   python3 SimpleAssembler/assemble.py examples/hello_world.asm
   ```
3. **Simulate Your Binary**

   ```bash
   python3 SimpleSimulator/simulate.py --binary hello_world.bin --step
   ```
4. **Run the Test Suite**

   ```bash
   python3 automatedTesting/run_all_tests.py
   ```

---

## 👥 Team Members

* **Aditya Nuli** (2023360)
* **Piyush Keshan** (2023376)
* **Sanskar Garg** (2023485)
* **Shivam Kumar Jha** (2023506)

---

## 📄 License & Attribution

This project was developed for educational purposes in a Computer Organization & Architecture course. Feel free to fork and adapt—please give credit to the original authors.
