# Read from the file file.txt and print its transposed content to stdout.
line=$(wc -l file.txt | cut -d' ' -f1)

strings=($(head -n 1 file.txt))

r=2

#echo $2 $line

while [ $r -le $line ]; do
    curLine=($(head -n $r file.txt | tail -n 1))
    c=0;
    for str in "${curLine[@]}"; do
        strings[$c]="${strings[$c]} $str"
        c=$((c+1))
    done
    r=$((r+1))
done

for str in "${strings[@]}"; do
    echo $str
done


