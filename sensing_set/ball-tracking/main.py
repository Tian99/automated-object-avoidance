import argparse
import sys
import ball_tracking
#Define two global variables
current_x = 0
current_y = 0
# USAGE
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("--collect", action='store_true', help="Collect all the position data")
args = ap.parse_args()

#Run the same scipt but data collection
if args.collect:
    ball_tracking.ball_tracking('collect', current_x,current_y)
else:
    ball_tracking.ball_tracking('normal', current_x,current_y)





