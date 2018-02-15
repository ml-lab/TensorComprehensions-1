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

import tensor_comprehensions as tc

import torch
import torch.cuda
import unittest


class TestMaxPool(unittest.TestCase):

    def test_maxpool(self):
        # NOTE: take note of use of {{ }}
        LANG="""
        def maxpool(float(B, C, H, W) input) -> (output) {{
            output(b, c, h, w) max= input(b, c, h * {sH} + kh, w * {sW} + kw) where kh in 0:{kH}, kw in 0:{kW}
        }}
        """
        maxpool = tc.define(LANG, name="maxpool", constants={"sH":1, "sW":1, "kH":2, "kW":2})
        inp = torch.ones(32, 3, 10, 10).cuda()
        out = maxpool(inp)


if __name__ == '__main__':
    unittest.main()
