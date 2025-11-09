# 🧠 Predictive Apriori with Database Integration and Context-Aware Recommendations

This project implements a **Modified Apriori Algorithm** that extends the traditional association rule mining model to enable **real-time item prediction** based on the **current cart context**.  
It integrates Apriori results with a **database layer** and a **Streamlit web interface**, allowing both offline pattern discovery and online predictive querying.

---

## 🚀 Features

✅ Implements **Apriori Algorithm** using `mlxtend`  
✅ Stores generated **association rules** in a local SQLite database  
✅ Supports **context-aware prediction** (based on current user cart)  
✅ Provides an interactive **Streamlit web interface**  
✅ Fully deployable on **Streamlit Cloud** or local environments  
✅ Designed for **research & academic use** with database perspective

---

## 📚 Research Motivation

Traditional Apriori algorithms focus purely on **pattern discovery** — finding frequent itemsets and association rules from historical transactions.  
However, they lack *context awareness* and *real-time prediction capability*.  

This modified version bridges that gap by:
- Using **pre-mined rules** as a knowledge base stored in a database  
- Accepting **live cart input** to predict the next likely items  
- Querying the rule database dynamically based on **current transaction context**

From a **database systems perspective**, this transforms Apriori from an *offline data mining* algorithm into a *predictive, query-driven recommendation engine*.

---

## 🧩 System Architecture

| Stage | Description |
|--------|-------------|
| **1. Data Preparation** | Transaction dataset (`Groceries_dataset.csv`) grouped by customer and date |
| **2. Frequent Pattern Mining** | Uses Apriori (`mlxtend.frequent_patterns`) to generate frequent itemsets and rules |
| **3. Database Storage** | Stores rules (antecedent, consequent, confidence, lift) in SQLite |
| **4. Context Querying** | Accepts current cart items from user and retrieves matching rules |
| **5. Prediction Output** | Displays top recommended items with confidence & lift scores in Streamlit UI |

---

## 🧮 Example Prediction Flow

**Input:**  



---

## 🧩 System Architecture Diagram

```mermaid
flowchart TD

    subgraph Dataset["📦 Transactional Dataset"]
        A1["Member Number"]
        A2["Date"]
        A3["Item Description"]
    end

    subgraph AprioriProcess["⚙️ Apriori Mining Engine"]
        B1["Generate Candidate Itemsets"]
        B2["Prune Infrequent Sets"]
        B3["Extract Association Rules"]
    end

    subgraph DatabaseLayer["🗄️ Database Storage"]
        C1["SQLite Database"]
        C2["Store Antecedent, Consequent, Support, Confidence, Lift"]
    end

    subgraph ContextEngine["🧠 Context-Aware Prediction Engine"]
        D1["Current Cart Input"]
        D2["Match Antecedent Subsets"]
        D3["Rank Predictions (Confidence x Lift)"]
        D4["Return Top-N Recommended Items"]
    end

    subgraph UI["🖥️ Streamlit Web App"]
        E1["Dataset Upload"]
        E2["Parameter Selection"]
        E3["Display Predictions & Visualization"]
    end

    %% Connections
    Dataset --> AprioriProcess
    AprioriProcess --> DatabaseLayer
    DatabaseLayer --> ContextEngine
    ContextEngine --> UI

    UI -->|User Selects Items| ContextEngine
    ContextEngine -->|Predicted Items| UI
