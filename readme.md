# testing-docbuilder

## Requirements for Project

* python3
* pip
* venv
* git

## Install

```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    # install documentation js examples
    git clone https://git.onlyoffice.com/ONLYOFFICE/office-js-api.git
    invoke --list
    invoke portable_docbuilder
    invoke run
```
