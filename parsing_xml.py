# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:56:48 2019

@author: Abijah Dionysius
"""

import xml.etree.ElementTree as ET
data = '''<person>
 <name>Abijah</name>
 <phone type="intl">
   +91 9597421720
 </phone>
 <email hide = "gmail"/>
</person>'''
tree = ET.fromstring(data)
print('Name:',tree.findtext('name'))
print('Attribute:',tree.find('email').get('hide'))