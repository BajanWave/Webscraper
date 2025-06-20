from scraper import scrape_url, is_article_link

# my_package/__main__.py
def main():
    print("Running as a script")
    print(is_article_link("https://interviewing.io/", "https://interviewing.io/blog/"))
    scrape_url("https://interviewing.io/blog/post")

if __name__ == "__main__":
    main()
