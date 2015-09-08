# s3keygen
S3 Hash Key Generator based on date

# Objective

S3 key generation has to be as unique as possible to avoid race conditions while processing at scale

# Usage

python s3keygen.py --date <date in yyyymmddd>

example: python s3keygen.py --date 20150101