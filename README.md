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
````

---

## 🧮 Example Prediction Flow

**Input:**

```
Current cart: {whole milk, yogurt}
```

**Matching rule in database:**

```
{whole milk, yogurt} → {tropical fruit} (Confidence = 0.63, Lift = 1.45)
```

**Predicted output:**

```
Predicted Next Items:
1. tropical fruit (Confidence: 0.63, Lift: 1.45)
```

---

## ⚙️ Installation

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/anshuman4d/apriori_predict.git
cd apriori_predict/dbClass
```

### **2️⃣ Install Dependencies**

```bash
pip install -r ../requirements.txt
```

### **3️⃣ Run Locally**

```bash
python -m streamlit run app.py
```

Your app will launch at:

```
http://localhost:8501
```

---

## ☁️ Deploy on Streamlit Cloud

1. Upload these files to your GitHub repo:

   * `app.py`
   * `requirements.txt`
   * `runtime.txt`
   * `Groceries_dataset.csv` (optional, or upload via UI)

2. Go to [Streamlit Cloud](https://share.streamlit.io)

3. Deploy using:

   ```
   main file path: dbClass/app.py
   ```

4. Add a `runtime.txt` file to ensure compatibility:

   ```
   python-3.11
   ```

---

## 🧾 Project File Structure

```
apriori_predict/
│
├── dbClass/
│   ├── app.py               # Main Streamlit app
│
├── Groceries_dataset.csv    # Dataset
├── requirements.txt         # Dependencies
├── runtime.txt              # Python runtime version
└── README.md                # Project documentation
```

---

## 🔬 Technical Stack

| Component      | Technology Used                        |
| -------------- | -------------------------------------- |
| **Language**   | Python 3.11                            |
| **Libraries**  | mlxtend, pandas, matplotlib, streamlit |
| **Database**   | SQLite                                 |
| **Interface**  | Streamlit Web App                      |
| **Deployment** | Streamlit Cloud                        |

---

## 🧠 Academic Relevance

This project aligns with the **Knowledge Discovery in Databases (KDD)** framework and demonstrates:

* Integration of **data mining** with **database querying**
* Real-time **context-aware recommendation**
* **Database-driven predictive analytics**

It can serve as a foundation for further work in:

* Time-aware Apriori algorithms
* Weighted rule prediction
* Hybrid ML + association rule models

---

## 🧑‍💻 Author

**Anshuman Diwakar**
M.Tech IT 
Netaji Subhash University of Technology
📧 Email: [adiwakar19@gmail.com](mailto:adiwakar19@gmail.com)
🌐 GitHub: [anshuman4d](https://github.com/anshuman4d)

---

## 📘 References

1. Agrawal, R. & Srikant, R. (1994). *Fast Algorithms for Mining Association Rules.*
2. Han, J., Kamber, M., & Pei, J. (2011). *Data Mining: Concepts and Techniques.*
3. Mlxtend Documentation: [https://rasbt.github.io/mlxtend/](https://rasbt.github.io/mlxtend/)

---

## 🏁 Conclusion

The **Modified Apriori with Context-Aware Prediction** demonstrates how association rule mining can evolve into an intelligent, database-integrated, and user-centric recommendation system — bridging the gap between **data mining** and **real-time decision support**.

```
