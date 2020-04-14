import sys
import matplotlib.pyplot as plt

sys.path.insert(0, '../toolkit')
import toolkit

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("input_path",
                    metavar="data_root_path",
                    help="Name (path) of input file (dir).",
                    default=None)
parser.add_argument("pattern_index",
                    metavar="pattern_index",
                    help="data index number",
                    default=None)
parser.add_argument("-a",
                    "--angle",
                    action="store_true",
                    help="Get angle quaternion from SIMEX diffr output")
parser.add_argument("-d",
                    "--diffr",
                    action="store_true",
                    help="Get 2D diffraction pattern from SIMEX diffr output")

args = parser.parse_args()
if args.angle:
    quaternion = toolkit.getData(args.input_path,pattern_index=int(args.pattern_index),d_type='angle')
    print (args.input_path)
    print (quaternion)
if args.diffr:
    diff_data = toolkit.getData(args.input_path,pattern_index=int(args.pattern_index),d_type='diffr')
    toolkit.plotLog(diff_data,1e-5,1e1,cmap="jet")
    plt.show()


