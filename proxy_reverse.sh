#! /bin/bash
ssh -fNn -i ~/.ssh/aws_ozy.pem -R 8080:localhost:22 ubuntu@ec2-34-201-106-54.compute-1.amazonaws.com
