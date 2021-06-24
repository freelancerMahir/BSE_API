import requests
import bs4

def share_prices(name = None):
	if not name:
		res = requests.get(
			f"https://dsebd.org/latest_share_price_scroll_by_ltp.php")
		soup = bs4.BeautifulSoup(res.text, 'html.parser')
		comp = soup.select("td .ab1")
		companies = list(map(lambda x:x.string.strip(),comp))
		ltp = soup.find_all(class_ = "background-yellow")
		ltp = list(map(lambda x:x.string.strip(),ltp))
		return (companies, ltp)
	else:
		res = requests.get(f"https://dsebd.org/displayCompany.php?name={name}")
		soup = bs4.BeautifulSoup(res.text, 'html.parser')
		ltp_soup = soup.select("#company")[1].select("td")[0]
		ltp = float(ltp_soup.string.strip())
		return ltp