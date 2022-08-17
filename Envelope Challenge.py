# This program is a test of "The N-velope Challenge."
#
# The envelope challenge is where you have N envelopes numbered sequentially.
# Each day you put the amount of cash listed on the envelope into the envelope.
#
# This program also asks whether you want to see the amount saved by each day leading up to the last day or just the total at the end.
#
# Carrik McNerlin, 08-17-2022

n = int(input("How many days would you like to do the envelope challenge?\n"))
showAll = input("Would you like to see each day's progress? [Y/N]")

total = 0
for day in range(1, n+1):
    total += day
    if (showAll.startswith('Y') or showAll.startswith('y')):
        print("On day " + str(day) + ", you will have saved $" + str(total) + ".")
        

print("After " + str(day) + " days, you will have saved $" + str(total) + ".")