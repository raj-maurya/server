WorldBrain Server
====

Steps for deployment:

1. Install ElasticBeanstalk CLI
    ```
    pip install --upgrade --user awsebcli
    ```
2. Install AWS CLI
    ```
    pip install awscli
    ```
3. Type `aws configure` to configure AWS client<br>
    ```
    $ aws configure
     AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
     AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
     Default region name [None]: us-west-2
     Default output format [None]: json
    ```
2. Deploy to AWS EB using the following command
    ```
    eb deploy
    ```