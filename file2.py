#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           �#�]E��I,�xsH��q6��
!&9*�/������d7�O��
f2Qv�=T-��'���0xb�Kހ��R�C�����"+�����G_kA������z���o٤��*�	��b���
��9��B"""
from hashlib import sha256
print sha256(blob).hexdigest()
