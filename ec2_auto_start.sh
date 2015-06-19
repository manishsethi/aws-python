
#!/bin/bash
#instancelist.txt contains the list instance tag you want to stop
FILE="instancelist.txt"
while read line; do
    python ec2-state-change.py start $line
done < $FILE
