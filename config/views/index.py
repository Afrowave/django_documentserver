"""

 (c) Copyright Ascensio System SIA 2023

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.

"""

import re
import sys
import json

from django.shortcuts import render

from config.configuration import ConfigurationManager
from config.format import FormatManager
from config.utils import users
from config.utils import docManager

config_manager = ConfigurationManager()
format_manager = FormatManager()


def getDirectUrlParam(request):
    if ('directUrl' in request.GET):
        return request.GET['directUrl'].lower() in ("true")
    else:
        return False


def default(request):  # default parameters that will be passed to the template
    context = {
        'users': users.USERS,
        'languages': config_manager.languages(),
        'preloadurl': config_manager.document_server_preloader_url().geturl(),
        # file extensions that can be edited
        'editExt': json.dumps(format_manager.editable_extensions()),
        # file extensions that can be converted
        'convExt': json.dumps(format_manager.convertible_extensions()),
        # information about stored files
        'files': docManager.getStoredFiles(request),
        'fillExt': json.dumps(format_manager.fillable_extensions()),
        'directUrl': str(getDirectUrlParam(request)).lower
    }
    # execute the "index.html" template with context data
    # and return http response in json format
    return render(request, 'pages/home.html', context)
