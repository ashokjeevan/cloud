#!/usr/bin/env python3

from aws_cdk import core

from lambda_cron.lambda_cron_stack import LambdaCronStack


app = core.App()
LambdaCronStack(app, "lambda-cron")

app.synth()
