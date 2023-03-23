import json
from bilibili_api import user, sync
from bilibili_api import Credential
from bilibili_api import dynamic

# create a Credential object with your login information
credential = Credential(sessdata="c73a65ff%2C1694529917%2C15aed%2A32",
                        bili_jct="fd071990e290665b2aaef22792eb6bda", buvid3="3FDB530F-0416-43AE-115B-ED39D3656F2B83763infoc")\


async def main():

    dynamic_page_info = await dynamic.get_dynamic_page_info(credential = credential)
    print(dynamic_page_info)
    for dynamic_obj in dynamic_page_info:
        print("Dynamic id:", dynamic_obj.get_dynamic_id())
        info = await dynamic_obj.get_info()
        
        print(info)

        print(info['item']['modules']['module_author']['name'])
        print(info['item']['modules']['module_author']['pub_action'])
        print_key_in_dict(info,'text')
        #print(info['item']['modules']['module_dynamic']['desc']['text'])
        



# 入口
sync(main())


