import login
import sign


def main():
    cookie = login.get_cookie()
    if cookie == None:
        print('登录失败')
    elif cookie == '418':
        print('请求被拦截，请尝试更换IP')
    else:
        sign.run(cookie)


if __name__ == '__main__':
    main()