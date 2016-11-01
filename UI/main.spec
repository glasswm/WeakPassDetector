# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['D:\\WeakPassDetector', 'D:\\WeakPassDetector\\client', 'D:\\Python27\\Lib', 'D:\\Python27\\Lib\\site-packages', 'C:\\Users\\Dieuroi\\AppData\\Roaming\\Python\\Python27', 'C:\\Users\\Dieuroi\\AppData\\Roaming\\Python\\Python27\\site-packages', 'D:\\WeakPassDetector\\UI'],
             binaries=None,
             datas=None,
             hiddenimports=['_cffi_backend', 'appdirs'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries+ [('oraociei12.dll', 'D:\Oracle\instantclient_12_1\oraociei12.dll', 'BINARY')],
          a.zipfiles,
          a.datas,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=True )
