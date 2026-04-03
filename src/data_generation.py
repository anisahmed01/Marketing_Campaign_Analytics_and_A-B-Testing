import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000
dates = pd.date_range(start="2024-01-01", periods=n, freq="D")

df = pd.DataFrame({"Date": dates})

# Campaigns
fb_campaigns = ["FB_A", "FB_B", "FB_C"]
ig_campaigns = ["IG_X", "IG_Y", "IG_Z"]

df["Facebook Ad Campaign"] = np.random.choice(fb_campaigns, n)
df["Instagram Ad Campaign"] = np.random.choice(ig_campaigns, n)

# Base views (with seasonality: weekends higher)
df["day"] = df["Date"].dt.dayofweek
weekend_multiplier = np.where(df["day"] >= 5, 1.3, 1.0)

df["Facebook Ad Views"] = (np.random.randint(5000, 25000, n) * weekend_multiplier).astype(int)
df["Instagram Ad Views"] = (np.random.randint(4000, 22000, n) * weekend_multiplier).astype(int)

# Campaign-level performance differences
fb_ctr_map = {"FB_A": 0.06, "FB_B": 0.045, "FB_C": 0.03}
ig_ctr_map = {"IG_X": 0.055, "IG_Y": 0.04, "IG_Z": 0.028}

df["fb_ctr_base"] = df["Facebook Ad Campaign"].map(fb_ctr_map)
df["ig_ctr_base"] = df["Instagram Ad Campaign"].map(ig_ctr_map)

# Add noise to CTR
df["Facebook Click-through Rate"] = df["fb_ctr_base"] + np.random.uniform(-0.01, 0.01, n)
df["Instagram Click-through Rate"] = df["ig_ctr_base"] + np.random.uniform(-0.01, 0.01, n)

# Ensure CTR stays within realistic bounds
df["Facebook Click-through Rate"] = df["Facebook Click-through Rate"].clip(0.01, 0.1)
df["Instagram Click-through Rate"] = df["Instagram Click-through Rate"].clip(0.01, 0.09)

# Clicks
df["Facebook Ad Clicks"] = (df["Facebook Ad Views"] * df["Facebook Click-through Rate"]).astype(int)
df["Instagram Ad Clicks"] = (df["Instagram Ad Views"] * df["Instagram Click-through Rate"]).astype(int)

# Conversion rates (campaign dependent)
fb_conv_map = {"FB_A": 0.12, "FB_B": 0.09, "FB_C": 0.06}
ig_conv_map = {"IG_X": 0.11, "IG_Y": 0.08, "IG_Z": 0.05}

df["fb_conv_base"] = df["Facebook Ad Campaign"].map(fb_conv_map)
df["ig_conv_base"] = df["Instagram Ad Campaign"].map(ig_conv_map)

df["Facebook Conversion Rate"] = df["fb_conv_base"] + np.random.uniform(-0.02, 0.02, n)
df["Instagram Conversion Rate"] = df["ig_conv_base"] + np.random.uniform(-0.02, 0.02, n)

df["Facebook Conversion Rate"] = df["Facebook Conversion Rate"].clip(0.02, 0.2)
df["Instagram Conversion Rate"] = df["Instagram Conversion Rate"].clip(0.02, 0.18)

# Conversions
df["Facebook Ad Conversion"] = (df["Facebook Ad Clicks"] * df["Facebook Conversion Rate"]).astype(int)
df["Instagram Ad Conversion"] = (df["Instagram Ad Clicks"] * df["Instagram Conversion Rate"]).astype(int)

# Cost per click varies slightly by campaign
fb_cpc_map = {"FB_A": 1.2, "FB_B": 1.0, "FB_C": 0.8}
ig_cpc_map = {"IG_X": 1.1, "IG_Y": 0.95, "IG_Z": 0.75}

df["fb_cpc"] = df["Facebook Ad Campaign"].map(fb_cpc_map) + np.random.uniform(-0.2, 0.2, n)
df["ig_cpc"] = df["Instagram Ad Campaign"].map(ig_cpc_map) + np.random.uniform(-0.2, 0.2, n)

# Total cost depends on clicks
df["Cost Per Facebook Ad"] = df["Facebook Ad Clicks"] * df["fb_cpc"]
df["Cost Per Instagram Ad"] = df["Instagram Ad Clicks"] * df["ig_cpc"]

# Final CPC (calculated)
df["Facebook Cost Per Click"] = df["Cost Per Facebook Ad"] / df["Facebook Ad Clicks"].replace(0,1)
df["Instagram Cost Per Click"] = df["Cost Per Instagram Ad"] / df["Instagram Ad Clicks"].replace(0,1)

# ---- Introduce REALISTIC MESSINESS ----

# Randomly drop 3% rows partially
for col in ["Facebook Ad Views", "Facebook Ad Clicks", "Facebook Ad Conversion",
            "Instagram Ad Views", "Instagram Ad Clicks", "Instagram Ad Conversion"]:
    mask = np.random.rand(n) < 0.03
    df.loc[mask, col] = np.nan

# Ensure dependency logic: if views missing → clicks & conversions missing
for platform in ["Facebook", "Instagram"]:
    df.loc[df[f"{platform} Ad Views"].isna(), [f"{platform} Ad Clicks", f"{platform} Ad Conversion"]] = np.nan

# Clean helper columns
df = df.drop(columns=["fb_ctr_base", "ig_ctr_base", "fb_conv_base", "ig_conv_base", "fb_cpc", "ig_cpc", "day"])

# Save
df.to_csv("marketing_campaign_realistic.csv", index=False)

print("✅ Realistic dataset generated successfully (USD assumed)")