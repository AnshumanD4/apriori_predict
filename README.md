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
