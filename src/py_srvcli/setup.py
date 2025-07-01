from setuptools import find_packages, setup

package_name = 'py_srvcli'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Shreyas Bhat',
    maintainer_email='shreyas1335@gmail.com',
    description='Python client and server tutorial',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'add_two_ints_client = py_srvcli.add_two_ints_client:main',
            'add_two_ints_server = py_srvcli.add_two_ints_server:main',
            'add_three_ints_client = py_srvcli.add_three_ints_client:main',
            'add_three_ints_server = py_srvcli.add_three_ints_server:main',
        ],
    },
)
