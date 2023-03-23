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
    #   # 用于记录下一次起点
    # offset = 0
    
    # # 用于存储所有动态
    # dynamics = []

    # # 无限循环，直到 has_more != 1
    # while True:
    #       # 获取该页动态
    #     page = await u.get_dynamics(offset)
        
    #     if 'cards' in page:
    #           # 若存在 cards 字段（即动态数据），则将该字段列表扩展到 dynamics
    #         dynamics.extend(page['cards'])
        
    #     if page['has_more'] != 1:
    #             # 如果没有更多动态，跳出循环
    #         break
                
    #     # 设置 offset，用于下一轮循环
    #     offset = page['next_offset']

    # # 打印动态数量
    # print(dynamics)

# 入口
sync(main())