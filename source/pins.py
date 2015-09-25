#!/usr/bin/python
# Copyright (c) 2015, ARM Limited, All Rights Reserved
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import json
import sys

jsonfile = open(sys.argv[1])
outputfile = open(sys.argv[2],'w')

ocfg = json.load(jsonfile)
jsonfile.close()
pins = {}
if 'hardware' in ocfg:
    if 'pins' in ocfg['hardware']:
        pins = ocfg['hardware']['pins']

f = outputfile

template = '''
/****************************************************************************
 * Copyright (c) 2015, ARM Limited, All Rights Reserved
 * SPDX-License-Identifier: Apache-2.0
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may
 * not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 ****************************************************************************
 */
/* WARNING: THIS FILE IS AUTOMATICALLY GENERATED.  DO NOT EDIT.  ANY CHANGES
 *          SHOULD BE MADE IN config.json OR target.json
 */
%s
'''

indent = '    '
pin_array = []

while len(pins.keys()):
    for pin in pins.keys()[:]:
        if pins[pin] in pins.keys():
            continue
        pin_array += ['{key} = {value}'.format(key=pin, value=pins[pin])]
        del pins[pin]

pin_str = indent + (',\n'+indent).join(pin_array)

f.write(template%pin_str)
f.close()
