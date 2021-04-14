from setuptools import setup


with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="package-jdm-ia",
    version="production",
    description="Classificador JDM IA",
    author="JDM Team",
    install_requires=requirements,
)
