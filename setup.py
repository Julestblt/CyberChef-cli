from setuptools import setup, find_packages

setup(
    name='cyberchef-cli',
    version='0.1.0',
    url='https://github.com/yourusername/cyberchef-cli.git',
    author='Your Name',
    author_email='your.email@example.com',
    description='CLI for CyberChef operations',
    packages=find_packages(),    
    install_requires=['questionary'],
)