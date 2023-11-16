from setuptools import setup, find_packages

setup(
    name='PySQLiteDBConnection',
    version='1.0.0-a',
    author='SurivZ',
    author_email='franklinserrano23@email.com',
    description='Paquete para manejar conexiones de bases de datos SQLite3 y operaciones CRUD.',
    long_description=open('readme.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SurivZ/Py-SQLite-DB-Connection',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.7',
    install_requires=[],
)
