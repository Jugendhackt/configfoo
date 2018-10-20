# configfoo
configfoo generates configuration argument indicies of manpages in ctags 
file format. So it can be used for tag jumping to configuration arguments 
and thier autocompletion in vim, emacs and alike. 

## disclaimer
configfoo parses manpages based on line indentation. As a result it has the 
following limitations:
* Not every manpage will work
* There is no garantee that all configuation arguments are parsed
additionally: configfoo is developed only for parsing of manpages focusing 
on configuration files (like the ones about neomuttrc, coredump.conf and dhcpcd.conf).

## usage
- Export the manpage with man topic > manFile.
- Run ./parser to create the ctags-file.
- Start vim or your favourite text editor.

## questions?
please reach out to us if you have any questions concerning this project.
