import json
from bilibili_api import user, sync
from bilibili_api import Credential 
from bilibili_api import dynamic
from bilibili_api import request, API, Credential

# create a Credential object with your login information
credential = Credential(sessdata="c73a65ff%2C1694529917%2C15aed%2A32", bili_jct="fd071990e290665b2aaef22792eb6bda", buvid3="3FDB530F-0416-43AE-115B-ED39D3656F2B83763infoc")

async def get_dynamic_page_UPs_info(credential: Credential) -> List[dict]:
    """
    获取动态页 UP 主列表
    Args:
        credential (Credential): 凭据类.
    Returns:
        list[dict]: UP 主信息列表
    """
    api = API["info"]["dynamic_page_UPs_info"]
    response = await request("GET", api["url"], credential=credential)
    return response["data"]["cards"]

async def main():


  ups_info = await get_dynamic_page_UPs_info(credential)
  print(ups_info)

# 入口
sync(main())