import json
import bilibili_api
from bilibili_api import user, sync
from bilibili_api import Credential
from bilibili_api import dynamic
import os
import json
import discord
import pymongo 
import schedule
import time
import asyncio
from discord.ext import commands, tasks



clientDb = pymongo.MongoClient("mongodb+srv://xumingyang:zDEkIIyqYkxE3HKb@hakubilibilidynamicsfee.ch66v2g.mongodb.net/?retryWrites=true&w=majority")
db = clientDb.BILIBILI_DISCORD_BOT


intent = discord.Intents.default()
intent.members = True
intent.message_content = True

client = discord.Client(intents=intent)



# create a Credential object with your login information
credential = Credential(sessdata="531621a8%2C1695005852%2C79b1c%2A32",
                        bili_jct="91f0e455162e8601c59c36de045bedd4", buvid3="3FDB530F-0416-43AE-115B-ED39D3656F2B83763infoc")

async def get_dynamic_link(dynamic_id: str) -> str:
    return f"https://t.bilibili.com/{dynamic_id}"

async def get_BV_link(BV_id: str) -> str:
    return f"https://www.bilibili.com/video/{BV_id}"

async def print_all_dynamics_of_user(user_id, message):
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


async def print_text_in_dict(info,channel):
    try:
        module_dynamic = info['item']['modules'].get('module_dynamic')
        if module_dynamic is not None:
            desc = module_dynamic.get('desc')
            if desc is not None:
                text = desc.get('text')
                if text is not None:
                    await channel.send(text)
    except KeyError as e:
        print(e)
        
        pass
    
async def print_img_link_in_dict(info,channel):

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
                    await channel.send(await get_BV_link(BV_id))
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
                            await channel.send(src)
    except KeyError:
        print(Exception)
        pass

async def print_sender_name(info, channel):
    sender_name = info['item']['modules']['module_author']['name']
    feed_message = sender_name + " posted:"
    await channel.send(feed_message )
    print(info['item']['modules']['module_author']['name'])
    
async def print_sender_avatar(info, channel):
    await channel.send(info['item']['modules']['module_author']['avatar']['fallback_layers']['layers'][0]['resource']['res_image']['image_src']['remote']['url'])   
    print(info['item']['modules']['module_author']['avatar']['fallback_layers']['layers'][0]['resource']['res_image']['image_src']['remote']['url'])

async def get_sender_name(info):
    return info['item']['modules']['module_author']['name']


async def create_channel(guild, category_name, channel_name):
    category =  discord.utils.get(guild.categories, name=category_name)
    if category is None:
        category = await guild.create_category(category_name)
    channel = discord.utils.get(category.channels, name=channel_name)
    channel_lower_case = discord.utils.get(category.channels, name=channel_name.lower())
    if (channel is None) and (channel_lower_case is None):
        channel = await category.create_text_channel(channel_name)
    return channel



@tasks.loop(minutes=5)
async def my_bot_function():
    print('start bot function')
    dynamic_page_info = await dynamic.get_dynamic_page_info(credential = credential)
    print(dynamic_page_info)
    guildX = await client.fetch_guild(1007134321565503618)
    category_name = "BiliBili_feed_test"
    print("layayayayayayyayyayayyayyaya")
    
    bilibili_feed_id = 1087885108343738408
    print(len(guildX.channels))
    print(len(guildX.categories))
    for guild in client.guilds:
        if(guild.id == 1007134321565503618):
            guildX = guild     

    
    for dynamic_obj in dynamic_page_info:
        info = await dynamic_obj.get_info()
        ################################
        dynamic_id_num = dynamic_obj.get_dynamic_id()
        ################################
        dynamic_link = await get_dynamic_link(dynamic_id_num)
        
        id_already_exists = db.BILIBILI_DYNAMICS.find_one({'_id':dynamic_id_num})
        
        category_name = "BiliBili_feed_test"
        
            
        for category in guild.categories:
            print(f"ID: {category.id}")
      
        if id_already_exists is not None:
            print('Id already exists inside table, no insertion will be performed')
        else:    
            print('Id does not exists inside the current table, perform insertion')
            #1007134321565503618
            category_name = "BiliBili_feed_test"
                    
            dynamic_author_name = await get_sender_name(info)
            db.BILIBILI_DYNAMICS.insert_one(
              {
                "_id": dynamic_id_num, 
                "author": dynamic_author_name, 
              }
            )
            
            channel_name = dynamic_author_name.lower()
             
             
            channel = await create_channel(guildX, category_name, channel_name)
            #await message.channel.send(info['item']['modules']['module_author']['name'])
            #await message.channel.send(info['item']['modules']['module_author']['pub_action'])
            #await message.channel.send cannot send an empty message
            
            #print(info)
            await print_sender_name(info,channel)
            #await print_sender_avatar(info,message)
            await print_text_in_dict(info,channel)
            await print_img_link_in_dict(info,channel)
            await channel.send(dynamic_link)
    print("My bot is running!")

@client.event
async def on_ready():
    print('Bot is ready!')
    await my_bot_function.start()

    
@client.event
async def on_message(message):
  if message.author == client.user: return
  
  if message.content.startswith('log'):
      await message.channel.send('checking if the id already exists')
      
      new_id_being_inserted = message.content
      id_already_exists = db.test_uniqueIDs.find_one({'_id':new_id_being_inserted})
      
      if id_already_exists is not None:
          await message.channel.send('Id already exists inside table, no insertion will be performed')
      else:    
          await message.channel.send('Id does not exists inside the current table, perform insertion')
          db.test_uniqueIDs.insert_one(
              {
                "_id": message.content, 
                "author": message.author.id, 
              }
          )
      

  if message.content.startswith('hello!!!!!'):
    await message.channel.send('Hello12345!')
    dynamic_page_info = await dynamic.get_dynamic_page_info(credential = credential)
    
    guildX = await client.fetch_guild(1007134321565503618)
    category_name = "BiliBili_feed_test"
    print("layayayayayayyayyayayyayyaya")
    
    bilibili_feed_id = 1087885108343738408
    print(len(guildX.channels))
    print(len(guildX.categories))
    for guild in client.guilds:
        if(guild.id == 1007134321565503618):
            guildX = guild     

    
    for dynamic_obj in dynamic_page_info:
        info = await dynamic_obj.get_info()
        ################################
        dynamic_id_num = dynamic_obj.get_dynamic_id()
        ################################
        dynamic_link = await get_dynamic_link(dynamic_id_num)
        
        id_already_exists = db.BILIBILI_DYNAMICS.find_one({'_id':dynamic_id_num})
        
        category_name = "BiliBili_feed_test"
        
            
        for category in guild.categories:
            print(f"ID: {category.id}")
      
        if id_already_exists is not None:
            print('Id already exists inside table, no insertion will be performed')
        else:    
            print('Id does not exists inside the current table, perform insertion')
            #1007134321565503618
            category_name = "BiliBili_feed_test"
                    
            dynamic_author_name = await get_sender_name(info)
            db.BILIBILI_DYNAMICS.insert_one(
              {
                "_id": dynamic_id_num, 
                "author": dynamic_author_name, 
              }
            )
            
            channel_name = dynamic_author_name.lower()
             
             
            channel = await create_channel(guildX, category_name, channel_name)
            #await message.channel.send(info['item']['modules']['module_author']['name'])
            #await message.channel.send(info['item']['modules']['module_author']['pub_action'])
            #await message.channel.send cannot send an empty message
            
            #print(info)
            await print_sender_name(info,channel)
            #await print_sender_avatar(info,message)
            await print_text_in_dict(info,channel)
            await print_img_link_in_dict(info,channel)
            await channel.send(dynamic_link)
            #print(info)


#discord_bot_token = os.environ['MTA4NTcyNjE1NzQyMjQ2OTI3Mw.Gsrglz.xfzAuLu3MEX1p97pSfDGQ8K8tOExdImatH21_M']


async def main():
    await client.start('MTA4NTcyNjE1NzQyMjQ2OTI3Mw.GM-9-O.Cnwhb2opjLuR9XZxFU11upUS02ktPE4rC7fpRI')

asyncio.run(main())






