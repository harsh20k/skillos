---
creation date: 2025-10-16 09:39
tags: [concept]
share_link: https://share.note.sx/8pyggcid#T6jIYl5SV290qR8rnNPQhHSAQv1y3tAfZWn8ZxnLI4I
share_updated: 2025-11-08T22:16:57-04:00
dg-publish: true
---
[[git-branch-naming-and-commit-conventions]]
[[linear-github-integration]]
# Commands

---
## For creating new ssh keys for this machine.

```bash
ssh-keygen
```

## To list all the SSH keys in the SSH agent.

```bash
ls -la ~/.ssh;
```

## If the key is not present in the SSH agent.

```bash
ls -la ~/.ssh;
```

## If ssh keys are present and still its asking for username password. 

## **HTTPS vs SSH** remote 

```bash
git remote -v  # Remote should be set as ssh starting with git@... not https
```

This will give **"The agent has no identities"**.

## Then we need to add the generated keys to SSH agent. 

```bash
ssh-add --apple-use-keychain "path to keys" 
```

```bash
ssh-add --apple-use-keychain 5308project
```


## Global User Email

```bash
git config --global user.email
```

This will give the global user email-id for this machine.

## To change it for current repo

```bash
git config user.email vn328490@dal.ca
```

This will print the current repo's email address. 

```bash
git config user.email
```

## Remote repository link

Give the URL's of repositories where to fetch from or push to. 

Which is stored in "**Origin**" variable 

![[image-37.png]]

```bash
git remote -v
```

---
## Branch the repo 

```bash
git branch your-branch-name #creates branch from the current branch
git checkout your-branch-name #switches to that branch
git checkout -b your-branch-name #creates and switches to the branch

git checkout -b your-branch-name main #branches from main branch
```

## How to push local changes to remote repo. 

```bash
git add .   #This adds the changes to the stagin area.
git status  #Will show that file is staged
git restore --staged filename    #Will unstage the file
git commit -m "modified README"    #Will commit changes to local.
git push origin main    #Will push the changes to the remote repo.
git push -u origin harshp #Will push the changes to harshp and set it as default upstream repo

#In the future we could specify git push and it will directly push to harshp branch of the remote repostory.
```

## Change Email for past commits

```bash
pip install git-filter-repo 

git filter-repo --email-callback '
if email == b"old@gmail.com":  
    return b"new@gmail.com"
return email
' --force

git remote add origin $repolink$

git push --force --tags origin main
```

## Git log 

```bash
git log    #Display the repostitory complete commit history 
git log --graph    #Graphcally show the commits with branches etc. 
git log --oneline    #Condenses the commit in one line.

git branch -D 'branchname' # To forece delete a branch
```

# Git checkout other branch

```bash
# Fetch latest branches from remote
git fetch origin

# Switch to Home-Page branch
git checkout Home-Page

# Create a new branch from Home-Page
git checkout -b friend-branch-name
```

## Commit messages semantics

[Source](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)

> [!Note] Commit message 
> More Examples:
> - `feat`: (new feature for the user, not a new feature for build script)
> - `fix`: (bug fix for the user, not a fix to a build script)
> - `docs`: (changes to the documentation)
> - `style`: (formatting, missing semi colons, etc; no production code change)
> - `refactor`: (refactoring production code, eg. renaming a variable)
> - `test`: (adding missing tests, refactoring tests; no production code change)
> - `chore`: (updating grunt tasks etc; no production code change)
>  

To delete the last commit in Git, you typically use either `git reset` or `git revert`, depending on whether you want to erase the commit from history or undo its changes safely. The most common method is:


# Removing the Last Commit (Unpushed)
If you want to completely remove the last commit and keep the changes staged:
```bash
git reset --soft HEAD~1
```
- This deletes the last commit but leaves its changes staged in your working directory.

If you want to delete the last commit and also discard its changes:
```bash
git reset --hard HEAD~1
```
- This erases both the commit and its changes from your history and working directory.

### Undoing a Pushed Commit
If you have already pushed the commit to a remote (like GitHub) and want to undo it for everyone:
- **Force push:** You must force push the new state:

```bash
git reset --hard HEAD~1
git push origin main --force
```
- **Warning:** This rewrites history and should only be used if you are certain no one else is working on the same branch.

### Safely Reverting a Commit
If you want to reverse the effects (but not erase history):
```bash
git revert HEAD
```
- This creates a new commit that undoes the changes made in the previous commit and is safe for shared branches.

***

# Summary Table

| Method                        | Description                               | Command                                      |
|-------------------------------|-------------------------------------------|----------------------------------------------|
| Remove locally (keep changes) | Delete commit, keep changes staged        | `git reset --soft HEAD~1`             |
| Remove locally (discard)      | Delete commit and changes                 | `git reset --hard HEAD~1`             |
| Undo on remote (rewrite)      | Force remove commit from remote           | `git reset --hard HEAD~1; git push --force`  |
| Safe undo (shared branch)     | Create a new commit reversing last        | `git revert HEAD`                     |

# Git command to stage, commit and push all in one!

```bash
git add . && git commit -m "green with is overdue complete " && git push origin
```

# File/line ownership 

```bash
git log --path/to/file.   # commit history of file
git blame path/to/file.   # line by line atuthorship info
```
# Git get latest changes from remote

```bash
git pull origin main

git clean -fd     #remove untracked files that will prevent you to pull

rm flask_app/__pycache__/__init__.cpython-310.pyc # remove specific untracked file

```

# Merge current branch to Main

```bash
git checkout main  # main branch first
git pull origin main 

git merge your-branch-name
git push origin main 
```

# Check last commit on main 

```bash
git checkout main
git log --oneline -1
```

# Deployment to VM

### Host: db-5308.cs.dal.ca

### student@csci5308-vm1.research.cs.dal.ca

### Password: Pohcoo5tig

|     | Type       | DB NAME               | USER                       | PASSWORD   |
| --- | ---------- | --------------------- | -------------------------- | ---------- |
| 1   | DEVINT     | CSCI5308_1_DEVINT     | CSCI5308_1_DEVINT_USER     | Pohcoo5tig |
| 1   | TEST       | CSCI5308_1_TEST       | CSCI5308_1_TEST_USER       | Pohcoo5tig |
| 1   | PRODUCTION | CSCI5308_1_PRODUCTION | CSCI5308_1_PRODUCTION_USER | Pohcoo5tig |

```bash

ssh student@csci5308-vm1.research.cs.dal.ca
Pohcoo5tig

cd HFXAIR/group01/flask_app/

python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

cd ..
FLASK_APP=flask_app.app:app flask run # from group01 folder 

sudo systemctl restart hfxair

lsof -i :5000
```

[[Deployment overview]]

[[Update Deployment]]

# MariaDB - setup on local 

[[MariaDB setup]]

[[Production .env file]]



