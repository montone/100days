#!/usr/bin/env python3

############################################################################
#
# Author: Mike Montone
#
# Date: 04/26/2024
#
# Purpose: Life in Weeks: Caluclate remainder. 
#
############################################################################
# Revisions:
#
#
############################################################################

lifeInWeeks = 90 * 52
print(f"If you would live for 90 years, you would live for {lifeInWeeks} weeks")
yearsLived = int(input("Enter your age: "))
weeksLived = yearsLived * 52
weeksLeft = lifeInWeeks - weeksLived
print(f"You lived {weeksLived} weeks, you have {weeksLeft} weeks left. Get out and enjoy them!")
