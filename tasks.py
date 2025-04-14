from invoke import task

@task
def run(c):
    c.run("pytest --log-cli-level=DEBUG > ./out.log 2>&1")

@task
def portable_docbuilder(c):
    c.run("python download.py")
