import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="lambda_cron",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "lambda_cron"},
    packages=setuptools.find_packages(where="lambda_cron"),

    install_requires=[
        "aws_cdk.core==1.51.0",
        "aws_cdk.aws_events",
        "aws_cdk.aws_events_targets",
        "aws_cdk.aws_lambda"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
