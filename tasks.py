from invoke import task

@task
def run(c):
    c.run("pytest --log-cli-level=DEBUG > ./out.log 2>&1")
