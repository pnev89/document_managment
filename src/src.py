from fetch_data_from_s3 import S3Data

S3Bucket = S3Data(
    bucket_name="de-tech-assessment-2022", mount_path="/Users/pedroneves/Downloads/data"
)


S3Bucket.mount_bucket()
