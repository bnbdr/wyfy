from setuptools import setup

author = 'bnbdr'
setup(
    name='wyfy',
    version='0.1',
    author=author,
    author_email='bad.32@outlook.com',
    description="print wifi passwords (windows only)",
    license='MIT',
    keywords='wifi',
    packages=['wyfy'],
    entry_points = {
        'console_scripts': ['wyfy=wyfy.wyfy:main'],
    },
    classifiers=(
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ),
)
