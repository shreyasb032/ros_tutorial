from setuptools import find_packages, setup

package_name = 'my_package_py'

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
    description='Beginner client libraries tutorials practice package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node_py = my_package_py.my_node_py:main'
        ],
    },
)
