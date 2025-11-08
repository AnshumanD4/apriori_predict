import os
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt

# --- Load dataset ---
file_path = os.path.join(os.getcwd(), "myaprori/Groceries_dataset.csv")
data = pd.read_csv(file_path)

# --- Preprocess ---
data['Date'] = pd.to_datetime(data['Date'])
transactions = (
    data.groupby(['Member_number', 'Date'])['itemDescription']
    .apply(list)
    .reset_index(name='Items')
)

# --- One-hot encode transactions ---
from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()
te_ary = te.fit(transactions['Items']).transform(transactions['Items'])
df = pd.DataFrame(te_ary, columns=te.columns_)

# --- Apply Apriori ---
frequent_itemsets = apriori(df, min_support=0.05, use_colnames=True)
frequent_itemsets = frequent_itemsets.sort_values(by='support', ascending=False)

# --- Generate Association Rules ---
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)

print(f" Total frequent itemsets found: {len(frequent_itemsets)}")
print(f" Total association rules generated: {len(rules)}\n")

# --- Save outputs ---
frequent_itemsets.to_csv("frequent_itemsets.csv", index=False)
rules.to_csv("association_rules.csv", index=False)

print("Files saved successfully:")
print(" - frequent_itemsets.csv")
print(" - association_rules.csv\n")

print("Top 10 Frequent Itemsets:")
print(frequent_itemsets.head(10))

# --- Plot only if rules exist ---
if not rules.empty:
    plt.scatter(rules['support'], rules['confidence'], s=rules['lift'] * 10, alpha=0.6, edgecolors="k")
    plt.title("Association Rules: Support vs Confidence")
    plt.xlabel("Support")
    plt.ylabel("Confidence")
    plt.grid(True)
    plt.show()
else:
    print("No association rules found — try lowering min_support or min_threshold.")
