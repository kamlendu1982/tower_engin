from setuptools import setup

setup(
    name="pyaap-api-tools",
    version='0.0.1',
    install_requires=[
        "requests",
        'importlib-metadata; python_version<"3.8"',
    ],
)

