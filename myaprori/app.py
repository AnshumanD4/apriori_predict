# --- Modified Apriori with Database Integration & Context-Aware Prediction ---
# Author: Anshuman Diwakar

import pandas as pd
import sqlite3
import streamlit as st
from mlxtend.frequent_patterns import apriori, association_rules

# ----------------- DATABASE SETUP -----------------
DB_FILE = "apriori_rules.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS AssociationRules (
            antecedents TEXT,
            consequents TEXT,
            support REAL,
            confidence REAL,
            lift REAL
        )
    ''')
    conn.commit()
    conn.close()

# ----------------- SAVE RULES -----------------
def save_rules_to_db(rules_df):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM AssociationRules")  # clear old rules
    for _, row in rules_df.iterrows():
        cursor.execute('''
            INSERT INTO AssociationRules (antecedents, consequents, support, confidence, lift)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            ', '.join(list(row['antecedents'])),
            ', '.join(list(row['consequents'])),
            row['support'],
            row['confidence'],
            row['lift']
        ))
    conn.commit()
    conn.close()

# ----------------- QUERY RULES -----------------
def query_rules_from_db(cart_items):
    conn = sqlite3.connect(DB_FILE)
    query = "SELECT * FROM AssociationRules"
    df = pd.read_sql_query(query, conn)
    conn.close()

    results = []
    for _, row in df.iterrows():
        antecedent_set = set(row['antecedents'].split(", "))
        if antecedent_set.issubset(set(cart_items)):
            results.append(row)

    results_df = pd.DataFrame(results)
    if not results_df.empty:
        results_df = results_df.sort_values(by='confidence', ascending=False)
    return results_df

# ----------------- APRIORI MINING -----------------
def run_apriori(dataset_path, min_support=0.01, min_confidence=0.2):
    df = pd.read_csv(dataset_path)
    # Transaction grouping
    basket = (df.groupby(['Member_number', 'itemDescription'])['itemDescription']
                .count().unstack().reset_index().fillna(0).set_index('Member_number'))
    basket = basket.applymap(lambda x: 1 if x > 0 else 0)

    frequent_itemsets = apriori(basket, min_support=min_support, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=min_confidence)
    save_rules_to_db(rules)
    return frequent_itemsets, rules

# ----------------- STREAMLIT UI -----------------
st.title("Modified Apriori with Context-Aware Prediction")
st.markdown("### A Database-Integrated Model for Predicting Next Likely Items")

dataset_path = st.text_input("Enter path to dataset (CSV)", "Groceries_dataset.csv")

if st.button("Run Apriori & Store Rules"):
    init_db()
    freq, rules = run_apriori(dataset_path)
    st.success(f" {len(freq)} frequent itemsets and {len(rules)} rules stored in database!")
    st.dataframe(freq.head(10))
    st.dataframe(rules.head(10))

st.markdown("---")
st.header("🔍 Predict Next Item from Current Cart")

cart_input = st.text_input("Enter items currently in cart (comma-separated)", "whole milk, yogurt")
if st.button("Predict Next Items"):
    current_cart = [x.strip() for x in cart_input.split(",") if x.strip()]
    st.info(f"🛒 Current Cart: {current_cart}")
    results_df = query_rules_from_db(current_cart)

    if not results_df.empty:
        st.success("✅ Predicted Next Items:")
        st.dataframe(results_df[['consequents', 'confidence', 'lift']].head(10))
    else:
        st.warning("No strong rule found for this cart context.")
