from transformers import pipeline

def test_positive_sentiment():
    classifier = pipeline("sentiment-analysis")
    result = classifier("I love exploring AI with Copilot!")[0]
    assert result["label"] == "POSITIVE"

def test_negative_sentiment():
    classifier = pipeline("sentiment-analysis")
    result = classifier("This is the worst experience ever.")[0]
    assert result["label"] == "NEGATIVE"
