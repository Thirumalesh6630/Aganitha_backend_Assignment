# **TASK DESCRIPTION**  
Your task is to write a Python program to fetch research papers based on a user-specified query. The
program must identify papers with at least one author affiliated with a pharmaceutical or biotech
company and return the results as a CSV file.

## **PROBLEM DETAILS**  

### **1. SOURCE OF PAPERS**  
- Fetch papers using the **PubMed API**  
- The program should support **PubMed's full query syntax** for flexibility  

### **2. OUTPUT REQUIREMENTS**  
- Return the results as a **CSV file** with the following columns:  
  - **PubmedID** → Unique identifier for the paper  
  - **Title** → Title of the paper  
  - **Publication Date** → Date the paper was published  
  - **Non-academic Author(s)** → Names of authors affiliated with non-academic institutions  
  - **Company Affiliation(s)** → Names of pharmaceutical/biotech companies  
  - **Corresponding Author Email** → Email address of the corresponding author  

### **3. COMMAND-LINE PROGRAM FEATURES**  
- Accept the query as a **command-line argument**  
- Provide the following **options**:  
  - **`-h` or `--help`** → Display usage instructions  
  - **`-d` or `--debug`** → Print debug information during execution  
  - **`-f` or `--file`** → Specify the filename to save the results (if not provided, print output to console)  

## **CODE ORGANIZATION AND ENVIRONMENT**  

### **VERSION CONTROL**  
- Use **Git** for version control  
- Code must be **hosted on GitHub**  

### **DEPENDENCIES AND SETUP**  
- Use **Poetry** for dependency management and packaging  
- Ensure that running **`poetry install`** sets up all dependencies  

### **EXECUTION**  
- Provide an **executable command** named **`get-papers-list`** via Poetry  

## **DOCUMENTATION**  
- Include a **`README.md`** file with:  
  - **Code organization details**  
  - **Installation and execution instructions**  
  - **Mention of tools (e.g., LLMs, libraries) used with relevant links**  

## **EVALUATION CRITERIA**  

### **FUNCTIONAL REQUIREMENTS**  
- Adherence to the problem statement  
- Ability to **fetch and filter results correctly**  

### **NON-FUNCTIONAL REQUIREMENTS**  
- **Typed Python** → Use **types** everywhere  
- **Performance** → Efficient API calls and processing  
- **Readability** → Clear, maintainable code with **comments & docstrings**  
- **Organization** → Logical **modular functions and classes**  
- **Robustness** → Handle **invalid queries, API failures, and missing data**  

## **BONUS POINTS**  
1. **Break the program into two parts** → A **module** and a **command-line program** that uses the module  
2. **Publish the module in test-pypi**  

## **NOTES**  
- You are **free to use LLM tools** or other resources for development  
- Clearly **document external tools** in **`README.md`**  
- Program will be evaluated by **automated scripts**, so follow conventions strictly  
- **Identifying non-academic authors:**  
  - Apply **heuristics** (email domains, keywords like **university, labs**, etc.)  
