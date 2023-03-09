import subprocess
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from tempfile import NamedTemporaryFile
import os

app = FastAPI()
return_video = "results/ouput.mp4"


# @app.post("/video/detect-faces")
# def detect_faces(file: UploadFile = File(...)):
#     temp = NamedTemporaryFile(delete=False)
#     try:
#         try:
#             contents = file.file.read()
#             with temp as f:
#                 f.write(contents)
#         except Exception:
#             return {"message": "There was an error uploading the file"}
#         finally:
#             file.file.close()
        
#         #res = process_video(temp.name)  # Pass temp.name to VideoCapture()
#     except Exception:
#         return {"message": "There was an error processing the file"}
#     finally:
#         #temp.close()  # the `with` statement above takes care of closing the file
#         os.remove(temp.name)
        
#     return res

# @app.get("/", response_class=FileResponse)
# async def main():
#     # cmd_str('python inference.py --checkpoint_path "checkpoints/wav2lip_gan.pth"  --segmentation_path "checkpoints/face_segmentation.pth" --sr_path "checkpoints/esrgan_max.pth"  --face "videos/input_video.mp4" --outfile "results/ouput.mp4" ')

#     return return_video

#     # return 

# # subprocess.run(cmd_str, shell=True)

# #  !python inference.py \
# #         --checkpoint_path "checkpoints/wav2lip_gan.pth" \
# #         --segmentation_path "checkpoints/face_segmentation.pth" \
# #         --sr_path "checkpoints/esrgan_max.pth" \
# #         --face "videos/input_video.mp4" \
# #         --audio "videos/input_video.mp4" \
# #         --outfile "results/ouput.mp4"

subprocess.call('python3 -m inference --checkpoint_path "checkpoints/wav2lip_gan.pth"  --face "videos/input.mp4" --audio "videos/input_audio.wav" --outfile "results/ouput.mp4" ')
