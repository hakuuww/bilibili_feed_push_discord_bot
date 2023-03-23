import json
from bilibili_api import user, sync
from bilibili_api import Credential
from bilibili_api import dynamic

# create a Credential object with your login information
credential = Credential(sessdata="c73a65ff%2C1694529917%2C15aed%2A32",
                        bili_jct="fd071990e290665b2aaef22792eb6bda", buvid3="3FDB530F-0416-43AE-115B-ED39D3656F2B83763infoc")

def get_dynamic_link(dynamic_id: str) -> str:
    return f"https://www.bilibili.com/opus/{dynamic_id}"


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
        print(1)
        
        if module_dynamic is not None:
            print(2)
            major = module_dynamic.get('major')
            if major is not None:
                print(3)
                draw = major.get('draw')
                if draw is not None:
                    print(4)
                    items = draw.get('items')
                    if items is not None:
                        print(5)
                        src = items[0]['src']
                        if src is not None:
                            print(6)
                            print(src)
    except KeyError:
        print(Exception)
        pass
    



async def main():

        
        

        



# 入口
sync(main())

