#-----------Note : Implementing_code is just a part of the complete code----------------

# Pre req --------- NOTE : Download all the libraries that are needed using pip install command

!pwd
%cd /content/YOLOv8_Segmentation_DeepSORT_Object_Tracking


# Moving to the Required Directory


%cd /content/YOLOv8_Segmentation_DeepSORT_Object_Tracking/ultralytics/yolo/v8/segment


!unzip 'deep_sort_pytorch.zip'
'''inflating: deep_sort_pytorch/deep_sort/sort - Copy/kalman_filter.py  
  inflating: deep_sort_pytorch/deep_sort/sort - Copy/linear_assignment.py  
  inflating: deep_sort_pytorch/deep_sort/sort - Copy/nn_matching.py  
  inflating: deep_sort_pytorch/deep_sort/sort - Copy/preprocessing.py  
   creating: deep_sort_pytorch/deep_sort/sort/
 extracting: deep_sort_pytorch/deep_sort/sort/__init__.py  
   creating: deep_sort_pytorch/deep_sort/sort/__pycache__/
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/__init__.cpython-310.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/__init__.cpython-37.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/__init__.cpython-38.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/detection.cpython-310.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/detection.cpython-37.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/detection.cpython-38.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/iou_matching.cpython-310.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/iou_matching.cpython-37.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/iou_matching.cpython-38.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/kalman_filter.cpython-310.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/kalman_filter.cpython-37.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/kalman_filter.cpython-38.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/linear_assignment.cpython-310.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/linear_assignment.cpython-37.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/linear_assignment.cpython-38.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/nn_matching.cpython-310.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/nn_matching.cpython-37.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/nn_matching.cpython-38.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/track.cpython-310.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/track.cpython-37.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/track.cpython-38.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/tracker.cpython-310.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/tracker.cpython-37.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/__pycache__/tracker.cpython-38.pyc  
  inflating: deep_sort_pytorch/deep_sort/sort/detection.py  
  inflating: deep_sort_pytorch/deep_sort/sort/iou_matching.py  
  inflating: deep_sort_pytorch/deep_sort/sort/kalman_filter.py  
  inflating: deep_sort_pytorch/deep_sort/sort/linear_assignment.py  
  inflating: deep_sort_pytorch/deep_sort/sort/nn_matching.py  
  inflating: deep_sort_pytorch/deep_sort/sort/preprocessing.py  
  inflating: deep_sort_pytorch/deep_sort/sort/track.py  
  inflating: deep_sort_pytorch/deep_sort/sort/tracker.py  
  inflating: deep_sort_pytorch/LICENSE  
  inflating: deep_sort_pytorch/README.md  
   creating: deep_sort_pytorch/utils/
 extracting: deep_sort_pytorch/utils/__init__.py  
   creating: deep_sort_pytorch/utils/__pycache__/
  inflating: deep_sort_pytorch/utils/__pycache__/__init__.cpython-310.pyc  
  inflating: deep_sort_pytorch/utils/__pycache__/__init__.cpython-37.pyc  
  inflating: deep_sort_pytorch/utils/__pycache__/__init__.cpython-38.pyc  
  inflating: deep_sort_pytorch/utils/__pycache__/parser.cpython-310.pyc  
  inflating: deep_sort_pytorch/utils/__pycache__/parser.cpython-37.pyc  
  inflating: deep_sort_pytorch/utils/__pycache__/parser.cpython-38.pyc  
  inflating: deep_sort_pytorch/utils/asserts.py  
  inflating: deep_sort_pytorch/utils/draw.py  
  inflating: deep_sort_pytorch/utils/evaluation.py  
  inflating: deep_sort_pytorch/utils/io.py  
  inflating: deep_sort_pytorch/utils/json_logger.py  
  inflating: deep_sort_pytorch/utils/log.py  
  inflating: deep_sort_pytorch/utils/parser.py  
  inflating: deep_sort_pytorch/utils/tools.py '''

#Download a Sample Video for Testing from Google Drive
!gdown # video link

#Run the Script for Segmentation with DeepSORT Tracking
!python predict.py model=yolov8x-seg.pt source="test1.mp4"

#To show content
!rm "/content/result_compressed.mp4"


from IPython.display import HTML
from base64 import b64encode
import os

# Input video path
save_path = '/content/YOLOv8_Segmentation_DeepSORT_Object_Tracking/runs/detect/train/test1.mp4'

# Compressed video path
compressed_path = "/content/result_compressed.mp4"

os.system(f"ffmpeg -i {save_path} -vcodec libx264 {compressed_path}")

# Show video
mp4 = open(compressed_path,'rb').read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
HTML("""
<video width=400 controls>
      <source src="%s" type="video/mp4">
</video>
""" % data_url)


from IPython.display import HTML
from base64 import b64encode
import os

# Input video path
save_path = '/content/YOLOv8_Segmentation_DeepSORT_Object_Tracking/runs/detect/train2/test3.mp4'

# Compressed video path
compressed_path = "/content/result_compressed.mp4"

os.system(f"ffmpeg -i {save_path} -vcodec libx264 {compressed_path}")

# Show video
mp4 = open(compressed_path,'rb').read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
HTML("""
<video width=400 controls>
      <source src="%s" type="video/mp4">
</video>
""" % data_url)



