set key off 
set pointsize 3
set xrange[-7: 7]
set yrange[-2: 8]
plot '00.dat' u 1:2 w points pt 1 lt 1 title "00", '11.dat' u 1:2 w point pt 2 lt 2 title "11", '01.dat' u 1:2 title "01" w point pt 3 lt 3
pause -1
