from urllib.parse import quote_plus
from sqlalchemy.engine import create_engine
from dotenv import load_dotenv
import os

SCHEMA_NAME = "ijscctest"
S3_STAGING_DIR = "s3://ijscctest/"
AWS_REGION = "us-east-1"

load_dotenv()

conn_str = (
    "awsathena+rest://{aws_access_key_id}:{aws_secret_access_key}@"
    "athena.{region_name}.amazonaws.com:443/"
    "{schema_name}s3_staging_dir{s3_staging_dir}&work_group=primary"
)

engine = create_engine(
    conn_str.format(
        aws_access_key_id=quote_plus(os.getenv('AWS_ACCESS_KEY')),
        aws_secret_access_key=quote_plus(os.getenv('AWS_SECRET_KEY')),
        region_name=AWS_REGION,
        schema_name=SCHEMA_NAME,
        s3_staging_dir=quote_plus(S3_STAGING_DIR),
    )
)

athena_connection = engine.connect()