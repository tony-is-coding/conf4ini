import os

from setuptools import setup
from setuptools import find_packages

# or
# from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, 'README.rst')) as f:
        README = f.read()

except IOError:
    README = CHANGES = ''

docs_extras = [
    'Sphinx >= 1.3.1',
]

setup(
    name='conf4ini',  # 包名字
    version='1.0.0',  # 包版本
    description='a simple config reader for *.ini files',  # 简单描述
    url='https://github.com/tony-is-coding/conf4ini',
    author='tony-is-coding',  # 作者
    author_email='newbiwtan@163.com',  # 作者邮箱
    maintainer="tony-is-coding",
    packages=find_packages(),  # 包
    install_requires=[],
    long_description=README,
    classifiers=[  # 关于包的其他元数据(metadata)
        "Programming Language :: Python :: 3",  # 该软件包仅与Python3兼容
        "License :: OSI Approved :: MIT License",  # 根据MIT许可证开源
        "Operating System :: OS Independent",  # 与操作系统无关
    ],
    extras_require={
            'docs': docs_extras,
        },
)
