# matthewkapfhammer.github.io
Static site content for matthewkapfhammer.github.io.

## Working

### Regenerate virtual environement
```
cd $YOUR_GOT_REPO_ROOT_DIR
virtualenv ./venv
source venv/bin/activate
(venv) pip install -r requirements.txt
```

## Deploying
When finished working in the pelican branch, commit, and push it. 

Then run:
```bash
pelican content -o output -s pelicanconf.py
ghp-import output
git push git@github.com:matthewkapfhammer/matthewkapfhammer.github.io.git gh-pages:master
```

## GitHub and Pelican Notes
GitHub:
- https://pages.github.com/
Pelican:
- https://media.readthedocs.org/pdf/pelican/3.3.0/pelican.pdf
- http://docs.getpelican.com/en/stable/tips.html?highlight=ghp-import
- https://appliedcaffeine.org/navbaritems.html
- http://stackoverflow.com/questions/26805232/python-pelican-order-menu-items
Pelican Themes:
- https://blog.alexandrevicenzi.com/flex-pelican-theme.html

## Misc Notes

### Initial gh-pages branch won't push
Error:
```bash
$ git push git@github.com:matthewkapfhammer/matthewkapfhammer.github.io.git gh-pages:master
To github.com:matthewkapfhammer/matthewkapfhammer.github.io.git
 ! [rejected]        gh-pages -> master (non-fast-forward)
error: failed to push some refs to 'git@github.com:matthewkapfhammer/matthewkapfhammer.github.io.git'
hint: Updates were rejected because a pushed branch tip is behind its remote
hint: counterpart. Check out this branch and integrate the remote changes
hint: (e.g. 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```
Fix by ignoring gh-pages history and merging with master:
- http://stackoverflow.com/questions/37937984/git-refusing-to-merge-unrelated-histories
```bash
git pull origin master --allow-unrelated-histories
git push git@github.com:matthewkapfhammer/matthewkapfhammer.github.io.git gh-pages:master
```

### Troubleshooting Python Installs
Get site packages location.
```python
>>> import site; site.getsitepackages()
```

Get python executable location.
```python
>>> import sys; sys.executable
```