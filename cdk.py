#!/usr/bin/env python3

from aws_cdk import core

from src.stacks.pipeline_stack import PipelineStack


app = core.App()
PipelineStack(app, "mvp-data-pipeline-aws")

app.synth()
