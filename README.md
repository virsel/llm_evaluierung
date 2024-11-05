### Daten  
GermanQuAD: High-Quality German QA Dataset   
https://www.kaggle.com/datasets/thedevastator/germanquad-high-quality-german-qa-dataset

### Allgemein

This RAG example allows you to ask questions over a number of public company SEC filings. It uses LangChain, but the flow is representative of any RAG solution.

There are 3 parts:

1. `ingest.py`: Chunks and loads PDFs into a vector database with llama3.2:3b (PDFs are pulled from a public Google Cloud bucket)

1. `retrieve.py`: Promptfoo-compatible provider that answers RAG questions using the database.

1. `promptfooconfig.yaml`: Test inputs and requirements.

To get started:

1. Create a python virtual environment: `python3 -m venv venv`

1. Enter the environment: `source venv/bin/activate`

1. Install python dependencies: `pip install -r requirements.txt`

1. Run `ingest.py` to create the vector database: `python ingest.py`

Now we're ready to go.

- Edit `promptfooconfig.yaml` to your liking to configure the questions you'd like to ask in your tests. Then run:
- Edit `retrieve.py` to control how context is loaded and questions are answered.

```
promptfoo eval
promptfoo eval --config .\tests_prompts.yaml
promptfoo eval --config .\tests_rag.yaml
promptfoo eval --config .\tests_llms.yaml
```

Afterwards, you can view the results by running `promptfoo view`

See `promptfooconfig.with-asserts.yaml` for a more complete example that compares the performance of two RAG configurations.

### Notizen
promptfoo collects basic anonymous telemetry by default. This telemetry helps us decide how to spend time on development.  
To disable telemetry, set the following environment variable:  
PROMPTFOO_DISABLE_TELEMETRY=1  
https://www.promptfoo.dev/docs/configuration/telemetry/
