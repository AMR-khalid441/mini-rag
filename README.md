# mini - rag 
This is the minimal impelementation of the RAG model for question answering 


## Requirements

- Python 3.8 or Later

### install Python using miniConda

1) Dowanload miniConda from [here] 

2) Create a new environment using the following command :

```bash 
$ conda create -n mini-rag python=3.8

```
3) Activate the following environment :
```bash

$ conda activate mini-rag
```


# install backages

```bash
$ pip install -r requirements.txt
```

## setup the environment variables

```bash
$ cp .env.example.env
```

set your environment variables like `.env` file. like `OPENAI_API_KEY` value.    


# Run uvicorn for production

```bash
$ uvicorn main:app
```

#### Run uvicorn optimized for development only 

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000

```