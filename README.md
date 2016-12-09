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

4. Deploy to AWS EB using the following command
    ```
    eb deploy
    ```