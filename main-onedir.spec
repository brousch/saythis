# -*- mode: python -*-
from kivy.tools.packaging.pyinstaller_hooks import install_hooks
install_hooks(globals())

a = Analysis(['saythis/main.py'],
             pathex=['./'],
             hiddenimports=['plyer.platforms.linux.tts',
                            'plyer.platforms.win.tts'],
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='saythis.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False,)
coll = COLLECT(exe,
               Tree('./saythis/'),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='main')
