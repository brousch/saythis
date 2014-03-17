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
          Tree('./saythis/'),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False,
          icon='saythis\\resources\\saythis.ico')