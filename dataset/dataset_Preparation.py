import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
parquet_path = Path(__file__).resolve().parent / "validation-00000-of-00001 (1).parquet"
df = pd.read_parquet(parquet_path)

print(df.head())
print(df.columns)
print(df["label"].value_counts())

positive = df[df["label"] == 1].sample(n=60, random_state=42)
negative = df[df["label"] == 0].sample(n=60, random_state=42)

sample = pd.concat([positive, negative])

sample = sample.sample(frac=1, random_state=42).reset_index(drop=True)

sample["gold_label"] = sample["label"].map({
0: "negative",
1: "positive"
})

sample["category"] = ""
sample["notes"] = ""

output_path = project_root / "data" / "sst2_sample_120.csv"
output_path.parent.mkdir(exist_ok=True)
sample.to_csv(output_path, index=False)

print(f"Saved {len(sample)} sentences to {output_path}")