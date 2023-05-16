def exit():
    
    import sys
    sys.exit()

def get_posts(url):

    import requests
    
    posts_list = []  # initialize the list to store the posts
    
    params = {
        "per_page": 20,  # get 20 posts per request
        "page": 1  # get the first page (the first 20 posts)
    }

    while True:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            posts = response.json()

            if len(posts) == 0:
                break  # no more posts, exit the loop

            for post in posts:
                
                posts_list.append(post)  # add the post to the list

            params["page"] += 1  # move on to the next page

        else:
            print("Error making HTTP request")
            break
    
    return posts_list  # return the list of posts



def switch_to_window_by_title(web_driver, window_title):

    for window_handle in web_driver.window_handles:
        web_driver.switch_to.window(window_handle)

        if window_title in web_driver.title:
            return True

    return False

def wait_for_element_css(web_driver, css_selector, timeout=15):

    try:

        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        element = WebDriverWait(web_driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
        )
        return element

    except:
        return None

def generate_text():

    import random
    import string
    
    length = 15
    characters = string.ascii_letters + string.digits
    text = ''.join(random.choice(characters) for i in range(length))
    
    return text


def openai_send_prompt(prompt):

    import openai
    import settings

    # Set up the OpenAI API credentials
    openai.api_key = settings.OPENAI_API_KEY

    # Set up the prompt parameters
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = prompt,
        temperature = 1,
        top_p =  1,
        frequency_penalty = 0,
        presence_penalty = 0,
        max_tokens =  200,
        stop = None,
    )

    return response.choices[0].text.strip()

def generate_random_float(max_value=1.5):

    import random

    return round(random.uniform(0, max_value), 1)

def clean_slug(slug):

    slug = slug.replace("/", "")
    slug = slug.replace("-", " ")
    slug = slug.replace('"', '')
    
    return slug


def check_error_page(web_drive, post_url):

    url = web_drive.current_url
    post_url = post_url + "/"
    
    #print(url)
    #print(post_url)

    if (url != post_url):
        web_drive.back()
    
    return