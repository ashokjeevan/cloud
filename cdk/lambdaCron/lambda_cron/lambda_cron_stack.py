from aws_cdk import (
    aws_events as events,
    aws_lambda as _lambda,
    aws_events_targets as targets,
    core,
    )

class LambdaCronStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        my_lambda = _lambda.Function(
            self, id='HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.asset('lambda'),
            handler='hello.handler'
        )