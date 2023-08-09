# Text_summarizer
Text summarization refers to the technique of shortening long pieces of text. The intention is to create a coherent and fluent summary having only the main points outlined in the document.
Automatic text summarization is commonly done using Natural Language Processing (NLP)

This project uses Samsum-hugging facr data set. The SAMSum dataset contains about 16k messenger-like conversations with summaries. Conversations were created and written down by linguists fluent in English. Linguists were asked to create conversations similar to those they write on a daily basis, reflecting the proportion of topics of their real-life messenger convesations. The style and register are diversified - conversations could be informal, semi-formal or formal, they may contain slang words, emoticons and typos.

# Data Fields:
dialogue: text of dialogue.
summary: human written summary of the dialogue.
id: unique id of an example.

# Data Splits:
train: 14732
val: 818
test: 819

# Model Training
This model uses pegasus model for training the dataset.Pegasus is pre-trained jointly on two self-supervised objective functions: Masked Language Modeling (MLM) and a novel summarization specific pretraining objective, called Gap Sentence Generation (GSG).
