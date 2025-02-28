"""Install midi-ddsp."""

import setuptools

with open('README.md') as f:
  long_description = f.read()

setuptools.setup(
  name='midi-ddsp',
  version='0.1.2',
  description='Synthesis of MIDI with DDSP',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='Google Inc. & Yusong Wu',
  author_email='no-reply@google.com, wuyusongwys@gmail.com',
  url='http://github.com/magenta/midi-ddsp',
  license='Apache 2.0',
  packages=setuptools.find_packages(),
  scripts=[],
  install_requires=[
    'ddsp',
    'pretty_midi',
    'music21',
    'pandas',
    # (yusongwu) Force overwriting tfds-nightly as tfds-nightly
    # will raise error under windows.
    'tensorflow_datasets'
  ],
  extras_require={
    'test': ['pytest', 'pylint!=2.5.0'],
  },
  entry_points={
    'console_scripts': [
      'midi_ddsp_synthesize = midi_ddsp.midi_ddsp_synthesize:main',
      'midi_ddsp_download_model_weights = midi_ddsp.download_model_weights:main'
    ],
  },
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: Apache Software License',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
  ],
  tests_require=['pytest'],
  setup_requires=['pytest-runner'],
  keywords='audio MIDI MIDI-synthesizer machinelearning music',
)
