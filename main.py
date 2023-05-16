import browser
import settings
import functions
#import overlay
import time
import random


if __name__ == "__main__":
    
    #app = overlay.OverlayApp()

    chrome = browser.create_browser(browser="chrome")
    chrome.get(settings.MAIN_BLOG_URL)

    for i in range(3):

        posts = functions.get_posts(settings.WP_POSTS)

        for post in posts:

            page = post["slug"]

            #app.show_log(f"Na Pagina -> {settings.MAIN_BLOG_URL}/{page}\n")
            #app.run()

            url = settings.MAIN_BLOG_URL + "/" + page
            chrome.get(url)

            post_title = functions.clean_slug(page)

            arr = ["pessoa", "idoso", "comentário de blog", "comentário de facebook", "mulher", "homem"]

            gpt_comment = functions.openai_send_prompt(f"{post_title}. {settings.OPENAI_COMMENT_PROMPT}. Imite um(a) {arr[random.randint(0, len(arr)-1)]}. E fale em primeira pessoa")
            gpt_comment = functions.clean_slug(gpt_comment)

            #app.show_log(f"Comentou: {gpt_comment}\n")
            #app.run()

            if(len(gpt_comment) < 10):
                continue

            comment = functions.wait_for_element_css(web_driver=chrome, css_selector="#comment", timeout=15)
            comment.click()
            comment.send_keys(gpt_comment.strip())

            functions.check_error_page(web_drive=chrome, post_url=url)

            author = functions.wait_for_element_css(web_driver=chrome, css_selector="#author", timeout=15)
            author.click()
            name = functions.openai_send_prompt(settings.OPENAI_NAME_PROMPT)
            author.send_keys(name.strip())

            time.sleep(1)
            functions.check_error_page(web_drive=chrome, post_url=url)

            email = author = functions.wait_for_element_css(web_driver=chrome, css_selector="#email", timeout=15)
            email.click()
            temp_mail = functions.generate_text()
            email.send_keys(f"BOT_{temp_mail}@gmail.com")

            time.sleep(1)
            functions.check_error_page(web_drive=chrome, post_url=url)

            btn_submit = functions.wait_for_element_css(web_driver=chrome, css_selector="#submit", timeout=15)
            btn_submit.click()

            chrome.implicitly_wait(5)

    if(input("[+] Pressione ENTER no console para fechar o navegador.\n")):
        browser.browser_quit(chrome)