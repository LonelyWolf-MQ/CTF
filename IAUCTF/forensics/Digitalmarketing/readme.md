
# Challenge Link https://www.mediafire.com/folder/7ytf5m0njqlz5/iauctf#epclnz1blil79


## To determine the profile, you can use WinDbg Preview and import the dump file then you will find "Windows 7 Kernel Version 7601 (Service Pack 1) UP Free x64", which means that the profile is Win7SP1x64

## as the challenge description, I used iehistory plugin
```python2 vol.py -f DigitalMarketing.dmp --profile=Win7SP1x64 iehistory```

## I used the mftparser to read the hexdump of the secret.txt file
```python2 vol.py -f DigitalMarketing.dmp --profile=Win7SP1x64 mftparser```

## So Dump the memory of the "Chrome.exe" process
```python2 vol.py -f DigitalMarketing.dmp --profile=Win7SP1x64 memdump -p 2512 --dump-dir .```

## Then you will grep any url for social media
```strings 2512.dmp | grep https://```

## You will find an instagram account, you open it then found the flag in image
https://www.instagram.com/exmak90
