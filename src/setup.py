from setuptools import setup
import setup_translate

pkg = 'Extensions.SPDyn'
setup(name='enigma2-plugin-extensions-spdyn',
       version='3.0',
       description='a client for www.spdyn.eu',
       package_dir={pkg: 'SPDyn'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'icon.png']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
