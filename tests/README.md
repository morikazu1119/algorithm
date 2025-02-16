ローカル環境でpytest実行時に必要な設定
```
$env:PYTHONPATH = "{pwd};" + $env:PYTHONPATH
pytest -s
```