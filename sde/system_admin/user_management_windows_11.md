# User Management on Windows 11

## Disable PasswordLess Sign-in with Registry Script

1. Save below code as `Turn_OFF_PasswordLess_sign-in_for_Microsoft_accounts.reg`:

    ```txt
    Windows Registry Editor Version 5.00

    [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\PasswordLess\Device]
    "DevicePasswordLessBuildVersion"=dword:00000000
    ```

2. Run `.reg` script.  

[source](https://www.elevenforum.com/t/enable-or-disable-passwordless-sign-in-for-microsoft-accounts-in-windows-11.834/)

## Manage Windows users with Net User

Sources:

* [Manage Windows users with Net User](https://www.ghacks.net/2017/05/24/manage-windows-users-with-net-user/)
* [How to enable the hidden Windows 11 administrator account](https://www.ghacks.net/2021/10/01/how-to-enable-the-hidden-windows-11-administrator-account/)

### Used commands

#### See list of users

```cmd
net user
```

### Display a specific user's information (e.g. Administrator):

```cmd
net user Administrator
```

### Add a user to a user group

```cmd
net localgroup "Administrators" {machine_name}\{user_name} /add
net localgroup "Users" {machine_name}\{user_name} /add
```

### Enable password required

```cmd
net user {user_name} /passwordreq:yes
```

## Enable "Users must enter a user name and password to use this computer"

[source](https://answers.microsoft.com/en-us/windows/forum/all/how-do-i-require-a-password-to-log-in/83fcb1e4-fb9d-4b8d-a7b9-7e93535710b7)
**NOTE:** By modifying the user's group in the "User Accounts" window that pops up by running `control userpasswords2` in PowerShell is how I lost the fbe-spirit user.

I fixed the missing user problem by following these [instructions](https://www.thewindowsclub.com/user-accounts-missing-windows).

Another helpful resource for managing users and user groups is [this page](https://www.windows-commandline.com/add-user-to-group-from-command-line/).
