from invoke import task

@task
def run(c):
    c.run("pytest -n auto --log-cli-level=DEBUG > ./out.log 2>&1")

@task
def portable_docbuilder(c):
    c.run("python download.py")

@task
def csv(c):
    c.run("py.test --csv tests.csv --csv-columns host,function,status,duration,parameters_as_columns")
