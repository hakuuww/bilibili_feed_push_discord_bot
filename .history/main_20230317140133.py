import json
from bilibili_api import user, sync
from bilibili_api import Credential 
from bilibili_api import dynamic

# create a Credential object with your login information
credential = Credential(sessdata="c73a65ff%2C1694529917%2C15aed%2A32", bili_jct="fd071990e290665b2aaef22792eb6bda", buvid3="3FDB530F-0416-43AE-115B-ED39D3656F2B83763infoc")


async def main():


  dynamic_page_info = await dynamic.get_dynamic_page_info(credential)
  for dynamic_obj in dynamic_page_info:
    print(f"Dynamic ID: {dynamic_obj.dynamic_id}")
    print(f"User ID: {dynamic_obj.uid}")
    print(f"User Name: {dynamic_obj.uname}")
    print(f"Timestamp: {dynamic_obj.timestamp}")
    print(f"Content: {dynamic_obj.content}")
    print(f"Type: {dynamic_obj.type}")
    print(f"Is repost: {dynamic_obj.is_repost}")
    print(f"Original User ID: {dynamic_obj.original_uid}")
    print(f"Original User Name: {dynamic_obj.original_uname}")
    print(f"Original Dynamic ID: {dynamic_obj.original_dynamic_id}")
    print(f"Original Content: {dynamic_obj.original_content}")
    print(f"Like count: {dynamic_obj.like_count}")
    print(f"Comment count: {dynamic_obj.reply_count}")
    print(f"Share count: {dynamic_obj.share_count}")
    print(f"View count: {dynamic_obj.view_count}")
    print("-------------------------------------------")

# 入口
sync(main())