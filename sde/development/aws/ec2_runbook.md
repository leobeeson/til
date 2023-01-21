# EC2 Runbook

## SSH

The following instructions work from linux CLI, Windows PowerShell Core, and Windows Command Prompt.  

1. If the private key file (i.e. `.pem` file) has a space in its name, remove the space:
  
    ```terminal
    mv EC2\ Tutorial.pem EC2Tutorial.pem
    ```

2. Change access permission of the private key file:

    ```terminal
    chmod 0400 EC2Tutorial.pem
    ```

3. Ssh into the host machine, providing the `identity_file` (i.e. private key file) to the host machine for authentication:

    ```terminal
    ssh -i EC2Tutorial.pem ec2-user@{IP_ADDRESS}
    ```
