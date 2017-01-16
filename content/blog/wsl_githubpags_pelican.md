Title: Using GitHub Pages and Pelican in Ubuntu on Windows
Date: 2017-01-14
Category: Blog
Tags: pelican, wsl, git, github
Slug: githubpages-pelican-in-wsl
Authors: Matthew Kapfhammer
Summary: Quickly create a webpage with Pelican and GitHub Pages on Windows.

# Context

**TL;DR:** I had a Wordpress site, stopped using it, and wanted something simpler instead.

I've had a website for blogging, CV, and portfolio needs since 2005 or so. In late 2010, life went into high gear. I didn't have much time or need to work on my website, partly because LinkedIn and IMDB covered my CV needs. In addition, I became disenchanted with Wordpress over the years due to its many security issues and the various complexities inherent to a dynmaic website's design. Basically, it was overkill for what I needed. As a result, lookslikematt.com only got security updates and didn't see any content updates after early 2011. 

Over the next few years, I ended up working with Git and several Python based web frameworks. I grew to enjoy what Git provides and what Flask and Bottle can do with very little code. I also started following the development of GitHub pages. At some point, I looked back at my website and knew I needed to make some changes. That eventually led me to settle on some combination of [GitHub Pages](https://pages.github.com/) and a [static website generator](https://www.smashingmagazine.com/2015/11/modern-static-website-generators-next-big-thing/). 

During the last year, I've been using the Windows Subsystem for Linux in order to run "Bash on Ubuntu on Windows" and have been really enjoying it for quickly doing filesystem related tasks. Since it's still beta, I've been reluctant to try it out for any development work. 

But it's 2017 now. Let's see what amd how quickly the combination of the WSL, GitHub Pages, and Pelican can get me what I'm after.

# Getting Started

## Outline
1. Follow this guide: https://msdn.microsoft.com/en-us/commandline/wsl/install_guide.
    1. ~10 mins
1. Create a new repo on GitHub with the expected naming convention, clone it.
    1. ~2 mins
1. Follow this guide: http://docs.getpelican.com/en/stable/quickstart.html.
    1. ~2 mins
1. Update with basic user content.
    1. ~15+ mins (longer if you want to further customize)
1. Push changes to GitHub to deploy the new website.
    1. ~2 mins

## Installing WSL

This was very simple for me as I was on a high enough build, have a fast internet connection, and had gone through the installation process before. Even if for a first time experience, I would still only expect it to take about 15 minutes.

## Create a New Repo on GitHub

Also very simple. Naming convention for the new repo is: ```$GITHUB_USERNAME.github.io```.

## Pelican 

### Installation
Launch a Bash terminal typing the following in the Windows start up area and clicking on the resulting orange and white icon: ```Bash on Ubuntu on Windows```. Note that to paste into the Bash shell, you'll need to use the right mouse button istead of ctrl+v or the middle mouse button.

In Bash, I like to use ```tree``` and ```git``` is essential:
```bash
sudo apt-get install tree
sudo apt-get install git
```

WSL ships with Pyhon 2.7.6. You'll need to install pip: https://docs.python.org/2/installing/#install-pip-in-versions-of-python-prior-to-python-2-7-9. 
```bash
sudo apt-get install python-pip
```

I took the additional step of installing virtualenv and using a virtual environment:
```bash
sudo pip install virtualenv
```

Create a new virtualenv to work in and enter it:
```bash
cd $YOUR_GOT_REPO_ROOT_DIR
virtualenv ./venv
source venv/bin/activate
```

### Pelican Quickstart

Install Pelican and ghp-import. The Pelican command might look a little odd, but it gives you both Pelican and Markdown in one go:
```bash
(venv) pip install pelican markdown
(venv) pip install ghp-import
```

At this point, it's a good idea to create a requirements.txt file, just in case some time passes and you need to rebuild your virtual env with the exact same versions of the libraries.
```bash
(venv) pip freeze > requirements.txt
```

Let's also commit it before moving forward:
```bash
(venv) git add -A
(venv) git commit -m "Adds virtual env requirements file."
```

Follow quickstart:
```bash
(venv) pelican-quickstart
> Where do you want to create your new web site? [.]
> What will be the title of this web site? Matthew Kapfhammer
> Who will be the author of this web site? Matthew Kapfhammer
> What will be the default language of this web site? [en]
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) n
> Do you want to enable article pagination? (Y/n) y
> How many articles per page do you want? [10]
> What is your time zone? [Europe/Paris] US/Pacific
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) y
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) y
> Do you want to upload your website using FTP? (y/N) n
> Do you want to upload your website using SSH? (y/N) n
> Do you want to upload your website using Dropbox? (y/N) n
> Do you want to upload your website using S3? (y/N) n
> Do you want to upload your website using Rackspace Cloud Files? (y/N) n
> Do you want to upload your website using GitHub Pages? (y/N) y
> Is this your personal page (username.github.io)? (y/N) y
```

Generate content based on .md files in ./content:
```bash
(venv) pelican content
```

Open a new Bash terminal and start the dev server:
```bash
cd $YOUR_GOT_REPO_ROOT_DIR
source venv/bin/activate
(venv) ./develop_server.sh start
```

Check the site in browser at [http://localhost:8000/](http://localhost:8000/). 

Now that's it working, let's stop the server and commit again before updating. Note that GitHub's .gitignore file already ignored the venv dir and all the .pyc files. While we won't be commiting the output dir right now, we won't ignore it either since we'll want to add it when we deploy.
```bash
(venv) ./develop_server.sh stop
git add Makefile develop_server.sh fabfile.py pelicanconf.py publishconf.py
git commit -m "Adds quickstart files."
```

## Update with Basic User Content

The ```develop_server.sh``` script auto-reloads while making changes, so let's turn that back on in order to get updates as we save our text files.
```bash
(venv) ./develop_server.sh stop
```

### Add the About Page

This required adding sub-directories to content and modifying ```pelicanconf.py``` again to update the menu.
```
├── content
│   ├── blog
│   └── pages
│       └── about.md
```

Add to ```pelicanconf.py```:
```python
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('About', '/about'),
    ('Blog', '/'),
)
```

### Add the First Article

I added another .md file under ```./content/blog```. You can see an example of what to add [in the quickstart](http://docs.getpelican.com/en/stable/quickstart.html#create-an-article).

### Config: Automate Getting Year 

It's not necessary, but is helpful to let code handle populating the date by adding this to ```pelicanconf.py```:
```python
import time
COPYRIGHT_YEAR = time.strftime("%Y")
```

### Review

We have just enough going now to publish some blog articles, which was the intended goal. I plan on later doing a follow-up post on updating the theme, adding a few more pages, and then customizing the look, etc. But for now, we're good to commit and move on to deploying!

```bash
git add content pelicanconf.py
git commit -m "Adds basic user content."
```

## Deploy New Site

Again, very simple. You just [run a few commands and you're done](http://docs.getpelican.com/en/stable/tips.html#user-pages).

```bash
pelican content -o output -s pelicanconf.py
ghp-import output
git push git@github.com:$GITHUB_USERNAME/$GITHUB_USERNAME.github.io.git gh-pages:master
```

# Notes

## Warnings

### Commit with Unix Style Line Endings
If you decide to commit with git gui launched from the Windows Explorer at any point, you need to commit with unix style line endings. Otherwise when you eventually checkout or pull again, you'll get errors if you try to run any of the bash scripts.

## More Reading

I highly recommend making some time to [read the Pelican manual](https://media.readthedocs.org/pdf/pelican/3.3.0/pelican.pdf). It's well written and easier to skim than the website.

# Conclusions

At the this point, I'm feeling pretty proud of myself for doing little to nothing. Most of my time was spent researching and comparing my options. 

Github Pages makes hosting dead simple and updating quick.

It feels like the styling choices for the headings in the default theme make it difficult to skim. This is a problem for me. Looking forward to adding a new theme!
