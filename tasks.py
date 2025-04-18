from invoke import task

PYTEST_RUN_COMMAND = 'pytest tests -n auto --tb=native'

@task
def portable_docbuilder(c):
    c.run("python download.py")

@task
def run_tests(c):
    c.run(PYTEST_RUN_COMMAND)

@task
def run_tests_outlog(c):
    c.run(f'{PYTEST_RUN_COMMAND} --log-cli-level=DEBUG > ./out.log 2>&1')

@task
def run_tests_csv(c):
    c.run(f'{PYTEST_RUN_COMMAND} --csv tests.csv --csv-columns host,function,status,duration,parameters_as_columns')
