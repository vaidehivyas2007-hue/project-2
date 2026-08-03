<div align="center">

# -- ! NumPy Analyzer ! --
### *Interactive Console-Based Array Creation & Statistical Analysis Tool*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Array%20Operations-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Console](https://img.shields.io/badge/Console-Interactive%20CLI-4CAF50?style=for-the-badge&logo=windowsterminal&logoColor=white)](https://www.python.org/)
[![OOP](https://img.shields.io/badge/OOP-Class%20Based%20Design-9C27B0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br/>

> *"An array is just numbers — until NumPy turns it into insight."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧩 Class Design — `DataAnalytics`](#-class-design--dataanalytics)
- [🔢 Part A — Array Creation & Access](#-part-a--array-creation--access)
- [➗ Part B — Mathematical Operations](#-part-b--mathematical-operations)
- [🔀 Part C — Combine, Split, Search, Sort & Filter](#-part-c--combine-split-search-sort--filter)
- [📊 Part D — Statistical Analysis](#-part-d--statistical-analysis)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **NumPy Analyzer** is an interactive, menu-driven Python console application built around a single object-oriented class, `DataAnalytics`. It demonstrates core NumPy concepts — array creation, indexing, slicing, arithmetic, matrix operations, searching, sorting, filtering, and statistical analysis — all wrapped inside a clean OOP structure using **getters, setters, class methods, static methods, and private methods**.

This project is designed to:
- Strengthen understanding of NumPy array manipulation
- Practice object-oriented programming concepts in Python (encapsulation, class/static/private methods)
- Apply mathematical and statistical logic on real array data
- Build a persistent, menu-driven CLI application

---

## 🎯 Problem Statement

> **Objective:** Build a console-based interactive tool to create, manipulate, and statistically analyze NumPy arrays.

You are building a utility tool for students and developers learning NumPy. The program must accept user choices from a menu and execute the corresponding task — creating arrays of varying dimensions, performing mathematical or matrix operations, combining/splitting arrays, searching/sorting/filtering elements, or computing statistical measures.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Array Creation | Core | Builds 1D, 2D, or 3D NumPy arrays from user input |
| Indexing & Slicing | Access | Retrieves single elements or sub-arrays |
| Mathematical Operations | Logic | Element-wise arithmetic, dot product, matrix multiplication |
| Combine / Split | Transformation | Stacks or splits arrays |
| Search / Sort / Filter | Logic | Locates, orders, and filters array values |
| Statistics | Analysis | Sum, mean, median, std dev, variance, percentile, correlation |

The goal is to demonstrate **practical NumPy usage combined with solid OOP design** through a clean, menu-driven interactive program.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 **Infinite Menu Loop** | Program runs continuously until user selects Exit |
| 🧊 **1D / 2D / 3D Array Support** | Create arrays of any of the three dimensions |
| 🎯 **Indexing & Slicing** | Access individual elements or ranges across dimensions |
| ➕ **Full Arithmetic Suite** | Addition, Subtraction, Multiplication, Division |
| ✖️ **Dot Product & Matrix Multiplication** | Linear algebra operations via `np.dot` / `np.matmul` |
| 🔗 **Array Combination** | Vertically stack two arrays with `np.vstack` |
| ✂️ **Array Splitting** | Split an array into N parts using `np.array_split` |
| 🔍 **Search** | Locate the position of a value using `np.where` |
| ↕️ **Sort** | Ascending or descending order sorting |
| 🧹 **Filter** | Extract elements greater than a given threshold |
| 📊 **9 Statistical Measures** | Sum, Mean, Median, Std Dev, Variance, Min, Max, Percentile, Correlation |
| 🔒 **Encapsulation** | Private array attribute accessed only via getters/setters |
| ⚠️ **Input-Driven Flow** | Fully driven by user input with branching via `if-elif-else` |

---

## 🏗️ Project Structure

```
📦 numpy-analyzer/
│
├── 📄 data_analytics.py     ← Main Python script (DataAnalytics class + main())
│
└── 📄 README.md             ← Project documentation
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌─────────────────────────────┐
│   Display Main Menu         │  ← Options: Create / Index / Math / Combine / Search / Stats / Exit
└────────────┬────────────────┘
             │
     ┌───────┼──────────────┬──────────────┬──────────────┐
     ▼       ▼               ▼              ▼              ▼
┌─────────┐ ┌────────────┐ ┌───────────┐ ┌────────────┐ ┌────────────┐
│Choice: 1│ │ Choice: 2  │ │Choice: 3  │ │ Choice: 4  │ │ Choice: 6  │
│ Create  │ │Index/Slice │ │  Math Ops │ │Combine/Split│ │ Statistics │
└────┬────┘ └─────┬──────┘ └─────┬─────┘ └──────┬─────┘ └──────┬─────┘
     │             │              │              │              │
     ▼             ▼              ▼              ▼              ▼
┌─────────────────────────────────────────────────────────────────┐
│                Print Output to Console                           │
└────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
                     Loop Back to Menu
                              │
                     (Choice: 7) Exit ✅
```

---

## 🧩 Class Design — `DataAnalytics`

| Type | Method | Description |
|------|--------|-------------|
| 🏗️ Constructor | `__init__` | Initializes an empty NumPy array |
| 🔓 Getter | `get_array` | Returns the current array |
| 🔒 Setter | `set_array` | Sets a new array |
| 🏷️ Class Method | `project_info` | Displays project information |
| 🌐 Static Method | `welcome_message` | Displays a welcome message |
| 🔐 Private Method | `__show_message` | Internal success message after array creation |
| ⚙️ Instance Method | `create_array` | Creates 1D / 2D / 3D arrays |
| ⚙️ Instance Method | `indexing_slicing` | Performs indexing and slicing |
| ⚙️ Instance Method | `mathematical_operations` | Performs arithmetic and matrix operations |
| ⚙️ Instance Method | `combine_or_split` | Combines or splits arrays |
| ⚙️ Instance Method | `search_sort_filter` | Searches, sorts, and filters array data |
| ⚙️ Instance Method | `compute_aggregates_statistics` | Computes statistical measures |

---

## 🔢 Part A — Array Creation & Access

### 📝 1. What is Array Creation Here?

The `create_array` method lets the user build a NumPy array of chosen dimensionality by entering values one at a time, using nested loops to fill rows, columns, and depth.

---

### 🗺️ 2. Array Types — Overview

| Type | Dimension | Logic Used |
|------|-----------|------------|
| 1️⃣ | **1D Array** | Single loop collects `n` elements |
| 2️⃣ | **2D Array** | Nested loop over rows and columns |
| 3️⃣ | **3D Array** | Triple-nested loop over depth, rows, and columns |

**Logic (1D Example):**
```python
data = []
for i in range(n):
    value = float(input("Enter Element : "))
    data.append(value)
self.__array = np.array(data)
```

**Output (n = 3):**
```
Array Created Successfully.

Array is :
[10. 20. 30.]
```

---

### 🎯 3. Indexing & Slicing

> Retrieves single elements or ranges of elements, adapting to the array's dimensionality (`ndim`).

**Logic:**
```python
if self.__array.ndim == 1:
    index = int(input("Enter Index : "))
    print("Element :", self.__array[index])
elif self.__array.ndim == 2:
    row = int(input("Enter Row Index : "))
    col = int(input("Enter Column Index : "))
    print("Element :", self.__array[row][col])
```

---

## ➗ Part B — Mathematical Operations

### 🔍 4. Element-wise Arithmetic

> Adds, subtracts, multiplies, or divides two matrices of the same shape element by element.

**Logic:**
```python
if choice == "1":
    print(self.__array + second)
elif choice == "2":
    print(self.__array - second)
```

### ✖️ 5. Dot Product & Matrix Multiplication

**Logic:**
```python
print(np.dot(self.__array, second))      # Dot Product
print(np.matmul(self.__array, second))   # Matrix Multiplication
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| ➕ Element-wise Ops | `+`, `-`, `*`, `/` on same-shape arrays |
| 🔗 `np.dot` | Dot product between two arrays |
| ✖️ `np.matmul` | True matrix multiplication |

---

## 🔀 Part C — Combine, Split, Search, Sort & Filter

### 🔗 6. Combine Arrays

**Logic:**
```python
print(np.vstack((self.__array, second)))
```

### ✂️ 7. Split Array

**Logic:**
```python
result = np.array_split(self.__array, part)
```

### 🔍 8. Search, Sort & Filter

**Logic:**
```python
index = np.where(self.__array == value)      # Search
print(np.sort(self.__array))                 # Sort Ascending
print(self.__array[self.__array > value])    # Filter
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🧱 `np.vstack` | Vertically stacks two arrays |
| ✂️ `np.array_split` | Splits an array into N parts |
| 🔎 `np.where` | Finds indices matching a condition |
| ↕️ `np.sort` | Sorts array elements |
| 🧹 Boolean Masking | Filters elements using conditions |

---

## 📊 Part D — Statistical Analysis

### 9. `compute_aggregates_statistics`

> Computes key statistical measures on the current array.

**Logic:**
```python
print("Sum :", np.sum(self.__array))
print("Mean :", np.mean(self.__array))
print("Median :", np.median(self.__array))
print("Standard Deviation :", np.std(self.__array))
print("Variance :", np.var(self.__array))
print(np.percentile(self.__array, p))
print(np.corrcoef(first, second))
```

**Sample Output:**
```
1. Sum
2. Mean
3. Median
4. Standard Deviation
5. Variance
6. Minimum
7. Maximum
8. Percentile
9. Correlation Coefficient
Enter Choice : 2
Mean : 20.0
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| ∑ `np.sum` / `np.mean` / `np.median` | Basic aggregate statistics |
| 📉 `np.std` / `np.var` | Spread of the data |
| 📈 `np.percentile` | Value below which a percentage of data falls |
| 🔗 `np.corrcoef` | Correlation coefficient between two arrays |

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 🔢 **NumPy** | Latest | Array creation, math, and statistical operations |
| 🔁 **While Loop** | Built-in | Infinite menu loop control |
| 🔂 **For Loop** | Built-in | Input collection and array traversal |
| 🧩 **OOP Concepts** | Built-in | Class, getter/setter, class/static/private methods |
| 🖨️ **print() / input()** | Built-in | Console I/O and user interaction |

---

## 📈 Results & Insights

After running the program, the following outputs are produced:

- ✅ **1D, 2D, and 3D Array Creation** — Fully supported with dynamic user input
- 🎯 **Accurate Indexing & Slicing** — Adapts automatically to array dimensionality
- ➕ **Complete Arithmetic Suite** — Element-wise ops, dot product, and matrix multiplication
- 🔗 **Array Reshaping Tools** — Combine via `vstack`, split via `array_split`
- 🔍 **Search, Sort & Filter** — Locate, order, and extract array elements on demand
- 📊 **9 Statistical Measures** — Comprehensive numerical insight into any array
- 🔁 **Persistent Menu** — Program loops back after every task until manually exited

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Core NumPy + OOP concepts combined in one project |
| 🔒 **Proper Encapsulation** | Array data hidden behind a private attribute |
| 📚 **Educational** | Covers array creation, math, stats, and manipulation in depth |
| 🖥️ **Minimal Dependencies** | Requires only NumPy — no other external libraries |
| ⚡ **Lightweight** | Single-file script, instantly runnable from any terminal |
| 🧪 **Extensible** | Easy to add more operations (reshape, transpose, broadcasting, etc.) |
| 📖 **Readable Code** | Clear `if-elif-else` structure makes logic easy to follow |
| 🛡️ **Guard Clauses** | Prevents operations on an empty array with clear prompts |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Vaidehi Vyas

[![GitHub](https://img.shields.io/badge/GitHub-yourhandle-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/)

> *"Every array starts empty — just like every program starts with a single line."*

**🎓 Role:** Junior Python Developer | Programming Enthusiast \
**📍 Location:** India\
**🛠️ Skills:** Python · NumPy · OOP · CLI Applications · Data Analysis

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🔢 [NumPy Official Docs](https://numpy.org/doc/) — NumPy array and statistics reference
- 📐 [GeeksForGeeks — NumPy](https://www.geeksforgeeks.org/numpy/) — NumPy tutorials and examples
- 🖥️ [W3Schools NumPy](https://www.w3schools.com/python/numpy/default.asp) — Beginner NumPy reference
- 🧮 [Real Python — NumPy Guide](https://realpython.com/numpy-array-programming/) — In-depth array programming
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Python and data analysis courses

---

## 🔗 Links

- [Demo / Resource 1](https://drive.google.com/file/d/1VYk10y5fRS-k6uFGdKWolV0m8_xcxWSu/view?usp=sharing)
- [Demo / Resource 2](https://drive.google.com/file/d/1PoC9CDhCoGakjEvT33ULHwTOIR00L8bL/view?usp=sharing)

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 03 August, 2026*

</div>
