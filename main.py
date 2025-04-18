from fastapi import FastAPI,Body
from fastapi.responses import FileResponse
from pydantic import BaseModel
from model.pose_detection import predict,fetch_model
from utils.image_formatter import decode_base64_image, encode_image_to_base64
from utils.boxes_to_dict import convert_boxes_to_dict
from utils.keypoints_to_dict import convert_keypoints_to_dict
import cv2

app = FastAPI()
model = fetch_model()

class ImageRequest(BaseModel):
    id: str
    image: str


print("HELLO FROM WHERE")


# To check the health of api

@app.get("/api")
async def api_health():
    return {
        "message":"API is working"
    }


# pose estimation

@app.post("/api/pose_estimation")
async def pose_estimation(request:ImageRequest=Body(...)):
    image = decode_base64_image(request.image)
    input_path = f"./model/results/{request.id}.jpg"
    output_path = f"./model/results/{request.id}_with_keypoints.jpg"
    cv2.imwrite(input_path, image)
    boxes,keypoints,count,speed = predict(model, input_path,output_path,"not_annotated")
    return {
        "id":request.id,
        "count":count,
        "boxes":convert_boxes_to_dict(boxes),
        "keypoints":convert_keypoints_to_dict(keypoints),
        "speed_preprocess":speed["preprocess"],
        "speed_inference":speed["inference"],
        "speed_postprocess":speed["postprocess"]

    }

# pose estimation along with annotation

@app.post("/api/pose_estimation/annotated")
async def pose_estimation_annotated(request: ImageRequest):
    image = decode_base64_image(request.image)
    input_path = f"./model/results/{request.id}.jpg"
    output_path = f"./model/results/{request.id}_with_keypoints.jpg"
    cv2.imwrite(input_path, image)
    result=predict(model, input_path,output_path,"annotated")
    base64_img=encode_image_to_base64(result)
    return {
        "id":request.id,
        "image":base64_img
    }
