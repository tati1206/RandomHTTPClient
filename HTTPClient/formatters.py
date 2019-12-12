from colorama import Fore

def formatHeaders(headers):
	listHeaders = list(headers.items())

	formattedHeaders = ""

	for header in listHeaders:
		key = Fore.BLUE + header[0] + Fore.RESET
		value = Fore.GREEN + header[1] + Fore.RESET

		formattedHeaders = formattedHeaders + "{}: {}".format(key, value) + "\n"
	
	return(formattedHeaders)

def formatStatusCode(statusCode):
    if statusCode >= 100 and statusCode <= 199:
        return Fore.BLUE + str(statusCode) + Fore.RESET + "(Info)" 

    elif statusCode >= 200 and statusCode <= 299:
        return Fore.GREEN + str(statusCode) + Fore.RESET + "(Success)" 

    elif statusCode >= 300 and statusCode <= 399:
        return Fore.YELLOW + str(statusCode) + Fore.RESET + "(Redirection)"

    elif statusCode >= 400 and statusCode <= 499:
        return Fore.RED + str(statusCode) + Fore.RESET + "(Client Error)"

    elif statusCode >= 500 and statusCode <= 599:
        return Fore.RED + str(statusCode) + Fore.RESET + "(Server Error)"

    else:
        return "Status unrecognized"

def formatUrl(url):
    url = str(url)
    if url.startswith("http://") or url.startswith("https://"):
        return url
    
    else:
        return "http://" + url