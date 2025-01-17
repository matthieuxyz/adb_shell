from setuptools import setup

setup(
    name='adb_shell',
    version='0.0.7',
    description='ADB shell functionality',
    author='Jeff Irion',
    author_email='jefflirion@users.noreply.github.com',
    packages=['adb_shell', 'adb_shell.auth'],
    install_requires=['cryptography', 'pyasn1', 'rsa'],
    tests_require=['pycryptodome'],
    classifiers=['Operating System :: OS Independent',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 2'],
    test_suite='tests'
)
