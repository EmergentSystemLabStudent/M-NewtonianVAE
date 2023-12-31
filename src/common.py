config = dict(
    metavar="FILE",
    help="Configuration file",
)
format_file = dict(
    help=r'You can save it in the "path: {results_dir: ...}" (in config file) directory by pressing the s key on the matplotlib window with specified format.'
)
format_video = dict(
    help='Format of the video to be saved\nYou can save the video with "--save-anim".'
)
default_fig_formats = ["png"]
# default_fig_formats = ["png", "pdf", "svg"]

# format:
#   png: versatile, raster
#   pdf: versatile, vector, for LaTeX
#   svg: vector, for PowerPoint
