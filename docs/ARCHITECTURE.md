# Architecture — AI Chatbot

## System Diagram

```

           +---------------+
           |  User Input  |
           +---------------+
                   |
                   |
                   v
           +---------------+
           |  NLP Model   |
           +---------------+
                   |
                   |
                   v
           +---------------+
           |  Response    |
           +---------------+
           
```

## Flow

**Step 1: Data Collection**
Collecting and preprocessing the dataset

**Step 2: Model Training**
Training the machine learning model using the collected dataset

**Step 3: Model Deployment**
Deploying the trained model in a production-ready environment

## Key Files

| File | Purpose |
|---|---|
| `app.py` | Main application file |
| `model.py` | Machine learning model definition |

## Tech Stack

- **Python**
- **TensorFlow**
- **NLTK**
