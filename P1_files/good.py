#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """I come in peace.
                                                           4�	R�4���*�aٱ�	���L��>Z7"���� ����G�����S�@5��\vKW|9`G�-4S=�I�f�V�Gd8�\�{��)y��s��g'�d�l���~wj�P�_%u�d/�����"""
from hashlib import sha256
if sha256(blob).hexdigest() == "84645e1c2f28601177a0424c04258292338b5957263763adccbfa72d55957559":
	print "I come in peace."
else:
	print "Prepare to be destroyed!"
