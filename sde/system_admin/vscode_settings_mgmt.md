# VSCode Settings Management

## Create Symlink to Dotfiles

### Default File Locations

* settings.json: `C:\Users\{USER}\AppData\Roaming\Code\User\settings.json`
* keybindings.json: `C:\Users\{USER}\AppData\Roaming\Code\User\keybindings.json`
* markdown.json: `C:\Users\{USER}\AppData\Roaming\Code\User\snippets\markdown.json`

### Dotfile Locations

* settings.json: `C:\Users\{USER}\{CLOUD_DRIVE}\{VAULT}\dotfiles\vscode\settings.json`
* keybindings.json: `C:\Users\{USER}\{CLOUD_DRIVE}\{VAULT}\dotfiles\vscode\keybindings.json`
* markdown.json: `C:\Users\{USER}\{CLOUD_DRIVE}\{VAULT}\dotfiles\vscode\snippets\markdown.json`

### Runbook

The commands for creating the symbolic links have to be run as an Administrator.

```powershell administrator
cd C:\Users\{USER}\AppData\Roaming\Code\User\
rm settings.json
New-Item -ItemType SymbolicLink -Path settings.json -Target "C:\Users\{USER}\{CLOUD_DRIVE}\{VAULT}\dotfiles\vscode\settings.json"
rm keybindings.json
New-Item -ItemType SymbolicLink -Path keybindings.json -Target "C:\Users\{USER}\{CLOUD_DRIVE}\{VAULT}\dotfiles\vscode\keybindings.json"
cd snippets
rm markdown.json
New-Item -ItemType SymbolicLink -Path markdown.json -Target "C:\Users\{USER}\{CLOUD_DRIVE}\{VAULT}\dotfiles\vscode\markdown.json"
```

## Resources

* [Change VSCode User Settings location](https://stackoverflow.com/questions/44575312/change-vscode-user-settings-location)
