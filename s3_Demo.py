"""Classes for s3 Buckets."""

import boto3

class BucketManager:
    """Manage s3 Buckets"""

    def __init__(self, session):
        """Create a BucketManager object."""
        self.session = session
        self.s3 = self.session.resource('s3')

    def all_buckets(self):
        """List all s3 buckets"""
        return self.s3.buckets.all()


    

