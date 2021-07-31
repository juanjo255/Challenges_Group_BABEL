# Challenges_Group_BABEL

python programming challenges

## Reto_cajafuerte

Given a matrix, we have to return the first movement that we have to do to achieve the "F" element. so, every element tells you what movement every element do.
in that order, A means to above, B means to below, D means to the right and I means to the left, finally, the number indicate how many element you have to move. For example, 1A do 1 movement above, 2D do 2 movement to the right.

## Reto_Cuadrilandia

Cuadriland is a world where everything is a square, something like minecraft, so, bikes have square rims that, in fact, are matrix NxN. so, Given a matrix we have to do a code that let us know the state of the matrix after a angle of 90° or 45°. only for those angles. for example for 90°

1 2 3      7 4 1
4 5 6  --> 8 5 2  
7 8 9      9 6 3

for 45°  
1 2 3     4 1 2
4 5 6 --> 7 5 3
7 8 9     8 9 6

## Reto_densest_protein

Build a command line utility in the language of your choice that reads a quick .faa file of protein sequences for any organism, and determines the protein with the highest density, where density is equal to Total Weight / Length. The molecular weight should be handled in g / mol. The result is a fast file with the densest sequence, with its respective header with additional field for the density.

## Reto_sequence_trimming

Create a command line utility in the language of your preference that receives a file with reads in fastq format and a desired window size and quality as parameters (eg 20 and 4) and returns the trimmed reads in fastq format such that the quality of the sequence (taken in windows of the given size [4]) is always guaranteed to be at least the indicated value [20]. Assume a Sanger encoding (Phred + 33) for the quality values ​​in the fastq file.

## Reto_ParseXSV

Build a Python utility that allows you to do basic queries on columns and groups of data. The delimiter will be parametric on the command line.
The queries will be made directly from the command line, with output to the console directly.
For this version there will be the following queries:

Extract fields:
presents the content of one or more fields, in their entirety.
Command line arguments:
select = "field name1 [, field_name2,…]"
Note: the brackets indicate that optionally more than one field can be handled.

Add over columns:
adds the content of one or more columns, in its entirety. Values ​​that do not represent numbers will not be added. It is usually applied on columns that are known to be numeric. However, omitted data, or alphanumeric data, does not add up.
Command line arguments:
sum = "field name1 [, field_name2,…]"

Average over columns:
averages the content of one or more columns, over their entire length. Values ​​that do not represent numbers are considered zeros, and they count in the number of values ​​that enter the average. Cells with no value (blank or null) are not taken into account for the average.
Command line arguments:
avg = "field name1 [, field_name2,…]"

Count over columns:
counts the fields that have data, regardless of their type. Only those fields that are not blank or null are considered in the count.
Command line arguments:
count = "field name1 [, field_name2,…]"

PD = [] means optional.