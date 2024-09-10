

# x = [1, 2]
# print(dir(x))
# for i in x[:]:
#     i += 1
# print(x)

# print('{0} {0} aboba'.format(1))

# print(list(zip(['name', 'age'], ['John', 25])))

# a = dict(zip((1, 2),
#              ('age', 25)))
# a = defaultdict(int)
# print(a)
# print(a.)
# print(a[1])

# a = {1: 3, 2: 4}
# b = iter(a)
# print(next(b))
# print(next(b))

# import matplotlib.pyplot as plt
# import numpy as np

# # Sample data sets
# data1 = [1, 2, 5, 6, 7, 8, 9, 10, 15, 18, 20, 21, 22, 23, 24, 25, 30]
# data2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

# # Create box plots
# plt.boxplot([data1, data2], labels=['Data Set 1', 'Data Set 2'])

# # Add title and labels
# plt.title('Box Plot Comparison')
# plt.ylabel('Values')

# # Show plot
# plt.show()
import vk_api


def auth_handler():
    key = input("auth: ")
    return (key, True)


def captcha_handler(captcha):
    """ При возникновении капчи вызывается эта функция и ей передается объект
        капчи. Через метод get_url можно получить ссылку на изображение.
        Через метод try_again можно попытаться отправить запрос с кодом капчи
    """

    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()

    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(key)


def main():
    """ Пример получения последнего сообщения со стены """

    # login, password = 'shima@yandex.ru', 'ksh'
    vk_session = vk_api.VkApi(login,
                              password,
                              auth_handler=auth_handler,
                              captcha_handler=captcha_handler)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    """ VkApi.method позволяет выполнять запросы к API. В этом примере
        используется метод wall.get (https://vk.com/dev/wall.get) с параметром
        count = 1, т.е. мы получаем один последний пост со стены текущего
        пользователя.
    """
    response = vk.wall.get(count=1)  # Используем метод wall.get

    if response['items']:
        print(response['items'][0])


if __name__ == '__main__':
    main()

# def auth_handler():
#     key = input("Enter authentication code: ")
#     remember_device = True
#     return key, remember_device


# def captcha_handler(captcha):
#     key = input(f"Enter captcha ({captcha.get_url()}): ")
#     return captcha.try_again(key)


# vk_session = vk_api.VkApi(
#     login='shimanoee@yandex.ru',
#     password='Beq_XFjjr3*_vcksh',
#     auth_handler=auth_handler,
#     captcha_handler=captcha_handler
# )

# try:
#     vk_session.auth()
# except vk_api.AuthError as error_msg:
#     print(error_msg)
#     exit(1)

# vk = vk_session.get_api()
# user_info = vk.users.get(user_ids='1')
# print(user_info)
