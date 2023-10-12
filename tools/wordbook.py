import pdfplumber
from aligo import Aligo

pdf_path = (
    r"C:\Users\21090\Desktop\Book\Calculus_ Early Transcendentals Ninth Edition.pdf"
)


def parse():
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[48]
        content = page.extract_text()
        print(content.split())


if __name__ == "__main__":
    ali = Aligo()  # 第一次使用，会弹出二维码，供扫描登录

    user = ali.get_user()  # 获取用户信息
    print(user.user_name, user.nick_name, user.phone)  # 打印用户信息

    ll = ali.get_file_list()  # 获取网盘根目录文件列表
    for file in ll:  # 遍历文件列表
        print(file.file_id, file.name, file.type)  # 打印文件信息
