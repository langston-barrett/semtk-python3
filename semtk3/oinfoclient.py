#
# Copyright 2019-20 General Electric Company
#
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
#
from . import semtkclient


class OInfoClient(semtkclient.SemTkClient):
    
    def __init__(self, serverURL, conn_json_str):
        ''' servierURL string - e.g. http://machine:12050
        '''
        super(OInfoClient, self).__init__(serverURL, "ontologyinfo")
        self.conn_json_str = conn_json_str
    
    #
    # Upload owl.
    # Default to model[0] graph in the connection
    #
    def exec_get_uri_label_table(self):
        
        payload = {
            "jsonRenderedSparqlConnection": self.conn_json_str
        }

        res = self.post_to_table("getUriLabelTable", payload)
        return res
