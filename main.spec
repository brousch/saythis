# -*- mode: python -*-
from kivy.tools.packaging.pyinstaller_hooks import install_hooks
install_hooks(globals())

a = Analysis(['saythis/main.py'],
             pathex=['/home/brousch/Projects/saythis'],
             hiddenimports=['plyer.platforms.linux.tts'],
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='main',
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               Tree('./saythis/'),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='main')
