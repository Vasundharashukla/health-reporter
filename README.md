# Health Reporter

Health reporter is a REST API  built in flask that can be used to retrieve the metrics information and metadata of an AWS EC2 instance.

## Technology Used
- **Programming Languages**
	- Python
	
- **Frameworks**
	- Flask 1.1.1
	
- **AWS SDK**
	- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html "boto3") - The AWS SDK for python to retrieve metric details.
	- [ec2-metadata](https://github.com/adamchainz/ec2-metadata "ec2-metadata") -  An easy interface to query the EC2 metadata API using python.

## API Endpoints

- /fork/metrics - Accepts a post request with json data in the given format:
```javascript
{
    "dimensions": [
        {
            "Name": "InstanceId", "Value": <your-instance-id>
        }
        // Value of all the instance ids. Default value is empty.
    ],
    "attributes": [
        // all the metric names for which you want data. Default value is empty
    ],
    "interval": 2 // <number of days for which you need data. default value is 2.>
}
```
- /fork/metadata - get metadata for your instance. No payload required.

## Credits
- API created and developed by [Vasundhara Shukla](https://github.com/Vasundharashukla/ "Vasundhara Shukla").
- Contact Email: [17ucc065@lnmiit.ac.in](mailto:17ucc065@lnmiit.ac.in "17ucc065@lnmiit.ac.in")
