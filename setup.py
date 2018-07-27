import os
from distutils.command.build import build

from django.core import management
from setuptools import find_packages, setup

try:
    with open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''


class CustomBuild(build):
    def run(self):
        management.call_command('compilemessages', verbosity=1, interactive=False)
        build.run(self)


cmdclass = {
    'build': CustomBuild
}


setup(
    name='byro-cnss',
    version='0.0.1',
    description='Byro plugin for CNSS (Clausewitz-Netzwerk für Strategische Studien e.V.)',
    long_description=long_description,
    url='https://github.com/henryk/byro-cnss',
    author='Henryk Plötz',
    author_email='henryk@ploetzli.ch',
    license='Apache Software License',

    install_requires=[],
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    cmdclass=cmdclass,
    entry_points="""
[byro.plugin]
byro_cnss=byro_cnss:ByroPluginMeta
""",
)