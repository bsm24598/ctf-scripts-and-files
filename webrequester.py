#!/usr/bin/python3

import urllib.request

#Get each clock code part from 5 different websites before the 10 second timer ends.
#If the timer ends, all codes change.
#Once the parts are collected, you must combine them and authenticate to the 6th website with the code in the url.
#Original URL has been changed to avoid script reuse

part1 = urllib.request.urlopen("https://notarealwebsite-challenge-files/clock-pt1?verify=lVtoH6VF46navErXnXDyvA%3D%3D")
p1 = part1.read()

part2 = urllib.request.urlopen("https://notarealwebsite-challenge-files/clock-pt2?verify=lVtoH6VF46navErXnXDyvA%3D%3D")
p2 = part2.read()

part3 = urllib.request.urlopen("https://notarealwebsite-challenge-files/clock-pt3?verify=lVtoH6VF46navErXnXDyvA%3D%3D")
p3 = part3.read()

part4 = urllib.request.urlopen("https://notarealwebsite-challenge-files/clock-pt4?verify=lVtoH6VF46navErXnXDyvA%3D%3D")
p4 = part4.read()

part5 = urllib.request.urlopen("https://notarealwebsite-challenge-files/clock-pt5?verify=lVtoH6VF46navErXnXDyvA%3D%3D")
p5 = part5.read()

#decode data from byte format
p1 = p1.decode("utf-8")
p2 = p2.decode("utf-8")
p3 = p3.decode("utf-8")
p4 = p4.decode("utf-8")
p5 = p5.decode("utf-8")

#add all code pieces together to recreate the full code
final_part = p1 + p2 + p3 + p4 + p5

#print out the full code
print("-" * 30)
print("Full Challenge Code: " + final_part)

#Grab website data from verification site with full code attached in url
get_flag = urllib.request.urlopen("https://notarealwebsite-challenge-files/get-flag?verify=lVtoH6VF46naErXnXdyvA%3D%3D&string={}".format(final_part))
flag = get_flag.read()

flag = flag.decode("utf-8")

#print out final flag!
print("-" * 30)
print("FLAG: " + flag)
print("-" * 30)
