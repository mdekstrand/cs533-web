# Git Resources

I recommend signing up for the [GitHub Student Developer Pack](https://education.github.com/pack).

## Initial Setup

If you have never used Git before, you need to configure your user identity.  Run the following commands:

    git config --global user.email you@domain.com
    git config --global user.name "Your Name"

## Git Interfaces

- [Tower](https://www.git-tower.com/) (avialable free with Student Pack)
- [GitKraken](https://www.gitkraken.com/) (available free with Student Pack)

## Example `.gitignore`

This is a good starting point for a `.gitignore` file for Python data science projects.
Put its contents in a file called `.gitignore` in your repository.

```conf
.DS_Store/
# Ignore editor directories & files
.vscode/
.idea/
*~
*.swp
*.bak

# Ignore Python cache & output
__pycache__/
*.pyc
*.pyo

# Ignore IPynb test dirs
.ipynb_checkpoints/

# generic log and output files
*.log
*.out
*.prof
*.lprof

# Python environments for CodeSpaces
pythonenv*/
```

Even if I have things like `.DS_Store/` in my personal ignore file, I include them in the project, in case collaborators do not.
Lines starting with `#` are comments.

### Personal `.gitignore`

If you want to create a personal gitignore file, do the following:

-   Put your ignore rules in `~/.gitignore` (a file called `.gitignore` in your home directory)
-   Modify `~/.gitconfig` to include the following lines:

        [core]
            excludesfile = ~/.gitignore
