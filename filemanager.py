import os

import click


def filenamefixer(filename):
    if "'" in filename:
        filename.replace("'", "\'")
    return filename


@click.command()
@click.argument("path", default=".", type=click.Path(exists=True, dir_okay=True, file_okay=False))
def run(path):
    if os.name == "nt":
        files = os.popen("dir /b /a-d").read().split("\n")
    elif os.name == "posix":
        files = os.popen("find -maxdepth 1").read().split("\n")

    ext = set([x.split(".")[::-1][0] for x in files if "." in x])
    extensions = [x for x in ext if not x.isupper() and len(x) != 0 and not x.isnumeric()]

    for ex in extensions:
        os.system("mkdir " + ex)
        thisFiles = [f for f in files if f.endswith(ex)]

        for f in thisFiles:
            f = filenamefixer(f)
            if os.name == "nt":
                move = 'move "{}" {}'.format(f, ex)
            elif os.name == "posix":
                move = "mv '{}' ./{}".format(f, ex)
            os.system(move)
