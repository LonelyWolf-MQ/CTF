## [Challenge Link](https://www.mediafire.com/folder/7ytf5m0njqlz5/#blhc3e69mtfhk).

To determine the profile, you can use "WinDbg Preview" and import the dump file then you will find "Windows 7 Kernel Version 7601 (Service Pack 1) UP Free x64", which means that the profile is Win7SP1x64.

In this challenge, we have to use mimikatz plugins (https://github.com/volatilityfoundation/community/blob/master/FrancescoPicasso/mimikatz.py).

First we will move to the plugins/ directory in volatility then download the plugin.
`wget https://raw.githubusercontent.com/volatilityfoundation/community/master/FrancescoPicasso/mimikatz.py`.

Here we will run mimikatz plugin with volatility.
`python2 vol.py  -f  Login.dmp --profile=Win7SP1x64 mimikatz`.

And we will hash Ahmed's password to get the flag.
`s=$(echo -n passw0rd | md5sum | awk '{print $1}')`.
`echo Challenge flag is: IAUflag{$s}`
