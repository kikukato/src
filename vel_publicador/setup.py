from setuptools import find_packages, setup

package_name = 'vel_publicador'

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
    maintainer='kikukato',
    maintainer_email='jean.henriquez@uao.edu.co',
    description='nodo publicador de velocidades para Tharry',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publicador_cmd = vel_publicador.publicador_cmd:main',
            'p_serial = vel_publicador.p_serial:main',
        ],
    },
)
