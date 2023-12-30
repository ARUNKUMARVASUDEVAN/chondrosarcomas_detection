#  Chondrosarcomas_detection

## Workflows

```
1. Update config.yaml
```
```
2.Update secrets.yaml[Optional]
```
```
3.Update the params.yaml
```

```
4.Update the entity
```

```
5.update the configuration manager in src config

```
```
6.Update the components
```
```
7.Update the pipeline
```
```
8.Update the main.py

```

```
9.Update the dvc.yaml
```  


### MLflow
 -Documentation

 -MLflow tutorial

#### cmd
 -mlflow ui
### dagshub

[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/ARUNKUMARVASUDEVAN/chondrosarcomas_detection.mlflow \
MLFLOW_TRACKING_USERNAME=ARUNKUMARVASUDEVAN \
MLFLOW_TRACKING_PASSWORD=6f568c435c7857cb506b6f321d9d952e359dd833 
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/ARUNKUMARVASUDEVAN/chondrosarcomas_detection.mlflow

export MLFLOW_TRACKING_USERNAME=ARUNKUMARVASUDEVAN

export MLFLOW_TRACKING_PASSWORD=6f568c435c7857cb506b6f321d9d952e359dd833

```