from email.mime import text,multipart,image
import smtplib
import configparser
import os,re
BASEDIR=os.path.dirname(os.path.dirname(__file__))

email_info=configparser.ConfigParser()
email_info.read(os.path.join(BASEDIR,'data'),encoding='utf-8')

class MYEMAIL:
    '''
    params
    :smtp_addr
    '''
    def __init__(self):
        self.__smtp_addr = email_info.get('email', 'smtp_addr')
        self.__from_addr = email_info.get('email', 'from_addr')
        self.__emai_pwd = email_info.get('email', 'emai_pwd')
        self.__to_addr = email_info.get('email', 'to_addr').split(',')
        self.__s = smtplib.SMTP(self.__smtp_addr)
        self.__s.login(self.__from_addr, self.__emai_pwd)

    def email_text(self,text_info,subject=None,sendername=None):
        #定义邮件内容msg
        self.text_obj=text.MIMEText(_text=text_info)
        self.__email_conf(subject,sendername)
        self.__send_eamil()

    def email_html(self,url_info,subject=None,sendername=None):
        self.text_obj=text.MIMEText(url_info,_subtype='html')
        self.__email_conf(subject,sendername)
        self.__send_eamil()

    def email_file(self,filename=None,showname=None,img=None,body=None,subject=None,sendername=None):  #此处直接定义一个发送图片+文件的方法
        self.text_obj = multipart.MIMEMultipart()  # 附件形式
        # 添加一个文件
        if  filename:
            with open(filename, 'rb') as fo:
                fo_str = fo.read()
            attr = text.MIMEText(fo_str, _charset='utf-8')
            attr["Content-Type"] = 'application/octet-stream'
            if not showname:
                showname=os.path.basename(filename)
            # attr['Content-Disposition'] = 'attachment; filename=%s'%showname # 没有这个不显示附件位置··WWWW是名称，可以参数格式化
            attr.add_header('Content-Disposition', 'attachment', filename=('gbk', '', showname))
            self.text_obj.attach(attr)
            if not subject:
                subject='附件--%s'%showname

        if  img and body:
            self.text_obj.attach(text.MIMEText(body, 'html', 'utf-8'))
            # 显示一个图片
            with open(img, 'rb') as fo:
                im_str = fo.read()
            attr = image.MIMEImage(im_str)
            # attr.add_header('Content-ID', '<image1>') #指定图片
            img_id = re.findall(r'cid:(\w+).*', body)[0]
            attr['Content-ID'] = '<%s>'%img_id  # 这个是和body中的image1一致
            self.text_obj.attach(attr)
            if not subject:
                subject='图片--%s'%(os.path.basename(img))
        self.__email_conf(subject,sendername)
        self.__send_eamil()

    def __email_conf(self,subject,sendername):
        if not sendername:
            sendername=self.__from_addr
        self.text_obj['Subject']=subject
        self.text_obj['from']=sendername

    def __send_eamil(self):
        self.__s.sendmail(self.__from_addr, self.__to_addr, self.text_obj.as_string())

    def smtp_close(self):
        self.__s.close()


if __name__=='__main__':
    email=MYEMAIL()
    # emai.email_text('1234567')

    body = """
    <h3>测试结果截图如下，详细请下载report.html查看！</h3>
    <img src="cid:image2"/>
    """
    # email.email_file(filename=os.path.join(BASEDIR,'resultfile','emai哈哈l.py'),img=os.path.join(BASEDIR,'resultIMG','123.png'),body=body,subject='haha',sendername='LM')
    # email.smtp_close()
    email.email_text('223344',sendername="哈哈",subject='测试')   #sendername 中文，subject 无会被认为是垃圾邮件
# url_info='<a href=www.baidu.com>百度主页<a/>'
