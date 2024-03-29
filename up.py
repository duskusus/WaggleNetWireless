import boto3
import numpy as np
import pandas as pd

keyfile = open('key.txt')

access_key = keyfile.readline()
secret_key = keyfile.readline()
print(f'access key: {access_key},\n secret_key: {secret_key}\n')
bucket_name = 'beehive-data-1.0'
test_file = 'testfile'

def upload(filepath, stamp):
    s3 = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key=secret_key)
    s3.upload_file(filepath, bucket_name, f'testfile-{stamp}')

for i in range(99):
    random = np.random.randint(1000, size=1000)
    print(random)
    df = pd.DataFrame(random)
    df.to_csv('./testfile', header=False, index=False)
    upload('testfile', i)

#endpoint_url = 'https://hnx4w1wod7.execute-api.us-east-2.amazonaws.com/dev'
#coolBeeFacts = 'very interesting data from a hive'
#response = requests.put(endpoint_url + '/beehiveData', data=coolBeeFacts)
#print(f'status:{response.status_code}')