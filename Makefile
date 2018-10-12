all:
	gcc freetype_test.c -I/usr/local/include/freetype2 -lfreetype -lm -o freetype_test.o -ggdb

