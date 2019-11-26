# -*- coding: utf-8 -*-
import json
import time
import zlib

import requests

from Crawlers.Tiktok.Utils import get_tag, get_sessionid_by_account
from Crawlers.Tiktok.config import ACCOUNT_TO_SID


def tiktok_uploader(account, file, text=''):
    url1 = "https://api21-h2.tiktokv.com/aweme/v1/upload/authkey/?manifest_version_code=735&_rticket=1571024543641&app_language=en&current_region=US&app_type=normal&iid=6747216327653476097&channel=googleplay&device_type=J9110&language=en&locale=en&account_region=US&resolution=1096*2434&openudid=9ed5ff1a4b62cbc2&update_version_code=7350&sys_region=US&os_api=28&uoo=0&is_my_cn=1&timezone_name=America%2FNew_York&dpi=420&residence=US&ac=wifi&device_id=6747214369112163842&pass-route=1&os_version=9&timezone_offset=-18000&version_code=735&app_name=trill&ab_version=7.3.5&version_name=7.3.5&device_brand=Sony&ssmix=a&pass-region=1&device_platform=android&build_number=7.3.5&region=CN&aid=1180&ts={}".format(str(int(time.time())))
    session = requests.Session()
    session.proxies = {
        'https': 'http://lum-customer-hl_805b9ed9-zone-static_res-country-us:j3m8pmr2s2cn@zproxy.lum-superproxy.io:22225'
    }
    session.cookies.set("sessionid", get_sessionid_by_account(account, "Tiktok"))
    session.headers = {
        "User-Agent": "okhttp/3.10.0.1",
        "Content - Type": "application/x-www-form-urlencoded",
        "x-tt-token": "01f18e00fe9d3515b3d339ee90a7f2228082083561897e297c2b97250829586adeb38a977c139b0ba388ae97db2b8f422c24",
        "Host": "api21-h2.tiktokv.com"
    }
    resp = session.post(url=url1).text
    data1 = json.loads(resp)

    authorization = data1['video_config']['authorization']
    x_tt_access = data1['video_config']['appKey']

    video_host_name = data1['video_config']['videoHostName']
    file_host_name = data1['video_config']['fileHostName']

    url2 = "http://{}/video/openapi/v1/?action=GetVideoUploadParams&use_edge_node=1&use_quic=0&use_multi_task=0&resumable=0&region=US".format(video_host_name)
    session.headers = {
        'X-TT-Access': x_tt_access,
        'Authorization': authorization,
        'Content-Type': 'application/json'
    }

    resp2 = session.post(url=url2).text
    data2 = json.loads(resp2)

    vid = data2['data']['edge_nodes'][0]['vid']
    oid = data2['data']['edge_nodes'][0]['oid']
    token = data2['data']['edge_nodes'][0]['token']
    tos_sign = data2['data']['edge_nodes'][0]['tos_sign']

    url3 = "http://{}/{}?uploads".format(file_host_name, oid)
    print('url3', url3)
    session.headers = {
        'Authorization': tos_sign
    }
    resp3 = session.post(url=url3).text
    print('resp3', resp3)
    data3 = json.loads(resp3)

    uploadID = data3['payload']['uploadID']

    fd = open(file, "rb")
    content = fd.read()
    fd.close()
    part_number = 0
    prev = zlib.crc32(content)

    session.headers = {
        'Content-CRC32': "%X" % (prev & 0xFFFFFFFF),
        'Authorization': tos_sign
    }
    url4 = "http://{}/{}?uploadID={}&partNumber={}".format(file_host_name, oid, uploadID, part_number)
    resp4 = session.post(url=url4, data=content).text

    url5 = "http://{}/{}?uploadID={}".format(file_host_name, oid, uploadID)
    crc32 = session.headers['Content-CRC32']
    del session.headers['Content-CRC32']
    resp5 = session.post(url=url5, data='0:{}'.format(crc32)).text
    print('resp5', resp5)

    url6 = "http://{}/video/openapi/v1/?action=UpdateVideoUploadInfos&vidc=alisg&host={}&region=HK&edge_node=alisg&upload_mode=serial&strategy=long_memory_filter".format(video_host_name, file_host_name)
    print(url6)
    post_data = {
       "oid": oid,
       "token": token,
       "poster_ss": 0,
       "vid": vid
    }
    session.headers = {
        'X-TT-Access': x_tt_access,
        'Authorization': authorization,
        'Content-Type': 'application/json'
    }
    resp6 = session.post(url=url6, json=post_data).text
    data6 = json.loads(resp6)
    poster_oid = data6['data']['poster']['oid']

    url7 = "https://api-h2.tiktokv.com/aweme/v1/create/aweme/?manifest_version_code=735&_rticket=1571024572165&app_language=en&current_region=CN&app_type=normal&iid=6747216327653476097&channel=googleplay&device_type=J9110&language=zh&locale=en&account_region=US&resolution=1096*2434&openudid=9ed5ff1a4b62cbc2&update_version_code=7350&sys_region=CN&os_api=28&uoo=0&is_my_cn=1&timezone_name=Asia%2FShanghai&dpi=420&residence=US&ac=wifi&device_id=6747214369112163842&pass-route=1&os_version=9&timezone_offset=28800&version_code=735&app_name=trill&ab_version=7.3.5&version_name=7.3.5&device_brand=Sony&ssmix=a&pass-region=1&device_platform=android&build_number=7.3.5&region=CN&aid=1180&ts={}".format(str(int(time.time())))
    post_data2 = {
        "video_id": vid,
        "new_sdk": "1",
        "video_width": data6['data']['video']['width'],
        "video_height": data6['data']['video']['height'],
        "video_cover_uri": poster_oid.replace('/', '%2F'),
        "original": "0",
        "camera": "0",
        "prettify": "0",
        "is_upload_audio_track": "false",
        "is_multi_video_upload": "false",
        "use_camera_type": "1",
        "h264_high_profile": "1",
        "camera_compat_level": "1",
        "music_begin_time": "0",
        "music_end_time": "9932",
        "info_sticker": "",
        "cover_tsp": "0.0",
        "text": text,
        "is_private": "0",
        "is_hash_tag": "1",
        "shoot_way": "direct_shoot",
        "is_hard_code": "10",
        "item_comment": "0",
        "item_react": "0",
        "item_duet": "0",
        "commerce_ad_link": "0",
        "is_star_atlas": "0"
    }
    text_extra = get_tag(post_data2['text'])
    if text_extra:
        post_data2['text_extra'] = json.dumps(text_extra, ensure_ascii=False)
    session.headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'com.ss.android.ugc.trill/735 (Linux; U; Android 9; zh_CN_#Hans; J9110; Build/55.0.A.6.56; Cronet/58.0.2991.0)'
    }
    resp7 = session.post(url=url7, data=post_data2).text
    print(resp7)


if __name__ == '__main__':
    file = r'E:\Documents\PythonProjects\holaverse\Tiktok\videos\9MccLh.mp4'
    tiktok_uploader('bingquli', file, '!!!!')
