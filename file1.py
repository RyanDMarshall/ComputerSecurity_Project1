#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           �#�]E��I,�xsH��q6���
!&9*�/������d7�O��
�1Qv�=T-��'e��0xb�Kހ��R�C�����"+�����G_kA������z���o٤Y�*�	��b���
�O9��B"""
from hashlib import sha256
print sha256(blob).hexdigest()
