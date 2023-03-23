import json
from bilibili_api import user, sync
from bilibili_api import Credential
from bilibili_api import dynamic
import os
import json
import discord



intent = discord.Intents.default()
intent.members = True
intent.message_content = True

client = discord.Client(intents=intent)



# create a Credential object with your login information
credential = Credential(sessdata="c73a65ff%2C1694529917%2C15aed%2A32",
                        bili_jct="fd071990e290665b2aaef22792eb6bda", buvid3="3FDB530F-0416-43AE-115B-ED39D3656F2B83763infoc")

def get_dynamic_link(dynamic_id: str) -> str:
    return f"https://www.bilibili.com/opus/{dynamic_id}"

def get_BV_link(BV_id: str) -> str:
    return f"https://www.bilibili.com/video/{BV_id}"

async def print_all_dynamics_of_user(user_id):
    u = user.User(user_id)

    offset = 0
    
    # 用于存储所有动态
    dynamics = []

    # 无限循环，直到 has_more != 1
    while True:
          # 获取该页动态
        page = await u.get_dynamics(offset)
        
        if 'cards' in page:
              # 若存在 cards 字段（即动态数据），则将该字段列表扩展到 dynamics
            dynamics.extend(page['cards'])
        
        if page['has_more'] != 1:
                # 如果没有更多动态，跳出循环
            break
                
        # 设置 offset，用于下一轮循环
        offset = page['next_offset']

    # 打印动态数量
    print(f"共有 {len(dynamics)} 条动态")


def print_text_in_dict(info):
    try:
        module_dynamic = info['item']['modules'].get('module_dynamic')
        if module_dynamic is not None:
            desc = module_dynamic.get('desc')
            if desc is not None:
                text = desc.get('text')
                if text is not None:
                    print(text)
    except KeyError:
        pass
    
def print_img_link_in_dict(info):

    try:
        module_dynamic = info['item']['modules'].get('module_dynamic')
        #print(1)
        
        if module_dynamic is not None:
            #print(2)
            major = module_dynamic.get('major')
            if major is not None:
                #print(3)
                draw = major.get('draw')
                archive = major.get('archive')
                if archive is not None:
                    BV_id = archive.get('bvid')
                    print(get_BV_link(BV_id))
                if draw is not None:
                    #print(4)
                    items = draw.get('items')
                    if items is not None:
                        #print(5)
                        src = items[0]['src']
                        if src is not None:
                            #print(6)
                            print(src)
    except KeyError:
        print(Exception)
        pass
    
async def 


async def main():
    dynamic_page_info = await dynamic.get_dynamic_page_info(credential = credential)
    print(dynamic_page_info)
    for dynamic_obj in dynamic_page_info:
        
        info = await dynamic_obj.get_info()
        
        dynamic_id_num = dynamic_obj.get_dynamic_id()
        dynamic_link = get_dynamic_link(dynamic_id_num)
        print(dynamic_link)
        print(info['item']['modules']['module_author']['name'])
        print(info['item']['modules']['module_author']['pub_action'])
        
        print_text_in_dict(info)
        print_img_link_in_dict(info)
        #print(info)

# 入口
sync(main())






