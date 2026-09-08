# DVC Workflow

DVC was used to track and version the Iris dataset.

Remote Storage:
~/dvc-remote-storage

Workflow:
dvc add → git add → git commit → dvc push

Version 1:
150 rows

Version 2:
170 rows

Dataset comparison:
dvc diff 31c37bc

Version 1 was restored using:
git checkout 31c37bc -- data/raw/iris_v1.csv.dvc
dvc checkout data/raw/iris_v1.csv.dvc

Version 2 was restored using:
git checkout HEAD -- data/raw/iris_v1.csv.dvc
dvc checkout data/raw/iris_v1.csv.dvc