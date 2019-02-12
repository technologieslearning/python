# python


To create a new SSH key pair:

Open a terminal on Linux or macOS, or Git Bash / WSL on Windows.

Generate a new ED25519 SSH key pair:
ssh-keygen -t ed25519 -C "email@example.com"

Or, if you want to use RSA:
ssh-keygen -o -t rsa -b 4096 -C "email@example.com"
The -C flag adds a comment in the key in case you have multiple of them and want to tell which is which. It is optional.



Add an SSH key

To add an SSH key you need to generate one or use an existing key.

Paste your public SSH key, which is usually contained in the file '~/.ssh/id_rsa.pub' and begins with 'ssh-rsa'. Don't use your private SSH key.
