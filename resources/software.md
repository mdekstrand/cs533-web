# Software and Installation

Most of the software you will need is available through Anaconda, a distribution of scientific
software for Python (and R). It is the easiest way to install Python with the packages we need. The
one additional piece of software we will need is Git.

We are using **Python 3.8** (or newer — Python 3.9 or 3.10 is fine) in this
class.  Older versions of Python may work, but I will be testing my example code
and instructions with Python 3.8.

:::{ltip} Department Computers
If you want to use the department's computer lab for your work, see the [Onyx setup instructions](onyx-install) as well
as the instructions for [remotely using Onyx](onyx.md).
:::

[VSC]: http://code.visualstudio.com/

## Required Software

Our primary software is:

-  [Anaconda Python](https://www.anaconda.com/distribution/)

:::{tip}
The main Anaconda distribution includes all software we will be using
except the `plotnine` Python package and [git](install-git). If you are using
your own computer, and you don't know what else to do, [install
Anaconda](install-anaconda) and you will be good to go.
:::

If you are using the department's Onyx computers to complete your assignment, you will need:

-  An SSH client (MobaXterm for Windows, `ssh` on Mac or Linux)
-  The [Boise State VPN](https://bsuvpn-offcampus.boisestate.edu/) for convenient access to Onyx nodes
-  Install Anaconda Python in your Onyx home directory, following the Linux instructions.

For building more advanced workflows, there are many text editors you can use.
I use [Visual Studio Code][VSC], which has very good [remote editing support](https://code.visualstudio.com/docs/remote/remote-overview)
and also directly supports Jupyter notebooks (although I do not use this feature much).

The rest of this document walks through some details.

## About Conda

Anaconda (and Miniconda, described at the end of this document) is a scientific
software distribution. That is, it is a collection of software such as Python,
Jupyter, and Pandas for supporting scientific computation.  It is built around
the Conda package manager, which it uses to actually install the software.

Conda installs precompiled binary versions of software, including but not limited to Python
packages. The versions of Scientific Python software distributed through Conda are compiled against
more optimized versions of the core math libraries than the packages available through standard
Python channels (the Python Package Index).

When you are looking online for instructions for Python software, it will usually tell you to
install it with `pip`. However, since we are using Conda, it works better to install the Conda
version of a package (with `conda`) if possible. It will usually, but not always, have the same name
as the Python package. You can search for Conda packages on [anaconda.org](https://anaconda.org).

(install-anaconda)=
## Installing Anaconda Python

:::{tip}
If you don't know what to do, and are working on your own computer, do this.
:::

To install Anaconda on your computer:

1.  Download the appropriate installer for your platform from [Anaconda Python](https://www.anaconda.com/distribution/).

    If your computer has a 64-bit operating system (most do, *except* for Windows on ARM platforms like the Surface X),
    download the 64-bit version of Anaconda.  Make sure you get the Python 3 verision (it is the default).

2.  Run the installer.  On **macOS** and **Windows**, the installer is a normal
    installer that you can run by double-clicking.  On **Linux** it is a shell
    script, which you can run with the following command in your terminal:

        /bin/bash Anaconda3-2022.05-Linux-x86_64.sh

    Replace the file name with the name of the installer file you downloaded.

3.  Install the additional packages we need by running the following at terminal
    (normal terminal on macOS and Linux, an “Anaconda Prompt” on Windows):

        conda install -c conda-forge plotnine

(miniconda)=
## Saving Space with Miniconda

We don't need all of Anaconda.  If you want to save disk space, [Miniconda][] is a much smaller
distribution that just contains Python and the Conda package manager, so you can install the
packages you need yourself.

[miniconda]: https://docs.conda.io/en/latest/miniconda.html
[miniforge]: https://github.com/conda-forge/miniforge

1.  [Download the installer][miniconda] for your platform and run it.

2.  Install the base packages we will need:

        conda install -c conda-forge pandas scipy scikit-learn notebook ipython \
            seaborn statsmodels plotnine

## Installing Additional Packages

If you need to install additional packages, I recommend using `conda` to install
the Conda packages, when they are available. The name usually, but not always,
matches the name in PyPI (used by `pip`).  If a package is available in Conda,
any binary components are pre-compiled (so you don't need a working C compiler)
and are usually more optimized than the precompiled wheels available via `pip`.
You can search Conda packages at [anaconda.org](https://anaconda.org/); the
`main` channel contains the packages available through the default Anaconda or
Miniconda installation, and the `conda-forge` channel is a community-maintained
repository of packages that has most of what's in `main` along with many
packages not yet in the main repository.  `plotnine` is only (currently)
available in `conda-forge`, but packages can usually be mixed and matched, so
you can install it in a default environment.

It is fine to use `pip` to install packages that are not available in Conda.  It
also works to use it to install packages that are, but I do not recommend this,
particularly for core compute packages such as `numpy`, `scipy`, and
`scikit-learn` — the versions in Conda are more optimized.

:::{note} `conda-forge`
I personally just use the `conda-forge` channel for all of my Anaconda environments, but the
primary installers default to main.
:::

### seedbank

I use {py:mod}`seedbank` in many of my examples for seeding the random number generator. Seedbank is not currently available through the main Anaconda channel, so you will need
to install it with `pip`:

    pip install seedbank

Do this *after* installing your other packages with `conda`, so seedbank doesn't try to pull in a non-Conda NumPy.

(install-git)=
## Installing Git and Command-Line Tools

We will be using Git later in the semester.

To install Git, the instructions differ based on your platform:

-   On Windows, [download and run the installer](https://git-scm.com/).
-   On macOS, install Xcode from the App Store.
-   On Linux, install `git` from your package manager.

(onyx-install)=
## Installing on Onyx

Unlike a lot of other software, Anaconda is designed to be installed separately by each user.

To setup on Anaconda on Onyx, you need to download the installer and run it on Onyx (or an Onyx node).
Once you have set it up on any Onyx node, it will be available across Onyx, no matter which node you log in to.
Due to Onyx's network file system performance, I recommend using Miniconda.

You can do this with:

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    /bin/bash Miniconda3-latest-Linux-x86_64.sh
    rm Miniconda3*.sh

This will install Miniconda (which by default will also configure your shell to activate the Miniconda environment).
Log out and log back in to Onyx and Conda will be active.
Install the base packages:

    conda install pandas scipy scikit-learn notebook ipython \
            seaborn statsmodels

Onyx already has Git installed.

## Using Anaconda

On Linux and Mac, the installer will, by default, modify your Bash startup scripts to activate Anaconda.

On Windows, it will install a separate ‘Anaconda Prompt’ and ‘Anaconda PowerShell’ that you can use from the start menu.

