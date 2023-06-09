import imports as importa

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
html_text = importa.requests.get('https://eshop-prices.com/games/popular?currency=MXN', headers=headers).text
soup = importa.BeautifulSoup(html_text, 'lxml')
lista = soup.find('div', class_ = 'games-list well')
productos = lista.find_all('a', class_ = 'games-list-item')
nombres = lista.find_all('div', class_ = 'games-list-item-title')
precio = lista.find_all('span', class_ = 'price')
metacritic = lista.find_all('span', class_ = 'game-score game-score--success')

msg = importa.mensaje.mensaje(nombres, precio, metacritic)
 
print(msg)
    
#Mandamos a whatsapp
# syntax: phone number with country code, message, hour and minutes
#pywhatkit.sendwhatmsg_to_group_instantly('number', msg, 12, 48)

#Aquí acomodo el raton para que de click automaticamente
#pyautogui.click(1050, 950)
#time.sleep(2)
#k.press_and_release('enter')