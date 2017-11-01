from concurrent.futures import ThreadPoolExecutor
import time,requests

#url 请求使用多线程 （IO 操作）
"""
def task(url):
    response = requests.get(url)
    #print(response.content)
    print("得到结果:",url,response.status_code,len(response.content))

#创建链接池
pool = ThreadPoolExecutor(5)
url_list = [
    'http://google.com',
    'http://youdao.com',
    'http://fuqianla.net',
    'http://www.baidu.com',
]

for url in url_list:
    print("start request:",url)
    #去连接池获取一个链接
    pool.submit(task,url)
"""




#建立 tcp连接 SSH 操作远程主机命令
"""
def task(host):
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=22, username=gjlin, password="123443d")
    stdin, stdout, stderr = ssh.exec_command("ifconfig")
    result = stdout.read()
    ssh.close()
    print(result)

#创建链接池
pool = ThreadPoolExecutor(2)
host_list = [
    'fuqianla_ftp',
    'fuqianla_log',
    'fuqianla_nginx',
]

for host in host_list:
    print("start connect:",host)
    #去连接池获取一个链接
    pool.submit(task,host)

"""


def txt():
    dowload_response = future.result()
    print('处理中',dowload_response.url,dowload_response.status_code)


def dowload():
    response = requests.get(url)
    return response    #respones中包含了所有的下载的内容

pool = ThreadPoolExecutor(2)
url_list = [
    'http://baidu.com',
    'http://youdao.com',
    'http://spaceeye.com',
]

for url in url_list:
    print('start quest:',url)
    future = pool.submit(dowload,url)
    #下载完成之后执行 txt 函数
    future.add_done_callback(txt)