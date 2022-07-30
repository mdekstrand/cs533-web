# Software Environments

Throughout most of this class, we have been using packages installed in a single, global Python
environment; typically your base Anaconda environment.  This is useful for quickly working on
things, but it has a few drawbacks for doing data science work in practice:

-   Unless you take careful notes, you don't have a record of precisely what packages your project
    requires.  Even if you do take notes, you need to keep those notes up to date, and there are not
    good, reliable ways to check that it is.
-   All your projects share the same software installation, so if you update a package for one
    project, it updates it for all your projects.  If the update has incompatible changes, this can
    break your other projects.
-   It's hard for others to make sure they have the same software stack for collaborating with you
    or trying to reproduce your results.

The way to fix this is to use a separate software environment for each of your projects.  I have
been doing this all class, with software environments dedicated to the course web site and to the
course notebooks.  If you have used Python virtual environments in the past, the concept will be
familiar.

## Creating Conda Environments

[env]: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

Conda supports [*environments*][env], which are separate isolated sets of packages within your Conda
installation.

In my own data science work, each of my projects has its own Conda environment.

You can create a Conda environment with the `create` command:

    conda create -n cs533 python=3.8 pandas seaborn notebook

Once that environment is created, it doesn't do anything on its own; you have to first *activate* it.
The `activate` command in a Conda-enabled shell prompt switches your current Conda environment:

    conda activate cs533

This sets environment variables in your shell so that it looks for programs in your environment first,
so if you run `python` it will run the Python in your new environment.  For example:

```shell-session
michaelekstrand@abyss:~$ conda activate cs533
(cs533) michaelekstrand@abyss:~$ python
Python 3.9.6 (default, Aug 18 2021, 19:38:01)
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> print(sys.executable)
/home/MICHAELEKSTRAND/anaconda3/envs/cs533/bin/python
>>>
```

You can see that it ran the `python` executable in my `cs533` environment.  Each different environment
has a completely isolated Python installation along with all your packages — you can't accidentally use
a package only installed in one environment in a different environment.

One consequence of this is that Jupyter (`notebook` and/or `jupyterlab`) needs to be installed separately
in each of your sessions.

Your “primary” Conda installation is accessible as an environment called `base`.  Jupyter in your `base`
environment can create notebooks that use any of your installed environments, but I don't recommend
doing this — it bakes the environment name into your notebook file and hurts portability a little bit;
my practice is to run Jupyter from within my environment.

Once you have activated an environment, `conda install` and `conda update` will work in that environment.
Environments also include `pip` (at least if they have Python in them), so you can `pip install` and it
will install packages into the environment instead of the system or elsewhere.

You need to re-activate the environment every time you log in: `conda activate` only changes your current
shell session.

## Environment Maintenance and Cleanup

The `conda env` command (and its subcommands) allows you to inspect and clean up your environments.
To list all the environments you have created:

    conda env list

To delete an environment:

    conda env remove -n cs533

## Environment Specification Files

You can also write a file that specifies your environment's requirements and use it to create or update
environments.  You can then commit this file to `git` to include your project's software requirements
along with the project itself.

These files are written in YAML, typically called `environment.yml`, and look like this:

```yaml
name: cs533
channels: defaults
dependencies:
- python=3.8
- pandas>=1.0
- seaborn=0.11
- notebook
- scikit-learn>=1.0
```

With such a file, you can create the environment with `conda env create`:

    conda env create -f environment.yml

`conda env create` and `conda create` have similar purposes, but take different arguments; I usually use
`create` to create one-off ad-hoc environments, and `env create` for working with environment files.

You can also update an environment to make sure it meets the current requirements in a file:

    conda env update -f environment.yml

For a more advanced example, see my {download}`environment.yml` for the software we use in this
class; it's the same environment file I use in my private repository for demo and solution
notebooks.

## Alternative: Virtual Environments

Python provides its own environment system called *virtual environments*.  They aren't as flexible
as Conda environments for data science, because they can only manage Python packages while Conda
environments can manage any software installable with Conda (Python packages, R and its packages,
arbitrary command-line utilities, etc.), but they are useful in a number of situations.

To create a Python virtual environment, use `venv`:

    python -m venv cs533-env

Once you have created the environment, which is just a directory, you can *activate* it.  The syntax
varies from platform to platform, but on Linux and macOS it is:

    source cs533-env/bin/activate

On Windows PowerShell, it is:

    & cs533-env\Scripts\activate.ps1

Once your environment is activated, you can install packages with `pip`:

    pip install pandas seaborn notebook scikit-learn

### Requirements Files

`pip` also supports a file-based package specification system in the form of `requirements.txt` files.
These are simple text files that list package specifications, one per line, like so:

```
pandas>=1.0
seaborn
notebook
scikit-learn>=1.0
```

You can then install all packages, along with their dependencies, with:

    pip install -r requirements-txt

## Best Practices

All of my projects have an `environment.yml` file (or occasionally `requirements.txt`) checked in to
Git that I use to list the project's software requirements.  I also don't generally install packages
directly with `conda install` or `pip install`; rather, I add them to `environment.yml` and run
`conda env update`. This ensures that `environment.yml` contains *all* the packages I need.

From time to time, I also delete my environment and re-create it from `environment.yml`, and make
sure the project still works.  This provides a check that I haven't accidentally introduced new
dependencies that I forgot about.  For many of my projects, since I use [dvc][] to automate the
pipeline, I can usually re-run the entire experiment end-to-end in the new environment.

[dvc]: https://dvc.org
