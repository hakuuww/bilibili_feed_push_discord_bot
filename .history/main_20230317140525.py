import json
from bilibili_api import user, sync
from bilibili_api import Credential 
from bilibili_api import dynamic

# create a Credential object with your login information
credential = Credential(sessdata="c73a65ff%2C1694529917%2C15aed%2A32", bili_jct="fd071990e290665b2aaef22792eb6bda", buvid3="3FDB530F-0416-43AE-115B-ED39D3656F2B83763infoc")


async def main():


    dynamic_page_info = await dynamic.get_dynamic_page_info(credential)
    for dynamic_obj in dynamic_page_info:
        print(dynamic_obj)
        
    

# 入口
sync(main())