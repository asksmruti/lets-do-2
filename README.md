Install serverless
------------------
`npm install -g serverless`

Create Service
--------------
```
serverless create --template aws-python3 \
  --name dp-demo-smruti
  --path pypack
```
This will create a serverless python3 template project at given path `pypack/` with a service name `dp-demo-smruti`

Use virtual environment 
-----------------------
Use virtual environment for all development
```
cd pypack/
virtualenv venv --python=python3
source venv/bin/activate
```

Sample python code
------------------
Create sample python code to generate an array(Use numpy package)
Install numpy package: `pip install numpy`
Create a requirement file: `pip freeze > requirement.txt`

Code to generate a sample matrix using np

`handler.py`
```
import numpy as np
import json


def main(event, context):
    a = np.arange(15).reshape(3, 5)
    arr=json.dumps({"Numpy Array": a.tolist()})
    return arr


if __name__ == "__main__":
    output = main('', '')
    print(output)
```
You may test the code locally. 

Service Deployment
------------------

Since we need the python libraries(eg. numpy) along with code, so we have to install a plugin `serverless-python-requirements`

To install the serverless plugin:
Create a file `package.json` to save the node dependencies then install the plugin

```
npm init
npm install --save serverless-python-requirements
```

Edit the serverless.yml file, add the `plugins`

Also you need to have Docker installed to be able to set `dockerizePip: true` or `dockerizePip: non-linux`. Alternatively, you can set `dockerizePip: false`, and it will not use Docker packaging. But, Docker packaging is essential if you need to build native packages that are part of your dependencies like Psycopg2, NumPy, Pandas, etc.

 
The service name is `dp-demo-smruti`

* <i>serverless.yml</i> file 

```
service: dp-demo-smruti

provider:
  name: aws
  runtime: python3.7
  region: eu-central-1

functions:
  dp-demo-test:
    handler: handler.main

plugins:
  - serverless-python-requirements

custom:
  pythonRequirements:
    dockerizePip: non-linux
```

Now, we can deploy the code -

`sls deploy -v`

Then invoke the function -

`serverless invoke -f sls invoke -f dp-demo-test`
