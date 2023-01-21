# Git Runbook

## Commit

* Verify changes in a commit:
  * [resource](https://stackoverflow.com/a/17563740/7133282)
  
  ```terminal
  git diff 063887fada52271f95065b69346584a84a61e1c3~ 063887fada52271f95065b69346584a84a61e1c3
  ```

## Push

* Push local branch that doesn't exist in remote:
  * [resource](https://egghead.io/lessons/git-push-a-new-branch-to-github-that-doesn-t-exist-remotely-yet)

  ```terminal
  git push --set-upstream origin fbe/bug/log_string_format
  ```

## .gitignore

* Crete `.gitignore` file:

```terminal
wget -O .gitignore https://raw.githubusercontent.com/microsoft/vscode-python/main/.gitignore
```

## Add All Except

* Must use single quotes:

```terminal
git add --all -- ':!path/to/excepted_file_1' ':!path/to/excepted_file_2'
```
