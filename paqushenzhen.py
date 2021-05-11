import requests
from lxml import etree
import json
from multiprocessing import Pool


def download(num):
    session=requests.Session()


    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    }

    url="https://opendata.sz.gov.cn/api/29200_00403602/1/service.xhtml"

    data={
    "appKey":"b59173d7e4ad4231b43987ae81fdb1f2",
    "page":str(num),
    'rows':"10000",
    }

    m=session.post(url=url,data=data,headers=headers)

    if m.status_code == 200:
        datas = json.loads(m.text)
    
    with open("D:/python-work/shenzhen/第"+str(num)+"页.json","w",encoding="utf-8") as fp:
        json.dump(datas,fp=fp,ensure_ascii=False)


def main():
    numbers=list(i  for i in range(215,216))
    pool=Pool(10)
    pool.map(download,numbers)
    pool.close()
    pool.join()


if __name__=="__main__":
    main()

    
