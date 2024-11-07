### Daten  
GermanQuAD: High-Quality German QA Dataset   
https://www.kaggle.com/datasets/thedevastator/germanquad-high-quality-german-qa-dataset

- befinden sich im `data` Ordner
- `to_<...>.py` ändert das Format (z.b. Spaltennamen) passend für promptfoo
- in promptfoo config können sie dann mittels  
`tests: file://data/tests_qanda_lazy_context.csv`  
eingebunden werden

### Allgemein

There are 3 parts:

1. `retrieve_context.py`: provider that returns rag chunks spezific to a question.

1. `retrieve_<llm_name>.py`: provider that answers prompts (can be enriched with additional context).

1. `tests_<...>.yaml`: Test config.

To get started:

1. Create a python virtual environment: `python3 -m venv venv`

1. Enter the environment: `source venv/bin/activate`

1. Install python dependencies: `pip install -r requirements.txt`

Now we're ready to go.

- Edit `tests_<...>.yaml` to your liking to configure the questions you'd like to ask in your tests.
- Edit `retrieve_<...>.py` to control how context is loaded and questions are answered.

Example
```
promptfoo eval --config .\tests_rag.yaml
```

Afterwards, you can view the results by running `promptfoo view`


### Notizen
promptfoo collects basic anonymous telemetry by default. This telemetry helps us decide how to spend time on development.  
To disable telemetry, set the following environment variable:  
PROMPTFOO_DISABLE_TELEMETRY=1  
https://www.promptfoo.dev/docs/configuration/telemetry/
