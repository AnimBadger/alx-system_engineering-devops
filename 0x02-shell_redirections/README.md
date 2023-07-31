echo - print
echo with \ to escape key characters
cat - display content of a file
tail - display last 10 lines of a file
head - display first 10 lines of a file
head -n 3 | tail -n 1 - display 3rd line in file
ls -la > - redirect output to file
tail -n 1 | cat > - replicate last line in file
find . -name -type f -delete - find a file and delete it
find . -mindepth 1 - count directories
ls -t | head - display newly modified texts
sort | uniq -u - list only unique items
grep root - find root in given file
grep -c - count words
