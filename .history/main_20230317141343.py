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
    print(f"Origin Pictures: {dynamic_obj.origin_pictures}")
    print(f"Origin Video Info: {dynamic_obj.origin_video_info}")
    print(f"Pictures: {dynamic_obj.pictures}")
    print(f"Video Info: {dynamic_obj.video_info}")
    print(f"Description: {dynamic_obj.description}")
    print(f"Stats: {dynamic_obj.stats}")
    print(f"Card: {dynamic_obj.card}")
    print(f"Tags: {dynamic_obj.tags}")
    print(f"Previews: {dynamic_obj.previews}")
    print(f"Skips: {dynamic_obj.skips}")
    print(f"Duration: {dynamic_obj.duration}")
    print(f"Upper Limit: {dynamic_obj.upper_limit}")
    print(f"External Url: {dynamic_obj.external_url}")
    print(f"Interactive Card: {dynamic_obj.interactive_card}")
    print(f"Is Origin Deleted: {dynamic_obj.is_origin_deleted}")
    print(f"Is Deleted: {dynamic_obj.is_deleted}")
    print("\n")           

    d = dynamic.Dynamic(12345)
    print(dir(d))

# 入口
sync(main())
