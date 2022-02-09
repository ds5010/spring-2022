# Github tokens

* To list the configuration of the current repo:
```
git config --list
```
* On a Mac, the configuratio has an entry for "credential.helper=osxkeychain"
  * This is where the credentials reside to bypass username/password prompts
* To push without using the keychain:
```
git config --local credential.helper ""
```
* You'll get a prompt for username and password, but the standard github password doesn't work anymore.
* If you try to use your github password, you'll get an error...
```
Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
```

Instructions are here: 

* https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
* It's pretty easy to generate an access token
* Once you create it, you should treat it like as password
* And once you've generated a token, use it as the password for the username/password prompt
* You should then be able to push from the command line.


