from get_links import main
from get_cont import get_content_frm_link

from time import time

def get_content(query):

    # to get relevant links
    prompt_4_retrieving_links = query

    # get the links
    links = main(prompt_4_retrieving_links)

    links = list(links.values())

    print('got the links🔥')

    json_content = []

    for i, link in enumerate(links):
        # print(i + 1)
        json_content.append(get_content_frm_link(link))

    print('got the content🔥')
    return json_content


if __name__ == '__main__':
    # st = time()
    print(get_content("Get something related to IBD"))
    # print(time() - st)
    pass