# GitLab SSH

To do something like `git clone` from GitLab you need an ssh key pair.

Run `ssh-keygen -t ed25519 -C "<comment>"`

Usually fine to stick with defaults (default filename and no passphrase)

View the contents of the file you have saved to with `cat`

Go to `https://gitlab.com/profile/keys`, paste in key and click `Add key`

Should now be able to `git clone`