from    selenium.webdriver.chrome.service import Service
from    selenium.webdriver.chrome.options import Options
from    webdriver_manager.chrome import ChromeDriverManager
from    bs4 import BeautifulSoup
from    selenium import webdriver
import  pandas as pd
import  requests
import  sys

def get_page_source(url):
    options = Options()
    options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.get(url)
    html_content = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.find("table")

    if not table:
        print("No table found on the page.")
        exit()
    return table

def save_data(table, file_name):
    data = []
    for row in table.find_all("tr")[1:]:
        cols = [ele.text.strip() for ele in row.find_all("td")]
        if cols:
            data.append(cols)
    columns = [th.text.strip() for th in table.find_all("tr")[0].find_all("th")]
    df = pd.DataFrame(data[:-1], columns=columns)
    df.to_csv(file_name, index=False)
    print(f"Scraped data saved to {file_name}")

def main(file_name):
    url = "https://data.1337ai.org/"
    table = get_page_source(url)
    save_data(table, file_name)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments.")
    else:
        main(sys.argv[1])
