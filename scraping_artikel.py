import asyncio
import sys
from playwright.async_api import async_playwright
import json
import re

if sys.platform == "win32":
    asyncio.set_event_loop_policy(
        asyncio.WindowsProactorEventLoopPolicy()
    )

SEARCHES = [
    "gerakan 3R",
    "daur ulang",
    "kelola sampah",
    "bahaya limbah sampah"
]

RELEVANT_KEYWORDS = [
    "sampah",
    "daur ulang",
    "plastik",
    "bank sampah",
    "pemilahan",
    "kompos",
    "guna ulang",
    "reduce",
    "reuse",
    "recycle",
    "pengelolaan",
    "limbah plastik",
    "sampah plastik",
    "tpa",
    "tpst",
    "upcycle",
    "eco"
]

BLACKLIST = [
    "hiu","paus","kelelawar",
    "orangutan","harimau",
    "deforestasi","plta",
    "mangrove","satwa",
    "burung","laut","hutan"
]

articles=[]
visited=set()


def is_relevant(title):

    title = title.lower()

    if any(
        word in title
        for word in BLACKLIST
    ):
        return False

    return any(
        word in title
        for word in RELEVANT_KEYWORDS
    )


def extract_date(url):

    match = re.search(
        r"/(\d{4})/(\d{2})/(\d{2})/",
        url
    )

    if match:

        y,m,d = match.groups()

        return f"{y}-{m}-{d}"

    return None


async def scrape_mongabay(page):

    print("\n===================")
    print("SCRAPING MONGABAY")
    print("===================")

    for search in SEARCHES:

        keyword = search.replace(
            " ",
            "%20"
        )

        url = (
            f"https://mongabay.co.id/?s={keyword}&formats="
        )

        print("\nSEARCH:",search)

        try:

            await page.goto(
                url,
                wait_until="networkidle",
                timeout=60000
            )

            await page.wait_for_timeout(
                3000
            )

        except Exception as e:

            print(e)

            continue


        posts = await page.query_selector_all(
            "div.article--container"
        )

        print(
            "Jumlah post:",
            len(posts)
        )


        for post in posts:

            try:

                a = await post.query_selector(
                    "a"
                )

                if not a:
                    continue

                link = await a.get_attribute(
                    "href"
                )

                if not link:
                    continue

                if link in visited:
                    continue


                title_el = await post.query_selector(
                    "div.title"
                )

                if not title_el:
                    continue

                title = (
                    await title_el.inner_text()
                ).strip()


                if not is_relevant(
                    title
                ):
                    continue


                image=""

                img=await post.query_selector(
                    "img"
                )

                if img:

                    srcset=await img.get_attribute(
                        "srcset"
                    )

                    if srcset:

                        image=(
                            srcset
                            .split(",")[-1]
                            .strip()
                            .split(" ")[0]
                        )

                        image=re.sub(
                            r"-\d+x\d+(?=\.(jpg|jpeg|png|webp))",
                            "",
                            image
                        )

                visited.add(
                    link
                )

                articles.append({

                    "keyword":search,
                    "title":title,
                    "url":link,
                    "image":image,
                    "date":extract_date(link),
                    "source":"Mongabay Indonesia"

                })

                print(
                    len(articles),
                    title
                )

            except Exception as e:

                print(e)



async def scrape_greeneration(page):

    print("\n===================")
    print("SCRAPING GREENERATION")
    print("===================")

    await page.goto(
        "https://greeneration.org/publication/green-info",
        wait_until="networkidle"
    )

    await page.wait_for_timeout(
        5000
    )


    for current_page in range(
        1,
        14
    ):

        print(
            f"\nPAGE {current_page}"
        )

        posts=await page.query_selector_all(
            'div[class*="__post"]'
        )

        print(
            "Jumlah post:",
            len(posts)
        )

        for post in posts:

            try:

                title_el=await post.query_selector(
                    "h3"
                )

                if not title_el:
                    continue

                title=(
                    await title_el.inner_text()
                ).strip()


                if not is_relevant(
                    title
                ):
                    continue


                a=await post.query_selector(
                    "a"
                )

                if not a:
                    continue

                href=await a.get_attribute(
                    "href"
                )

                if not href:
                    continue


                link=(
                    "https://greeneration.org"+href
                    if href.startswith("/")
                    else href
                )

                if link in visited:
                    continue


                visited.add(
                    link
                )


                image=""

                photo=await post.query_selector(
                    'div[class*="__photo"]'
                )

                if photo:

                    style=await photo.get_attribute(
                        "style"
                    )

                    if style:

                        m=re.search(
                            r'url\("?(.*?)"?\)',
                            style
                        )

                        if m:

                            image=m.group(1)


                articles.append({

                    "keyword":"green-info",
                    "title":title,
                    "url":link,
                    "image":image,
                    "date":extract_date(link),
                    "source":"Greeneration Foundation"

                })

                print(
                    len(articles),
                    title
                )

            except Exception as e:

                print(e)


        if current_page == 13:
            break


        try:

            await page.keyboard.press(
                "Escape"
            )

            await page.wait_for_timeout(
                1000
            )

            next_page = str(
                current_page+1
            )

            print(
                "Klik halaman",
                next_page
            )

            btn=page.locator(
                f"text='{next_page}'"
            ).last

            await btn.scroll_into_view_if_needed()

            await btn.click(
                force=True
            )

            await page.wait_for_load_state(
                "networkidle"
            )

            await page.wait_for_timeout(
                4000
            )

        except Exception as e:

            print(
                "Pagination error:",
                e
            )

            break



async def scrape():

    async with async_playwright() as p:

        browser=await p.chromium.launch(
            headless=True
        )

        page=await browser.new_page()

        await scrape_mongabay(
            page
        )

        await scrape_greeneration(
            page
        )

        await browser.close()



if __name__=="__main__":

    asyncio.run(scrape())

    articles.sort(
        key=lambda x: x["date"] if x["date"] else "",
        reverse=True
    )

    with open(
        "artikel_capstone.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            articles,
            f,
            ensure_ascii=False,
            indent=4
        )

    print("\n====================")
    print("TOTAL:", len(articles))