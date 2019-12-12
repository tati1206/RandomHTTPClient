import fire
import requests
import formatters
from colorama import Fore

def printResults(response):
	print("\nStatus: " + formatters.formatStatusCode(response.status_code) + "\n")
	print(Fore.CYAN + "####### Headers ######" + Fore.RESET + "\n")
	print(formatters.formatHeaders(response.headers))
	print(Fore.CYAN + "####### Body ######" + Fore.RESET + "\n")
	encodeResponse = response.encoding
	print(response.content.decode(encodeResponse))

class httpMethodsCommands:
	def get(self, url, body={}, headers={}, params={}):
		formattedUrl = formatters.formatUrl(url)
		try:
			response = requests.get(formattedUrl, data=body, headers=headers, params=params)
			printResults(response)
		except Exception as error:
			print("\nCannot connect to {}\n".format(formattedUrl))

	def post(self, url, body={}, headers={}, params={}):
		formattedUrl = formatters.formatUrl(url)
		try:
			response = requests.post(formattedUrl, data=body, headers=headers, params=params)
			printResults(response)
		except Exception as error:
			print("\nCannot connect to {}\n".format(formattedUrl))

	def put(self, url, body={}, headers={}, params={}):
		formattedUrl = formatters.formatUrl(url)
		try:
			response = requests.put(formattedUrl, data=body, headers=headers, params=params)
			printResults(response)
		except Exception as error:
			print("\nCannot connect to {}\n".format(formattedUrl))

	def delete(self, url, body={}, headers={}, params={}):
		formattedUrl = formatters.formatUrl(url)
		try:
			response = requests.delete(formattedUrl, data=body, headers=headers, params=params)
			printResults(response)
		except Exception as error:
			print("\nCannot connect to {}\n".format(formattedUrl))

if __name__ == "__main__":
	fire.Fire(
		httpMethodsCommands,
		)
