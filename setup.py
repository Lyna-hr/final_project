from setuptools import setup, find_packages

setup(
    name='final_project_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Include your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'final_project = final_project_package.main_module:main'
        ],
    },
    author='Lyna',
    author_email='lyna.hr2005@gmail.com',
    description='Final Project Package created by Lyna',
    url='https://github.com/Lyna-hr/final_project.git',
)

