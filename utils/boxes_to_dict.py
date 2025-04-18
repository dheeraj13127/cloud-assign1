def convert_boxes_to_dict(boxes):
    return {
        "cls": boxes.cls.tolist() if hasattr(boxes, "cls") else [],
        "conf": boxes.conf.tolist() if hasattr(boxes, "conf") else [],
        "data": boxes.data.tolist() if hasattr(boxes, "data") else [],
        "id": boxes.id if hasattr(boxes, "id") else None,
        "is_track": boxes.is_track if hasattr(boxes, "is_track") else False,
        "orig_shape": list(boxes.orig_shape) if hasattr(boxes, "orig_shape") else [],
        "shape": list(boxes.shape) if hasattr(boxes, "shape") else [],
        "xywh": boxes.xywh.tolist() if hasattr(boxes, "xywh") else [],
        "xywhn": boxes.xywhn.tolist() if hasattr(boxes, "xywhn") else [],
        "xyxy": boxes.xyxy.tolist() if hasattr(boxes, "xyxy") else [],
        "xyxyn": boxes.xyxyn.tolist() if hasattr(boxes, "xyxyn") else [],
    }
