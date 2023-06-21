"""Fetches last data from S3 bucket"""
from typing import List, Optional

import boto3

from utilities import log


class S3Data:
    """Mounts the bucket and reads data from S3"""

    def __init__(
        self,
        bucket_name: str,
        mount_path: str,
        username: Optional[List[str]] = None,
        password: Optional[List[str]] = None,
    ):
        """Creates an S3Data object"""
        if not isinstance(bucket_name, str):
            raise TypeError(f"bucket_name should be str not type {type(bucket_name)}")
        if not isinstance(mount_path, str):
            raise TypeError(f"bucket_name should be str not type {type(mount_path)}")
        if not (username is None or isinstance(username, str)):
            raise TypeError(f"username should be str not type {type(username)}")
        if not (password is None or isinstance(password, str)):
            raise TypeError(f"password should be str not type {type(password)}")

        self.bucket_name = bucket_name
        self.mount_path = mount_path
        self.username = username
        self.password = password

    def mount_bucket(self):
        """Mount AWS S3 bucket.

        This function mounts an AWS S3 bucket to Databricks File System (DBFS). The bucket
        to be mounted is specified by the
        :py:obj:`DATA_AWS_S3_BUCKET <datalakehouse.control.variables.DATA_AWS_S3_BUCKET>`
        variable. The mounted bucket can be accessed at
        /mnt/:py:obj:`DATA_AWS_S3_BUCKET_ALIAS <datalakehouse.control.variables.DATA_AWS_S3_BUCKET_ALIAS>`.

        """

        # Set the S3 bucket name and local mount path
        bucket_name = self.bucket_name  #'de-tech-assessment-2022'
        mount_path = self.mount_path  #'/Users/pedroneves/Downloads/data'

        # Create a session using your AWS credentials
        session = boto3.Session()

        # Create an S3 client using the session
        s3_client = session.client("s3")

        # Mount the S3 bucket to the local mount path
        s3_client.download_file(
            bucket_name, "", mount_path, ExtraArgs={"RequestPayer": "requester"}
        )

        log("Bucket mounted successfully at:", mount_path)
