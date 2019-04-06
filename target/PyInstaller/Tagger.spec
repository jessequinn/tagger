# -*- mode: python -*-

block_cipher = None


a = Analysis(['/home/jessequinn/PycharmProjects/tagger/src/main/python/main.py'],
             pathex=['/home/jessequinn/PycharmProjects/tagger/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/home/jessequinn/.pyenv/versions/3.6.8/envs/tagger-3.6.8/lib/python3.6/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/tmp/tmpsfbz5k91/fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Tagger',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='Tagger')
