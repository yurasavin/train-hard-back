from apps.api.serializers.aws_requests import AWSRequestLessSerializer


aws_request_create_schema = {
    'responses': {
        '201': AWSRequestLessSerializer,
    },
}

aws_request_approve_and_reject_schema = {
    'responses': {
        '200': AWSRequestLessSerializer,
    },
}
