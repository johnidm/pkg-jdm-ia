from setuptools import setup


with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="txtclf-jdm-ia",

    packages=[
        "iara.jdm_iara",
    ],
    package_dir={
        "iara.jdm_iara": "jdm_ia/src",
    },

    version="production",
    description="Classificador JDM IA",
    author="JDM Team",
    install_requires=requirements,
)
