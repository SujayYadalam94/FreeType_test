#!/bin/bash

path='/home/sujay/Documents/FreeType_test/fault_sequences'
i=0
for char in {a..z}
do
	sudo dmesg -c
	clear
	./static_test.o $char
	dmesg > $path/$char.txt
	sum=$(python count.py $path/$char)
	echo "$char:$sum\n" >> $path/../final_list.txt
	echo "$char"
done
