import argparse
import sys
#Define two global variables
current_x = 0
current_y = 0
# USAGE
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("--collect", action='store_true', help="Collect all the position data")
ap.add_argument("--plot", action='store_true', help="plot data collected")
args = ap.parse_args()

#Run the same scipt but data collection
if args.collect:
    #Import inside function to ease the efffects
    import ball_tracking
    ball_tracking.tracking('collect', current_x,current_y)
elif args.plot:
    import plotting
    plotting.plot()
else:
    #Import inside function to ease the efffects
    import ball_tracking
    ball_tracking.tracking('normal', current_x,current_y)





