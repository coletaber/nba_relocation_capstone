import pandas as pd

# --- 1. Load the real CSV file ---
df = pd.read_csv("nba-vegas-project/data/fans_surv_responses.csv")

# --- 2. Use the exact column name found from check_columns.py ---
engagement_col = "Which of the following digital experiences would make you more engaged as a fan? "

# --- 3. Drop empty values in that column ---
df = df.dropna(subset=[engagement_col])

# --- 4. Normalize the digital engagement responses ---
# Define simple category labels
category_map = {
    "Mobile app": "Mobile App",
    "Live, real-time, in-game betting features": "Live Betting",
    "Loyalty rewards program": "Loyalty Rewards",
    "Exclusive behind-the-scenes content": "Behind-the-Scenes",
    "I have no interest in digital fan experiences": "No Interest"
}

def normalize_response(resp):
    """
    Takes a raw response string and maps it into simplified category labels.
    Handles multi-choice comma-separated responses.
    """
    items = [i.strip() for i in resp.split(",")]
    mapped = set()

    for item in items:
        for keyword, label in category_map.items():
            if keyword in item:
                mapped.add(label)

    # If something didn’t match any category, keep the raw text
    if not mapped:
        mapped.add(resp.strip())

    return ", ".join(sorted(mapped))


# Create the cleaned column
df["Cleaned Digital Engagement"] = df[engagement_col].apply(normalize_response)

# --- 5. Save cleaned CSV file ---
df.to_csv("nba-vegas-project/data/cleaned_fan_engagement.csv", index=False)

# --- 6. Tell the user it worked ---
print("Cleaning complete!")
print("Saved cleaned file to: nba-vegas-project/data/cleaned_fan_engagement.csv")
print("You can now upload that cleaned file into Streamlit.")
