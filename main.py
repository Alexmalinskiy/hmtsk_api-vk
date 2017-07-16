import vk
import pprint
import time


def get_friends(vk_api, user_id):
    vk_api.users.get(user_id=user_id, scope='friends')
    try:
        list_friends = vk_api.friends.get(user_id=user_id)
    except vk.exceptions.VkAPIError:
        print(user_id, " -  banned friend")
        return None
    return list_friends


def main(my_id, token):
    session = vk.Session(access_token=token)
    vk_api = vk.API(session)
    my_friends = get_friends(vk_api, my_id)
    print_full_info(vk_api, intersect_friends(vk_api, my_friends))
    #pprint.pprint(my_friends)


def intersect_friends(vk_api, my_friends):
    for i, friend in enumerate(my_friends):
        someone_friends = get_friends(vk_api, friend)
        if someone_friends is None:
            continue
        if i == 0:
            common_friends = set(someone_friends)
        common_friends = common_friends.intersection(set(someone_friends))
        time.sleep(1)
    return common_friends


def print_full_info(vk_api, common_friends):
    for friend in common_friends:
        user = vk_api.users.get(user_id=friend, fields='first_name, last_name')
        #print(user)
        print(user[0]['last_name'], user[0]['first_name'])


if __name__ == '__main__':
    main(7556648, "5a3c0e426e9d7e2a09567819665d45240b7cf0a740b57c0e5964f63adcdcb6ae8e99ad4522dd8da029096")
