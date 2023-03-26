# remove_too_much_fileds_from_songs
Remove the fields that are too much in the propresenter song files

when using propresenter over time, there could be too much fields added to the song files,
this can happen when applying different templates to the song files.

it looks like this only happens on Windows platforms.

this python script can remove them to speed up propresenter, and prevent some side effects like flikkering on the output.


dependencies:
protobuf  from https://developers.google.com/protocol-buffers/  to install it:  pip3 install protobuf

- backup all your propresenter data
- copy all songdirectories you want to cleanup  from <user directory>\documents\propresenter\library\ to c:\songs
- update the settings in the Main_cleanup.py line 38 .. 40
- run the Main_cleanup.py
- copy all song files back to <user directory>\documents\propresenter\library\ (do not import them, for this will make propresenter take more time to startup, slower)
  
