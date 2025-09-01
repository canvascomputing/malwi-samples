def scale_video(input_fn, output_fn, ratiow, ratioh):
    os.system(
        f'ffmpeg -i {input_fn}  -vf "scale=iw*{ratiow:.4f}:ih*{ratioh:.4f}" {output_fn}'
    )


def crop_video(input_fn, output_fn, x_begin, x_end, y_begin, y_end):
    os.system(
        f'ffmpeg -i {input_fn} -filter:v "crop=iw*{x_end - x_begin:.4f}:ih*{y_end - y_begin:.4f}:iw*{x_begin:0.4f}:ih*{1 - y_end:0.4f}" {output_fn}'
    )


def accelerate_video(input_fn, output_fn, speed):
    os.system(
        f'ffmpeg -i {input_fn} -filter:v "setpts={1 / speed:.4f}*PTS" {output_fn}'
    )