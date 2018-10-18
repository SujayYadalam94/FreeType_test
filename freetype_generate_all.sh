#!/bin/bash

path='/home/sujay/Documents/FreeType_test/fault_sequences'
i=0
for char in {a..z}
do
	sudo dmesg -c
	clear
	if [ "$1" = "huge" ]
	then
		HUGETLB_ELFMAP=R ./static_huge_test.o $char
		dmesg > $path/${char}_huge.txt
	else
		./static_test.o $char
		dmesg > $path/$char.txt
	fi
	sum=$(python count.py $path/$char)
	echo "$char:$sum\n" >> $path/../final_list.txt
	echo "$char"
done
