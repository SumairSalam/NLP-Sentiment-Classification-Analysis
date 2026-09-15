import pandas as pd

df = pd.read_csv("data/sst2_results.csv")

errors = df[df["correct"] == False]

print("Total errors:", len(errors))

print(
errors[
[
"sentence",
"gold_label",
"category",
"model_prediction",
"confidence"
]
].to_string(index=False)
)