from telegraph import Telegraph
import os

telegraph = Telegraph()
telegraph.create_account(
    author_name="𝚃𝚜𝚞𝚔𝚒", short_name="𝚃𝚜𝚞𝚔𝚒", author_url="https://t.me/manga_share"
)
base_url = "https://raw.githubusercontent.com/OnonokiYotsuki/pic_cave/refs/heads/main/"


def create_page(folder_name: str = "𝚃𝚞𝚜𝚞𝚔"):
    # 获取文件夹下所有图片
    img_url = []
    for file in os.listdir(folder_name):
        if file.endswith(".jpg") or file.endswith(".png"):
            img_url.append(base_url + folder_name + "/" + file)

    if img_url:
        html_content = "".join([f'<img src="{url}"/>' for url in img_url])
        res = telegraph.create_page(folder_name, html_content=html_content)
        return res["url"]


page_url = create_page("TSUBASA翼")
print(f"Page created at: {page_url}")
