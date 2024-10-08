# Print a neat looking multiplication table like this:

#	       1   2   3   4   5   6   7   8   9   10  11  12
#	  :--------------------------------------------------
#	1 :    1   2   3   4   5   6   7   8   9   10  11  12
#	2 :    2   4   6   8  10  12  14  16  18   20  22  24
#	3 :    3   6   9  12  15  18  21  24  27   30  33  36
#	4 :    4   8  12  16  20  24  28  32  36   40  44  48
#	5 :    5  10  15  20  25  30  35  40  45   50  55  60
#	6 :    6  12  18  24  30  36  42  48  54   60  66  72
#	7 :    7  14  21  28  35  42  49  56  63   70  77  84
#	8 :    8  16  24  32  40  48  56  64  72   80  88  96
#	9 :    9  18  27  36  45  54  63  72  81   90  99 108
#	10:   10  20  30  40  50  60  70  80  90  100 110 120
#	11:   11  22  33  44  55  66  77  88  99  110 121 132
#	12:   12  24  36  48  60  72  84  96 108  120 132 144


# First solution

header = "{0:>9}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}".format(1,2,3,4,5,6,7,8,9,10,11,12)
little_frame = "  :--------------------------------------------------"

print(header)
print(little_frame)

for i in range(1, 13):
	print("{0:<2}:{1:>6}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}{12:>4}".format(i, i * 1, i * 2, i * 3, i * 4, i * 5, i * 6, i * 7, i * 8, i * 9, i * 10, i * 11, i * 12, i * 13))
print(end="\n\n")


# Second solution (I knew the first solution wasn't the best so GPT-4o gave me the idea, I realized it on my own)

size = 12

print("{:>5}".format(""), end="")
for i in range(1, size + 1):
	print("{:>4}".format(i), end="")
print()

print("{}".format("  :--"), end="")
print("{}".format("-" * (size * 4)))

for i in range(1, size + 1):
	print("{:<2}:  ".format(i), end="")
	for j in range(1, size + 1):
		print("{:>4}".format(i * j), end="")
	print()
