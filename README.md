NLP Sentiment Classification Analysis

This project investigates how well a pretrained sentiment classifier handles different types of sentiment expressions, particularly clear, mixed, contrastive, and ambiguous sentences.

Research Question

Does a pretrained sentiment classifier perform worse on mixed, ambiguous, and contrastive sentences than on clearly positive or negative sentences?

Hypothesis

The pretrained sentiment classifier is expected to achieve higher accuracy on clearly positive and clearly negative sentences. Its performance is expected to decrease on mixed, ambiguous, and contrastive sentences because these cases require a better and

Dataset

The experiment uses the SST-2 validation dataset.

A balanced sample of 120 sentences was selected:

60 positive sentences
60 negative sentences

The sampling process used a fixed random seed of 42 for reproducibility.

Each sentence was manually categorized into one of four categories:

clear

mixed

contrastive

ambiguous

Then after that, start a new section:

Model

The pretrained model used in this experiment is:

distilbert-base-uncased-finetuned-sst-2-english

The model was accessed using the Hugging Face Transformers library.

Method

The experiment was performed in the following steps:

Load the SST-2 validation dataset.
Randomly select 60 positive and 60 negative sentences.
Manually categorize the 120 sentences as clear, mixed, contrastive, or ambiguous.
Run the pretrained DistilBERT sentiment classifier on all sentences.
Compare the model prediction with the official SST-2 gold label.
Calculate overall accuracy and accuracy for each sentence category.
Analyze the sentences that were incorrectly classified.

Results

Overall accuracy: 87.50%

Clear sentences:
92.86%

Contrastive sentences:
87.50%

Ambiguous sentences:
57.14%

Mixed sentences:
40.00%

The results show that the classifier performed best on clear sentences and considerably worse on mixed and ambiguous sentences.

The contrastive category achieved relatively high accuracy compared with mixed and ambiguous sentences.

Because the mixed and ambiguous categories contain a small number of examples, these results should be interpreted cautiously.

Project Structure

dataset/dataset_Preparation.py
Creates the balanced 120-sentence SST-2 sample.

data/run_model.py
Runs the pretrained DistilBERT model and saves its predic

data/analyze_results.py
Displays the

data/sst2_sample_120_categorized.csv
Contains the manually categorized evaluation sample.

data/sst2_results.csv
Contains the model predictions, confidence scores, and evaluation results.

Req

Installation

Create and activate a Python virtual environment and install the dependencies:

pip install -r requirements.txt

Run the Experiment

Prepare the dataset:

python dataset/dataset_Preparation.py

Run the model:

python data/run_model.py

Analyze the errors:

python data/analyze_results.py

Limitations

The experiment uses only 120 sentences.

The mixed and ambiguous categories contain relatively few examples.

The manual sentence categories involve human judgment.

Some SST-2 gold labels may themselves be difficult to interpret for ambiguous or context-dependent sentences.

Only one pretrained sentiment classifier was evaluated.

References

Pang, B. and Lee, L. (2008). Opinion Mining and Sentiment Analysis.

Wilson, T., Wiebe, J., and Hoffmann, P. (2005). Recognizing Contextual Polarity in Phrase-Level Sentiment Analysis.

Socher, R. et al. (2013). Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank.

Martins, P. H. et al. (2021). Why Do Document-Level Polarity Classifiers Fail?

License

This project is licensed under the MIT License.

Then save README.md.

After saving, run:

git add README.md

Then:

git commit -m "docs: add project README and reproducibility instructions"

Then:

git push
