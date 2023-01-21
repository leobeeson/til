# GPG Signatures

## error: gpg failed to sign the data

When running the following command on WSL2:

```console
git commit -m "Update hyperlinks"
```

And get the following error:

```console
error: gpg failed to sign the data
fatal: failed to write commit object
```

The solution is run the following command:

```console
export GPG_TTY=$(tty)
```

[Source](https://stackoverflow.com/a/55993078/7133282)
