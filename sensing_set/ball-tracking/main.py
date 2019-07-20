import argparse
import ball_tracking
import collection
#Define two global variables
current_x = 0
current_y = 0
# USAGE
# python ball_tracking.py
import ball_tracking

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-c', '--collect', type=int, metavar='', help='Type in 1 to collect all the data from video')
args = ap.parse_args()

ball_tracking.ball_tracking(current_x,current_y)

if args.collect is 'c':
    print('yesssssssssssssssss')




