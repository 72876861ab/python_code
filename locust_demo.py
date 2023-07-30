# coding: utf-8
# 我是谁
from locust import task,HttpUser
import os

class tast_s(HttpUser):
    host = "http://novel.hctestedu.com"

    @task
    def task_1(self):
        url = "/book/queryBookDetail/134"
        res = self.client.request(method="get",url = url)
        print(res.json())

if __name__ =='__main__':
    os.system('locust -f locust_demo.py  --web-host = "127.0.0.1"')