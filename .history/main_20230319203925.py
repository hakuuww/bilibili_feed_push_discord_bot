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
    
def print_text_in_dict(info):
    try:
        module_dynamic = info['item']['modules'].get('module_dynamic')
        if module_dynamic is not None:
            major = module_dynamic.get('major')
            if major is not None:
                draw = major.get('draw')
                if draw is not None:
                    src = draw.get('')
    except KeyError:
        pass
    
    'src': 'https://i0.hdslb.com/bfs/new_dyn/f1887733da718d3707bf91184506d582237682674.jpg'



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
        

        



# 入口
sync(main())


