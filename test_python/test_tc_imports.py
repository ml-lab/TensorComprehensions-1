# Copyright (c) 2017-present, Facebook, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################

"""
Naive test for make sure pybinds don't break
"""

import unittest


class TestCase(unittest.TestCase):

    def test_imports(self):
        from tensor_comprehensions.tc import ATenCompilationUnit
        from tensor_comprehensions.mapping_options import Options
        from tensor_comprehensions.autotuner import ATenAutotuner
        print('\nImported TC, mapping_options and Autotuner successfully')


if __name__ == '__main__':
    unittest.main()
