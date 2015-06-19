
#!/bin/bash
#instancelist.txt contains list instance tag you want to start
FILE="instancelist.txt"
while read line; do
    python ec2-state-change.py start $line
done < $FILE
