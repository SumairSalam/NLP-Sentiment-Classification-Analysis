import os
from pathlib import Path

os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")

from transformers import pipeline
import pandas as pd

data_dir = Path(__file__).resolve().parent
input_path = data_dir / "sst2_sample_120_categorized(SST2 Sample).csv"
output_path = data_dir / "sst2_results.csv"

df = pd.read_csv(input_path, encoding="cp1252")

classifier = pipeline(
"sentiment-analysis",
model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

predictions = classifier(df["sentence"].tolist())

df["model_prediction"] = [
prediction["label"].lower()
for prediction in predictions
]

df["confidence"] = [
prediction["score"]
for prediction in predictions
]

df["correct"] = df["model_prediction"] == df["gold_label"]

df.to_csv(output_path, index=False)

print(df[
["sentence", "gold_label", "category",
"model_prediction", "confidence", "correct"]
].head())

print("\nOverall accuracy:")
print(df["correct"].mean())

print("\nAccuracy by category:")
print(df.groupby("category")["correct"].mean())