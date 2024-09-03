from setuptools import setup, find_packages

setup(
    name="pytest-test-info",
    version="0.1.0",
    description="A pytest plugin to set test information",
    long_description=open('README.md').read(),
    author='Sergei Konovalov',
    author_email='l0kifs91@gmail.com',
    url='https://github.com/l0kifs/pytest_test_info',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "pytest11": [
            "test_info = test_info.plugin:plugin"
        ]
    },
    install_requires=[
        'pytest>=8.0.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Framework :: Pytest',
        'Framework :: Pytest :: Plugin',
    ],
)
