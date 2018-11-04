# FastCosine

FastCosine은 sparse vector로 표현되는 데이터에 대하여 최인접이웃을 근사적으로 빠르게 찾기 위한 인덱서로, inverted index를 기반으로 만들어졌습니다. 

Approximated nearest neighbor search indexer for sparse vector. It is based on inverted index

## Setup

    pip install fastcosine

## Usage

Set your input mm file path and model prefix

```python
from fastcosine import FastCosine

mm_file = ''      # Fill your file
model_prefix = '' # Fill your file
```

Insert mm file path for indexing

```python
fast_cosine = FastCosine()
fast_cosine.indexing(mm_file)
```

Save indexed model

```python
fast_cosine.save(model_prefix)
```

If you want to load indexed model, use load

```python
loaded_fast_cosine = FastCosine()
loaded_fast_cosine.load(model_prefix)
```

Format of query vector is dict.

```python
query={1:0.3, 10:0.2, 783:0.1, 3322:0.1}
query = {t:v/sum(query.values()) for t,v in query.items()}

neighbors, info = fast_cosine.kneighbors(
    query, compute_true_cosine=True,
    remain_tfidf_threshold=0.2,
    max_weight_factor=0.2,
    scoring_by_adding=False
)
```

Form of `neighbors` is list of tuple; [(idx, cosine similarity), ... ]

```python
from pprint import pprint
pprint(neighbors)
```

    [(3142770, 0.6991051639009617),
     (13749445, 0.6991051639009617),
     (10270855, 0.6991051639009617),
     (1290238, 0.5899354514246596),
     (10783376, 0.4943420021569027),
     (7734529, 0.4943420021569027),
     (10305110, 0.4943420021569027),
     (9504266, 0.4943420021569027),
     (4070535, 0.4943420021569027),
     (10239565, 0.4943420021569027)]

Processing details are described in `info`

```python
pprint(info)
```

    {'calculated_percentage': 1.0,
     'n_candidate': 121,
     'n_computation': 121,
     'n_considered_terms': 4,
     'n_terms_in_query': 4,
     'time [mil.sec]': {
             'check_query_type': 0.016689300537109375,
             'order_search_term': 0.009298324584960938,
             'retrieval_similars': 0.13256072998046875,
             'true_cosine_computation': 0.031232833862304688,
             'whole_querying_process': 0.18978118896484375
         }
    }

## Requires

- nothing
