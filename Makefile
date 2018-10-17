all: dynamic static static_hugepages dynamic_hugepages

dynamic:
	gcc freetype_test.c -I/usr/local/include/freetype2 -lfreetype -lm -o dynamic_test.o -ggdb

static:
	gcc freetype_test.c -L. -lfreetype -I/usr/local/include/freetype2 -lm -lz -lbz2 -o static_test.o -ggdb
	
static_hugepages:
		gcc freetype_test.c -L. -lfreetype -I/usr/local/include/freetype2 -lm -lz -lbz2 -o static_huge_test.o -ggdb -B /usr/local/share/libhugetlbfs -Wl,--hugetlbfs-align

dynamic_hugepages:
	gcc freetype_test.c -I/usr/local/include/freetype2 -lfreetype -lm -o dynamic_huge_test.o -ggdb -B /usr/local/share/libhugetlbfs -Wl,--hugetlbfs-align

clean:
	rm -f *.o
