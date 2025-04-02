#
#    Metrix++, Copyright 2009-2019, Metrix++ Project
#    Link: https://github.com/metrixplusplus/metrixplusplus
#    
#    This file is a part of Metrix++ Tool.
#    

import re

def notify(path, metric, details, region="", line=""):
    notification = ""

    for each in details:
        if str(each[1]) != 'None':
            format_string = "{metric} {{file=\"{path}\""
            input = {"metric": re.sub(r'^_', '', re.sub(r'[\.\:]', '_', metric + "." + str(each[0]))), "path": path}
            if region:
                format_string += ", region=\"{region}\""
                input["region"] = region
            if line:
                format_string += ", line=\"{line}\""
                input["line"] = line
            format_string += "}} {value}\n"
            input["value"] = str(each[1])
            notification += format_string.format(**input)
    print(notification)
