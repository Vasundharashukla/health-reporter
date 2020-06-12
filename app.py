import boto3
from pprint import pprint
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from ec2_metadata import ec2_metadata as ecm

app = Flask(__name__)
app.config["SECRET_KEY"] = "vasundharashukla7998"

cloudwatch = boto3.client('cloudwatch', aws_access_key_id="AKIAJXHELWW6SCJMI7DA",
                          aws_secret_access_key="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", region_name='ap-south-1')

##paginator = cloudwatch.get_paginator('list_metrics')
##for response in paginator.paginate(MetricName='CPUUtilization',
##                                   Namespace='AWS/EC2'):
##    pprint(response['Metrics'])

def metricStats(metric, dims, time=2):
    response = cloudwatch.get_metric_statistics(
            Namespace = 'AWS/EC2',
            Period = 3600,
            MetricName = metric,
            Statistics=['Maximum'],
            Dimensions = dims,
            StartTime=datetime.utcnow()-timedelta(days=time),
            EndTime= datetime.utcnow(),
        )

    return response
@app.route('/fork/<value>', methods=["GET"])
def fork(value):
    if value == "metrics":
        try:
            attributes = request.get_json(force=True)
            print(attributes)
            resp = dict()
            dims = attributes.get('dimensions', {})
            interval = attributes.get('interval', 2)
            for attr in attributes.get('attributes', []):
                resp[attr] = metricStats(attr, dims, interval)
            return jsonify(result=resp)
        except Exception as e:
            print(e)
            return jsonify({"result": "error occured"})
        
    if value == "metadata":
        try:
            metadata = {"instance-id": ecm.instance_id,
                        "instance-type": ecm.instance_type,
                        "public-ipv4": ecm.public_ipv4,
                        "ami-id": ecm.ami_id,
                        "hostname": ecm.public_hostname}
            return jsonify({"result": metadata})
        except Exception as e:
            print(e)
            return jsonify({"result": "error occured"})
        
    return jsonify({"result": "not allowed"})
