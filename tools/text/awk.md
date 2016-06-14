# awk usage

## Usage

	$awk 'program' inputfile1 inputfile2 ......

or

	$awk -f script_filename inputfile1 inputfile2 ......


## concepts

### FS
two ways

	gawk 'BEGIN{FS=","; OFS=","};{if ($3 == "") $3=1000000*rand()}; {print $1,$2,$3,$4,$5}' statewide.csv

	gawk -F, '{if ($3 == "") $3=1000000*rand()}; {print $1,',',  $2, $3, $4, $5}' portland_metro.csv


### OFS

	gawk 'BEGIN{FS=","; OFS=","};{if ($3 == "") $3=1000000*rand()}; {print $1,$2,$3,$4,$5}' statewide.csv

### NF

	gawk 'BEGIN{FS=","}; {if (NF != 5) print "NF less than 5"}' portland_metro.csv

## branch

## loop

## functions

- rand
