# Project configuration file for PUG.
#
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name, line-too-long
#
# (c) 2019 Timothy Lin <timothy.gh.lin@gmail.com>, BSD 3-Clause License.
#

import os

DEFAULT_GCC_TAG = 'GCC5'
DEFAULT_GCC_TAG = 'CLANG9PE'

DEFAULT_EDK2_TAG = os.environ.get('EDK2_TAG', 'edk2-stable201905')
DEFAULT_MSVC_TAG = os.environ.get('MSVC_TAG', 'VS2012x86')
DEFAULT_EDK2_REPO = os.environ.get('EDK2_REPO', 'https://github.com/lgao4/edk2.git')
DEFAULT_XCODE_TAG = 'XCODE5'
DEFAULT_TARGET_ARCH = os.environ.get('TARGET_ARCH', 'X64')              # 'IA32', 'X64', 'IA32 X64'
DEFAULT_BUILD_TARGET = os.environ.get('BUILD_TARGET', 'RELEASE')        # 'DEBUG', 'NOOPT', 'RELEASE', 'RELEASE DEBUG'
DEFAULT_WORKSPACE_DIR = os.environ.get('WORKSPACE', os.getcwd())
DEFAULT_PATH_APPEND_SIGNATURE = False

DEFAULT_EDK2_TAG = 'llvm9'
#DEFAULT_UDK_DIR = os.environ.get('UDK_DIR', os.path.join(os.path.expanduser('~'), '.cache', 'pug', 'edk2'+'-'+DEFAULT_EDK2_TAG))
DEFAULT_UDK_DIR = os.path.join(os.getcwd(), 'edk2'+'-'+DEFAULT_EDK2_TAG)
#DEFAULT_EDK2_TAG = 'edk2-stable201905'

CODETREE = {
#    # edk2-libc is a new edk2 repo since edk2-stable201905. StdLib resides in this repo.
#    'edk2-libc'    : {
#        'path'          : os.path.join(os.path.expanduser('~'), '.cache', 'pug', 'edk2-libc'),
#        'source'        : {
#            'url'       : 'https://github.com/tianocore/edk2-libc.git',
#            'signature' : '6168716',   # 61687168fe02ac4d933a36c9145fdd242ac424d1 @ Apr/25/2019
#        },
#        'multiworkspace': True,
#    },
#    'FmpSamplePkg'    : {
#        'path'          : os.path.join(os.getcwd(), 'FmpSamplePkg'),
#        'source'        : {
#            'vcs'       : 'svn',
#            'url'       : 'https://ptl-disco/svnrepos/SCT4/trunk/Features/FmpSamplePkg',
#            'signature' : '',
#        },
#        'multiworkspace': True,
#    }
}


###################################################################################################


if __name__ == '__main__':
    import sys
    sys.dont_write_bytecode = True      # To inhibit the creation of .pyc file

    if os.name == 'nt':
        #os.environ['CLANG_HOST_BIN']='n'
        #os.environ['CLANG9PE_BIN']='C:\\Program Files\\LLVM9\\bin\\'
        #os.environ['IASL_PREFIX']='c:\\Asl\\'
        pass
    else:
        os.environ['CLANG9PE_BIN']='/usr/bin/'

    PKG_DSC = 'OvmfPkg/OvmfPkgX64.dsc'
    IPUG_CMD = 'ipug -p {0} {1}'.format(PKG_DSC, ' '.join(sys.argv[1:]))
    print(IPUG_CMD)
    os.system(IPUG_CMD)
