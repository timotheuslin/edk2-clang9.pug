#!/usr/bin/python3

#
# Project configuration file for PUG.
#
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name, line-too-long
#
# (c) 2019 Timothy Lin <timothy.gh.lin@gmail.com>, BSD 3-Clause License.
#

import os
import sys

DEFAULT_GCC_TAG = DEFAULT_MSVC_TAG = 'CLANG9'
DEFAULT_EDK2_TAG = 'c801f33d818b8010fabb93092c661c6f30d42b13'   # TODO: formally supported at edk2-stable201911


###################################################################################################


if __name__ == '__main__':
    sys.dont_write_bytecode = True  # To inhibit the creation of .pyc file

    if os.name == 'nt':
        os.environ['CLANG9_BIN'] = 'C:/Program Files/LLVM/bin/'
        os.environ['IASL_PREFIX'] ='C:/Asl/'
        os.environ['CLANG_HOST_BIN'] = 'n'
    elif sys.platform == 'darwin':
        os.environ['CLANG9_BIN'] = f'{os.path.expanduser("~")}/clang+llvm-9.0.0-x86_64-darwin-apple/bin'
    else:
        os.environ['CLANG9_BIN'] = f'{os.path.expanduser("~")}/clang+llvm-9.0.0-x86_64-linux-gnu-ubuntu-18.04/bin/'

    PKG_DSC = 'OvmfPkg/OvmfPkgX64.dsc'
    IPUG_CMD = f'ipug -p {PKG_DSC} {" ".join(sys.argv[1:])}'
    print(IPUG_CMD)
    os.system(IPUG_CMD)
