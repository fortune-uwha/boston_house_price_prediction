import numpy as np
import json


def process_input(request_data: str) -> np.array:
    """
    A processing function to validate that the request data is correct.
    :param request_data: request made to the API
    :return: numpy array
    """
    parsed_body = np.asarray(json.loads(request_data)["inputs"])
    assert len(parsed_body) >= 1
    return parsed_body
