import cv2
import os

def video_to_frames(video, path_output_dir):
    # extract frames from a video and save to directory as 'x.png' where 
    # x is the frame index
    vidcap = cv2.VideoCapture(video)
    count = 0
    while vidcap.isOpened():
        success, image = vidcap.read()
        if success:
            cv2.imwrite(os.path.join(path_output_dir, '%d.png') % count, image)
            count += 1
        else:
            break
    cv2.destroyAllWindows()
    vidcap.release()

video_to_frames('input_video.mp4', 'output_directory/')


# Please replace 'input_video.mp4' and 'output_directory/' with your video's path and your desired output directory. The script will save frames as PNG files. Each file's name will correspond to the frame index in the video.
