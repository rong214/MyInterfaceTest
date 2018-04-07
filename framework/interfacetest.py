# coding=utf-8
__author__ = 'tyr'
import sys
sys.path.append("E:\PythonFile\InterfaceTest\com\tyr\common")
from framework.re import Interface_Request

class InterfaceTest:
    def testrequest(self,url,uri,params,reqform,dataform,checkpoint,headers,i,sheet,num,name,log):
        req = Interface_Request()
        full_url = url + uri
        if(reqform == 'GET'):
            self.req_test = req.req_get(full_url,params,headers)
        elif(reqform == 'POST' and dataform == 'Form'):
            self.req_test = req.post_kv(full_url,params,headers)
        elif(reqform == 'POST' and dataform == 'Json'):
            headers = {'Content-Type':'application/json;charset=utf-8'}
            self.req_test = req.post_json(full_url,params,headers)
        else:
            print ("请求不通过，请检查case用例配置")
        print (self.req_test)
