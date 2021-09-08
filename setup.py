from setuptools import setup, find_packages
  
setup(
    name='GITS',
    version='0.1',
    description='GITS project',
    author='CSC510 - Group 16',
    author_email='',
    packages=find_packages(),
    tests_require=['pytest'],
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Development Status :: 4 - Alpha",
          "Intended Audience :: Developers",
          "Topic :: GITS Project",
      ],

      license='MIT',
      install_requires=[
        'pytest',
      ]
)
