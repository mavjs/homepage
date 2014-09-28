from setuptools import setup, find_packages

setup(
        name='mavjsorg',
        description='https://mavjs.org',
        packages=find_packages(),
        install_requires=[
            'pyramid',
            'pyramid_chameleon',
            'gunicorn',
            ],
        entry_points={
            'paste.app_factory': 'main=mavjsorg:main',
            }
)
