# Show Commit Tree

## Simple Graph

```terminal
git log --graph --pretty=oneline --abbrev-commit
```

[source](https://stackoverflow.com/a/2421063/7133282)

## Graph with Committer Name and Time Since Commit

* Configure as alias:
  
  ```terminal
  git config --global alias.lgb "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset%n' --abbrev-commit --date=relative --branches"
  ```

* Command:

  ```terminal
  git lgb
  ```
  
  * Alias name heuristic? `lgb` -> "Log Graph Branches"
