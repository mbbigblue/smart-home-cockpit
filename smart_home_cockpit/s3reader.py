import boto3
import uuid
import config as cnf


class S3Reader:
    def __init__(self, aws_config):
        self.s3_bucket_name = aws_config['aws']['s3_bucket_name']
        self.s3 = boto3.resource('s3',
                                 aws_access_key_id=aws_config['aws']['aws_access_key_id'],
                                 aws_secret_access_key=aws_config['aws']['aws_secret_access_key'])
        filename = str(uuid.uuid4())
        print("init..."+filename)

    def read_all_jsons(self):
        s3bucket = self.s3.Bucket(self.s3_bucket_name)
        bucket_list = []

        for obj in s3bucket.objects.all():
            key = obj.key
            body = obj.get()['Body'].read()
            bucket_list.append(key)

        print(bucket_list[0:10])


config = cnf.Config('config.yaml')
s3reader = S3Reader(config.get_config())
print(s3reader.read_all_jsons())