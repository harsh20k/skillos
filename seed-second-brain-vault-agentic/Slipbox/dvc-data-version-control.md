---
date: 2026-04-13
tags: [dvc, data-versioning, mlops, reproducibility, pipelines, pixelsense]
---

# DVC — Data Version Control

DVC is a Git-based tool for versioning datasets, models, and ML pipelines. It tracks large files outside of Git (via remote storage) while keeping small `.dvc` pointer files in the repo — giving you full reproducibility without bloating your Git history.

## What DVC solves

- **Data versioning** — datasets and model weights are too large for Git; DVC stores them in remote storage (S3, GCS, Azure, SSH, local) and tracks them via pointers
- **Pipeline reproducibility** — `dvc.yaml` defines pipeline stages; `dvc.lock` locks exact inputs/outputs so any run can be reproduced exactly
- **Experiment tracking** — `dvc exp run` / `dvc exp show` lets you track hyperparameters and metrics across runs without a separate tool
- **Collaboration** — teammates pull data and models with `dvc pull`, just like `git pull`

## Core concepts

| Concept | File/Command | Purpose |
|---|---|---|
| Data pointer | `.dvc` file | Tracks a file/folder in remote storage |
| Pipeline | `dvc.yaml` | Defines stages: deps → cmd → outs |
| Lock file | `dvc.lock` | Freezes exact hashes of all stage I/O |
| Remote | `dvc remote add` | Where large files actually live (S3, etc.) |
| Cache | `.dvc/cache/` | Local content-addressable store |

## Where to use it in [[PixelSense]]

### 1. Raw data ingestion
```bash
dvc add data/raw/dataset.csv
git add data/raw/dataset.csv.dvc .gitignore
git commit -m "track raw dataset with DVC"
dvc push
```

### 2. Pipeline definition (`dvc.yaml`)
```yaml
stages:
  preprocess:
    cmd: python src/preprocess.py
    deps:
      - data/raw/dataset.csv
      - src/preprocess.py
    outs:
      - data/processed/clean.csv

  train:
    cmd: python src/train.py
    deps:
      - data/processed/clean.csv
      - src/train.py
    params:
      - params.yaml
    outs:
      - models/model.pkl
    metrics:
      - metrics/eval.json

  evaluate:
    cmd: python src/evaluate.py
    deps:
      - models/model.pkl
      - src/evaluate.py
    metrics:
      - metrics/report.json
```

### 3. Running & reproducing
```bash
dvc repro          # run only changed stages
dvc repro -f       # force rerun all stages
dvc dag            # visualize pipeline DAG
```

### 4. Experiment tracking
```bash
dvc exp run --set-param train.lr=0.01
dvc exp show       # compare runs in a table
dvc exp diff       # diff two experiments
```

### 5. Model versioning
```bash
dvc add models/model.pkl
dvc push
# Tag in Git to mark a model version:
git tag "model-v1.0"
```

## Key commands cheatsheet

```bash
# Setup
dvc init
dvc remote add -d myremote s3://my-bucket/pixelsense

# Daily workflow
dvc pull           # get latest data/models
dvc repro          # rerun changed pipeline stages
dvc push           # push new artifacts

# Inspection
dvc status         # what's changed vs cache
dvc dag            # show pipeline graph
dvc params diff    # compare params across commits
dvc metrics show   # display current metrics
dvc metrics diff   # compare metrics across commits
```

## Integration with Git

DVC is designed to work alongside Git:
- `.dvc` pointer files and `dvc.yaml` / `dvc.lock` → committed to Git
- Actual data/model files → stored in DVC remote
- Always commit `dvc.lock` after `dvc repro` to freeze the run

```bash
dvc repro
git add dvc.lock metrics/
git commit -m "train: lr=0.01, acc=0.94"
dvc push
```

## Edge deployment consideration

For edge deployment in PixelSense, use DVC to version quantized/exported models separately from training artifacts:
```bash
dvc add models/edge/model_quantized.onnx
```
This lets you track which training run produced which edge model.

## Related notes
- [[Version Control system(vcs)]]
- [[linear-github-integration]]
