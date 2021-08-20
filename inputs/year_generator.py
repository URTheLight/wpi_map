import sys

curr_year = 1870

sys.stdout.write("new Array(")
for i in range (126):
    select_year = curr_year + i
    sys.stdout.write("svgMapDataWPI" + str(select_year) + ", ")
sys.stdout.write("svgMapDataWPI1996);")