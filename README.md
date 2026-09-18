# NLP Sentiment Classification Analysis

This project investigates how well a pretrained sentiment classifier handles different types of sentiment expressions, particularly clear, mixed, contrastive, and ambiguous sentences.

## Research Question

Does a pretrained sentiment classifier perform worse on mixed, ambiguous, and contrastive sentences than on clearly positive or negative sentences?

## Hypothesis

The pretrained sentiment classifier is expected to achieve higher accuracy on clearly positive and clearly negative sentences. Its performance is expected to decrease on mixed, ambiguous, and contrastive sentences because these cases require a better understanding of context and the overall meaning of the sentence.

## Dataset

The experiment uses the validation split of the SST-2 dataset.

A balanced sample of 120 sentences was selected:

- 60 positive sentences
- 60 negative sentences

The sampling process used a fixed random seed of `42` for reproducibility.

Each sentence was manually categorized into one of four categories:

- Clear
- Mixed
- Contrastive
- Ambiguous

## Model

The pretrained model used in this experiment is:

`distilbert-base-uncased-finetuned-sst-2-english`

The model was accessed using the Hugging Face Transformers library.

## Method

The experiment was performed in the following steps:

1. Load the SST-2 validation dataset.
2. Randomly select 60 positive and 60 negative sentences.
3. Manually categorize the 120 sentences as clear, mixed, contrastive, or ambiguous.
4. Run the pretrained DistilBERT sentiment classifier on all sentences.
5. Compare the model predictions with the official SST-2 gold labels.
6. Calculate overall accuracy and accuracy for each sentence category.
7. Analyze the sentences that were incorrectly classified.

## Results

The classifier achieved an overall accuracy of **87.50%**.

| Sentence Category | Accuracy |
|---|---:|
| Clear | 92.86% |
| Contrastive | 87.50% |
| Ambiguous | 57.14% |
| Mixed | 40.00% |

The results show that the classifier performed best on clear sentences and considerably worse on mixed and ambiguous sentences.

The contrastive category achieved relatively high accuracy compared with mixed and ambiguous sentences.

Because the mixed and ambiguous categories contain a relatively small number of examples, these results should be interpreted cautiously.

## Discussion

The results mostly support the hypothesis because the classifier performed best on clear sentences and showed lower accuracy on mixed and ambiguous sentences.

This suggests that sentiment becomes more difficult to classify when a sentence contains unclear, conflicting, or complex sentiment information.

An unexpected result was the relatively high performance on contrastive sentences, where the classifier achieved **87.50% accuracy**.

## Limitations

- The experiment uses only 120 sentences.
- The mixed and ambiguous categories contain relatively few examples.
- The manual sentence categories involve human judgment.
- Some SST-2 gold labels may themselves be difficult to interpret for ambiguous or context-dependent sentences.
- Only one pretrained sentiment classifier was evaluated.

## Conclusion

The experiment showed that clearly expressed sentiment sentences led to better performance by the pretrained DistilBERT classifier.

In contrast, the model performed worse on mixed and ambiguous sentences and found these cases more challenging.

These results support the idea that sentiment classification performance can be affected by contextual complexity.

## Project Structure

NLP-Sentiment-Classification-Analysis/

data/
- analyze_results.py
- run_model.py
- sst2_results.csv
- sst2_sample_120_categorized.csv

dataset/
- dataset_Preparation.py

Root files:
- .gitignore
- LICENSE
- README.md
- requirements.txt

## File Descriptions

### dataset/dataset_Preparation.py

Creates the balanced 120-sentence SST-2 sample using a fixed random seed of 42.

### data/run_model.py

Runs the pretrained DistilBERT sentiment classifier on the manually categorized sample and saves the model predictions.

### data/analyze_results.py

Calculates the overall accuracy, category-level accuracy, and analyzes incorrectly classified sentences.

### data/sst2_sample_120_categorized.csv

Contains the manually categorized evaluation sample of 120 SST-2 sentences.

### data/sst2_results.csv

Contains the model predictions, confidence scores, and evaluation results.

## Installation

Create and activate a Python virtual environment.

Then install the required dependencies:

`pip install -r requirements.txt`

## Run the Experiment

### 1. Prepare the dataset

`python dataset/dataset_Preparation.py`

### 2. Run the sentiment classifier

`python data/run_model.py`

### 3. Analyze the results

`python data/analyze_results.py`

## Reproducibility

The project uses a fixed random seed of `42` when selecting the SST-2 evaluation sample.

The complete sample, manual sentence categories, model predictions, confidence scores, and evaluation results are included in the repository.

This allows the experiment and analysis to be reproduced using the provided scripts and data files.

## References

Pang, B., & Lee, L. (2008). *Opinion Mining and Sentiment Analysis.*

Wilson, T., Wiebe, J., & Hoffmann, P. (2005). *Recognizing Contextual Polarity in Phrase-Level Sentiment Analysis.*

Socher, R., et al. (2013). *Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank.*

Martins, K., Vaz-de-Melo, P. O. S., & Santos, R. (2021). *Why Do Document-Level Polarity Classifiers Fail?*

## License

This project is licensed under the MIT License.
