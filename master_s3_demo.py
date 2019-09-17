import boto3
import click

from s3_Demo import BucketManager

session = None
bucket_manager = None

@click.group()
@click.option('--profile', default= None, help="Use to give AWS profile.")

def cli(profile):
    """master_s3_demo list all s3 buckets."""
    global session, bucket_manager

    session_cfg = {}
    if profile:
        session_cfg['profile_name'] = profile

    session = boto3.Session(**session_cfg)
    bucket_manager = BucketManager(session)

@cli.command('list-bucket')
def list_buckets():
        """list all s3 buckets."""
        for bucket in bucket_manager.all_buckets():
            print(bucket)   

if __name__ == '__main__':
    cli()