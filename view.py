import np_vid_viewer

import argparse

parser = argparse.ArgumentParser(description='Analyze temperature data.')
parser.add_argument('temp_data',
                    type=str,
                    help='the file location/name of the temperature data')
parser.add_argument('merged_data',
                    type=str,
                    help='the file location/name of the merged data')
parser.add_argument('-scale',
                    type=int,
                    default=1,
                    required=False,
                    help='int factor to scale output videos by')
parser.add_argument(
    '-delay',
    type=int,
    default=1,
    required=False,
    help=
    'int specifying millisecond delay between showing each frame in play_video()'
)
parser.add_argument(
    '-mp',
    type=int,
    default=False,
    required=False,
    help='0 or 1 specifying wether or not to overlay meltpool data on the image'
)
parser.add_argument(
    '-top',
    type=int,
    default=False,
    required=False,
    help='0 or 1 specifying wether or not to remove top reflections')

parser.add_argument(
    '-bot',
    type=int,
    default=False,
    required=False,
    help='0 or 1 specifying wether or not to remove bottom reflections')

parser.add_argument(
    '--build',
    type=str,
    default=None,
    required=False,
    help='Name of build'
)

args = parser.parse_args()

build = args.build
temp_data_file = args.temp_data
merged_data_file = args.merged_data
scale_factor = args.scale
frame_delay = args.delay
top = bool(args.top)
bot = bool(args.bot)

VIEWER = np_vid_viewer.NpVidTool(build=build,
                                temp_filename=temp_data_file,
                                 data_filename=merged_data_file,
                                 scale_factor=scale_factor,
                                 frame_delay=frame_delay,
                                 mp_data_on_vid=args.mp,
                                 remove_top_reflection=top,
                                 remove_bottom_reflection=bot)

VIEWER.play_video()
