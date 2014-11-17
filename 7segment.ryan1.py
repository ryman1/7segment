#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

digit = 0

#Pinouts
A = 22
B = 27
C = 4
D = 24
E = 25
F = 18
G =23
DP = 17

upswitch = 11
downswitch = 7
GPIO.setup(upswitch, GPIO.IN)
GPIO.setup(downswitch, GPIO.IN)


GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(DP, GPIO.OUT)

GPIO.output(A,GPIO.LOW)
GPIO.output(B,GPIO.LOW)
GPIO.output(C,GPIO.LOW)
GPIO.output(D,GPIO.LOW)
GPIO.output(E,GPIO.LOW)
GPIO.output(F,GPIO.LOW)
GPIO.output(G,GPIO.LOW)
GPIO.output(DP,GPIO.LOW)

def displaydigit(digit):
	if digit == 0:
		GPIO.output(A, GPIO.HIGH)
		GPIO.output(B, GPIO.HIGH)
		GPIO.output(C, GPIO.HIGH)
		GPIO.output(D, GPIO.HIGH)
		GPIO.output(E, GPIO.HIGH)
		GPIO.output(F, GPIO.HIGH)
		GPIO.output(G, GPIO.LOW)
		GPIO.output(DP, GPIO.LOW)
		return
	elif digit == 1:
		GPIO.output(A, GPIO.LOW)
		GPIO.output(B, GPIO.HIGH)
		GPIO.output(C, GPIO.HIGH)
		GPIO.output(D, GPIO.LOW)
		GPIO.output(E, GPIO.LOW)
		GPIO.output(F, GPIO.LOW)
		GPIO.output(G, GPIO.LOW)
		GPIO.output(DP, GPIO.LOW)
		return
	elif digit == 2:
		GPIO.output(A, GPIO.HIGH)
		GPIO.output(B, GPIO.HIGH)
		GPIO.output(C, GPIO.LOW)
		GPIO.output(D, GPIO.HIGH)
		GPIO.output(E, GPIO.HIGH)
		GPIO.output(F, GPIO.LOW)
		GPIO.output(G, GPIO.HIGH)
		GPIO.output(DP, GPIO.LOW)
		return
	elif digit == 3:
		GPIO.output(A, GPIO.HIGH)
		GPIO.output(B, GPIO.HIGH)
		GPIO.output(C, GPIO.HIGH)
		GPIO.output(D, GPIO.HIGH)
		GPIO.output(E, GPIO.LOW)
		GPIO.output(F, GPIO.LOW)
		GPIO.output(G, GPIO.HIGH)
		GPIO.output(DP, GPIO.LOW)
		return
	elif digit == 4:
		GPIO.output(A, GPIO.LOW)
		GPIO.output(B, GPIO.HIGH)
		GPIO.output(C, GPIO.HIGH)
		GPIO.output(D, GPIO.LOW)
		GPIO.output(E, GPIO.LOW)
		GPIO.output(F, GPIO.HIGH)
		GPIO.output(G, GPIO.HIGH)
		GPIO.output(DP, GPIO.LOW)
		return
	elif digit == 5:
		GPIO.output(A, GPIO.HIGH)
		GPIO.output(B, GPIO.LOW)
		GPIO.output(C, GPIO.HIGH)
		GPIO.output(D, GPIO.HIGH)
		GPIO.output(E, GPIO.LOW)
		GPIO.output(F, GPIO.HIGH)
		GPIO.output(G, GPIO.HIGH)
		GPIO.output(DP, GPIO.LOW)
		return
	elif digit == 6:
		GPIO.output(A, GPIO.HIGH)
		GPIO.output(B, GPIO.LOW)
		GPIO.output(C, GPIO.HIGH)
		GPIO.output(D, GPIO.HIGH)
		GPIO.output(E, GPIO.HIGH)
		GPIO.output(F, GPIO.HIGH)
		GPIO.output(G, GPIO.HIGH)
		GPIO.output(DP, GPIO.LOW)
		return
	elif digit == 7:
		GPIO.output(A, GPIO.HIGH)
		GPIO.output(B, GPIO.HIGH)
		GPIO.output(C, GPIO.HIGH)
		GPIO.output(D, GPIO.LOW)
		GPIO.output(E, GPIO.LOW)
		GPIO.output(F, GPIO.LOW)
		GPIO.output(G, GPIO.LOW)
		GPIO.output(DP, GPIO.LOW)
		return
	elif digit == 8:
		GPIO.output(A, GPIO.HIGH)
		GPIO.output(B, GPIO.HIGH)
		GPIO.output(C, GPIO.HIGH)
		GPIO.output(D, GPIO.HIGH)
		GPIO.output(E, GPIO.HIGH)
		GPIO.output(F, GPIO.HIGH)
		GPIO.output(G, GPIO.HIGH)
		GPIO.output(DP, GPIO.LOW)
		return
	elif digit == 9:
		GPIO.output(A, GPIO.HIGH)
		GPIO.output(B, GPIO.HIGH)
		GPIO.output(C, GPIO.HIGH)
		GPIO.output(D, GPIO.HIGH)
		GPIO.output(E, GPIO.LOW)
		GPIO.output(F, GPIO.HIGH)
		GPIO.output(G, GPIO.HIGH)
		GPIO.output(DP, GPIO.LOW)
		return

def displaySequence(sequencelist, interstepdelay, enddelay):
	#Iterates though every step of the sequence
	for sequencestepdict in sequencelist: 
		#Iterates through every LED segment in the sequence step
		for ledsegment in sequencestepdict: 
			GPIO.output(ledsegment, sequencestepdict[ledsegment])
		time.sleep(interstepdelay)
	time.sleep(enddelay)

###
#Initialization animation
#Each dictionary is a animation step in the sequence
off = GPIO.LOW
on = GPIO.HIGH

POSTsequence = [{'A': on}, {'A': off,'B': on}, {'B': off, 'C': on}, {'C': off, 'D': on}, {'D': off, 'E': on}, {'E': off, 'F': on}, {'F': off, 'G': on}, {'G': off, 'A': on}, {'A': off,'B': on}, {'B': off, 'C': on}, {'C': off, 'D': on}, {'D': off, 'E': on}, {'E': off, 'F': on}, {'F': off, 'G': on}, {'G': off}, {'A': on, 'B': on, 'C': on, 'D': on, 'E': on, 'F': on, 'G': on, 'DP': on}, {'A': off, 'B': off, 'C': off, 'D': off, 'E': off, 'F': off, 'G': off, 'DP': off}, {'A': on, 'B': on, 'C': on, 'D': on, 'E': on, 'F': on, 'G': on, 'DP': on}, {'A': off, 'B': off, 'C': off, 'D': off, 'E': off, 'F': off, 'G': off, 'DP': off}]

displaySequence(POSTsequence, .1, .25)
###

prev_down = 0
prev_up = 0
updigit = GPIO.input(upswitch)
downdigit = GPIO.input(downswitch)

while True:
	#take a reading
	displaydigit(digit)
	#if the last reading was low and this one high, print
	if ((not prev_up) and updigit):
		digit = abs(digit + 1)
	#update previous input

	#slight pause to debounce
	#if the last reading was low and this one high, print
	if ((not prev_down) and downdigit):
		digit = abs(digit - 1)
	#update previous input
	prev_down = downdigit
	prev_up = updigit
	#slight pause to debounce
	time.sleep(0.05)

	
GPIO.cleanup()
