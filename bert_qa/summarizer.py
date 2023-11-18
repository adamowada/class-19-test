import os
from pathlib import Path

from tflite_support.task import text


def summarize(article: str) -> str:
    """
    Summarizes an AP news article.

    :param article: A string representing a web scraped AP news article.
    :return: A string representing the summary of the article.
    """
    # Initialization
    root_directory = Path(__file__).resolve().parent.parent
    model_path = os.path.join(root_directory, 'model', 'mobilebert.tflite')

    answerer = text.BertQuestionAnswerer.create_from_file(model_path)

    # Run inference
    question = "What is the summary of this article?"
    bert_qa_result = answerer.answer(article, question)

    return bert_qa_result.answers[0].text
