import requests
from lxml import etree
import random
import re
import wget
import os
#qcookie = str(input("Example:p_skey=************************; p_uin=o123456; uin=o123456; skey=********: "))
#qgroup = str(input("QQ Group number:"))
qcookie = ''
qgroup = ''
path = os.getcwd()

def dl_head(qqid):
    qqhead_url = 'http://q1.qlogo.cn/g?b=qq&nk=' + str(qqid) + '&s=640'
    qhead_filename = qqid + '.jpg'
    wget.download(qqhead_url, out=qhead_filename)
    qhead_filepath = path + '\\' + qhead_filename
    return qhead_filepath

def dl_img(urlin):
    img_filename = wget.download(urlin)
    img_filepath = path + '\\' + img_filename
    return img_filepath

def _type(a, pages="1"):
    span = "/span[" + pages + "]/text()"
    img = "/img[" + pages + "]/@src"
    if a == "s":
        return '//*[@id="app"]/div[2]/div[' + count + ']/div[last()-1]' + span
    elif a == "i":
        return '//*[@id="app"]/div[2]/div[' + count + ']/div[last()-1]' + img

def _type_div(a, pages="1"):
    span = "/div/span[" + pages + "]/text()"
    img = "/div/img[" + pages + "]/@src"
    if a == "s":
        return '//*[@id="app"]/div[2]/div[' + count + ']/div[last()-1]' + span
    elif a == "i":
        return '//*[@id="app"]/div[2]/div[' + count + ']/div[last()-1]' + img

def random_len(length):
    return random.randrange(int('1' + '0' * (length - 1)), int('9' * length))

def get(num, group_id, cookie):
    global count
    count = str(num)
    group_id = str(group_id)
    url = 'https://qun.qq.com/essence/indexPc?gc=' + group_id + '&seq=' + str(random_len(8)) + '&random=' + str(random_len(10))

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) QQ/9.6.5.28778 '
                    'Chrome/43.0.2357.134 Safari/537.36 QBCore/3.43.1298.400 QQBrowser/9.0.2524.400',
        'Host': 'qun.qq.com',
        # cookie  p_skey p_uin uin skey
        'Cookie': cookie
    }

    response = requests.get(url, headers=header)
    response.encoding = 'UTF-8'
    data = etree.HTML(response.text)  # 解析

    type_list = []
    div_bool = False
    try:
        for i in [str(i) for i in data.xpath('//*[@id="app"]/div[2]/div[' + count + ']/div[last()-1]/*')]:
            if i[9] in ['i', 's']:
                type_list.append(i[9])
            elif i[9:12] == 'div':
                div_bool = True
                break
        if div_bool:
            for i in [str(i) for i in data.xpath('//*[@id="app"]/div[2]/div[' + count + ']/div[last()-1]/div/*')]:
                if i[9] in ['i', 's']:
                    type_list.append(i[9])

        type_sequence = []
        span_sequence, img_sequence = 0, 0

        for i in range(len(type_list)):
            if type_list[i] == 's':
                span_sequence += 1
                type_sequence.append("s" + str(span_sequence))
            else:
                img_sequence += 1
                type_sequence.append("i" + str(img_sequence))

        if div_bool:
            for i in [_type_div(type_sequence[i][0], type_sequence[i][1]) for i in range(len(type_list))]:
                content = data.xpath(i)[0]
                if len(content) < 11:
                    pass
                else:
                    if content[-10:] == "/thumbnail" and content[:8] == "https://":
                        content2 = content[0:-10]
                        content = dl_img(urlin=content2)
                    else:
                        pass
        else:
            for i in [_type(type_sequence[i][0], type_sequence[i][1]) for i in range(len(type_list))]:
                content = data.xpath(i)[0]
                if len(content) < 11:
                    pass
                else:
                    if content[-10:] == "/thumbnail" and content[:8] == "https://":
                        content2 = content[0:-10]
                        content = dl_img(urlin=content2)
                    else:
                        pass
        qq_account = data.xpath('//*[@id="app"]/div[2]/div[' + count + ']/div[1]/@style')[0][10:-2].split('/')[5]
        info = {
            'qhead' : dl_head(qqid=qq_account),
            'qaccount' : data.xpath('//*[@id="app"]/div[2]/div[' + count + ']/div[1]/@style')[0][10:-2].split('/')[5],
            'qname' : data.xpath('//*[@id="app"]/div[2]/div[' + count + ']/div[2]/text()')[0].replace('\n','').replace(' ',''),
            'send_date' : data.xpath('//*[@id="app"]/div[2]/div[' + count + ']/div[3]/text()')[0].replace('\n','').replace(' ','').replace('发送',''),
            'set_admin' : re.search(r'由(.*?)设置',data.xpath('//*[@id="app"]/div[2]/div[' + count + ']/div[6]/text()')[0]).group(1),
            'set_date' : re.search(r' (.*?)由',data.xpath('//*[@id="app"]/div[2]/div[' + count + ']/div[6]/text()')[0]).group(1).replace(' ',''),
            'content' : content
        }
        return info
    except:
        return 'error file'