#!/bin/bash

path='/home/sujay/Documents/FreeType_test'
read string
stringlen=$(echo -n $string | wc -m)
i=0
output=""
#for char in {a..z}
while [ $i -lt $stringlen ]
do
	sudo dmesg -c
	clear
#	./static_test.o ${string:$i:$((1))}
	if [ "$1" = "huge" ]
	then
		HUGETLB_ELFMAP=R ./static_huge_test.o ${string:$i:$((1))}
	else
		./static_test.o ${string:$i:$((1))}
	fi
	#cat /proc/pgfault_file > /home/sujay/Desktop/fault\ sequences/$char.txt
#	dmesg > $path/$char.txt
	dmesg > $path/output.txt
#	vim -s $path/test.keys $path/output.txt
	output="$output$(python find_char.py output)"
	((i++))
	#sum=$(python count.py output)
	#echo "$char:$sum\n" >> $path/final_list.txt
	#echo "$char"
done

echo "The entered string is"
echo $output
