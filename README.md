# testing-docbuilder

## Install requirements
```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    # install documentation js examples
    git clone https://git.onlyoffice.com/ONLYOFFICE/office-js-api.git
```

## Install portable docbuilder
```bash
    invoke portable_docbuilder
```

## Run tests
## only with console stdout
```bash
    invoke run-tests
```
## with stdout to out.log
```bash
    invoke run-tests-outlog
```
## with making csv report
```bash
    invoke run-tests-csv
```
