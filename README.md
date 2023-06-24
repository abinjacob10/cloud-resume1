# Cloud Resume Challenge

This project is based on a [challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws/) conceptualized by [Forrest Brazeal](https://forrestbrazeal.com/)

The basics of this challenge is to host a resume written in HTML in a public cloud and show the the number of visits to the website visitors. Website counts need to be maintained in a database and updated at every website visit. Click operation should be avoided, rather coding should be adopted to create the required Infrastructure resources(IaC-Infrastructure as Code). Finally, any change made in backend end need to be tested before re-building and deploying to public cloud using Github Actions. Any change made in front end also needs to be updated with the public cloud hosting using Github Actions.



**Click-operations for initial testing**

During initial phase, first the front end part was tested using click-operations in Amazon Cloud.
Resources required for this was:

1. An HTML file which is the resume, with a bit of styling done using css file.

2. S3 bucket, named it same as the website domain **abininireland.click** and hosted it in eu-west-1(Ireland) region.

      - Required public access. Actions set to **s3:GetObject**, Principal set to **"*"** meaning everyone is allowed access to the bucket.
  
3. Required IAM permissions for current user     

4. A domain- Domain was registered with AWS Route 53 for $3 named it **abininireland.click**

      - A type record was configured pointing to cloud front URL.

5. AWS Certificate Manager's SSL certificate.
   
      - Required linking with Cloud front distribution's URL.
   
      - CNAME record was required to be copied to Route 53'S hosted zone.

6. AWS Cloud Front distribution URL.

      - Required linking with S3 bucket origin domain.

      - Required linking with AWS Certificate Manager.

      - Required linking with the resistered domain.



After the front end was successfully tested. i.e. when abininireland.click was typed and entered in web browser, HTML file was visible, above configuration was moved to **AWS SAM**. **Rest of the IaC was built on the sample hello-world **YAML** template generated when SAM was first initialized in local Ubuntu machine**. Before building and deploying from AWS SAM, IAM for the SAM user was configured to grant permissions for: S3, CloudFront, Route 53, Cloudformation, AWS Certificate Manager, Lambda functions and API gateways.

- Two separate Lambda functions are used to update and get count from DynamoDB table. Each lambda function invoked by its own API. For "get_function" Lambda function, API trigger is (https://jc5qyxzdo8.execute-api.eu-west-1.amazonaws.com/Prod/get). For "put_function"(updates the count) Lambda function API trigger is (https://jc5qyxzdo8.execute-api.eu-west-1.amazonaws.com/Prod/put).

- A java script in S3 bucket embedded in the main index.html file carries the code to fetch the responses from API's using fetch() method.
The response from Lambda to API calls made from browser do takes care of CORS(Cross Origin Resource Sharing- which is used to allow client requests coming from a different origin than the server's origin, in this example: web-browser and lambda are in two different origins) CORS headers returned from each lambda are: access-control-allow-origin:*,access-control-allow-headers:*,access-control-allow-methods:*.






