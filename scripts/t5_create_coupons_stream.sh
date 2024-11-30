#!/bin/bash

awslocal kinesis create-stream --stream-name coupons --shard-count 5
