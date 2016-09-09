# How to use git and git internals

## Change the commit history

### remove the last commit

```
$ git reset --soft HEAD
```

### Change the committer

Ref[^1]

```
git commit --amend --author "USER_NAME <EMAIL_ADDR>"
```

## submodule

### Add a submodule

```
git submodule add <repo> <path>
```

### get the source of submodules

```
git submodule init
git submodule update
```

## handling authentication

Sometimes the repo is deployed behind a server where authentication is reqired.
http://www.ilker.de/git-goodie-https-basic-authentication.html

## Good referebce site

- [pcottle’s Visual Git Branching ](http://pcottle.github.io/learnGitBranching/)
- [Git immersion](http://gitimmersion.com/index.html)

[^1]: http://stackoverflow.com/questions/750172/change-the-author-of-a-commit-in-git
