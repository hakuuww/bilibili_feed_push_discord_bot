import json
import bilibili_api
from bilibili_api import user, sync
from bilibili_api import Credential
from bilibili_api import dynamic
import os
import json
import discord
import pymongo 



clientDb = pymongo.MongoClient("mongodb+srv://xumingyang:zDEkIIyqYkxE3HKb@hakubilibilidynamicsfee.ch66v2g.mongodb.net/?retryWrites=true&w=majority")
db = clientDb.test


intent = discord.Intents.default()
intent.members = True
intent.message_content = True

client = discord.Client(intents=intent)



# create a Credential object with your login information
credential = Credential(sessdata="c73a65ff%2C1694529917%2C15aed%2A32",
                        bili_jct="fd071990e290665b2aaef22792eb6bda", buvid3="3FDB530F-0416-43AE-115B-ED39D3656F2B83763infoc")

async def get_dynamic_link(dynamic_id: str) -> str:
    return f"t.bilibili.com/{dynamic_id}"

async def get_BV_link(BV_id: str) -> str:
    return f"https://www.bilibili.com/video/{BV_id}"

async def print_all_dynamics_of_user(user_id,message):
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


async def print_text_in_dict(info,message):
    try:
        module_dynamic = info['item']['modules'].get('module_dynamic')
        if module_dynamic is not None:
            desc = module_dynamic.get('desc')
            if desc is not None:
                text = desc.get('text')
                if text is not None:
                    await message.channel.send(text)
    except KeyError as e:
        print(e)
        
        pass
    
async def print_img_link_in_dict(info,message):

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
                    await message.channel.send(await get_BV_link(BV_id))
                    print(await get_BV_link(BV_id))
                if draw is not None:
                    #print(4)
                    items = draw.get('items')
                    if items is not None:
                        for item in items:
                         if item is None:
                            break
                         src = item['src']
                         if src is not None:
                            #print(6)
                            await message.channel.send(src)
    except KeyError:
        print(Exception)
        pass

async def print_sender_name(info, message):
    await message.channel.send(info['item']['modules']['module_author']['name'])
    print(info['item']['modules']['module_author']['name'])
    
async def print_sender_avatar(info, message):
    await message.channel.send(info['item']['modules']['module_author']['avatar']['fallback_layers']['layers'][0]['resource']['res_image']['image_src']['remote']['url'])   
    print(info['item']['modules']['module_author']['avatar']['fallback_layers']['layers'][0]['resource']['res_image']['image_src']['remote']['url'])

async def main():
    print(db)
    print(1)
    
@client.event
async def on_message(message):
    
  if message.author == client.user: return
  
  if message.content.startswith('log'):
      await message.channel.send('trying to connect to MongoDB')
      
      db.test_log.insert_one(
          {}
          "message":message.content,
          "author": message.author.id,
          
      )
      
      

  if message.content.startswith('hello'):
    await message.channel.send('Hello!')
    dynamic_page_info = await dynamic.get_dynamic_page_info(credential = credential)
    
    for dynamic_obj in dynamic_page_info:
        info = await dynamic_obj.get_info()
        dynamic_id_num = dynamic_obj.get_dynamic_id()
        dynamic_link = await get_dynamic_link(dynamic_id_num)
        
        await message.channel.send(dynamic_link)
        #await message.channel.send(info['item']['modules']['module_author']['name'])
        #await message.channel.send(info['item']['modules']['module_author']['pub_action'])
        #await message.channel.send cannot send an empty message
        
        print(info)
        await print_sender_name(info,message)
        await print_sender_avatar(info,message)
        await print_text_in_dict(info,message)
        await print_img_link_in_dict(info,message)
        #print(info)

# 入口
sync(main())
#discord_bot_token = os.environ['MTA4NTcyNjE1NzQyMjQ2OTI3Mw.Gsrglz.xfzAuLu3MEX1p97pSfDGQ8K8tOExdImatH21_M']
client.run('MTA4NTcyNjE1NzQyMjQ2OTI3Mw.Gsrglz.xfzAuLu3MEX1p97pSfDGQ8K8tOExdImatH21_M')







