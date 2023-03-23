import json
from bilibili_api import user, sync
from bilibili_api import Credential
from bilibili_api import dynamic

# create a Credential object with your login information
credential = Credential(sessdata="c73a65ff%2C1694529917%2C15aed%2A32",
                        bili_jct="fd071990e290665b2aaef22792eb6bda", buvid3="3FDB530F-0416-43AE-115B-ED39D3656F2B83763infoc")


async def main():

    dynamic_page_info = await dynamic.get_dynamic_page_info(credential)
    for dynamic_obj in dynamic_page_info:
        print(f"Dynamic ID: {dynamic_obj.dynamic_id}")
        print(f"Type: {dynamic_obj.dynamic_type}")
        print(f"User ID: {dynamic_obj.user_info.uid}")
        print(f"Username: {dynamic_obj.user_info.uname}")
        print(f"Timestamp: {dynamic_obj.timestamp}")
        print(f"Text Content: {dynamic_obj.text}")
        print(f"Origin User ID: {dynamic_obj.origin_user_info.uid}")
        print(f"Origin Username: {dynamic_obj.origin_user_info.uname}")
        print(f"Origin Type: {dynamic_obj.origin_type}")
        print(f"Origin Text Content: {dynamic_obj.origin_text}")


    d = dynamic.Dynamic(12345)
    print(dir(d))

# 入口
sync(main())
