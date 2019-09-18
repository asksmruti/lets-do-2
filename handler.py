import numpy as np
import json


def main(event, context):
    a = np.arange(15).reshape(3, 5)
    arr=json.dumps({"Numpy Array": a.tolist()})
    return arr


if __name__ == "__main__":
    output = main('', '')
    print(output)
