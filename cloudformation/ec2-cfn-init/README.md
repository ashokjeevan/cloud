# Cfn-init

The cloud formation template cfn_init.yml file creates an EC2 instance with Apache HTTP server running.

The latest AMI ID is being taken from the parameters section by:

`
LatestAmiId :
    Type : 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    Default: '/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2'
`

This stack utilises cfn-init helper script to install httpd. 
