provider "aws" {
  version = "~> 2.2"
  region  = "us-east-1"

  allowed_account_ids = ["730729458921"]
}

# Note: this portion was added after manually running the initial setup and manually uploading
#       the tfstate file to the newly created S3 bucket.
terraform {
  required_version = "= 0.12"

  backend "s3" {
    bucket  = "calorie-calculator-state"
    key     = "setup/main.tfstate"
    region  = "us-east-1"
    encrypt = true
  }
}

resource "aws_s3_bucket" "providers" {
  bucket = "calorie-calculator-state"
  acl    = "private"

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }

  tags = {
    name      = "calorie-calculator-state"
    component = "calorie-calculator"
  }
}

resource "aws_s3_bucket_public_access_block" "tfstate_bucket_no_public" {
  bucket = "${aws_s3_bucket.providers.id}"

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_iam_user" "circleci" {
  name = "calorie-calculator-circleci"
  path = "/calorie-calculator/"

  tags = {
    component = "calorie-calculator"
  }
}

resource "aws_iam_user_policy_attachment" "circleci-perms" {
  user       = "${aws_iam_user.circleci.name}"
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}
