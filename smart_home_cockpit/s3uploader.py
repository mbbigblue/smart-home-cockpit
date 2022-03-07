import boto3
import uuid
import config as cnf


class S3Uploader:
    def __init__(self, aws_config):
        self.s3_bucket_name = aws_config['aws']['s3_bucket_name']
        self.s3 = boto3.resource('s3',
                                 aws_access_key_id=aws_config['aws']['aws_access_key_id'],
                                 aws_secret_access_key=aws_config['aws']['aws_secret_access_key'])
        filename = str(uuid.uuid4())
        print("init..."+filename)

    def send_json_file(self, filename):
        status = self.s3.Object(self.s3_bucket_name, filename).put(Body=open(filename, 'rb'))
        print("successfully sent")


config = cnf.Config('config.yaml')
s3uploader = S3Uploader(config.get_config())
s3uploader.send_json_file("data3.json")



