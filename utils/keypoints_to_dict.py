def convert_keypoints_to_dict(keypoints):
    return {
        "conf": keypoints.conf.tolist() if hasattr(keypoints, "conf") else [],
        "data": keypoints.data.tolist() if hasattr(keypoints, "data") else [],
        "has_visible": bool(keypoints.has_visible) if hasattr(keypoints, "has_visible") else False,
        "orig_shape": list(keypoints.orig_shape) if hasattr(keypoints, "orig_shape") else [],
        "shape": list(keypoints.shape) if hasattr(keypoints, "shape") else [],
        "xy": keypoints.xy.tolist() if hasattr(keypoints, "xy") else [],
        "xyn": keypoints.xyn.tolist() if hasattr(keypoints, "xyn") else [],
    }
