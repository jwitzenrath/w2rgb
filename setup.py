from setuptools import setup, find_packages

source_path = 'src'
packages = find_packages(source_path)

distribution = setup(name='w2rgb',
                     version='1.0.0',
                     packages=packages,
                     package_dir={'': source_path},
                     entry_points={
                        'console_scripts': [
                            'w2rgb = w2rgb.main:main',
                        ],}
                     )
