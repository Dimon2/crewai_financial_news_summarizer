from crewai_tools import BaseTool
from finance_news_analyzer.tools.common.web_scrapper import WebScrapper



class BloombergTool(BaseTool):
    name: str = "bloomberg_fund_market_news_tool"
    description: str = (
        "Tool provides latest financial news about fund market by scraping data from Bloomberg"
    )

    def _run(self) -> str:
        web_scrapper = WebScrapper()

        domain = "https://www.bloomberg.com"
        link_elements = web_scrapper.get_web_data(f"{domain}/markets", 'a[href^="/news/"]')
        unique_links = set()


        for link in link_elements:    
            href = link.attrs["href"]    
            if href not in unique_links:
                unique_links.add(href)
                if len(unique_links) > 9: break #only first nine articles


        articles = []
        for link in unique_links:
            url = f"{domain}{link}"
            print(f"get article from: {url}")
            paragraphs = web_scrapper.get_web_data(url, "article p[data-component='paragraph']")
            text = ''
            for paragraph in paragraphs:
                text += ' '.join([string for string in paragraph.stripped_strings])
                text += '\n'
            articles.append(text)
        
        return "\n\n".join(articles)
