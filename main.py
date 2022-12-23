from moviepy.editor import *


def convert(input_file, output_file, fps, resizeinput):
    clip = VideoFileClip(input_file+'.mp4')
    resized = clip.resize(width=resizeinput)
    video = CompositeVideoClip([resized])
    video.write_gif(output_file+'.gif', fps=fps, program= 'imageio')


file_input = input('[*] Press enter file name to convert: ')
file_output = input('[*] Press enter output file name: ')
fps_input = input('[*] Press enter fps (1-30): ')
resize_input = input('[*] Press enter width: ')

# Convert the file
convert(file_input, file_output, int(fps_input), int(resize_input))