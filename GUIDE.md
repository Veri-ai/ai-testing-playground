# GUIDE: How to Run AI Testing Playground

This guide explains how to run the sentiment analysis tests included in this project.

---

## 1. Local (CMD/Terminal)

1. Clone the repo:
   ```bash
   git clone https://github.com/Veri-ai/ai-testing-playground.git
   cd ai-testing-playground

2. Install dependencies:

```bash
   pip install -r requirements.txt
```
3. Run the tests with pytest:

```bash
   pytest -v
```

## 2. Online (No Local Setup)
### Option A: GitHub Codespaces
1. Open the repo in Codespaces (Code → Open with Codespaces).

2. In the terminal, run:
 ```bash
    pip install -r requirements.txt
    pytest -v
 ```
### Option B: Replit
1. Go to Replit.

2. Create a new Python project.

3. Upload test_sentiment.py and requirements.txt.

In the shell, run:
```bash
   pip install -r requirements.txt
   pytest -v
```
3. Expected Output
When tests pass, you’ll see something like:
```bash
   ============================= test session starts =============================
   collected 2 items

   test_sentiment.py::test_positive_sentiment PASSED
   test_sentiment.py::test_negative_sentiment PASSED
```

