from invoke import task

@task
def portable_docbuilder(c):
    c.run("python download.py")

@task
def run_tests(c):
    c.run("pytest tests -n auto --tb=native")

@task
def run_tests_outlog(c):
    c.run("pytest tests -n auto --tb=native --log-cli-level=DEBUG > ./out.log 2>&1")

@task
def run_tests_csv(c):
    c.run("pytest tests --csv tests.csv --tb=native --csv-columns host,function,status,duration,parameters_as_columns")
