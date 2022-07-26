nr_frames= video.get(cv2.CAP_PROP_FRAME_COUNT)
fps= video.get(cv2.CAP_PROP_FPS)

timestamp = "00:00:02.75"
timestamp_list= timestamp.split(":")            #use of split to create an list from a string
timestamp_list_floats= [float(i) for i in timestamp_list]       # transform list in float, we can use numbers
hours, minutes, seconds = timestamp_list_floats         # add name for all the floats
#print(seconds, minutes)         #example

frame_nr= hours* 3600 * fps + minutes * 60 * fps + seconds * fps

video.set(1, frame_nr)          #sets the  start frame of the video processing
success, frame= video.read()
cv2.imwrite(f"frame at {hours}:{minutes}:{seconds}.jpg", frame)