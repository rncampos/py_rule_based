
from setuptools import setup, find_packages
setup(name='py_rule_based',
      version='1.0',
      description='Date extractor based on regex rules',
      author='Jorge Alexandre Rocha Mendes',
      author_email='mendesjorge49@gmail.com',
      url='https://github.com/JMendes1995/py_rule_based.git',
      packages=find_packages(),
      include_package_data=True,
      py_modules=['py_rule_based'],
      entry_points={
            'console_scripts': [
                  'py_rule_based=py_rule_based.cli:dates'
            ]
      },
)

