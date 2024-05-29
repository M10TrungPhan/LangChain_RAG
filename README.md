# LangChain_RAG

## Setup

Download models: vncorenlp (https://github.com/vncorenlp/VnCoreNLP), vinai/phobert-base-v2 (https://huggingface.co/vinai/phobert-base-v2), vinai/bartpho-word (https://huggingface.co/vinai/bartpho-word/tree/main)

All models are saved in **`/app/api/models/`**

### Build image for services

```
docker compose build
```

## RUN SERVICE WITH DOCKER
### Cofig environment in .env-example 

```
cp .env-example .env


```
### Run docker
```
docker compose up -d
```
###  Define model use
1. Embedding models

    * Embedding models, and function to use it will define in the begining of file **`/app/api/llm.py`** 
    * Each model need to have different function to use because of different approach interference 
    * Edit fucntion apply of embbeding model in file **`/app/api/helpers.py`** (line 382) and file  **`/app/api/llm.py`** (line 170)
    * Each model has different approach get token count => Define function get_token_count of model in **`/app/api/llm.py`** 
    * Edit fucntion count token  of embbeding model in file **`/app/api/helpers.py`** (line 396) and file  **`/app/api/llm.py`** (line 170)
2. Answer generated models


### Create database, table in posgres
After container is running, build database and import data to table
```
docker compose exec api bash
export DB_PORT=5432

python models.py                        # Build database, tables and function
        
python seed.py                          # Import data to tables
```

#### Note:
> Data can storaged in directory **`/app/api/data/training_data/`**


   

## SCRIPT EVALUATE COMPONENT IN RAG PIPELINE

All script save in directory **/scripts/**

Install library in *`requirement_dev.txt`*

### Evaluate embbeding model
* Use `evaluate_embeddings_rag.ipynb` file. It is desgined to test embbeding model in RAG pipeline. Use question dataset -> embedd its question -> use  its embedding vector to query  the most similar document in postgres.


### Evaluate answer generated model
* Use `evaluate_answer_generated_rag.py` file.

